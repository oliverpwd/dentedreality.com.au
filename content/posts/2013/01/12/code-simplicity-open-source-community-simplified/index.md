---
title: Code Simplicity » Open Source Community, Simplified
date: '2013-01-12T12:03:48-07:00'
format: link
service: instapaper
tags:
- read
external_url: http://www.codesimplicity.com/post/open-source-community-simplified/
---

[Code Simplicity » Open Source Community, Simplified](http://www.codesimplicity.com/post/open-source-community-simplified/)

> berkun: Excellent post on communities and managing them http://t.co/qh1lbkbU by @mkanat via @nearyd

Growing and maintaining an open-source community depends essentially on three things:

1. Getting people interested in contributing
2. Removing the barriers to entering the project and contributing
3. Retaining contributors so that they keep contributing

If you can get people interested, then have them actually contribute, and then have them stick around, you have a community. Otherwise, you don’t.

If you are just starting a project or need to improve the community of an existing project, you should address these points in reverse order. If you get people interested in a project before you do the later two steps, then people won’t be able to enter and won’t stick around when they do enter. You won’t actually expand your community. So first, we want to be sure that we can retain both existing and new contributors. Once we’ve done that, then we want to remove the barriers to entry, so that interested people can actually start contributing. Only *then* do we start worrying about getting people interested.

So let’s talk about how you accomplish each step in reverse order:

### Retaining Contributors

For the [Bugzilla Project](http://www.bugzilla.org/), this was our biggest challenge. Once somebody started contributing, what made them *keep* contributing? How did we keep people around?

Well, we had an interesting advantage in answering these questions, in that we are one of the older open-source projects in existence, having been around since late 1998. So we had a tremendous wealth of actual data to work with. We mined this data in two ways: First, we did a survey of all our past developers who had left the project, asking them why they had left. This was just a free-form survey, allowing people to answer any way they wanted. Then, we created a graph of the number of contributors over time, for the whole ten years of the project, and correlated the rise and fall of the graphs to various actions we took or didn’t take over time.

Once all this was done, I sent [an email](http://groups.google.com/group/mozilla.dev.apps.bugzilla/browse_thread/thread/520f5aa32917a517/bb7c1a42bcc400d9) that out to the developers Bugzilla Project, describing the results of the research. You can read the whole email if you’d like, but I’ll summarize the findings here:

* **Don’t freeze the trunk for long periods.**
  
  The Bugzilla Project has a fairly-standard system of having stable branches that receive little change (for example, the “3.4” branch where we commit bug fixes and do minor releases like 3.4.1, 3.4.2, etc.), and a main-line “trunk” repository where all new features go, and which eventually becomes our next *major* release.
  
  In the past, before a major release, we would “freeze” the trunk. This meant that no new features could be developed for several weeks or months until we felt that trunk was stable enough to call a “release candidate.” Then we would create a new stable branch from the trunk and re-open the main-line trunk for features. However, while trunk was frozen, there was no feature development happening *anywhere* in the Bugzilla Project.
  
  Graph analysis showed *very clearly* that every time we would freeze, the community would shrink drastically and it would take *several months* after we un-froze for the size of the community to recover. It happened uniformly, every single time we would freeze, over many years and many releases.
  
  Traditional wisdom in open-source is that people like to work on features and don’t like to fix bugs. I wouldn’t say that that’s *exactly* true, but I would say that if you *only* let people fix bugs, then most of them won’t stay around.
  
  We addressed this issue by never freezing the trunk. Instead, we branch immediately at the point that we normally would have “frozen” the trunk. The trunk *always* stays open for new feature development. Yes, this means that for a while, our attention becomes split between the trunk and the latest branch. We’re committing the same bug fixes to the branch and the trunk. We are also doing feature development on the trunk simultaneously with those bug fixes. However, we’ve found that not only does the community expand more rapidly this way, but we also actually get our releases out *more quickly* than we used to. So it’s a win-win situation.
* **Turnover is inevitable.**
  
  The survey found that the number one reason that contributors leave is that they no longer have time to contribute, or that they were contributing as part of their job and now they have changed jobs. Essentially, it is inevitable that most contributors eventually leave.
  
  So if it community members are definitely going to be leaving, the only way to consistently expand the community is to figure out how to retain **new** contributors. If you don’t get new members to stick around, then the community will continuously shrink as old contributors leave, no matter what else you do.
  
  So while retaining existing contributors is important–after all, you want people to stick around and contribute for as long as reasonably possible–what matters the most is retaining new contributors. How do you do that? Well, that’s a lot of what the rest of these points are about.
* **Respond to contributions immediately.**
  
  The Bugzilla Project has a system of code reviews that requires that all new contributions be reviewed by an experienced developer before they can become part of Bugzilla. There have been various complaints about the system over the years, but analyzing the survey data showed that people leave the project because getting a review takes *too long*, not because the reviews are too *hard*. In fact, the reviews can be as hard as you want as long as they happen almost *instantly* after somebody submits a contribution.
  
  People don’t (usually) mind having to revise a contribution. They even generally don’t mind revising it several times. But they *do* mind if they post a patch, don’t get a review for three months, and *then* they have to revise it, only to wait another three months to be told that they have to revise it again. It’s the delay that matters, not the level of quality control.
  
  There are other ways of responding rapidly to contributions, too. For example, immediately thanking somebody for posting a patch can go a long way toward retaining new contributors and “converting” them into long-term developers.
* **Be extremely kind and visibly appreciative.**
  
  For nearly every person who responded to our survey, the factors involved in not staying–beyond “my job changed” or “I didn’t have time”–were surprisingly personal. I know that we all work with computers, and perhaps we’d like to think that engineering should be a totally cold scientific profession where we all do our jobs correctly according to the requirements of the machine, and not worry about our emotional or personal involvements. However, nothing could be further from the truth–the personal interactions that people have with community members, the amount they feel appreciated, and the amount they feel assaulted, are actually the **most important aspects of retaining community members**.
  
  When people contribute on a volunteer basis, they aren’t getting paid in money, they are getting paid in admiration, appreciation, the sense of a job well done, and the knowledge that they are helping create a product that affects millions of people. When somebody has contributed a patch, **you need to thank them**. It doesn’t matter if the patch is total crap and has to be re-written entirely, **you need to thank them**. They have put some work into this, and if you don’t appreciate that, **they will leave before they even start**. After all, most people get little enough appreciation at their workplace–they stay there because they get paid in money! They don’t need to work *for free* with some other organization if it also doesn’t appreciate their work, or even worse, assaults every aspect of their contribution before even thanking them for it.
  
  Of course, you still need to correct people on the faults in their contributions. “Kindness” does not include putting bad code into your system. That isn’t kind to anybody, including the contributor whose skills probably need to improve, and who may go on believing that something they did in error was in fact correct. You have to still be careful reviewers and very good coders.
  
  What this *does* mean is that in addition to telling people what’s *wrong* with their contribution, it’s important to appreciate what’s *right* about their contribution, even if it’s simply the fact that they took the time to contribute. And you have to **actually tell the contributor that you appreciate the contribution**. The more frequently and genuinely that you do this, the more likely you are to retain the contributor.
* **Encourage a total absence of personal negativity.**
  
  One thing that drives people away from a project with lightning speed is when they get personally attacked for attempting to do something positive. A “personal attack” can be as little as an unpleasant joke about their code, instead of just a straightforward technical description of what is wrong. Saying something like, “What is wrong with you?” instead of actually leaving some helpful comment. Disguising personal criticism as “an attempt to help them code better” or “help them get along with others.” No matter how well-justified these actions may seem to be, they are all personal attacks that are extremely dangerous to your community.
  
  Now truthfully, coding and working on a collaborative project with people who have different viewpoints can get really frustrating sometimes, and I’ve been an offender in this area just as much as anybody has been. But we all have to learn that it’s not okay to insult other developers as people just because we’re personally frustrated with them.
  
  The solution isn’t just to say “everybody, now bottle up your frustrations until you explode,” though. There are lots of practical solutions. One of the best is to set up some specific system for handling problematic contributors. If there’s some contributor that Bob just can’t live with, there needs to be somebody in the community who Bob can go to to help work things out. We’ll call this go-to person the “community moderator.” So Bob tells the moderator about the problem, and maybe the moderator sees that other contributor really was being a terrible person or bad coder, and so this “community moderator” gently corrects that contributor. But it’s also possible that there was some communication problem between Bob and the other contributor that the moderator just needs to help resolve.
  
  This “moderator” system isn’t the only way to deal with the problem. You can resolve the problem in numerous ways–the most important thing is that you *do* resolve it. Without some channel or method for dealing with personal frustrations, individual contributors will take these frustrations out on each other. You will in fact foster an environment where it’s *okay* for one contributor to personally attack another contributor, because that’s the only avenue they have to resolve their problems, and nobody’s stopping them.

Basically, those last two points can be summed up as: **be really, abnormally, really, really kind, and don’t be mean**.

We’ve been applying all of these principles in the Bugzilla Project for the past several months, and we saw an increase in the number of retained contributors almost immediately after we started applying them. I’m finally starting to feel like the community is *growing* again, after shrinking almost continuously since 2005 due to violations of all of the above points.

### Removing the Barriers

The next step is to remove the *barriers to entry*. What prevents people from getting started on the project?

Usually, the biggest barrier is a lack of documentation and direction. When people already *want* to contribute, their next step is figuring out *how* to contribute. They will go to your project’s website and look around. They will wonder, “Who do I talk to about this? How do I start contributing? What do you guys want me to work on?”

For the Bugzilla Project, we solved this problem in several ways:

1. **A list of easy starting projects.**
   
   Whenever we see a bug or feature request that looks like it would be easy for a newcomer to solve, we tag it as a “good intro bug” in our bug tracker. This gives us a [list of good introductory projects](https://bugzilla.mozilla.org/buglist.cgi?quicksearch=prod:Bugzilla+whiteboard:%22%5BGood+Intro+Bug%5D%22) that anybody can come and look at without having to ask us “where do I get started?”
2. **Create and document communication channels.**
   
   People will almost immediately want to *talk* to somebody else about the project. You should have email lists and also some method of instantaneous communication like an IRC channel. For example, we have an email list for Bugzilla developers and also an [IRC channel](http://landfill.bugzilla.org/irc/) where almost all our contributors hang out. In fact, we don’t just have a normal IRC channel–we also have a web page that people can use to chat in that IRC channel. That way, people don’t have to install an IRC client just to come talk to us. Setting up that web page enormously increased the number of new people coming into the channel and communicating with us. (And the increase was entirely positive–I can’t think of a single person who used the web gateway to cause us trouble.)
   
   Then once you have these channels, they need to be documented! People have to know how to get into them, they need to know that they exist. We have a [wiki page](http://wiki.mozilla.org/Bugzilla:Communicate) that explains how to talk to us if you want to contribute. (Note that this is separate from our [support](http://www.bugzilla.org/support/) page that describes how to get *support* for the project.)
   
   Also, as a final but perhaps obvious point, the existing community has to *use* the communication channels. If the main contributors do all their work in an office and just talk to the people next to then and you don’t use the mailing lists or IRC channels, then the community members aren’t going to want to use those communication systems either. After all, the new contributors aren’t there to talk to each other–they’re there to talk to *you*!
3. **Excellent, complete, and simple documentation describing exactly how a contribution should be done.**
   
   Fully document every step of your development process, and put that documentation onto a public web site. Don’t invent a new process, just document out what the existing actual process is. How do people get the code? How can they submit patches or other contributions to you? How do those contributions become an official part of the system?
   
   We have a [very simple page](http://wiki.mozilla.org/Bugzilla:Developers) that describes the basic steps of our whole process, and links to documents that describe each step in more detail. It also specifically encourages people to get into communication with us, so that we know that they are there and want to help.
4. **Make all this documentation easy to find.**
   
   This is a simple final step, but sometimes projects forget it! You can have all the wonderful developer documentation in the world, but if new contributors can’t find it *super-easily*, then you’re not actually removing any barriers to entry! We have a big “Contribute!” button on [our website](http://www.bugzilla.org/) that describes all the different ways that people can contribute (not just code!) and links to more information about each of those.

We saw a definite upswing in the number and quality of contributions once we completed all these steps. Also, having everything documented and clearly stated on a public website meant that we no longer had to personally explain it all, every time, to every new contributor.

Direction and documentation aren’t the *only* things you can do though. Ask yourself, “What is stopping people from contributing?” and remove all the barriers there that you reasonably can.

### Getting People Interested

How do you make people think, “Gee, I want to contribute to this project?” That’s the first step they have to take before they can become become contributors. Well, traditional wisdom states that people contribute to open-source projects because:

* They like helping.
* They enjoy being part of a community.
* They want to give back.
* They think that something is wrong and they need/want to fix it.

So you may want to make it apparent that help is needed, that an enjoyable community is there, that giving back is appropriate and appreciated, and that there are problems that need solving.

Now, to be fair, this is an area that I don’t have fully mapped out or figured out for the Bugzilla Project, yet. So I don’t have a lot of personal experience to draw on. But if we analyze other projects, we can see that some good ways of getting contributors are:

* **Be a super-popular product.**
  
  This may seem obvious, but it is indeed the primary way of getting new contributors. If a zillion people use your product, it’s statistically likely that many of them will want to contribute. The Linux Kernel and [WordPress](http://wordpress.org/) are good examples of this–they have millions of users, so there’s just bound to be a lot of contributors, provided that the “barriers to entry” and the “retaining contributors” aspects of the project have also been handled.
  
  One way to *become* a super-popular product–even if you’re just starting out–is to be *heavily needed*. The Linux Kernel was very much needed when it was first written, which is probably one of the reasons that it became popular as quickly as it did. It desperately needed to exist and didn’t exist yet.
* **Be written in a popular programming language.**
  
  Generally, people are more likely to contribute to a project if it’s written in a language that they already know. WordPress has a *huge* contributor community, and it’s in PHP. Say what you will about PHP, it is extremely popular. There’s a large number of people who already know the language, which increases the likelihood that some of them will start supplying patches for your code.
  
  This not the only reason you should choose a particular programming language, but it’s certainly a major motivator if you’re going to have an open-source project. I may think that [Eiffel](http://en.wikipedia.org/wiki/Eiffel_(programming_language)) is a remarkable language, but if I wrote an open-source project in it, I would have a *very* hard time getting contributors.

Beyond those points, there are lots of clever ways of getting people interested in contributing to your projects, including speaking at conferences, publishing blogs, encouraging people on a one-to-one basis, and other methods that basically add up to “contact and encourage.”

I’d love to hear some of your ideas in this area, though. How do you get new people interested in contributing to your project? Has anything been particularly successful?

### Summary

An open-source community is somewhat of a fluid thing–there are always going to be people coming and going for one reason or another. What’s important is that the rate of people entering and staying is *greater* than the rate of people leaving. All of these points help assure that, and hopefully they also make our communities productive and enjoyable places to be for everybody, even ourselves!

-Max