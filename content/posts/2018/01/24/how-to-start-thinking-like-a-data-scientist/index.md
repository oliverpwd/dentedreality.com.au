---
title: How to Start Thinking Like a Data Scientist
date: '2018-01-24T21:20:41-06:00'
format: link
service: instapaper
tags:
- read
external_url: https://hbr.org/2013/11/how-to-start-thinking-like-a-data-scientist
---

[How to Start Thinking Like a Data Scientist](https://hbr.org/2013/11/how-to-start-thinking-like-a-data-scientist)  



Slowly but steadily, data are forcing their way into every nook and cranny of every industry, company, and job. Managers who aren’t data savvy, who can’t conduct basic analyses, interpret more complex ones, and interact with data scientists are already at a disadvantage. Companies without a large and growing cadre of data-savvy managers are similarly disadvantaged.

Fortunately, you don’t have to be a [data scientist](https://hbr.org/2012/10/data-scientist-the-sexiest-job-of-the-21st-century/) or a [Bayesian statistician](http://en.wikipedia.org/wiki/Bayesian_statistics) to tease useful insights from data. This post explores an exercise I’ve used for 20 years to help those with an open mind (and a pencil, paper, and calculator) get started. One post won’t make you data savvy, but it will help you become data literate, open your eyes to the millions of small data opportunities, and enable you work a bit more effectively with data scientists, analytics, and all things quantitative.

While the exercise is very much a how-to, each step also illustrates an important concept in analytics — from understanding variation to visualization.

First, start with something that interests, even bothers, you at work, like consistently late-starting meetings. Whatever it is, form it up as a question and write it down: “Meetings always seem to start late. Is that really true?”

Next, think through the data that can help answer your question, and develop a plan for creating them. Write down all the relevant definitions and your protocol for collecting the data. For this particular example, you have to define when the meeting actually begins. Is it the time someone says, “Ok, let’s begin.”? Or the time the real business of the meeting starts? Does kibitzing count?

Now collect the data. It is critical that you [trust the data](https://hbr.org/2013/12/datas-credibility-problem/ar/1). And, as you go, you’re almost certain to find gaps in data collection. You may find that even though a meeting has started, it starts anew when a more senior person joins in. Modify your definition and protocol as you go along.

Sooner than you think, you’ll be ready to start drawing some pictures. Good pictures make it easier for you to both understand the data and communicate main points to others. There are plenty of good tools to help, but I like to draw my first picture by hand. My go-to plot is a [time-series plot](http://en.wikipedia.org/wiki/Time_series), where the horizontal axis has the date and time and the vertical axis has the variable of interest. Thus, a point on the graph below (click for a larger image) is the date and time of a meeting versus the number of minutes late.

[![](https://i1.wp.com/hbr.org/resources/images/article_assets/2013/11/taking-data-picture1.jpg?w=607&ssl=1)![](https://i1.wp.com/hbr.org/resources/images/article_assets/2013/11/taking-data-picture1.jpg?w=607&ssl=1)](https://i1.wp.com/hbr.org/resources/images/article_assets/2013/11/taking-data-picture1.jpg?ssl=1)

Now return to the question that you started with and develop summary statistics. Have you discovered an answer? In this case, “Over a two-week period, 10% of the meetings I attended started on time. And on average, they started 12 minutes late.”

But don’t stop there. Answer the “so what?” question. In this case, “If those two weeks are typical, I waste an hour a day. And that costs the company $X/year.”

Many analyses end because there is no “so what?” Certainly if 80% of meetings start within a few minutes of their scheduled start times, the answer to the original question is, “No, meetings start pretty much on time,” and there is no need to go further.

But this case demands more, as some analyses do. Get a feel for variation. Understanding variation leads to a better feel for the overall problem, deeper insights, and novel ideas for improvement. Note on the picture that 8-20 minutes late is typical. A few meetings start right on time, others nearly a full 30 minutes late. It might be better if one could judge, “I can get to meetings 10 minutes late, just in time for them to start,” but the variation is too great.

Now ask, “What else does the data reveal?” It strikes me that five meetings began exactly on time, while every other meeting began at least seven minutes late. In this case, bringing meeting notes to bear reveals that all five meetings were called by the Vice President of Finance. Evidently, she starts all her meetings on time.


So where do you go from here? Are there important next steps? This example illustrates a common dichotomy. On a personal level, results pass both the “interesting” and “important” test. Most of us would give anything to get back an hour a day. And you may not be able to make all meetings start on time, but if the VP can, you can certainly start the meetings you control promptly.

On the company level, results so far only pass the interesting test. You don’t know whether your results are typical, nor whether others can be as hard-nosed as the VP when it comes to starting meetings. But a deeper look is surely in order: Are your results consistent with others’ experiences in the company? Are some days worse than others? Which starts later: conference calls or face-to-face meetings? Is there a relationship between meeting start time and most senior attendee? Return to step one, pose the next group of questions, and repeat the process. Keep the focus narrow — two or three questions at most.

I hope you’ll have fun with this exercise. Many find a primal joy in data. Hooked once, hooked for life. But whether you experience that primal joy or not, do not take this exercise lightly. There are fewer and fewer places for the “data illiterate” and, in my humble opinion, no more excuses.