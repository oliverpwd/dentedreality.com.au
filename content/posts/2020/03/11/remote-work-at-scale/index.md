---
title: Remote Work At Scale
date: '2020-03-11T14:26:57-06:00'
service: jetpack
tags:
- automattic
- coronavirus
- covid-19
- distributed company
- remote work
categories:
- posts
image: https://dentedreality-content.s3.amazonaws.com/wp-content/uploads/2020/03/11143416/IMG_8102-scaled-1.jpg
---

![](https://dentedreality-content.s3.amazonaws.com/wp-content/uploads/2020/03/11143416/IMG_8102-scaled-1.jpg)

COVID-19 (aka coronavirus) has many companies suddenly experimenting with remote work for the first time. I tweeted yesterday that unfortunately people are likely to have a pretty rough time due to the rushed nature of the experiment, and some folks asked if I could expand on that, so here we are. There are already a bunch of write-ups, resources, and tools if you look around (including [one from our CEO Matt](https://ma.tt/2020/03/coronavirus-remote-work/), and this great [webinar-format session from Cate and Nicole](https://en.blog.wordpress.com/2020/03/06/a-crash-course-in-remote-management/)), so it’s worth getting other views and ideas as well.

> If this is your first experience at remote work, it’s unfortunately probably going to be pretty rough. Don’t let it taint your view though – to do it well requires cultural and process change in your org plus a lot of adaptation.
> 
> — Beau (@beaulebens) [March 10, 2020](https://twitter.com/beaulebens/status/1237493485038710784?ref_src=twsrc%5Etfw)

<https://platform.twitter.com/widgets.js>


We’ll look at some concepts that I think underpin successful distributed work, and then we’ll dive into a loosely-structured “day in the life” to look at some of the specific tools and approaches we use currently at [Automattic](https://automattic.com/). This is all based on about 13 years worth of working remotely or fully-distributed, 11 of which have been with Automattic where I’ve been a part of growing the company from ~40 people to ~1,200 people, spread across 76 countries. I’ve been everything from an individual engineer to a leader across groups up to about 60 people. We’ll focus on the day-to-day type work of an engineering-heavy organization rather than the business/human resources/operations side of things. This is going to be long, and probably a bit rambling.

Before we get into it, three quick notes;

1. I tend to use the term “[distributed work](https://distributed.blog/)” rather than “remote work”, because at Automattic we don’t have a central office to be “remote” from. We’re fully distributed. Like a decentralized network. Have been since day zero.
2. We operate across many timezones ([almost all of them](https://automattic.com/map/)), which creates its own complexities and amplifies the need for certain practices and approaches. If you’re taking an existing shared office remote, that might not be the case, but a lot of the approaches we use will probably still be useful to enable more async work (we’ll get to that below).
3. Tools are not the answer. Working remotely requires a cultural shift from your org, and a change in how you do business. Tools are part of the puzzle, and having good tools helps, but they won’t make or break your success.

Table Of Contents
hide

* [Key Concepts](#key-concepts)

* [Transparency, Trust, Access](#transparency-trust-access)
* [Communicate, Communicate, Communicate](#communicate-communicate-communicate)
* [Optimize for async](#optimize-for-async)
* [Spend time face to face](#spend-time-face-to-face)

- [A Day In The Life](#a-day-in-the-life)

* [Schedules & Timezones](#schedules-amp-timezones)
* [Calendars, Calls, & GTD](#calendars-calls-amp-gtd)
* [Active Communication](#active-communication)

* [Slack](#slack)
* [Zoom, and…](#zoom-and)

- [Async Communication](#async-communication)

* [P2](#p2)
* [GitHub](#github)

- [Archive Communication](#archive-communication)

* [Field Guide](#field-guide)


.gutentoc-toc-wrap ul li a, .gutentoc-toc-title-wrap .text\_open{ color: undefined}}

## Key Concepts

### Transparency, Trust, Access

Our DNA at Automattic is firmly rooted in the [WordPress open source community](https://wordpress.org/). From that world, our default is open; most people can access most information (including most conversations) about most things across the company. We trust everyone to make good decisions and spend their time wisely, and so they have access to “as much as possible” (and of course is prudent). This gives everyone much better context for what they’re doing, eliminates many “can I get access” type requests (and associated delays), and allows people to operate more independently which is critical when any kind of feedback loop can potentially stretch into days (if there are timezone differences, back and forth/approvals required, etc). This is probably one of the hardest things for a lot of companies to adapt to/adopt.

1. **Default to open**. There’s probably no harm in most people having access to most of your work communications. If there is harm, consider why. It turns out there’s actually a lot of good to be had here.
2. **Trust people to make good decisions**. You hired them, hopefully because they are good. Don’t optimize for the lowest common denominator. Implement minimal policies/guard-rails to help people keep making good decisions.

### Communicate, Communicate, Communicate

I firmly believe that communication is critical to any successful endeavor, but when you are in a remote or distributed context, that criticality is amplified and multiplied. In an office or shared space there’s a certain amount of ambient or baseline communication — you run into people in a hallway, you see them flip a table or slam a laptop shut, you overhear a conversation — online you have none of that. You have to get a lot more intentional, and probably a lot more “prolific” in your communication. Overcommunicate. What you think is overcommunicating is probably not. So communicate more than that. Then figure out a sustainable pace. When people are not communicating in remote work, they become invisible. Invisible is bad. Over time it tends to indicate someone is disengaged, struggling, or already checked out. Don’t be invisible.

Get really good at illustrating and explaining things in written form, because it’s still the native format of the internet. Supplementing with [videos](https://www.loom.com/), diagrams, animated gifs or whatever else works is very valuable, but the written word still rules. In the almost-11 years that I’ve worked at Automattic, I’ve written 1,769,219 words across 29,620 posts and comments on our internal P2s. I’ve probably written a similar amount across IRC and Slack (about 2,000 messages a month on Slack), and have consumed/read multiple times that many.

The vast majority of our communication (see below for more detail) happens via:

1. [P2](https://p2theme.com/)
2. [GitHub](https://github.com/)
3. [Slack](https://slack.com/)
4. [Zoom](https://zoom.us/)

### Optimize for async

When everyone is working from their own space, on their own schedule (might not be relevant if you continue requiring people to work 9-5 in your local timezone, but it’s a big part of the benefit of distributed work), it becomes really important to make sure people can work independently (“asynchronously” from each other). That doesn’t mean that they always have to work on their own, but they should ideally never be blocked or held up because of someone or something else (that’s out of their control). Avoid requiring people to constantly interrupt each other just to keep moving. Write everything down. This is a weird cultural shift for some orgs, but we make sure all decisions especially, but often the discussions that lead to the decision, are published internally as written text. It requires people to be able to communicate their ideas clearly, in sentences (and diagrams, videos, whatever else), but becomes more and more valuable over time. “If you can’t link to it, it doesn’t exist” is a common refrain for us. We often refer back to conversations or decisions from months, if not years ago.

Some specific tactics:

1. **Document everything**. Having things documented and available to reference means people can self-serve rather than having to ask/interact on every little detail. This goes for decisions, architectures, vision, mission, roadmaps, project plans, discussions, processes, etc. We’ll explore a few options for *where* to document things further down.
2. **Prioritize unblocking other people**. Do whatever you can to make sure that other people are never waiting on you for anything. Sometimes that means telling them you’re going to take a while, or that you’re not going to do something. That’s better than waiting.
3. **Reduce cycle time on communication**. Compress greetings and questions into a single message/exchange, rather than “hi, are you there?” (delayed response) “cool, can i ask you a question?” (delayed response) “how do i…”, just send it all together so that the other person can see, prioritize, and respond in a single hit “hi beau! don’t know if you’re the right person to ask this, but how do i…”.
4. **Anticipate possible responses and provide alternatives**. This is a variation on the above, but instead of doing something like asking “does this time work for you?” and then possibly having to go back and forth, it’s faster over all to offer a few options, and anticipate that the first option might not work. The same goes for all sorts of interactions, where you can ask a question and add “if not that, then what about…” alternatives.

### Spend time face to face

Sorry coronavirus, but this is actually a key part of making remote work successful longer term. This one might not be as relevant in the current environment, since presumably you already know your coworkers and have spent time together, and the whole point is to avoid being face to (coughing) face. For us, it’s really important to get together a few times a year and really get to know our coworkers. Spending some time with people allows you to get to know them on a level that I’ve just never seen replicated through the types of transactional, work-based video chats we normally do (more on that later).

We normally hold meetups at the team level once or twice a year, and at the entire company level once a year. They go from ~4 days to a full week, and people are together “24/7” during that time (except sleep, of course) during that time getting to know each other, planning, working on projects, participating in activities together (like going on photo walks, bike tours, museums, cooking classes, all kinds of stuff).

---

OK, so now that you have some of the underlying concepts, let’s look at a day in the life. I’ll try to break this up into some chunks that make sense, and we’ll dive into some detail here and there where I think context is useful. Feel free to ask in the comments if something doesn’t make sense, or you’d like more examples or whatever.

---

## A Day In The Life

I mostly work from home. Some people prefer co-working spaces, cafes, libraries, or whatever, but my schedule tends to be heavily-laden with video calls these days, so it’s easier for me to just work from home most of the time. I’m lucky enough to have space for a separate office, and no one else is home during the day, so it’s quiet and I can avoid distractions (or distracting others). I don’t know how people do it when they’ve got a whole family at home with them. I used to work at a stand up desk (literally) inside a closet because New York. It worked for a while, but I don’t miss it at all. As you can see below, I have a Mac laptop, with an external screen. In the second photo you can see that I use the built in keyboard on the laptop now. I go back and forth using an external mouse and just using the built in trackpad.

![Remote Work At Scale](https://dentedreality-content.s3.amazonaws.com/wp-content/uploads/2020/03/11143416/IMG_8102-scaled-1.jpg)![Remote Work At Scale](https://dentedreality-content.s3.amazonaws.com/wp-content/uploads/2020/03/11143416/IMG_8102-scaled-1.jpg)

My standing-desk-in-an-IKEA-closet when I lived in Brooklyn.



![Remote Work At Scale](https://dentedreality-content.s3.amazonaws.com/wp-content/uploads/2020/03/11143416/IMG_3682-scaled-1.jpg)![Remote Work At Scale](https://dentedreality-content.s3.amazonaws.com/wp-content/uploads/2020/03/11143416/IMG_3682-scaled-1.jpg)

My sit/stand desk at home in Denver. Obviously I cleaned up a lot for this photo.


### Schedules & Timezones

1. Set your own boundaries/delineation between work and non-work. It turns out your commute was doing that for you.
2. Timezones are terrible, and will likely require you to be a bit more flexible with earlier/later appointments.
3. Setting some scheduled time to work might be better than being super flexible.

I usually get up at about 7:15am. I try to have something resembling breakfast, but highest priority is coffee and breakfast is often skipped until later in the morning (or entirely). I think the cool kids call that intermittent fasting? Whatever. I make a single mug of [very nice pour-over](https://bivouac.coffee/) every day, and try not to have more than that unless I’m really dragging. I have no real need to leave the house in the morning, although when the weather warms up it’s nice to get outside and walk around the block, check out my garden, or otherwise get some fresh air. I actually miss my previous commute of about 20 minutes once in a while, because it was a great time to read, listen to a podcast, and just “mentally prepare” for the day. Sorry productivity experts, I don’t meditate, go to the gym, journal 1,000 words or all of the other “must haves” in the morning.

Once I’ve got my coffee, I will take a little bit of time to read something non-work-specific, and “ramp up” a bit. Sometimes that devolves into trawling Twitter and Instagram. Then I’ll start checking in on Slack, P2s, etc (more below) and get into the swing of the day.

Thanks to timezones (uuugghhhh), and my teams being spread all over the world, my mornings are often heavier on calls/”meetings” (hi, UTC+!). I try not to schedule anything earlier than 8:30am, but sometimes I’ll have something important or unavoidable at 8, or as early as 7:30. I’m pretty non-functional earlier than that. Since I’m on Mountain time, and since we tend to have fewer folks in the APAC region, my afternoons are when I can get more of my own solo work done. Don’t get me started on Daylight Savings Time. You think it’s bad within the US? Combine that with different timezones and DST schedules across the rest of the world.

I try to end my day around 5:15pm by going to the gym (or doing something else) rather than just having the day fade out and me wandering out of my office to flop on the couch (literally 5 steps away). Setting boundaries is pretty important when you’re working from home (or are you living at work?). I’m quite bad at setting those boundaries myself so having something like a scheduled session at the gym helps force the end of my day. Sometimes I’ll come back and work more in the evening, but at that point I’m making a decision rather than just sliding into it. It turns out that a commute is good for something — explicitly starting and ending your work day.

I’ve experimented with much more flexible schedules over the years (split time early and late, weekends, etc), but have found that I work better and more sustainably if I just set clearer boundaries, and keep it roughly in line with a “normal office work day” (in my timezone). While I may have a flexible schedule, my wife and friends don’t, so if I want to spend time with them, it’s easier to just be at least roughly on the same hours as them. I also need to be available for certain scheduled calls/interactions, so that dictates things to an extent.

### Calendars, Calls, & GTD

1. Zoom for video and audio calls.
2. Google Calendar (and Fantastical) for calendaring/schedules.
3. Google Docs for collaborative docs, meeting notes.
4. Calendly for external scheduling.
5. Dynalist for personal productivity/lists.

What you refer to as a meeting, I probably refer to as a call. All of my calls are done through Zoom. You could use Google (whatever their latest renamed video conf thing is), or any number of alternatives, but Zoom works well, and everyone at the company is on it so it’s the easiest for us. I use a [Sennheiser headset (this one is USB-C!)](https://www.amazon.com/gp/product/B07P68C7Y7/) to improve audio quality. For most calls (especially repeating ones like 1:1s with direct team members/manager), I use running [Google Docs](https://www.google.com/docs/about/) where we both/all have access and can set agenda items and take notes collaboratively. Some teams use something like [HackMD](https://hackmd.io/) to similar effect, but despite its weight, I think Google Docs feels pretty natural and works well. Add a link to the doc in the calendar invite so you can always find it. Always send an invite so that everyone has the event on their calendar. Move important things/summaries to P2 (more below) so others can find and reference it easily. Consider recording the video/audio of a call if it would be useful for others to watch/reference as well.

Speaking of calendars, I use [Google Calendar](https://www.google.com/calendar) (via [GSuite](https://gsuite.google.com/)) to schedule everything and then have [Fantastical](https://flexibits.com/fantastical) on my Mac to help keep on top of multiple calendars (personal/work/others). GSuite works well to easily add other people within the company, confirm availability etc. If something is not in my calendar, I’m unlikely to remember to do it, so I schedule in personal stuff as well, and include blocked out chunks of time to get things done.

I use [Calendly](https://calendly.com/) when I need to give someone (especially external) the ability to quickly find a 30 minute slot in my schedule.

It’s changed multiple times over the years, but I’m currently using [Dynalist](https://dynalist.io/) to keep track of my own things that need doing. I’m not using a strict [GTD](https://gettingthingsdone.com/) approach, but I have some daily lists, longer running stuff, repeating items etc, and try to move everything to a list somewhere if I’m going to actually do it. I also use [iDoneThis](https://idonethis.com/) (via an [Alfred](https://www.alfredapp.com/) shortcut) to track what I do throughout the day.

### Active Communication

1. Slack for immediate or ephemeral communication.
2. Use emoji reactions for fun, efficiency, empathy, emotion.
3. Zoom for screen sharing/pairing.
4. Weekly (possibly more) team sync calls.
5. Multiplayer mode required for everything.

#### Slack

We use Slack a lot. When I started with Automattic, we used [IRC](https://en.wikipedia.org/wiki/Internet_Relay_Chat) (really!), so Slack is an upgrade, but fundamentally it’s pretty similar. We do have a lot of automated bots posting into Slack for various things (new P2 posts, GitHub activity, outage alerts, all kinds of stuff), and some that we can interact with for various workflows. We also have some automations around adding/removing people from certain channels and groups which make it easier to notify groups to certain things, or know where you’re supposed to go to talk about something.

Within Slack we have (lots of) channels based around all sorts of things. Every team has their own. Most large projects have their own. We have some announcement-only ones for various levels of the org (entire company, different roles, business units within the org). There are channels for specific working groups and cross-team groups as well. There are watercooler channels for all sorts of things (#bake, #great-outdoors, #bike, #gardening, #fishin, you name it). Mostly they’re public, but there are definitely a lot of private groups and DMs as well. More than we’d like/like to acknowledge, but at our size you do start to have a lot of conversations that either need some level of privacy, or it’s just easier to pull in a specific group.

I think Slack is generally good for quick questions, clarifications, updates (“here’s what I’m doing today”) and things like that. It’s bad for nuanced topics, things that require a lot of detail or thought, or anything you’d like to be “evergreen” (something you might reference later). We encourage people to move to P2 for those sorts of things, as well as for documenting decisions that might get made in Slack. It’s dangerously-good at being distracting though, so you need to manage your notifications and availability carefully. I think emoji-reactions are a deceptively powerful addition because they allow for micro-interactions while conveying a surprising amount of information. We have 7,954 custom emoji in Slack (😱).

Teams at Automattic mostly have at least one synchronous call a week. Depending on your role and what you’re working on you might have more than that (sprint planning, solving a specific problem etc). These calls are all scheduled to try to cater to the timezones of those involved, and on a cadence that makes sense (most either weekly or [fortnightly](https://en.wikipedia.org/wiki/Fortnight), some monthly). They are a chance to spend some time with your team, chat through personal (get-to-know-you) and work things, hash out blockers, plan for the upcoming period, etc. We heavily encourage teams to post notes from their meetings covering what was discussed and any decisions or actions to come out of the meeting.

#### Zoom, and…

Ad-hoc calls are used when you need to get into a deep problem, discuss something in more detail or at a faster pace than is possible via Slack or P2, or if you need a higher-bandwidth back and forth (e.g. diagramming, design, whiteboard style). I mentioned Zoom already, and it’s the tool of choice for most calls/meetings. It’s also used a fair bit to supplement other real-time collaboration such as screen sharing and pair programming. We’re in the process of onboarding a few junior engineers and they’re spending a lot of time in “knowledge transfer” and pairing sessions with more senior folks (all over Zoom), learning, watching, asking questions, etc.

[MURAL](https://mural.co/) works quite well for a lot of post-it or diagramming type collaboration, and I love [Whimsical](https://whimsical.com/) for certain types of diagrams. I’ve heard good things about [Miro](https://miro.com/), but haven’t personally used it. Our designers all love [Figma](https://www.figma.com/). Opening a Zoom audio channel while collaborating on any of these tools adds an extra dimension to the interaction, and of course multiplayer mode is critical for anything to be useful in this area (e.g. they need to be good at real-time, multi-user interactions).

### Async Communication

The hallmark of a good collaboration tool in my mind is that it can span across async and sync collaboration, while it probably leans more towards one or the other. I think Google Docs leans more towards async (write a bunch of stuff, then someone reads it all in one hit), but it’s also good for real-time collaboration as mentioned above. [Notion](https://www.notion.so/) is the new hotness in this space and a lot of people seem to love it, but I haven’t really used it much so can’t comment too heavily.

#### P2

[P2](https://p2theme.com/) is the evolution of a WordPress theme we built within Automattic over a decade ago to help us communicate internally. We wanted something longer-form and more thoughtful than IRC, but more dynamic than monolithic-feeling blog posts. It uses WordPress (of course!), and provides a more real-time feel (live-updating posts/comments), formats things in a more conversational manner, and elevates comments to be closer to posts in importance. It leverages the full media (embedding, linking, etc) capabilities of WordPress, and allows you to use tags, @mentions, and a bunch of other tools that make collaboration easier. I use Google Docs extensively to draft things for P2 publication when I expect to have others collaborate/give feedback before publishing.

Similar to Slack, we have P2s for “everything”. Teams, projects, announcements, roles, watercooler topics, etc. I just checked and we’ve got 989 different P2s in various states of activity. We customize our P2s *very heavily*, mostly through CSS, so that each one has its own personality. Because it’s all WordPress, we can also change menus/navigation, add widgets to the sidebar, make posts stick to the front and other things.

P2 is what I would consider the central communication system for Automattic. It’s the longest lived, most consistent thread throughout the history of the company. We control (and host) it completely, have customized it heavily, and added things like the ability to search across all of them in one place, get notifications when any [regular expression](https://en.wikipedia.org/wiki/Regular_expression) is matched within our network of sites, all sorts of custom syntax and embed formats, etc etc. As I mentioned it’s also based on WordPress, so it’s interoperable with all sorts of tools including most of what we build on WordPress.com (especially things like notifications), the WordPress mobile apps, and more.

#### GitHub

Most of our engineering work happens in GitHub these days, although we do still have some code bases in Subversion (and using [Phabricator](https://www.phacility.com/phabricator/) on top of that). We have hundreds of repos across multiple organizations that are a mix of public (open source) and private. We use project (kanban-style) boards a lot, and some teams also include tools like [Zenhub](https://www.zenhub.com/) or [Asana](https://asana.com/) as part of managing their projects. We’re generally pretty disciplined about writing good commit messages/issue descriptions, labeling things, etc. We treat most work as if it could be public, which changes the tone of interaction, and the expectations around documentation and workflows.

### Archive Communication

Once they’re no longer active, our P2 interactions form a part of the greater Automattic corpus. They become part of the “archive”, although they’re never truly static. Everything has a permalink (including comments), and you can always go back and add more detail later. For the most part things move into a “read only” state after a few weeks.

P2s also usually have (WordPress-style) *Pages* (static pages, outside the normal chronological flow of a P2) that are used for P2-specific documentation, similar to a mini Field Guide (below). Teams use these for their own context-relevant documentation, some projects might have them on their own P2, etc.

#### Field Guide

One last thing worth mentioning would be our Field Guide. This is our employee handbook, but it also includes all sorts of evergreen documentation, processes, and reference material. It’s another WordPress site, and uses a theme that makes it work similar to a wiki (or Notion). Anyone can edit it, add to it, etc, and it’s referenced heavily when onboarding new folks, establishing new processes, and formalizing things.

For more about different types of collaboration, check out this excellent post from my colleague Erin: [The Three Speeds of Collaboration: Tool Selection and Culture Fit](https://intenseminimalism.com/2015/the-three-speeds-of-collaboration-tool-selection-and-culture-fit/). I like using Active, Async, and Archive, because… alliteration and mnemonics.

---

That’s all I’ve got to share for now. There’s a ton of other interesting things to talk about in a distributed environment, but hopefully this gives you something to work with, some idea of how we operate at Automattic, and perhaps sparks some questions. Good luck out there, and let us know how it goes for you. This is going to be a huge learning experience for a lot of people, so I think it’s going to be valuable if people share what’s working and what’s not, especially in companies that are trying to rapidly move to a more remote model.