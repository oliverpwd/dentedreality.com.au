---
title: The Principles and Habits of Healthy Software
date: '2022-03-25T18:12:36-06:00'
format: link
service: instapaper
tags:
- read
external_url: https://leaddev.com/building-better-software/principles-and-habits-healthy-software
---

[The Principles and Habits of Healthy Software](https://leaddev.com/building-better-software/principles-and-habits-healthy-software)  



I believe both can help us be better people and drive positive change around us – in general, but in software in particular.

Principles help us go in the direction we want, towards an ideal state. Developing software with this in mind is fulfilling. (If you want to feel inspired about principles, read [Design Principles Behind Smalltalk](https://www.cs.virginia.edu/~evans/cs655/readings/smalltalk.html) by Daniel Ingalls).

Habits are powerful. They help us to get from point A to B at a constant pace, starting small and taking many small steps. They allow us to work towards a higher goal, with purpose. It’s like developing muscles; it’s not possible to get there with a magic meal, you need strict gym activity and a lot of discipline. You also need small increments otherwise you’ll get hurt. So what are the *muscles* in the software we write, and what habits can we adopt to maintain those muscles and avoid injury?

In the title, I also mention healthy software. That’s what I called my [engineering blog](https://ngarbezza.hashnode.dev/), referring to another way to think about how we maintain software. Terms like ‘legacy code’ and ‘technical debt’ bring up negative feelings in the community, and caring for unhealthy (or ‘elderly’) tech feels like a burden for many. There are more [makers than menders](https://corgibytes.com/blog/2015/08/14/makers-vs-menders/), and it seems that we’re still dealing with the same maintenance issues over and over, despite the great work done by [Michael Feathers](https://twitter.com/mfeathers?ref_src=twsrc%5Egoogle%7Ctwcamp%5Eserp%7Ctwgr%5Eauthor) and [Ward Cunningham](https://twitter.com/wardcunningham).

We need to get better at caring for unhealthy software and, most importantly, build more software that’s set up for a long, healthy life. I see this health metaphor as more human, and as humans, health is something we always wish to have and to keep. As developers, we are doctors of software, both curing and preventing problems, and putting health as priority zero all the time.

Here I’m going to share the four key principles that drive my day as a developer (software doctor), tech leader, and change agent, as well as the habits that help me keep up with the principles. I hope you enjoy them!

### **1. Simplicity**

All the projects I’ve worked on that have had maintenance issues had one thing in common: they weren’t simple. Keeping a piece of software simple isn’t easy, but no software is born complex; it gets complex over time.

It’s worth mentioning that complexity comes in two flavors: **essential** and **accidental**. We can’t avoid the former, it comes from the domain we’re modeling, but we can work to reduce the latter. Accidental complexity comes from programming languages, tools, and the poor design decisions we make.

Alright, so we value simplicity… but which habits can help us keep our software simple?

* **Define some complexity metrics and visualize their progress**  
  
  For example, you can tell how complex is your application by looking at the number of dependencies it has. Dependencies add more code to your application code, thus augmenting maintenance costs. Other complexity indicators are the number of endpoints (if the app provides web services) and the number of database tables. Pick one, or a few, and measure how they evolve over time.
* **Think about complexity at a low and high level**  
  
  Complexity at a low level has to do with small pieces of code (like method definitions). For instance, if you have many conditional statements in a method, you can extract them in separate methods or use polymorphism. Dealing consistently with low-level complexity help make the whole application better.
  
  But sometimes this is not enough and we need to think about complexity at a high level. The difficult thing about this is that you need some help to visualize it. One tool I recommend is [Madge](https://github.com/pahen/madge). It displays a graph of all your modules and the interactions between them, providing a visual way to see your app all at once. The more readable the image (fewer boxes and lines) the simpler your project is. It helped me make some important design decisions, and showed me something I could have never seen by looking at code only.

### **2. Sustainability**

In software, we sometimes go faster at a very high cost. If we focus only on the short term, we will end up with technical debt later. That’s why thinking about sustainable development is important. It makes us aware that there is a future in which our software needs to live. You may still have reasons to go faster and take shortcuts, but at least all the design tradeoffs will be more explicit.

Let’s look at some habits that help me think about sustainability:

* **Identify, measure, and address tech debt as you go**  
  
  Most tech debt is acquired unconsciously. Or developers think for a second, ‘this is going to cause issues’, but never record that conversation and it gets forgotten. I recommend adding tech debt tickets to the backlog and linking them in the code when possible (to increase visibility). I also recommend keeping those tickets to a relatively small size. This is important because it increases the possibility of actually fixing them. You’ll have less ‘refactoring sprints’ and more fixing-as-we-go tasks. You can also discuss percentages, for example, ‘this week we’ll dedicate 20% of our time fixing tech debt’.
* **Constant, small-scale refactorings**  
  
  Did you come across a poorly named variable? Go ahead and rename it. Adding comments, extracting small methods, relocating files are also good examples. IDEs make it easy nowadays. Those things do not take much time, and if we never stop doing them, the overall quality will increase. And (super important) do not ask for permission. You are the expert so trust your judgment about quality. Plan your big refactorings, and do the small refactorings right away.

### **3. Immediate feedback everywhere!**

Feedback is important to adapt and learn. The more immediate the better. That’s the essence of test-driven development (TDD): very short iterations with feedback between each one. Could we apply this philosophy in all software engineering activities? How long are our feedback loops? What information comes from our feedback loops?

There are multiple habits you can adopt to have more feedback, but here are the top two:

* **Keep the tests fast and accurate**  
  
  Having unit tests and even doing TDD is not enough to make sure the feedback is accurate. Keep an eye on continuous integration times. Rank your slowest tests and prioritize fixing them. Identify flaky tests and fix them. Write powerful assertions; these messages can help you to spot problems and make sure the tests pass.
* **Integrate changes often**  
  
  We sometimes forget that integrating changes closes a loop and it may generate some interesting feedback. Your solutions need to coexist with all the rest of the app. Integrate and test how your system behaves. I’m referring to both integration from your dev branch into the trunk, and from the latest trunk changes into your branch. I’m not saying anything new; continuous integration is one of the twelve XP practices identified by Kent Beck back in 1999. The interesting question to ask ourselves is not ‘do we have continuous integration?’ but ‘how continuous is our integration?’

(For more inspiration on this topic, check out  [this series of posts](https://www.geepawhill.org/series/many-much-more-smaller-steps/) by GeePaw Hill.)

### **4. Humans behind lines of code**

Making software is a human activity. We build software for humans *and* computers, and we mustn’t forget the human aspect. We need to make sure we work as a group and that our behavior is appropriate.

Again, we can adopt a lot of healthy habits in this area:

* **Empathy as a default**  
  
  The way you perceive and interact with the world should include empathy, including when you are reviewing code. Behind every line of code, there’s a human with a unique history, feelings, learnings, insecurities, and so on. Also, if you know something another person does not know, try to kindly explain it, the way you wish you had learned it. ([No feigning surprise](https://jvns.ca/blog/2017/04/27/no-feigning-surprise/) when people say they don’t know something is a great piece of advice from Julia Evans).
* **Keep knowledge distributed**  
  
  It’s easy to end up with knowledge silos. I see them all the time. The only way to avoid this is to proactively work on enabling spaces for team interaction as we build pieces of our software. Here are some examples of ways you can empower knowledge sharing:
  + *Pair/mob programming*: I’d say this is the most efficient way to share knowledge. Depending on the individuals, pairing may be something that naturally emerges or needs to be planned. It doesn’t need to take the entire day or be for the entire ticket/story. I’ve seen pairing better when it’s sporadic, when we feel we need it.
  + *Design sessions:* before tackling an important piece of work, it’s worth gathering to talk about the problem we’re trying to solve, making sure everyone understands it, and starting to think on different solutions with pros/cons analysis for each one. High-level drawings are good at this point.
  + *Learning spaces*: gather together to look at how X works, or to play with a new technology. It’s like a ‘nerd’ space, where everyone can build the agenda. Give the space a cool name so it sticks into your team culture.
  + *Document architectural decisions*: Understanding *why* something was done in a particular way is very helpful when looking at code that was already written, perhaps by people that are no longer in the organization. This type of documentation will help you to explain the work in the future, either for yourselves in X years or for other people. I recommend [Architectural Decision Records (ADRs)](https://adr.github.io/) which is a known pattern and a way to keep documentation closer to the code.

### **Reflections**

Habits, principles, and healthy software are the words that resonate with my career and have helped me to be a better professional. Try reflecting on your experiences and come up with some words of your own that might help (or have already helped) you and your team.

Alternatively, try defining your own principles. Discuss them as a team, write them down, or have them somewhere defined in a digital format (it can be inspiring!). Revisit them if your team structure changes, and reinforce them in day-to-day discussions. Keep in mind that both human and technical aspects are important. Whatever principles you build should take both into account.

Finally, you could reflect on the habits you already have. Which of them are healthy? How can you keep accountability? How small are your increments? Could you start smaller? This type of thinking takes time but it’s well worth the investment, and could be the difference between good and great software. Good luck!