---
title: Incremental Note-Taking
date: '2021-07-26T22:14:25-06:00'
format: link
service: instapaper
tags:
- read
external_url: https://thesephist.com/posts/inc/
---

[Incremental Note-Taking](https://thesephist.com/posts/inc/)  



I’ve been delving deeper into the vast and strange world of knowledge organizing tools (notes apps, contact organizers, personal search engines). During this rather abstract expedition, one of my goals has been to emerge with some opinionated thesis about the way these tools should be designed to harbor and extend our knowledge effectively.

Though I’m hesitant to say I’m there yet, I’ve found myself repeatedly coming back to a group of related ideas I’m going to call **incremental note-taking** about how to best gather knowledge into notes, and how we should design tools [built around this workflow](https://thesephist.com/posts/tools/). This post is one attempt (of hopefully many more) to share them with you. This is a longer post, so here’s a roadmap. If you’re impatient, I suggest you begin with the *principles*.

1. – a story of how I arrived at the ideas in this post
2. – my current beliefs about how to build a good note-taking system
3. – how existing tools support (or don’t support) taking incremental notes, and some insights into the tools I’m building for myself today

![](https://thesephist.com/img/incremental.jpg)![](https://thesephist.com/img/incremental.jpg)

## Good notes should behave like memory

At its best, a good collection of notes is like a powerful extended memory. It helps us quickly answer questions like, “What did this person tell me?” “What should I remember about this topic?” “What things am I currently working on?” We think tens of thousands of thoughts every single day, and the job of a good note-taking system is to help us make the most of them, even when our squishy, biological brains can’t.

Curiously, most of the thoughts we think are not what traditional note-taking apps consider “important”. **The mind is like an iceberg: most of our everyday thoughts go unnoticed.** By this, I mean: Most productivity solutions focus on the 10% of our thoughts that are easy to categorize and structure, like lecture notes, meeting minutes, people’s contacts, and highlights of readings. But the vast majority of thoughts we think – the other 90% – still hold underrated, underestimated latent value. In these 90% are things you pick up in conversations, only to forget by the next minute. These are the shower thoughts and ideas that slip past you so elusively, and to-dos that you let yourself forget because they’ll come back if they’re really *that* important. Without the right tools, our minds are hopelessly leaky. We forget much of what we think.

In an ideal world, we won’t have to forget things from our minds and workspaces. We could live in an [infinite room for thought](https://thesephist.com/posts/medium/#an-infinite-room):

> What if, on a single sheet of paper that lasts an entire lifetime, you could inscribe every thought you’ve ever had? It would be the written version of Jess’s infinite room for thought. Every idea you have would have a place here. In a perfect world, when you stumbled across a new idea that relates back to a previous memory, you’d simply take a pencil and draw arrows from this new idea all the way back to the ideas that came before. In this way, we’d construct an infinite *transcript of our thoughts* that was our life’s canvas for ideas. This infinite notebook would reflect the way we learn – we would connect related ideas together to trace out a web of memories, and label and sort them for future recollection.

This kind of an “infinite room” or “infinite paper” behaves like our memory. Our memory doesn’t ever really run out of space (though some ideas fade out over time). Our memory is also much less selective about what is remembered than most of our knowledge tools. We don’t remember things because we’ve somehow deemed something worthy of remembering, we simply remember things *because they’re remembered*, because they happened, because they stuck in our minds. I think a great note-taking system should inherit these properties of memory to properly extend it.

An age-old note-taking method that preserves these characteristics of memory is to [carry a small notebook](https://christine.website/blog/gtd-on-paper-2021-06-13) with you wherever you go. Christine Dodrill writes in the linked blog post:

> Paper is cheap. Paper is universal. Paper doesn’t run out of battery. Paper doesn’t vanish into the shadow realm when I close the window. Paper can do anything I can do with a pencil. Paper lets me turn back pages in the notebook and scan over for things that have yet to be done. Honestly I wish I had started using paper for this sooner. Here’s how I use paper:
> 
> * Get a cheap notebook or set of notebooks. They should ideally be small, pocketable notebooks. Something like 30 sheets of paper per notebook.
> * Label it with the current month (it’s best to start this at the beginning of a month if you can). Put contact information on the inside cover in case you lose it.
> * Start a new page every day. Put the date at the top of the page.
> * […]
> 
> And then just write things in as they happen. Don’t agonize over getting them all. You will not. The aim is to get the important parts.

In this method, we take notes with a pencil in small handheld notebooks, each labelled with a month. We note things down and cross things out over time as ideas occur to us in the course of days and weeks. Paper notes created by this workflow aren’t some evergreen, digital garden, so much as a record of our thoughts and actions in life. No need for “edit history” here – the history is alive in between pages of crossed-out and postponed tasks and ideas.

Though I don’t personally have a pencil-and-paper workflow, I can see the appeal of this kind of a note-taking system. It records your thoughts *over time* – how they change, where they came from, when they came to you, and the context in which you had them. Just like the way we remember things in time, these notes improve by *growing incrementally*, with each new line and entry. Old notes become outdated, but are never replaced. And recalling past ideas is as simple as flipping through the pages to go back in time.

For some reason, when we moved our workflows into the digital realm, we began to lose respect for this way of taking notes, of simply adding new information to an ever-growing log of our thoughts. Instead, we built tools that encourage us to keep only the most current version of reality. Popular tools like Notion and Roam Research are about maintaining a timeless web of ideas, but life is anything but timeless! Old guards like Evernote feel much more like well-curated collections of notes over time, but it’s so difficult to organize and connect ideas in those apps that they quickly become black holes, where notes go in but rarely come out again. Most notes apps these days don’t lead us to collect notes, so much as simply keep them up to date. In that transition, I think we’ve forgotten the power of keeping notes over time, and remembering our past through our old notes.

**Incremental notes** is my push against this trend of note-taking tools that only live in the present and deny the reality of learning and living through time. We don’t remember things by modifying our past memories – we simply accumulate more, as if adding entries to a log or a journal. We search through them by traversing time, looking for links between ideas and experiences. These are the principles from which I want to build tools that augment our minds. With such tools, hopefully, we’ll be able to make more of the 10% of our ideas we’ve already retained, and hold on to much more of that lost 90%.

## Principles of incremental notes

When designing something as complex as a note-taking system, I find it useful to lay down a few ground rules, the “principles” of the domain, to help make the right trade-offs. I’ve condensed my principles of incremental note-taking into four big ideas.

1. **Captured ideas are better than missed ones.** No self-respecting “note-taking system” should ever allow an idea to escape our minds un-recorded because it took too long, or was too much of a hassle to write it down. In order to make the most of the invisible 90% of our ideas that float through our minds, we need a tool that can capture ideas in the moment, however fleeting. This means our tool has to be fast, and can’t burden you with questions like “In what folder should I put this?” that aren’t relevant in the moment.
2. **Adding new ideas is better than updating old ones.** When our notes become outdated, our natural instinct is to go erase what’s now incorrect and fill that blank with the new information. But in that rewrite, we lose all of the original context we could have remembered about the history of our idea. Updating notes in-place is inherently lossy, and I think it’s unnecessary. Very often, it’s useful to have a record of our processes – how we came to some understanding, how we learned something through experience, how our relationships with the people close to us have changed over time. One of my favorite things about keeping handwritten notes is that the *history* of my thoughts are right there, next to my latest and greatest ideas. If we simply erased our old notes every time our understanding of the world changed, we would quickly forget how we got here. Just as our memory grows by remembering new things rather than “updating” old memories, our notes should also grow by incrementally gaining new knowledge, rather than replacing old valuable ideas with more recent ones.
3. **Ideas that can’t be recalled are worse than useless** – effective search and recall form the soul of great notes. Apple Notes (the notes app that comes pre-installed on all iPhones) is probably one of the most widely used knowledge capture systems in the world. Nearly everyone I know who owns an iPhone uses Apple Notes for *something* in their lives. The tragedy of Apple Notes is that it’s an idea black hole. Most of what goes into the app never leaves it again, because people rarely remember what they need to recall, and searching for the right things in an Apple Notes collection is tough. Of course, keyword search is not the only way to recall notes. Many tools these days have time and location-based reminders, as well as references and backlinks to connect related notes together into a graph. Regardless of how you recall information back from your notes, a great note-taking system should make it trivial to get ideas out, as well as in.
4. **Time is essential to how we remember**, and should be a first-class concept in a good note-taking system. The moment in time when we learned or thought something isn’t just some arbitrary metadata, it’s a mental anchor we use to remember nearly everything. We use daily and weekly planners, divide up school into semesters, plan engineering tasks into two-week sprints… time is absolutely essential to remembering what we learn. Whatever tool we use should recognize this, and help place our knowledge in the context of time.

Taken together, these principles of incremental note-taking lead us to a note-taking system designed less like a place you must “move into” with all your past notes slung behind your shoulders, and more like an extra layer of memory you [grow around yourself](https://thesephist.com/posts/ivy/), incrementally and gradually over time.

## Tools for incremental note-taking

I’m at the very early days of putting these ideas and principles to use, but I want to share my perspective on existing note-taking solutions through the lens of incremental notes, and a few experiments I find interesting that put some of these principles to use.

Many of the current crop of popular note-taking tools, like Notion, Roam Research, Obsidian, and whatever you use at work (probably), are about helping you build a snapshot of your world *as it is today*. Some of them put some of these incremental note-taking principles into practice, but few of them honor all four faithfully.

### Notion

[Notion](https://www.notion.so/) is probably the worst offender of them all – calling Notion an effective “note taking” app that extends your memory would be charitable. Notion is great at what it does, which is helping everyone easily create a shared web of documents that look and feel great. But it is not a note-taking app. It’s too slow to capture every thought I have. Its search is rudimentary and rarely helps me find the one thought I’m looking for. And it’s not designed to be used to recall thoughts from my past self. As far as I can tell, it’s primarily designed to act as a source of truth for a team. You can bend Notion to do most of these other things, but the result is slow and unergonomic. When you have just a moment and your idea is about to slip through your mind, you probably aren’t going to open a new page in your Notion workspace to add a quick note.

### Roam (and others)

[Roam](https://roamresearch.com/) and its clones fare much better. Roam is designed to help you incrementally build up a connected, sophisticated knowledge graph of ideas. It doesn’t force you to figure out exactly where to place every idea you record. Instead, you just write things down, perhaps on a “Daily notes” page, and connect each thing to other related things. If Roam can become and stay fast, I think it’s a promising platform for taking incremental notes. But Roam’s notion of time is weak at best – each day is treated as just another “thing” in a Roam graph of notes, rather than a first-class concept around which the tool is designed. In Roam, my thoughts don’t live “in time” – moments in time are just a special kind of idea. It doesn’t really make much sense, and I think this is a place where Roam has stayed too axiomatic for its own good.

### Mira

The first tool I personally built that embodied the incremental note-taking principles is probably [Mira](https://thesephist.com/posts/mira/), which I still use a year later as my primarily “people notes” app. I built it to replace my ever-growing mess of a note about everyone I knew and wanted to keep in touch with. Mira is fast – it often loads fully in the time it takes for Notion to start showing its loading spinner. After a conversation with someone, I always go back to Mira and add a few things I remember from the conversation, marked by the day’s date. When I open the app, Mira will show me people I’ve spoken to most recently, based on the conversations I’ve recorded. This means Mira is aware of time. In Mira, I rarely ever delete something from my past notes. Rather than removing “works at GFC” and replacing it with “works at Ideaflow”, I simply add a new entry: “Spoke at a tech dinner in New York, now working at Ideaflow”. In this way, Mira is a collection of notes grown incrementally over time. It describes a world changing through time, rather than a snapshot of it today. Lastly, Mira has some structured and free-form search. It’s lacking, but hopefully improving soon.

### Ideaflow

[Ideaflow](https://thesephist.com/posts/ideaflow/), the note-taking software I help build at work, also embodies many of these principles. In fact, Ideaflow is my current “main” notes app. Ideaflow’s main interface is a timeline of notes, what we’ve internally called your “thought stream”. Imagine a long Twitter-style timeline, where each tweet is a note of some arbitrary length, potentially linking to many other notes. Many of these notes are short and simple, like random ideas or interesting links I read on the subway. There are even little facts I probably wouldn’t have put in my notes in most other apps, like transcripts of important emails and a list of publicly accessible bathrooms around the city. These are the 90%, underneath-the-surface thoughts that don’t really belong anywhere specific. Of course, there are also detailed, long-form notes like plans for conference talks, a folder of potential blog topics, records of conversations, and project ideas. Between my 980 notes today, there are around 1250 connections linking people to conversations, companies to investors, and ideas to their progenitors and other ideas inspired by them. So in a sense, incrementally, over time, Ideaflow helps me built up a sophisticated knowledge graph too. But in Ideaflow, time is a first-class citizen. Rather than a haphazard web of connections and words, notes go neatly into a timeline, grouped by days and weeks. This organization works together with my natural memory to help me remember things in units of time that I already use to understand my life. When I learn something new, I simply push another note onto the top of my timeline of notes, perhaps something connected to an older idea. Over time, this web grows denser and more populous like a forest of ideas growing around my life. I’m biased, of course, but I’ve found what I’ve been using so far to feel like a *true* extended memory, more than simply another database of facts.

### Inc(remental)

Most recently, this week I began hacking on a tool called **[inc](https://github.com/thesephist/inc)** (short for “incremental”), a minimal notes app that delivers only the features promised by the principles above, and little else, in a small command-line driven package.

Inc is an experimental, [append-only](https://en.wikipedia.org/wiki/Append-only) notes app. This means you grow your notebook by adding information to existing notes, or adding new notes; never modifying older ones. This approach to taking notes feels strange at first. Why would we want a notebook where we can never update our notes? What if something about the world changes?

Rich Hickey, in his talk about the design of the Datomic database, gives us the answer:

> If my favorite color was red and now it’s blue, we don’t go back and change the fact that my favorite color was red to be blue – that’s wrong. Instead, we add a new, updated fact that my favorite color is now blue, but the old fact remains historically true.

In other words, this database (like our memory) doesn’t update information by forgetting what was once true, and overwriting it with the new fact; instead, it simply remembers that the fact changed at some point in **time**. Using this approach, we can have a notes app where we only add new information, and never delete old ones. (With this approach, it’s also obviously extra-important for our tools to understand time.)

Inc is currently just a command-line utility with a few commands:

* `+ Some note about #ink` adds the note “Some note about #ink” to my notes. `#ink` is a tag I might use to search through my notes more effectively, but it has no special meaning beyond showing up in a different color in the app.
* `/some keyword` searches my notes database using the keywords, and gives me a numbered list of the matching notes. Because the results are numbered here, I can then take another action:
* `@12 Goes to Stanford` adds the information “Goes to Stanford” to note number 12 returned from my previous search.
* Typing `history` shows us the full edit history of my notes database. In Inc, the way my notes *came to be today* is just as important as the information it currently holds. Using the history, I can rewind my notes back to any specific day, or just remember what I learned at any point in the past.

There are a few other shorthands and commands, but this is the core of Inc. Thought of something? Write it down in seconds. Trying to remember something? Search for it immediately. Want to review and understand your notes? Sift through time with a full history of your notes. Inc is focused on quickly capturing what’s on your mind, growing a knowledge base incrementally around your life, and helping you understand your notes with a first-class concept of time.

![](https://thesephist.com/img/inc-history.jpg)![](https://thesephist.com/img/inc-history.jpg)

Above is how I use Inc in practice, to manage development of Inc itself, captured in the form of an `inc history` output. The most visible parts are all the notes I add, but in between them are the quick searches I do to remember and keep track of my ideas, and the occasional history lookup to help myself remember what I was doing, and place myself in the right mental context where I left off.

Truth be told, Inc is a new project (as are Ideaflow and many other projects in this space), so my hypotheses about incremental note-taking and the way these tools work are only so strong. But as a good investigator should, I want to hold myself to these principles laid out here, build tools around the **incremental note-taking workflow**, and see where the ideas take me. Perhaps I’ll come to believe them even more over time. There’s also a good chance I’ll correct myself, and look for a new thesis. Regardless, I’m excited by the vast design possibilities we’ve yet to explore in this space of building tools that embrace and extend the way our minds make sense of the world.

Thanks to Jared Pereira, Jacob Cole, and Jess Martin among others for the many conversations with me that have led, sometimes through long winding paths, to my thoughts in this post.

I share new posts on my [newsletter.](https://thesephist.com/#newsletter)  

If you liked this one, you should consider joining the list.

Have a comment or response? You can [email me.](https://thesephist.com/#get-in-touch)