---
title: Seniorless — 4 Tips for Effectively Onboarding Juniors
date: '2020-05-13T13:47:26-06:00'
format: link
service: instapaper
tags:
- read
external_url: https://medium.com/@gabrielgrinberg/seniorless-4-tips-for-effectively-onboarding-juniors-50268ab8df0a
---

[Seniorless — 4 Tips for Effectively Onboarding Juniors](https://medium.com/@gabrielgrinberg/seniorless-4-tips-for-effectively-onboarding-juniors-50268ab8df0a)  



# Seniorless — 4 Tips for Effectively Onboarding Juniors


[![](https://miro.medium.com/fit/c/96/96/0*oZR4AQidfPIPmyxf.jpg)![](https://miro.medium.com/fit/c/96/96/0*oZR4AQidfPIPmyxf.jpg)](https://medium.com/@gabrielgrinberg?source=post_page-----50268ab8df0a----------------------)
[Gabriel Grinberg](https://medium.com/@gabrielgrinberg?source=post_page-----50268ab8df0a----------------------)
[Mar 30](https://medium.com/@gabrielgrinberg/seniorless-4-tips-for-effectively-onboarding-juniors-50268ab8df0a?source=post_page-----50268ab8df0a----------------------) · 8 min read



The previous post — “[Seniorless — 5 Reasons You Should Hire More Juniors](https://medium.com/@gabrielgrinberg/seniorless-5-reasons-you-should-hire-more-juniors-cb6fdfd03f63)” was about why juniors are a great, and even essential, assets to your engineering group.

Of course, hiring non-experienced members comes with risks/costs. The main reasons I get from other team leaders for not doing so are:

1. Training and onboarding is hard and time consuming
2. There are no “junior” suitable tasks in my team

In this post, I’ll try to share some of the lessons learnt from 5 years of hiring and onboarding juniors, hoping that you’ll get answers for both #1 and #2.

# **1. Task Based Formal Training**

The first student that moved from support to our team had no formal onboarding process. The team was small and the tech stack was *far* simpler. If you knew *some* Javascript and a bit about how the web works, *we could use you*

Since then, the web development world had huge advancements that made a classic on-job-training very inefficient.

For the next couple of members that joined, I felt like a structured, formal training system was mandatory. I started to throw every topic I felt one needed to know in a paper. The year was 2015, and knowing basic JS was not enough. One needed to have some basic knowledge of TypeScript, Angular, SCSS, testing, Node and even Gulp (!) to add value to our team.

I didn’t have the time to write/curate training material for all the required topics, nor did I believe that just reading tutorials was enough. Instead, I tried to imagine a small isolated task, that if accomplished, would provide a strong signal of one’s understanding of a topic. Each skill / topic in our training kit would have one task or more, with a reviewable result.

A great example of this is the “Basic HTML & CSS” skill. There are countless guides and courses about HTML & CSS. It would be pretentious of us to write our own guides to it. So what we did was simply define a task — to create a static pixel perfect replica of our help center. I threw in some links for recommended learning materials, but the focus was on the task.

If one completed the task, it’s a great indicator that he knows HTML & CSS. It gives us far more confidence than passing some course. Throw in a 10 minute review from a mentor, and the learning is almost maximized.

![](https://miro.medium.com/max/1104/1*iyD8foAdH1FY6fZz7JBGJQ.png)![](https://miro.medium.com/max/1104/1*iyD8foAdH1FY6fZz7JBGJQ.png)



For our recent hirings, we created a very structured, formal and task-based training for new members. The topics are varied, and include industry specific topics (JS, React, Typescript), skills related to the Wix ecosystem, and skills devoted to learning our domain (i.e, build your own website using [Corvid](https://www.wix.com/corvid)).

So while the internet is full of great (and no so great!) material, by defining short and independent tasks you can achieve great confidence that the topic is well learnt, and also empower self-learning — a priceless skill in our modern world.

Also, with proper mentorship review feedback on the tasks can increase the learning effectiveness significantly.

**Pro tip:** create a task that embodies a mini-version of your app or a model version of a real feature you created. For us, it is creating a simplified version of our article management dashboard, a task that involves combining together all previous skills learnt. This is done with our real stack, adding a real page to our app (which is never merged to master, of course 😉 ).

# **2. Well Defined Mentorship & Review Process**

So let’s say you have great training material, and everything is task-based.

Now you need someone to review those tasks. At first, I was the only one doing the reviews. The team was small (3 other members) and it made sense. Later, when the team grew, most of the team could provide great feedback on the basic level tasks (i.e. basic React training). I understood that their feedback can be better than mine, as they suffer less from the [curse of knowledge](https://en.wikipedia.org/wiki/Curse_of_knowledge). They have been in the mentee’s shoes not long ago and can better relate to the learning process.

![](https://miro.medium.com/max/1104/1*pzRfz1BZtMCjsggSbP0TWw.jpeg)![](https://miro.medium.com/max/1104/1*pzRfz1BZtMCjsggSbP0TWw.jpeg)



In our team, each new member is assigned a formal mentor. The mentor’s responsibilities are reviewing completed tasks, monitoring the training progress and helping out with all the logistics (from installations and accounts and up to finding the best restaurants around).

The main guideline for mentors is to invest only around 10%-20% of their time with their mentees. We feel it’s enough for an optimal combination between self-learning and proper feedback and review. Thus, reviews should be brief, focused on what matters and ensure understanding of the topics to the required level.

**Pro tip:** mentors and reviewers shouldn’t necessarily be the most experienced. On the contrary, we try to search for the most *inexperienced* member that qualifies for a task to take it, and reviewing onboarding tasks is no exception.

# 3. Mix Training & Contribution

At Wix Answers, we split our tasks into 4 types:

1. **Tiny tasks —** small bug fixes or CSS tweaks. Small tweaks to existing features. A good indicator for this task type is that it usually results in a small modification of an existing file, and not a creation of new files / modules.
2. **View components** — we’re big believers [of separating the view layer](https://medium.com/@dan_abramov/smart-and-dumb-components-7ca2f9a7c7d0) of our components and the logic. Creating isolated, tested and designed view components has its challenges, but is a great next step after small bug fixes. View components are derived from features that other, more experienced members are working on.
3. **Small features** — a full end-to-end feature, involving no more than 1 active member. Usually a new section or page in our app. Unlike the **view components** step, this step involves communicating directly to all stakeholders (server, PM, QA, designer).
4. **Large features** — features involving other members as well. Owners of “large features” are considered their techleads and are in charge of performing syncs, providing estimates and mentoring members.

By formally acknowledging the various task types we can create a fragmented training process, and ensure that each training part is mixed with tasks from the previous section. For example, by the time a member is training for the “small features” phase she is an active contributor to view components.

Mixing contribution and training has proven a great tool to maximize training efficiency & the value each member brings.

**Pro tip:** formal learning shouldn’t stop in the first 3 months, it should decrease in intensity. We all are in a constant learning path, and if you as a manager manage to formalize further steps of this process into your team member’s day to day routine, it will ensure healthy growth and happy members.

# 4. Well Defined, Gradually Expanding Tasks

As a young manager, my first inclination was to assign hard & ambitious tasks to my team members. I was sure that this was the best way for one to learn and for me to show trust one’s work.

However, it’s easy to forget that aside from the task itself and the challenge it brings, there is usually a large component of implicit knowledge involved — that thing that comes with what we call *experience.*It might be related to your project’s setup, undocumented feature, legacy code, office politics and what not. Such nuances might hold back experienced members, let alone one that just recently grasped the mysteries of the DOM API.

Therefore, after a long trial and error with scoping tasks, we are now taking a much more limited approach into tasks and their definition. We start with small, well defined tasks, and gradually grow as all parties feel confident. I try to stress that the boundaries are there to protect and not limit. It’s better to complete twice as many smaller tasks, than get stuck in one larger one.

For example, in the beginning of the “view component” tasks phase, a mentor will prepare the API for the component (the Prop types), and the tests that need to be written. Only after a few “guided” view comps one will move to suggest their own API and tests.

This brings to mind Kent Beck’s famous quote “Make it work, make it right, make it fast.” to a whole new meaning! First make sure the tasks you’re assigning are getting done, then dedicate the time to review them properly, and then focus on how to improve their speed. Once you reach a steady pace it’s time to move up the ladder for more complex tasks.

![](https://miro.medium.com/max/1104/1*hrWiFbv97AYIn0g8zadCNg.png)![](https://miro.medium.com/max/1104/1*hrWiFbv97AYIn0g8zadCNg.png)



Since then, we believe in setting proper task boundaries, giving **total** freedom in the implementation, review and repeat. Naturally, those boundaries keep increasing as experience is gained, but keeping them strict helps both ensure there is value from the work being made, and the team member doesn’t feel frustrated most of the time.

When I found out about [the situational leadership model](https://situational.com/situational-leadership/) and about and the [Dreyfus model of skill acquisition](https://en.wikipedia.org/wiki/Dreyfus_model_of_skill_acquisition), I understood that this is definitely the right track for us.

**Pro tip:** a good sign of knowing when to increase boundaries is that a certain task takes only 2x the time it takes your most experienced member. A good sign that you are taking someone out of his comfort-zone and encouraging growth is that it takes (and is completed successfully!) 5x-10x time compared to your most experienced member.

# Summary

I truly believe that by having a formal training program, one that mixes gradually growing tasks and training, together with dedicated mentorship can really make a difference in making the process easy and fun for all parties.

I really hope that I made you consider a passionate junior for your next hire, and gave you some ideas on how to make it efficient.

While I am aware that my own story is an outlier, I do think that combining juniors is the only way to build a scalable, sustainable R&D organization.

And just like there “serverless” development isn’t really server**less**, seniorless also relies on having a few strong and experienced team members to make it happen.

I know this is a controversial topic, and I’d love to hear your thoughts / questions / feedback about it in the comments section!

Thanks for reading 💙