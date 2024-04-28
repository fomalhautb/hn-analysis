# I analyzed 4 millions HN posts and used the tricks I found to get to the top Show HN of the day

## A failed launch

Last week, my friend Stan has built a really cool project pgmock, which is an in-memory postgres written in WebAssembly for unit testing. I have been reading hacker news for a while and I knew this is something that HN people would love. However, when we launched it, it only got 3 upvotes. It was very frustrating and also hard to believe that something like this gets no attention on hackernews just based on my intuition. So I hypothesize is that we didn't launch it correctly.

Then the natural question is: what is a better way to launch? I decided to download the HN post dump and try to find out if there are some patterns. And it was suprising to me that there are some patters that are super obvious and strong.

We launched again and applied some of these tricks. This time it was a huge success and we got more than 300 upvotes within 24 hours and became the top 1 post on Show HN for that day.

If these sound interesting to you, now I am going reveal the tricks.

## Some basic statistics of HN posts

There are around 4 million posts between 2011 and 2022 on hacker news, around 120k of them are Show HN. The average upvotes of posts is 15.2. Show HN generally have more upvotes of an average 17.0.

Since our goal is launch successfully, we mainly focus on Show HN posts from now on. 

The first trick I found is that the Show HN posts with a link have a higher average upvotes of 17.3, compare to the average upvotes of 11.2 for posts without a link. So **always post with a link**

We mentioned before that Show HN posts have an average of 17.0 upvotes, doesn't sound too bad. However, **the median is a painfully low 3.0**. That means half of the posts don't even get more than 3 upvotes and our first launch is already an average launch. That is very sad. If we plot the score distribution, it looks like this:

![plot](./imgs/score_num_posts.png)

The power law is so strong you can't even see the data clearly anymore. If we limit the score range from 0 to 100, the power law is still crazy

![plot](./imgs/score_num_posts_range.png)

**Only around 19% of the posts get more than 10 upvotes, 4% get more than 100 upvotes, and 0.8% get more than 300 upvotes.**

One learning from this is that don't be too disappointed if your HN post didn't get any traction, that is actually the most possible outcome.


## Timing

There are some posts on HN saying what is the best time to launch already, but I didn't see any one backing this with data. So I analyized the timing of posts and can confirm that most of the common agreement on the best timing are indeed correct

Here is the average score on which week day you post:

![plot](./imgs/score_weekday.png)

We can see that weekend is inded the best time to post.

If we plot the day time of posts in California PT time, we can also see that posts posted in the morning between 4AM and AM have the highest average score

![plot](./imgs/score_hour.png)

Even though the common agreement on the HN for best posting time is indeed correct, but no one has given a good explanetion of why these times are better. I will give my best guess on why:

- Why morning is better: This is more of a subjective guess. Most people start their day by reading HN, if you post at that time, it is more likely that you will get intense attention in a short period of time, so it is easier to be ranked better by the algorithm. Also most of the posts are posted between 6AM and 10AM. If you do slightly ealier than them, you will get less competition.

![plot](./imgs/posts_hour.png)

- Why weekend is better: The reason might be relatively simple, it is because the less people post on the weekend, so you have less competition and more likely to get more attention. Here is the graph of number of posts in each weekday:

![plot](./imgs/posts_weekday.png)

Conclusion: **Always post on weekend between 4AM and 6AM PT time**

## Title

Now is the most interesting part: what kind of titles are the best? Let's first start from analyzing the length. Here is a plot of the average score of each title word count:

### Title length

![plot](./imgs/title_length_score.png)

We can see that very short and very long titles perform better. The reason for this might be that most posts have a medium length of title, so if you have very short or very long titles, you can stand out more:

![plot](./imgs/title_length_count.png)

Conclusion: **Write titles that are as long as the length limit**

### Title cases

It is quite suprising that all capital lowercase titles (like "This is a title") have a higher average upvotes of 17.5 than all capital uppercase titles (like "This Is A Title") of 14.6. My guess is that HN people are very ads avert and captial uppercase titles give people a marketing vibe.

Conclusion: **Write lower-cased titles**

### Title keywords

One pattern I noticed when browsing hacker news is that it seems like posts with "I built ..." or "I ..." have more stars than normal posts. Is that really the case? I ran an analysis and suprisingly, **Show HN posts with "I" in it has a much higher average upvotes of 34.4 instead of 17.0.** This is an increadabily large advantage.

So what are all the words that gives much higher average upvotes? I lemmatized all the words and counted the average scores of all lemmas that has more than 100 occurance. And this is the list of words:

```
Top 100 stems by average score(stem, avg_score, num_occurence):
im 48.45723684210526 304
wrote 45.00923076923077 325
altern 43.29887410440123 977
year 41.26732673267327 404
opensourc 40.01171605789111 1451
linux 37.5967365967366 429
simul 35.66522678185745 463
i 34.36167485580004 4681
brows 31.606811145510836 323
book 30.422890397672163 1031
sql 30.05841121495327 428
modern 29.99357601713062 467
pdf 29.516806722689076 476
made 28.853241077931536 2746
faster 28.837628865979383 388
css 28.764238410596025 755
html5 28.348837209302324 430
program 28.30256898192198 1051
termin 27.821739130434782 690
editor 27.70179640718563 835
hacker 27.60766283524904 1305
databas 27.451487710219922 773
languag 26.92922794117647 1088
’ 26.92128279883382 343
algorithm 26.5 382
thi 26.41343669250646 774
3d 26.148529411764706 680
comput 26.10955710955711 429
where 25.986263736263737 364
built 25.984189723320156 2530
markdown 25.577319587628867 582
puzzl 25.47147147147147 333
color 25.29136690647482 556
ui 25.24869109947644 764
turn 25.241726618705037 695
webgl 25.00920245398773 326
look 24.96398891966759 361
deep 24.781094527363184 402
who 24.569190600522195 383
server 24.536941580756015 1164
fast 24.52421959095802 929
c 24.486140724946694 938
engin 24.48249027237354 1542
instant 24.46969696969697 330
tini 24.412371134020617 388
rust 24.41222366710013 769
10 24.411078717201168 343
written 24.320121951219512 984
web 24.240506329113924 3713
privat 24.201044386422975 383
os 24.143712574850298 334
cours 24.107954545454547 352
learn 24.085054080629302 2034
git 23.91283676703645 631
interact 23.859066427289047 1114
us 23.659442724458206 323
minim 23.64066193853428 423
static 23.57676348547718 482
anim 23.570434782608697 575
stock 23.371681415929203 339
minimalist 23.226044226044227 407
an 23.18394587675992 5469
work 23.095281306715062 1102
not 23.035714285714285 420
stack 23.013333333333332 375
no 22.98005698005698 702
compil 22.87319884726225 347
site 22.799185888738126 1474
encrypt 22.753424657534246 511
distribut 22.74660633484163 442
but 22.59360730593607 438
nativ 22.554982817869416 582
edit 22.526806526806528 429
game 22.513951979234264 3082
shell 22.493865030674847 326
reddit 22.48131868131868 455
open 22.36896046852123 2049
visual 22.363581367211133 1653
bootstrap 22.358974358974358 351
browser 22.34550408719346 1835
write 22.331189710610932 933
maco 22.13235294117647 408
minut 21.932608695652174 460
text 21.868306801736615 1382
render 21.82747603833866 313
side 21.746963562753038 494
have 21.700808625336926 371
my 21.63968734241049 3966
a 21.619241923517908 29654
make 21.562937062937063 1716
hack 21.494529540481402 457
desktop 21.478527607361965 489
sourc 21.448827292110874 1876
queri 21.401515151515152 396
type 21.287378640776698 515
it 21.194331983805668 1235
– 21.188303244730715 33069
lightweight 21.187772925764193 458
machin 21.17655172413793 725
javascript 21.147673314339983 2106
```