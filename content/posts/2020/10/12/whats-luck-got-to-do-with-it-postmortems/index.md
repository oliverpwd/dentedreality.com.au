---
title: What’s Luck Got to Do With It? (Postmortems)
date: '2020-10-12T23:01:13-06:00'
format: link
service: instapaper
tags:
- read
external_url: https://jpaulreed.com/thoughts/whats-luck-got-to-do-with-it.html
---

[What’s Luck Got to Do With It? (Postmortems)](https://jpaulreed.com/thoughts/whats-luck-got-to-do-with-it.html)  



###### October 6, 2020

One element I’ve seen repeatedly is reference to “How did we get lucky in this incident?” It’s an aspect of incidents some like to discuss, because I also hear it in conversations and stories about incidents: “Oh man, we were so lucky that Beth happened to be on-call that particular night!”

But I’ve always wondered: why do people bother asking this question? What’s the goal of discussing what amounts to the finer points of randomness and “noise” in a complex socio-technical system? Unless you happen to be in possession of one of those probability-altering devices from the second season of Deep Space Nine, it seems like a pretty pointless digression.

A couple of years ago, [I asked if anyone knew the genesis of this question](https://twitter.com/jpaulreed/status/1014941480866074624). I only got one lead: it’s apparently asked on Google’s standard postmortem template. An example of this template was published in [O’Reilly’s SRE book](https://landing.google.com/sre/books/). And that may be one of the reasons we started asking each other in post-incident reviews “How was our luck today?” as if we were checking in on a bleary-eyed gambler, glued to a Vegas slot machine.

It’s beyond time we reexamine the post-incident question of luck, and **I submit: asking “how we were lucky” in an incident retrospective is not only a waste of you and your colleague’s time, it is distractingly detrimental to post-incident analysis**.

An obvious reason why “luck” discussions are not useful: what are you supposed to do with aspects of the incident attributed to a good outcome of a roll of the dice? We don’t follow-up a “lucky” attribution by asking “What will you do next time to be lucky? How can we all get luckier in the future? Can you teach me how to flick my wrists just right when I let go of the dice?” Director James Cameron is oft-quoted as saying “Hope is not a strategy; luck is not a factor” and spending time talking about something, by definition, we have no control over is placing a pretty big bet on hope. For all of the discussions of “luck” I’ve heard in incident retrospectives, I’ve never seen anyone put “Be more lucky again next time” on the list of action items that goes to the boss’ boss.

A second, and more important, reason why an attribution of “luck” is unhelpful in incident analyses: its use often masks other aspects of the system that we can influence and when we chalk it up to “luck” and move on, we miss a big opportunity. In a recent retrospective, someone said “We were really lucky Sam happened to be on the call for this incident; he’s worked here a really long time, and he noticed that error code didn’t look quite right, which led us all to investigate and find the triggering issue. Nobody else would’ve found that as quickly.”

**That’s not luck: *it’s expertise***.

Describing it as luck leaves no space to explore questions like “how did Sam know to look at the error codes? What ‘seemed off’ to him about those error codes?” We can’t “package up” luck and give it to other people, but we can seek to understand how Sam gained his expertise in the system at hand, and re-package *that* for other folks to use in the future.

(It’s worth noting: as I dug more into how that particular incident unfolded, the only reason Sam got involved in the first place was because the on-call engineer slept through the initial page and escalations. As the team’s manager, Sam eventually got paged. The irony, of course, is that our experience of Sam’s “lucky” involvement was the result of of the on-call engineering being “unlucky.” If we stopped at “Yah, we sure were lucky Sam was with us,” we would also have missed deeper questions around on-call practices and on-call health for Sam’s team.)

The “Where we got lucky?” question in the SRE book’s “[Example Postmortem](https://landing.google.com/sre/sre-book/chapters/postmortem/)” has a curious footnote: “This section is really for near misses,” along with an example of what they consider a “near miss.” The example isn’t a “near miss,” in fact, but rather an embodiment of adaptive capacity within the system, which is another important capability teams use to counter incidents, and one which “luck” will handily obscure.

In fact, all of the “lucky” items in the SRE book’s example represent the use of adaptive capacity in response to a perturbation in the system and the expression of operator expertise, either in the moment of the incident itself or in the earlier design of the system. As an example of the latter, “Server logs had stack traces pointing to file description exhaustion” is listed as “how we go lucky” (or a “near miss,” if you believe the footnote). But stack traces on errors are a common industry tool to record and debug problems. We build our systems with these successful patterns, *precisely because we were successful using them in the past*, not because we “got lucky.”

One of my favorite Dekker quotes is about human error: “Human error is not the conclusion of an investigation. It is the starting point.” As it is with “luck”: when someone says “we were lucky,” your ears should perk up; it should be the beginnings of a line of inquiry, not a settled explanation representing an endpoint. Relying on luck as an explanation leaves swaths of opportunity to learn how your systems actually function unexplored and chances to see how your people actually go about their work a “mystery.”

It’s time to retire “luck” as a framing in our post-incident analyses. As [Tina](https://en.wikipedia.org/wiki/Tina_Turner) reminds us: “What’s luck got to do with it? What’s luck… but a second-hand rationalization?”

(At least, I think that’s how [that song](https://www.youtube.com/watch?v=oGpFcHTxjZs) goes…)