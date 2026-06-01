---
title: Building Great Engineering Teams
date: '2020-09-27T22:30:36-06:00'
format: link
service: instapaper
tags:
- read
external_url: https://evolutionarymanager.com/building-great-engineering-teams-gergely-orosz/
---

[Building Great Engineering Teams](https://evolutionarymanager.com/building-great-engineering-teams-gergely-orosz/)  



![](https://images.unsplash.com/photo-1519389950473-47ba0277781c?ixlib=rb-1.2.1&q=80&fm=jpg&crop=entropy&cs=tinysrgb&w=2000&fit=max&ixid=eyJhcHBfaWQiOjExNzczfQ)![](https://images.unsplash.com/photo-1519389950473-47ba0277781c?ixlib=rb-1.2.1&q=80&fm=jpg&crop=entropy&cs=tinysrgb&w=2000&fit=max&ixid=eyJhcHBfaWQiOjExNzczfQ)

If you have ever come across [The Pragmatic Engineer](https://blog.pragmaticengineer.com/), you probably know the man behind it, [Gergely Orosz](https://twitter.com/GergelyOrosz). More than a simple blog, or newsletter, it is a treasure trove of knowledge on the ins and outs of Engineering, Engineering Management and, in general, all things leadership in tech. As the website name implies, Gergely is all about pragmatism and helping engineering leaders develop themselves, while delivering massive value to their companies and those around them.

![](https://evolutionarymanager.com/content/images/2020/09/orosz-resized-1.jpg)![](https://evolutionarymanager.com/content/images/2020/09/orosz-resized-1.jpg)

Gergely Orosz

Exploring the interface between Product and Engineering, and building world-class Engineering teams are two interrelated topics that we both share as interests. For that reason, I invited Gergely for a chat with me to continue the discussion I started here in an [earlier conversation](https://evolutionarymanager.com/chasing-agile-rainbow/) with my good friend [Mohammed Rizwan](https://twitter.com/kettiby).

**Gergely, thanks for joining me. Tell us a little about yourself and your background.**

I’ve been in engineering for more than a decade, starting at smaller companies, but then joined JP Morgan where I worked for a year. JP Morgan was more an investment bank than a tech company but I learned a lot about finance. Then I moved to Skype, which had just been acquired by Microsoft and we were building Skype for Xbox One in London, collaborating with the Xbox team in Redmond. That was a really good experience, working with a US-based company but from Europe. Then I moved to Skyscanner, where I built a small mobile team, building a B2B travel tool.

Finally, I moved to Uber, which has been a really good learning so far. I joined the Amsterdam office when it was about 25 engineers, and three years later we were up to 150, essentially almost doubling every year. I actually joined as an engineer – which gave me the opportunity of knowing the codebase – did that for 6 months and then became a manager. Eventually, I started leading multiple teams and managed my first manager in a bigger group. Initially, my team owned everything payments in the Rider app but now we’ve transitioned to a platform based approach. I would call it a platform-focused team with product impact.

**That’s actually a good segue into the first question. How do you think about understanding the value of what the teams build and deciding what to work on?**

When I joined Uber, we changed directions more frequently based on new priorities coming fromTravis Kalanick, like adding tipping to the app. This time was very much about growth and making bold decisions. Now, with Dara as CEO and the business environment maturing, I would actually compare it to how Amazon operates, with a focus on efficiency, getting to profitability and operational excellence.

At some point, I started to put my foot down on not starting to work on a project that did not have some sort of impact estimated. Uber is big on data driven decisions, with lots of data scientists, and PMs typically pair with them. So we’d estimate impact on everything and then just stack-rank it. This, by the way, doesn’t necessarily have to be dollars. With tech debt work, engineers often say we should refactor this API, for example. Well, what’s the impact? If it’s a system that’s going to be retired or has little to no users, then the impact will be meaningless. So you have to ask yourself: are we saving money? Is it about reliability? Is it reducing frustration? Often people will say, “You know what? You’re right, it doesn’t make sense”. Or, “Holy Moly! This has impact on so many people”.

One example of not using dollars to make business decisions was how a Developer Experience team made the case that 6-core Macbooks would compile the mobile app 30% faster, shaving off around a minute for each compilation. Multiply that by 400 engineers, each doing a few builds per day, and it adds up to a lot. This is how this team upgrading to better hardware for mobile engineers at the company. I found this data-driven approach eye-opening…

**A key element of high-performance in tech teams is visibility into how the team operates and therefore the ability to surface issues earlier. How do you think about this in the context of your teams?**

A lot of people are doing the whole JIRA thing, looking at story points and velocity. I personally am not a huge fan of deferring to these metrics. To me, first you need a spec that makes it clear what the work is and why it’s important. Not many things are formalized at Uber, but two things are: first, the product requirements specification, owned by the product managers, which also needs to be signed off by the business. In the past,I have seen projects built where legal later came in and stopped the launch. In that case, months of work went to waste. Another thing we do is an engineering plan, no matter how lightweight it may be.

My approach then is to think more in terms of milestones rather than sprints. For example, we had this massive project building Skype for Xbox from the ground up. We broke down a year-long project to four milestones: something like audio, video, chat and production-ready. And regardless of JIRA and boards, the question was always: what is the next milestone? And what can we do about it? So until audio calling were not working, we weren’t doing anything on video. Everyone swarmed, helping get audio up and running first. I like to replicate this teamwork focused on finishing the current milestone.

Also for visibility, and because I believe in helping people grow into more leadership roles, I typically ask the teams to write up a weekly email update, including maybe one or two stakeholders, describing current progress. This pushes accountability on the teams, acting as a sort of contract I like to have. And it helps you stay focused on what the next milestone is.

**Love the clarity in that. Another aspect I find critical is the ability to change, both in terms of the code and the teams themselves. How do you look at maintaining “changeability” in the face of extreme growth?**

At Uber, where I’ve been for the past 4 years, a good chunk of time has been spent on [migrations](https://lethain.com/migrations/), just because we grew so fast. For example, many of our old systems were built on the assumption that we’d be doing Rides only, and now you have Eats and Freight and other new businesses. In an environment like this you just have to get good at migrations. When you start doing it a lot, you learn what the costs are and how to do it well.

I think people sometimes [overthink architecture](https://blog.pragmaticengineer.com/software-architecture-is-overrated/), and spend far too much time on this area, upfronts. You can try to build all these beautiful systems that are easy to customize and extend but that really is an unrealistic goal. My two cents is that infrastructure is more important than architecture: when it’s easy to deploy, monitor, spin up a new service – and Uber is a good example of this – you end up with thousands of microservices because it’s just so easy to do it. So you can build a service with monitoring and start moving things over. That’s not possible if it’s really hard to set things up with data included. So I would say, focus on infrastructure and worry less about maintainability.

The other thing about changeability is that struggling organizations usually have leaders who haven’t gone through the “migration hell” of a fast-growing organization before. But if you don’t act in tackling your tech debt, you’ll start to have churn and you can lose your best engineers over a matter of years. So next time around, as a leader you’re going to put your foot down and maybe you’ll be at a VP or CTO level position. At Uber, I observed our CTO understanding this and creating time for engineering to tackle tech debt that was caused by the fast growth. For example, the whole company did Fixit Weeks – a week to tackle tech debt – and engineering foundations work was prioritized at the company level. You can, of course, do a lot of this bottom-up but if people at the top don’t appreciate the importance of it, as an engineer, you’re bound to get frustrated.

**Wade Chambers, a former VP Engineering at Twitter, once said the role of any Engineering Manager is to win and to increase your capacity to win. It resonated with me a lot in terms of continuous improvement. How do you promote that explicitly within your teams?**

I find that when a new team comes together, they learn really fast. If you just give them a basic framework, and you’re solving new problems and you reflect on them and how you did it, you improve a lot. Autonomy helps greatly as well. Instead of getting a project manager who’ll tell everybody what to do, I [give that autonomy to the engineers](https://blog.pragmaticengineer.com/a-team-where-everyone-is-a-leader/), with some guardrails. So the people in my teams tend to eventually all become pretty decent project managers.

Continuous improvement comes from pushing teams to commit, giving them space to fail and then ensuring there’s reflection on what happened and what we should change. So that’s one way to grow. The second thing is being ruthless about not doing manual work. In most cases, either figure out how to automate it or don’t do it, which might require thinking outside the box.

I tell people that I’m always accountable for what we do, and our projects, which means that if someone should get in trouble or get fired, that someone should be me, the engineering manager. And in return, I ask others to take on responsibility for their work. Hopefully, this creates an environment where failure is not a problem but something we can learn from. Whatever happens, as long as someone tells me what they’ve learned and how they’re going to change things, I’m super happy. And, by the way, there’s this great book about this mindset called [*Turn the Ship Around!: A True Story of Turning Followers into Leaders*](https://www.amazon.com/Turn-Ship-Around-Turning-Followers/dp/1591846404)*.* I recommend this book for people to read.

So, in the end, continuous improvement boils down to “forcing” or encouraging people to think on their feet, come up with suggestions and have them follow through with it. I’m curious about your own take on this, as I am likely biased on this.

**I subscribe to everything you said and would add that the expectation that we must always strive to be better than the day before – that a world-class engineering team is made of world-class habits and practices – should be set explicitly. And I try to showcase what good looks like, for example by sharing the best examples happening in the teams in my internal communication (e.g. bi-weekly emails).**

Yeah, I think it’s really important to aim for “world class”.

**One last question, Gergely. You already mentioned** ***Turn The Ship Around*** **but what is another book you’ve often recommended or gifted to other people?**

I would say both [*The Goal: A Process of Ongoing Improvement*](https://www.amazon.com/Goal-Process-Ongoing-Improvement/dp/0884271951/ref=sr_1_1?crid=HOPIBFIHFY9H&dchild=1&keywords=the+goal&qid=1599567330&s=books&sprefix=the+goal%2Cstripbooks-intl-ship%2C226&sr=1-1)and, for new engineering managers especially, I would recommend James Stanier’s book, [*Become an Effective Software Engineering Manager: How to Be the Leader Your Development Team Needs*](https://www.amazon.com/Become-Effective-Software-Engineering-Manager/dp/1680507249/ref=sr_1_1?dchild=1&keywords=james+stanier&qid=1599567409&s=books&sr=1-1). I enjoyed that one because it adds a very fresh voice to the topic. *(Gergely has a number of* [*great book recommendations on his website*](https://blog.pragmaticengineer.com/my-reading-list/)*.)*

*If you enjoyed this content, you will probably enjoy* [*The Weekly Hagakure*](https://hagakure.substack.com/)*, a weekly newsletter to help tech leaders build better teams and more humane workplaces.*

*You can also find me on Twitter [@prla](https://twitter.com/prla/). Join the conversation!*