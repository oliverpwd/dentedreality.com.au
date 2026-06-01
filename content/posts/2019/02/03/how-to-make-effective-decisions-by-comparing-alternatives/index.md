---
title: How to make effective decisions by comparing alternatives
date: '2019-02-03T20:50:10-06:00'
format: link
service: instapaper
tags:
- read
external_url: https://hackernoon.com/how-to-make-effective-decisions-by-comparing-alternatives-99ab7d4388bb
---

[How to make effective decisions by comparing alternatives](https://hackernoon.com/how-to-make-effective-decisions-by-comparing-alternatives-99ab7d4388bb)  



[![](https://cdn-images-1.medium.com/fit/c/100/100/0*vRuQAghGl2RZgFgw.)![](https://cdn-images-1.medium.com/fit/c/100/100/0*vRuQAghGl2RZgFgw.)](https://hackernoon.com/@alonkiriati?source=post_header_lockup)
[Alon Kiriati](https://hackernoon.com/@alonkiriati)
Jan 19


![](https://i0.wp.com/cdn-images-1.medium.com/max/1600/1*D1a3wrXwc0gWi65Na_fdyg.jpeg?w=607&ssl=1)![](https://i0.wp.com/cdn-images-1.medium.com/max/1600/1*D1a3wrXwc0gWi65Na_fdyg.jpeg?w=607&ssl=1)

Photo by [rawpixel](https://unsplash.com/photos/3Zt0qoHUYb0?utm_source=unsplash&utm_medium=referral&utm_content=creditCopyText) on [Unsplash](https://unsplash.com/search/photos/decisions?utm_source=unsplash&utm_medium=referral&utm_content=creditCopyText)

### Not better, not worse… just different

“React.js is so much better than Angular”, “Java sucks, no one uses it anymore… we should use Golang”, “Pineapple is the worst pizza topping”. You’ve probably heard one of these very straight opinions — one option is the best, the other is the worst, X is better than Y and so on. But Java is still one of the most popular languages in the world, Angular gives a decent fight to React.js, and pizza with pineapple… well, that’s ewwww.

Does that mean that more than half of the people are clueless, don’t know how to tell which technology is better or make the right choices? Maybe we should stop using terms like “better”, “worse”, “best” and shallow comparisons when evaluating alternatives. Instead, we should focus on the benefits of each solution, the disadvantages, and which one is a better fit for our specific problem.

### Evaluating alternatives

One way to do this is by creating an alternatives comparison table:

* Write the different alternatives in the header. Use each column to evaluate one alternative. Pick 2–5 alternatives.
* Write the different properties that you think are important for evaluating the different alternatives. Pick 2–5 most important comparison properties.
* Keep the last row for summing up. There is no better/worse solution, focus on why each alternative solves the problem .

### “What would you have to believe to choose this approach?”

For example, let’s assume that we have a problem that can be solved in two ways. One is [S.O.L.I.D](https://en.wikipedia.org/wiki/SOLID) and the other one is hackier. Some might say that we should always use a S.O.L.I.D solution, regardless of the circumstances. Does that mean that anyone who uses hacky code is a bad developer? I doubt it.

Let’s put the alternatives in a table:

![](https://i0.wp.com/cdn-images-1.medium.com/max/1600/1*yqcTIBeDRjjFL43hOy7m3A.png?w=607&ssl=1)![](https://i0.wp.com/cdn-images-1.medium.com/max/1600/1*yqcTIBeDRjjFL43hOy7m3A.png?w=607&ssl=1)

After composing this table, we can focus on the bottom line, and tie it directly to our goal.

An example of cases for *“shipping as fast as possible, and we are ok with compromising on future quality”* could be:

* A severe bug that exists in the system. Every day that passes without a solution can cause long-term damage.
* We have a contract with a customer to ship the solution on a specific date. If we miss the deadline, there may be legal consequences.
* The company has cash flow issues. Shipping the solution early can have a huge impact on our business stability.

As you can see, using S.O.L.I.D is not always the better approach. If we care about code quality, we should definitely default to it, but we must make sure that we know the tradeoffs. Choose one solution over the other because you believe this is the best path to reach your goals; don’t do it just because [Uncle Bob](https://blog.cleancoder.com/) or someone in your company said it’s better.

### Don’t do reviews only to get the “stamp”

![](https://i1.wp.com/cdn-images-1.medium.com/max/1600/1*Naaux1mCrGaSnQfVuB8u6Q.jpeg?w=607&ssl=1)![](https://i1.wp.com/cdn-images-1.medium.com/max/1600/1*Naaux1mCrGaSnQfVuB8u6Q.jpeg?w=607&ssl=1)

Photo by [Hello Lightbulb](https://unsplash.com/photos/hgITU7cj7k8?utm_source=unsplash&utm_medium=referral&utm_content=creditCopyText) on [Unsplash](https://unsplash.com/search/photos/stamp?utm_source=unsplash&utm_medium=referral&utm_content=creditCopyText)

In many companies, reviews (design reviews, product reviews, etc.) have the same ritual — the feature owner writes the spec; their manager then reviews it; the group schedules a meeting to review the spec. More than once, there is a feeling that the purpose of these meetings is to get the stamp from the stakeholders rather than actually engage in an open discussion. The reasons why this can happen:

* If you already have a spec ready, why would you need 7 or so people gather in a room and “go over” it?
* The meetings tend to be boring and can turn to be a monologue when the feature owner reads the spec they wrote.
* Sometimes these meetings tend to be nit-picky, and the conversation can focus on things that are not crucial for the feature success (*“why do we use int32 and not int16?”, “strings or enums?”, “tabs or spaces?”).*
* Some people are more introverted than others. Are all the voices heard, or are there only a few people that are engaging in the conversation?
* The conversation on some details can take longer than expected, time then runs out before the feature owner can cover the whole spec, sometimes even less than half of it. This can frustrating. Moreover, if a follow-up meeting is required, it can also postpone the decision making and the whole project timeline.

### Be prepared with alternatives and goals, not with the solution

At my current company, we take a different approach. Reviews are made offline, using [Paper](https://paper.dropbox.com/) (benefiting from its features like sharing, comments, tasks which makes the collaboration more efficient), but any other online editor can work. For the design meetings, we use a different template. The decision maker chooses the 3–4 most important open questions that are critical to the feature’s success and composes an alternative table like we saw before. They can also recommend an alternative, but shouldn’t be very opinionated about it — the purpose of the meeting **is** to choose the proper approach based on the project goals.

The meeting then turns from a monologue that is focused on “stamping” a solution to an open conversation about the best approach. The audience turns from being approvers to being advisors. The feature owner doesn’t need to “defend” their selected solution, and turns into a decision maker that bases their solution on the stakeholder advice. By setting time (10–15 min.) for each question, you can make sure that you cover all open question, and that a decision was taken by the feature owner when the time is up. Making sure that everyone’s voice is heard, even the introverts, is just as easy as “Hey Jane, we didn’t hear your opinion, which option do you think will serve our goals? X,Y or Z?”

So next time you want to compare two or more alternatives, replace “React.js is better than Angular” with “React.js is easier to learn, more flexible, and is updated more frequently, so if we aim to quickly ramp up new engineers and move faster with the most top-notch technologies, this should be our choice between these two”.

As for “Pineapple is the worst pizza topping” — maybe some things aren’t meant to have alternatives 🍕

Thanks for spending 4 minutes of your time, until next time.

-Alon