---
title: Written Communication Is Remote Work Super Power
date: '2020-09-21T23:32:39-06:00'
format: link
service: instapaper
tags:
- read
external_url: https://snir.dev/blog/remote-async-communication/
---

[Written Communication Is Remote Work Super Power](https://snir.dev/blog/remote-async-communication/)  



**Update:** An interesting discussion around this started in [hacker news](https://news.ycombinator.com/item?id=23577228)

The remote work environment is different from the office. Different environments call for different communication systems. A communication system that is adapted to the remote work reality can unlock amazing benefits: (even) better productivity, a competitive advantage in the long run and much a better work-life balance on top of it all.

Asynchronous written communication is the tool best suited for remote work. We are so used to talking to each other in the office, expecting immediate responses in work chat, and having meetings all day, that we tried to replicate that at home with zoom and slack.

Writing to each other in slack while expecting immediate answers, or setting up multiple zoom meetings every day will fail with remote work in the long run.

![](https://snir.dev/blog/remote-async-communication/remote.jpg)![](https://snir.dev/blog/remote-async-communication/remote.jpg) Photo by Goran Ivos on Unsplash

# Chats and video calls are problematic

Using synchronous chats such as slack or Microsoft teams is not like talking to a teammate that sits next to you:

* It’s harder to initiate. When it’s a teammate beside to you, just talking is far easier than typing a question. This leads to quick and easy thing being dragged on longer than necessary because the teammate will first try to resolve it himself.
* It’s too easy to initiate. When it’s someone from different department, on the office he will usually first check up with his own teammates. But now, it’s as easy to go directly to the source. So you’ll be spammed.
* Everybody expects an immediate response. It’s a chat. It’s designed to give us the feel of urgency. Even when it is not really urgent.
* You’ll lose your history. Even if you invest time in explaining a concept of the company to someone in the chat, it’s not saved anywhere in an organized or discoverable way. It’ll be lost in the chat logs. Soon enough, you’ll find yourself explaining the same stuff again.
* It promotes secrecy. People are naturally shy, and prefer not to show “weakness” to other teammates. So they will keep their questions and updates mostly in private chats or private rooms.

Video meetings are problematic too:

* Only one person can talk at a time. In reality, more than one can talk and still everyone will be able to understand. This is a software limitation.
* No side-talks. In reality, in big meetings you might whisper something to a sub-section group of people in the meeting. You can’t do this in video meetings.
* This all leads to video meetings feeling more like a lecture. A true discussion is harder to facilitate (although not impossible).
* Video calls are tiring. The camera is focused on your face and everyone sees you all the time. You can’t lose focus or wander away to give your mind some rest.

# Synchronous communication is problematic

Even if we discard the specific tools of chats and video calls, we still have the underlying problems of synchronous communication. That is, communication that expects the other participants to respond within a very limited time span.

Having that expectation promotes bad work culture and limits your flexibility.

When everyone is expected to be available at any point, the cost of interrupting someone and getting an immediate answer is lower than looking for an answer yourself. Be it in the 3rd party documentation or the company’s internal documentation.

That is, if internal documentation even exists. When everybody expects to be asked about things anyway, why go through the effort of properly documenting anything?

Planning is another culprit. Most people will not go through proper in-depth planning for their tasks ahead of time. They’ll prefer to define the end goal, and discover issues and details as they go. They know they will never get stuck, people will answer their questions on time.

This creates a culture of interruptions in the organization. It feeds itself so deeply, that the organization can’t really operate without interruption. Since the organization as a whole is dependent on that, it becomes part of the culture. Once you have culture of interruptions, even the best communicator in the world will not be able to change it.

Work time flexibility will be broken too. Since everyone is dependent on everyone else to be available for interruptions within the work day, you have a work day.

You must be in sync about your work day times with everyone else. You therefore give up the ability for real work time flexibility.

Working from home and dreaming on picking up your children at noon, hangout with them and get back to some work later in the night? Forget about it. You will get stuck on something very quickly and no one will be there for you. Not to mention you will get your colleagues stuck as you won’t answer their questions on the afternoon.

Real remote is out of the question too. You can’t realistically have team members from the US and Europe and India together when you need everyone to be available at the same time.

# Async writing can solve this

Writing intentionally for asynchronous communication can solve all the issues mentioned above.

Async writing is different from chat messages. It lives longer, targets more potential audience and is easy to discover.

To live longer, the text needs to be aware of a larger reader group context. Where chats often consider just one/two readers that have the context to understand what you talk about, the long live text should consider entire group of potential readers. Now, and at some point in the future.

For the text to live longer and target wider audience, it needs to assume less pre-existing reader context. Chat messages target one/two readers, at a specific time. So they assume those readers have the current context that will be clear to them specifically.

Async writing don’t assume a specific person context nor does it assume “current” events knowledge. Surprisingly, that doesn’t necessarily make the text longer or harder to write.

As an example, we consider a scenario where we have a DB issue in our team in which the MySQL instance fails occasionally due to out-of-memory errors. Writing just for your team, they know what is the issue now and what DB it is. Others, might not know which DB have the issue (say you also use mongodb somewhere) not they know what the issue is.

A message sufficient for chat context that will not live long might be: “I’ll fix the DB today”. Async text equivalent will be to log the issue in a system, mark it as “working on it” for today with the text “MySQL out of memory issue”.

The text is not longer, yet it has all the context any outsider might need to understand what is going on without the need to contact anyone asking “What DB we have issue on?” “What is the issue?” “Since when do we know about it?” “Who’s on it?” etc’ etc’.

![](https://snir.dev/blog/remote-async-communication/async_chat_example.png)![](https://snir.dev/blog/remote-async-communication/async_chat_example.png)

Discoverability is the next essential part of this communication system. You need your writings to be easily discoverable for everyone who might need them in the future.

Relying on full-text search is usually not a good idea. You need organization system in place. Where tasks description go? Where the system design documents go? Do they all live in one place or per project? Or maybe per department in large organizations?

Every company have some sort of system, usually guided by their knowledge sharing too. Be it Jira, Basecamp, Monday or anything else. You just have to make sure the system is consistent and tight enough such that new people in a project will be able to self discover everything they need.

Taking the MySQL issue example here too, let’s say a new team member gets the task. The task is marked with tags “database”, “infrastructure”. He can follow the “database” tag to find recent past tasks done, to see if there are any obvious suspects.

He finds none, so he decides to check if some data analyst did something spooky. He goes to the tasks list of the data analyst teams, finds tag “new dashboard”. Those look like a great lead, he find a new dashboard task was done the day the issue started.

Now he needs to check out this dashboard, but it uses a visualization system he is not familiar with. He heads to the data team wiki, where he finds a document on “how we use our visualization system”. He sets up his credentials and gets in to explore the queries.

You see where I’m getting with it. When everything is easily accessible and obvious, you can focus on the task itself without interruption to the flow.

Imagine a scenario where in each step you’d have to stop and ask someone:

* Josh from my team: “Hey, did someone do something to the DB recently?”
* Dani from data team: “Hey, did you launch or changed any heavy query recently?”
* Ramon from data infrastructure: “Hey, how do we use our visualization tool to edit a dashboard?”

In this case, you are dependent on other to be available and to remember all the answers. Your flow is constantly interrupted without any way to progress before you get answers. You can’t focus on flexible work time, because you must have all the team members constantly available.

# Key takeaways

In this essay I described why in my opinion synchronous communication as we use to do from the office is not optimal for remote. Then I demonstrated how async communication via writing can fix most of the synchronous communication culprits.

* Synchronous communication while remote rely on chats and video calls, both are inferior communication tools trying to mimic office conversations. But they are not.
* Synchronous communication is tiring, repetitive and takes away most of the remote work benefits (such as flexible hours, hiring from all over the world etc’)
* Async communication allows for self discovery without interruptions:
  + You can keep on your flow without waiting for someone to give you details
  + You can get into “deep focus” session without context switching that allows for better productivity
  + You can work whenever, since you are not dependent on anyone immediately
* Async communication preserve the company knowledge better:
  + You have written records of everything
  + Tutorials and guides are constantly refined, so people won’t waste time on the same thing twice
  + You have one place for knowledge via writing, instead of private knowledge in private calls or chat room that is lost soon after