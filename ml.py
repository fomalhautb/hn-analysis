import csv
import matplotlib.pyplot as plt
import numpy as np
import transformers
import datasets
import evaluate
import random

# id,title,url,score,time,comments,author

with open('data.csv', 'r') as file:
    reader = csv.DictReader(file)
    data = list(reader)

for d in data:
    d['score'] = max(1, int(d['score']))

data = random.sample(data, 100000)

bin_edges = [0, 5, 10, 20, 30, 50, 100, 200, 300]

def score_transform(scores):
    bin_indices = np.digitize(scores, bin_edges + [100000]) - 1
    return bin_indices

scores = np.array([int(d['score']) for d in data])
scores = score_transform(scores)

MODEL_NAME = 'FacebookAI/roberta-base'
tokenizer = transformers.AutoTokenizer.from_pretrained(MODEL_NAME)
model = transformers.AutoModelForSequenceClassification.from_pretrained(MODEL_NAME, num_labels=len(bin_edges))

processed_data = []
for d, s in zip(data, scores):
    processed_data.append({'text': d['title'], 'label': s})

def preprocess_function(examples):
    return tokenizer(examples["text"], truncation=True)

dataset = datasets.Dataset.from_list(processed_data)
dataset = dataset.map(preprocess_function, batched=True)
dataset = dataset.train_test_split(test_size=2000 / len(dataset))

accuracy = evaluate.load('accuracy')
data_collator = transformers.DataCollatorWithPadding(tokenizer=tokenizer)

def compute_metrics(eval_pred):
    predictions, labels = eval_pred
    predictions = np.argmax(predictions, axis=1)
    return accuracy.compute(predictions=predictions, references=labels)


training_args = transformers.TrainingArguments(
    output_dir='./results',
    learning_rate=1e-5,
    per_device_train_batch_size=16,
    per_device_eval_batch_size=16,
    num_train_epochs=3,
    weight_decay=0.01,
    evaluation_strategy="steps",
    save_strategy="steps",
    eval_steps=50
)

trainer = transformers.Trainer(
    model=model,
    args=training_args,
    train_dataset=dataset['train'],
    eval_dataset=dataset['test'],
    tokenizer=tokenizer,
    compute_metrics=compute_metrics,
    data_collator=data_collator,
)

trainer.train()