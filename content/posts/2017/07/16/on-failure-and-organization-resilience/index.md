---
title: On Failure and Organization Resilience
date: '2017-07-16T18:03:06-06:00'
format: link
service: instapaper
tags:
- read
external_url: https://beero.ps/2017/06/17/on-failure-and-resilience/
---

[On Failure and Organization Resilience](https://beero.ps/2017/06/17/on-failure-and-resilience/)  



Like many people in ops-adjacent parts of the internet, I had a lot of feels around [this reddit post](https://www.reddit.com/r/cscareerquestions/comments/6ez8ag/accidentally_destroyed_production_database_on/), where a new software developer trying to follow instructions to set up his development environment accidentally borked the production database and was summarily fired as a result. Dr. Richard Cook of SNAFUCatchers wrote [a piece in response looking at different ways that organizations can respond to failure](https://www.snafucatchers.com/single-post/2017/06/04/BorkedTheDatabaseCase). The reddit story is a pretty clear example of what Dr. Cook calls “blame and train”, but he notes that this is not the optimal reaction to failure as it tends to lead to organizational brittleness. More positive reactions to failure can lead instead towards organizational resilience, and Dr. Cook encouraged me to share a story of what that could look like.

So, let me tell you all about the time I borked Etsy.

> So pleased to have won this year’s Three-Armed Sweater Award for that time I accidentally upgraded apache! Thanks [@allspaw](https://twitter.com/allspaw)! <3 [#opslife](https://twitter.com/hashtag/opslife?src=hash) [pic.twitter.com/1hP6WLjqPD](https://t.co/1hP6WLjqPD)
> 
> — (╯°□°）╯︵ ┻━┻ sdoɹǝǝq (@beerops) [December 7, 2016](https://twitter.com/beerops/status/806576489798004737)

Once upon a time, back in 2016, I needed to provision some new servers for something I was doing. Due to some fun idiosyncrasies of our provisioning setup, I ran into the not-totally-uncommon case where our yum repo had synced a newer version of a package from upstream than the version that we had pinned in Chef. This means that boxes will get provisioned ok, but then Chef will fail on the first run due to refusing to downgrade to the older version that we have pinned. Normally what we do in these situations is test the new package to make sure it doesn’t break anything, and then pin that newer version in Chef.

In this case, the package that was causing this problem was apache. “Fine,” I said to myself, “it’s a point release newer, I’ve tested it, it should only affect new boxes anyways, I’ll just push out the new version in Chef and get on with my provisioning.” So I did. And I logged onto a random web host to watch the chef run and make sure it did the right thing (which was supposed to be nothing) and… it did not do the right thing.

First of all, it installed the new package, which it was for sure not supposed to do, because our Chef recipe explicitly told it not to. Then it restarted apache, because it had to, and apache didn’t restart cleanly. That’s when I knew that that afternoon was about to get a lot more interesting. The first thing I did was turn to my colleague sitting next to me, who happened to be the ops engineer on call at the time. “Heyyyyyy friend,” I said, “I’m pretty sure you’re about to get paged a bunch because I just set apache on fire.” Then I hopped into our #sysops channel on Slack (which at the time was The Cool Place To Be for all your “what’s up with the site” questions) and let people there know what was going on.

The immediate response from *everyone* around was to ask, “What help do you need?” We brainstormed some ideas. The first thought was, since apache hadn’t come back up cleanly after the upgrade, was to downgrade again. But remember how that particular version was breaking provisioning because it wasn’t in our repos anymore? Yup, meaning we couldn’t roll back to the old version because it was gone. Someone hopped on another random web host and ran Chef again, and discovered that apache started up fine after a second Chef run. While a couple people started digging in to figure out why, some more of us coordinated using dsh to force a Chef run everywhere. Others were keeping an eye on graphs and logs – and we realized that while the site did get very slow for the ~10 minutes this was actually going on, it didn’t actually go down because a few servers hadn’t run Chef for whatever reason so hadn’t gotten the upgraded version in the first place.

It was a beautiful scene of empathetic and coordinated chaos. People were using Slack to coordinate, to figure out what the status was and what still needed to be done and to just *help do it*. People who arrived a few minutes late to the scene didn’t jump into asking who’s “fault” it was, because that’s not how we roll, they just wanted to know what was going on and *how they could help*.

We got the site back to where it needed to be pretty quickly. Once that was done, some people went back to what they were doing before while others jumped right into figuring out things like, why did Chef upgrade the package on existing servers that’s never happened before that was weird (fun with apache modules and yum) or, why did the second Chef run fix things (our chef recipe deletes a default config file that ships with apache that broke with this particular version). The only person who had anything negative to say to me about the whole incident was me.

At some places, I would have been blamed, called out, even fired. At Etsy, I got a [sweater](https://qz.com/504661/why-etsy-engineers-send-company-wide-emails-confessing-mistakes-they-made/).

![](https://beerops.files.wordpress.com/2017/06/screen-shot-2017-06-17-at-11-58-29.png)![](https://beerops.files.wordpress.com/2017/06/screen-shot-2017-06-17-at-11-58-29.png)

We of course held a post-mortem to talk through what happened, what we learned from the event, and how we could make our systems more resilient to this sort of thing in the future. The SNAFUCatchers talked about it at their [Brooklyn rendezvous in March](https://www.snafucatchers.com/single-post/2017/03/18/SNAFUCatchers-Rendezvous).

To me, this kind of response to an incident feels not only productive but like a hallmark of organizational maturity. It can be a challenge if you’re starting with or coming from a “blame and train” or “blame and shame” culture to a “blameless” or “blame-aware” one, but the focus on desired outcome and how people can work together to help resolve a situation in the moment as well as make the systems involved better equipped to handle situations in the future, can do wonders for system and organizational resilience.