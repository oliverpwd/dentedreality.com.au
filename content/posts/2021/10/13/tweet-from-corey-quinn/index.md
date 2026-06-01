---
title: Tweet from Corey Quinn
date: '2021-10-13T21:46:30-06:00'
format: link
service: instapaper
tags:
- read
external_url: https://twitter.com/QuinnyPig/status/1445151389122842624
---

[Tweet from Corey Quinn](https://twitter.com/QuinnyPig/status/1445151389122842624)  



![](https://pbs.twimg.com/profile_images/1431046769262006274/7GJFLo-A.jpg)![](https://pbs.twimg.com/profile_images/1431046769262006274/7GJFLo-A.jpg)

And now, a thread of Ancient Sysadmin Wisdom: an incomplete list of things we have learned from decades of outages.

![](https://pbs.twimg.com/tweet_video_thumb/FA41hCTVkAc6ywO.jpg)![](https://pbs.twimg.com/tweet_video_thumb/FA41hCTVkAc6ywO.jpg)

“It’s always DNS.” Yup. Everything relies upon DNS, those relationships are non-obvious, and some things like to cache well beyond your TTL.

“If an outage lasts more than ten minutes, it’s likely to last for hours.” Yup. Usually related to electric power, but this is a good rule of thumb for “do we activate our DR plan” decisions.

“The bootstrapping problem.” We don’t usually take EVERYTHING down at once. Very often the thing needed to boot the server lives in one of the VMs that’s hosted on that server.

“The herd of elephants.” When users find your site is down, they start spamming the refresh button like it’s my shitpost button. This dramatically increases load on an already-wobbly site.

![](https://pbs.twimg.com/tweet_video_thumb/FA42SgsVkAcQ5OO.jpg)![](https://pbs.twimg.com/tweet_video_thumb/FA42SgsVkAcQ5OO.jpg)

“Don’t use external domains for internal things.” You really want the thing you provide to the world not to power your internal systems; ideally you want outages that take down outside things or internal things but not both at once.

“The Internet has opinions.” As much fun as it is to blame cyberattacks or insiders acting in bad faith, the real world is usually a lot less interesting.

![](https://pbs.twimg.com/tweet_video_thumb/FA42-xXUcAI3cuW.jpg)![](https://pbs.twimg.com/tweet_video_thumb/FA42-xXUcAI3cuW.jpg)

“Not all downtime is equal.” If you sell shoes and your site goes down, a lot of customers will come back an hour later to buy shoes. Conversely, nobody’s coming back in an hour to click an ad for you.

“You’ll never map all of your dependencies.” How many folks pay a third party vendor to defend against AWS outages, but don’t realize that that vendor relies completely upon AWS?

![](https://pbs.twimg.com/tweet_video_thumb/FA43_YPVQAEvLuy.jpg)![](https://pbs.twimg.com/tweet_video_thumb/FA43_YPVQAEvLuy.jpg)

“BGP is the devil.” Yes, it is. I’m astounded it works. @ioshints for the professional analysis of that. It’s not my area because I still aspire to happiness.

![](https://pbs.twimg.com/tweet_video_thumb/FA44f-rUcAYFFCc.jpg)![](https://pbs.twimg.com/tweet_video_thumb/FA44f-rUcAYFFCc.jpg)

“An outage won’t destroy your business.” It feels like the world is ending at the time, but taking an outage from time to time is generally okay. If a site is down every third day, in time people go elsewhere.

“Plan for failure.” If it can break, it will break. If it can’t break, fuck you yes it can.

“Outages like to travel in clusters.” Sometimes it’s a batch of hard drives failing together, other times it’s downstream issues surfacing a day or two later, other other times it’s attempted fixes breaking other things subtly. Plan to be busy after a big one.

“Out-of-band access will save your life.” Seriously. I’ve had entire secondary networks installed in data center cages just so I could use some crappy residential DSL line to get in after I’d REALLY broken the firewall. Cheaper than an interstate flight…

“Outage communications should be planned for.” Seriously, have a template. You don’t want to have to wing it when half of the internet is pounding down your door. And saying nothing enrages people.

“Ignore best practices.” Seriously: not having any single points of failure or important nodes is great in theory, so is distributed observability, but if my bastion host that lets me get into the busted firewall goes down, I want good old Nagios blowing me up about it.

“Internal messaging.” We all rely on other platforms. When one of them goes down, you’re basically stuck until they come back up. Make sure that’s messaged to your leadership so it doesn’t look like you just don’t give a shit that the site is broken.

“Be a good person, do good things.” Seriously. Outages are hard. You probably don’t want to work somewhere that inspires most of the world to cheer when you go offline. Ahem.

![](https://pbs.twimg.com/tweet_video_thumb/FA49SgQVgAAC7Pb.jpg)![](https://pbs.twimg.com/tweet_video_thumb/FA49SgQVgAAC7Pb.jpg)

“Rate limits help.” As the site recovers, the flock of elephants will attempt to stampede onto it in huge numbers, taxing already overworked systems. Have a way to defer recovery across a broad swath of your users.

“Ensure your vendors all have up to date emergency contacts.” Every once in a while I still get a call from the data center I helped set up a decade ago at a long-ago employer. Next time I’m telling them to “shut it down, we have another provider.”

“Split horizon DNS is a bad plan.” I can’t believe I have to mention this, but “you’ll send internal data to a different destination depending upon which network your laptop is on” is a horrifying mode.

“Keep your eye on the prize.” The outage is big and momentous and important but you should probably not ignore that email about an SSL cert expiring in three days.

“Remember that computers are dumb.” If you have alarms that fire a week after an outage because holy SHIT the week-over-week metrics look WAY different right now,” you have no one to blame but yourself.

“Institutional knowledge matters.” No matter how you run things or document your systems, Pat’s been here for twenty years and knows how and why that system runs.

You didn’t just Frugally fail to retain Pat last cycle, did you?

“You will hate yourself.” It’s super important that you find out when certain things break. If the core network breaks, you’re about to find out how long it takes your cell provider to work through a backlog of 20k automated SMS messages alerting you about it.

“Wait, what?” Gmail has a hard limit of 3,600 emails it will let an account receive per hour. All of those alert emails get through; anything above the limit bounces.

“This list is not comprehensive.” There are always outages caused by things not on this list. What’ve I missed that you’ve experienced?