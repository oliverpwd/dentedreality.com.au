---
title: Cargo Culting Software Engineering Practices
date: '2022-06-14T21:20:36-06:00'
format: link
service: instapaper
tags:
- read
external_url: https://isthisit.nz/posts/2022/cargo-culting-software-engineering-practices/
---

[Cargo Culting Software Engineering Practices](https://isthisit.nz/posts/2022/cargo-culting-software-engineering-practices/)  



Three months into my first Big Tech gig I was talking to a mentor about the overhead involved with the way the organisation worked. Meetings for standups, tech huddles, refinements, retros and product reviews; Processes such as limiting work in progress, desk checks, spikes, stories, and tasks. Coming from a startup we delivered high quality software without all of that labelled process. The mentor lent me his copy of *Extreme Programming* by Kent Beck, and that book gave me a framework to develop my own philosophy on software delivery and engineering practices. Since then I’ve followed Beck’s writings and talks.

I recently came across an interview with Beck from 2019 where he talks about his time at Facebook. He joined Facebook in 2011 when the organisation was 700 engineers, and left in 2018. The interview goes into a lot of technical detail on interesting scaling problems organisations like Facebook encounter. What interested me most, and is the topic of this blog, is around engineering practices; ie. agile ways of working, quality practices, design patterns, and feedback loops.

It’s 2011 and Beck, already a software engineering luminary, joins Facebook. He expects it to follow common and uncontroversial software engineering practices, perhaps even some of those he writes about. Instead:

> It’s crazy, it looks like a clown show and yet, things are working really well. They weren’t doing the things in my books. I like to joke, I don’t mind if people don’t do this stuff in my books. I just want them to fail. They weren’t doing that. I thought, well – My first thought is I’ll come in and explain how this stuff works.
> 
> In the back of my mind, there is this mystery of this bumble bee. In theory, this process should  
> 
> be a disaster and in practice, it’s working extremely well at two things at the same time; at  
> 
> scaling and at exploration. I wanted to figure that out.

During a hackathon he runs a class on Test-driven Development.

> Nobody’s using TDD, so well, of course, they’ll want to learn from me … The class just before mine on the list of classes was about advanced techniques in Excel and it  
> 
> was full and there was a waitlist. The class just after mine was on Argentinian tango and it was  
> 
> full and there was a waitlist. I had zero people sign up for my class. I thought, “How am I going  
> 
> to have any impact here, if people don’t listen to me?”

Starting writing code:

> In boot camp, you’re supposed to put code into production the first week. I was very careful to write tests and do everything properly. I got in a fair amount of heat, because my first feature didn’t land for three weeks. People are like, “Man, I don’t know how this is going to work out.” Well, and I was wondering that too. I had a huge case of imposter syndrome when I landed at Facebook and realized just how different everything was.
> 
> Then the tests that I had written broke almost immediately. They were deleted. That was one of the things that surprised me. If you had a test and it failed, but the site was up, they just delete the test. If you had tests that were intermittent, that were non-deterministic, they were just deleted. At first, I was shocked. Like, delete a test. This is producing noise and it’s not producing signal. If you eliminate this noise production, per definition the situation is clearer all of a sudden. The fact that you wish that you had a test for something, well you didn’t. Yeah, just chuck it and let’s move on.

When in Rome..

> I deliberately chose to forget everything I knew about software engineering. I just said, “I’m  
> 
> going to try and be a programmer and I’m going to watch what people do. I’m just going to copy  
> 
> what they do. If somebody says this is two diffs instead of one, it will be two diffs. If somebody  
> 
> says you need tests for this, I’ll write tests. If they say you don’t need tests for that. Why are you writing tests? Then I won’t write tests, even if I think that’s my – that’s the natural thing to do.
> 
> That’s the only way that: One, that I was going to be able to explore this mystery of how this software engineering process worked. Two, this is the only way that I was going to have any influence, because clearly, nobody was going to listen to me based on reputation.

What engineering practices can other companies and startups learn from Facebook?

> Nothing. People should figure out what their style is and do their style. I’ve been talking about software process for a long, long time. Something I notice is there are people who are uncomfortable taking responsibility. They want a process where they can say, “Well, hey, we executed the process. We failed, but we executed the process.”
> 
> I think losing that and realizing that there’s no such thing as a technical success, that you’re all in it together and that your process is your process and you should play with it, you should experiment with it, you should try out a bunch of ideas. In the end, it needs to be yours. I think that’s the real lesson. Facebook did that. They did things that weren’t conventional, not because they were unconventional, but because it made sense in the Facebook context.
> 
> Everybody should be doing that and not copying – Spotify is the flavor of the month. Well, let’s copy the Spotify model. Well, Spotify didn’t copy the Spotify model, so what makes you think copying is the right thing to do?

So how should one look at engineering practices then?

> You can only be fairly certain of the things you’ve tried yourself in your context, and only as – and those decisions are like fish. A month later, you should definitely question their value. If you let go of this low, what should our process be and say, what should our process be for refining our process, if you let go of the need for an answer and you embrace answering as a continuous process, then I don’t think you can do better than that.
> 
> Just because there isn’t one way that works, there are a bunch of ways that work really badly. There are a few ways that work well, and I think of them as attractors in the space of process. There’s a few ways that work well and there are a whole bunch of ways that work horribly. The first thing to do is identify where you’re doing something that’s horrible and stop doing that.
> 
> We can write useful stories about software development process, but they’re stories, they’re not recipes. The person listening to the story is going to have to take it in and digest it and apply it in their own specific context, because every single day at every single company is a different context. Of course, the answer is going to be different. The inputs are different.

## Teams and Engineering Practices

Job titles, both formal and not, can influence how teams conduct engineering practices. In some situations this is an enabler, in others it reduces the autonomy teams have over their engineering practices.

*SCRUM Master™* is an obvious one; those teams aren’t going to be following Kanban or whatever delivery methodology is trending on Twitter.

Teams with a *Software Tester* will approach Quality Engineering very differently to those without. Ideally testing should be automated, but if there is headcount for a tester then investment in automated tests will have a different relative value.

On-call comes into play here as well. As engineers we should be writing our software to *not* fall over the second a cosmic ray hits the server (or AWS Lambda floating in the ether). By mandating on-call it sends a message to the team: no amount of engineering, quality, or resiliency work they do is enough to mitigate having to sleep beside your phone. How will this change the way those engineers write software?

Teams must revisit their engineering practices. Familiar practices are great, the team has learned them, and they require relatively little overhead to execute. But the context of the team is always changing. It could be new personnel, new software, or a transition of software such as a prototype into stable service. It’s more important engineering practices be effective than easy.

## This Software Will Self Destruct in 3-2-1

What are the largest factors that influence the engineering practices we adopt? What about those which can we never know ahead of time? Here’s a thought experiment.

In an ideal world the Software Engineering we do, and the practices we carry out, should be the absolute minimum required. Where this minimum is some combination of product value, reliability, maintainability, team happiness, etc. To work our way towards finding this minimum,  

what if every time we started a project we talked about when it will be shut down? Would knowing the deprecation date of the service, before it’s written, effect the software engineering practices used?

We already carry out the minimum approach in some frames:

* For scripts that will run once we don’t write unit tests or a changelog.
* For code bases we want to iterate on we invest in writing the CI/CD stack.
* For systems that need to be reliable we invest in logging and monitoring.
* For systems that are long-lived we choose languages, frameworks, and platforms that we believe will be around in 10 years.

Asking this question on production systems such as databases and APIs is much more difficult. We don’t know if it will still be running 2, 5, 10, 20 years later, but I think there’s value in trying to narrow it down. From the engineering team’s perspective, they can pick a technology stack, architecture, and engineering practices which fit this horizon. From the organisation’s perspective they now know when this liability of a codebase needs to be replaced.

–

The full interview with Kent Beck is available: [audio](https://softwareengineeringdaily.com/2019/08/28/facebook-engineering-process-with-kent-beck/), [transcript](https://softwareengineeringdaily.com/wp-content/uploads/2019/08/SEDFB15-Facebook-Process-Kent-Beck.pdf)