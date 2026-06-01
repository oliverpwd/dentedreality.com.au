---
title: Reducing Product Risk and Removing the MVP Mindset
date: '2021-08-05T23:42:33-06:00'
format: link
service: instapaper
tags:
- read
external_url: https://caseyaccidental.com/product-risk-and-mvp-mindset/
---

[Reducing Product Risk and Removing the MVP Mindset](https://caseyaccidental.com/product-risk-and-mvp-mindset/)  



*I originally wrote this piece internally at Eventbrite and thought it might be valuable to folks who do not work at Eventbrite as well. Slightly edited to remove Eventbrite jargon.*

What is the right way to build products? Earlier in my career, I would have told you everything should be AB tested, and that you should build only as little as you need to validate a hypothesis. Every problem should have user research involved at the beginning, aligned on the problem instead of just validating or invalidating solutions. Every key result should be outcome based. Every engineer, designer and product manager on the team should be involved in defining the problem and the solution. These are all good ideas. However, once you add enough of these “best practices” up, it reads kind of like those articles talking about the morning habits of the most successful people in the world. If you actually try to follow all of those habits, it would take you six hours a day and cost a lot of money. I was once reading an article about what a futurist at Google eats for breakfast every morning to live longer. The article added up that his diet of food and pills cost him $1 million per year. My morning ain’t that long, and I ain’t got that much money.

So if the documented “best practices” take too long or are too expensive, how do you approach different product situations? I want to share a few frameworks that I think can help, but there is no substitute for judgment here. Eventbrite has lots of different product problems. One of the things we are trying to get better at is defining [the type of product problem](https://www.reforge.com/blog/product-work-beyond-product-market-fit) we are working on, and outlining *how* we build based on *who* we are building for, whether it’s consumers or the many different types of event creators we support.

**RULE #1 OF PRODUCT WORK: IT IS NEVER DONE**

We should all know that products and features need to continually improve to stay relevant for our users over time. And it should come as no surprise that no product or feature is perfect on initial release. They need to be refined over time to get better, incorporating feedback from actual users. Many companies just launch new features and forget they exist, rarely improving them. This is not how great products are built. What this means though is that initial releases will never have everything teams want. But if you continue to iterate, this is not a problem. As long as we’re getting value to users as they become available.

If you’re going to continue to iterate on features, supporting them takes effort to maintain and improve over time. The much bigger question then becomes whether product work should be started, and when progress should be shared with users over time. If you start the work, you’re implicitly saying the company should expect to support it for years. That’s a big commitment. So, at Eventbrite we try to do work to de-risk that commitment up front. And if you have a long amount of work mapped out, figuring out what chunks can be released independently so that incrementally more value is being experienced by users is tricky. I’ll dive into how at Eventbrite we are trying to improve our approach to reduce risk and ship releases incrementally. 

**A FRAMEWORK FOR REDUCING RISK IN WHAT WE BUILD**

Product development projects always have very high opportunity cost. So, no matter who we are building for, we try to de-risk investments into projects by learning more about the problems before we invest time in solutions. How do you de-risk projects? An obvious answer may be to talk to customers, right? But it’s not that simple. Users of products are generally unreliable narrators of their own behaviors and preferences. How unreliable depends on who the customer is. For our consumer products, asking our consumers what they want is usually a lost cause. Sure, we can and should regularly talk to them about their problems, but we have to infer solutions ourselves. We can’t expect our consumers to be excellent product thinkers. If we did build what they asked for, they probably wouldn’t end up using it. As Henry Ford allegedly said, “If I’d asked customers what they wanted, they would have said a faster horse.” 

For event creators, it depends on how sophisticated they are. Eventbrite is a broad, horizontal platform used for many different types of events, from small meetups to large festivals and conferences and everything in between. For our most sophisticated customers (and most enterprise businesses), it’s not a bad approach to ask customers what they want, ask them to prioritize how bad they want it, and build and charge for things in that order. For less sophisticated customers, it’s still likely a bad idea. This ends up creating two spectrums to help you understand what to do by level of sophistication of the user vs. how much data users generate. Each of these quadrants tends to have a different approach to de-risking projects.

[![](https://caseyaccidental.com/wp-content/uploads/2021/05/Screen-Shot-2021-05-25-at-8.17.35-AM-1024x577.png)![](https://caseyaccidental.com/wp-content/uploads/2021/05/Screen-Shot-2021-05-25-at-8.17.35-AM-1024x577.png)](https://caseyaccidental.com/wp-content/uploads/2021/05/Screen-Shot-2021-05-25-at-8.17.35-AM.png)

So what this implies is that our approach to de-risking projects should be very different depending on the type of customer we’re building for. Eventbrite isn’t Instagram, but we do have a lot of consumers compared to most companies. So, attendee experience projects are going to bias toward a data-first approach with research to back up the why when needed. They will also be the most likely to AB test. The self-service creator side of our business is more towards the middle of these axes. So we’ll blend some data and some research needed in addition to direct or proxy customer feedback. We also have segments of frequent creators that are smaller in number, but more sophisticated than the average self-service creator, so direct feedback plays more of a role in what we build, but it also has to be supported by data and user research. When we expanded our sales team into enterprise segments in the past, we were much more likely to build what they asked for.

**A FRAMEWORK FOR DIFFERENT PRODUCT APPROACHES WITH DIFFERENT LEVELS OF AMBIGUITY**

Cody Evol, a Director of Product Design at Eventbrite, helped develop one of our more useful frameworks to help us understand how much time we devote to a project. When I joined Eventbrite almost two years ago, every team was describing their project as an MVP, which is quite strange, as the Minimum Viable Product framework was built for launching new products, which is not what most teams were doing.

[![](https://caseyaccidental.com/wp-content/uploads/2021/05/inconceivable.jpeg)![](https://caseyaccidental.com/wp-content/uploads/2021/05/inconceivable.jpeg)](https://caseyaccidental.com/wp-content/uploads/2021/05/inconceivable.jpeg)

*Product teams using inappropriate frameworks off the internet to justify their approach? Inconceivable!*

The key thesis of Cody’s design quality framework is that the level of investment before something reaches a customer is tied to how confident we are that we understand both the problem and viability of the solution.

[![](https://caseyaccidental.com/wp-content/uploads/2021/05/Screen-Shot-2021-03-31-at-4.15.09-PM-1024x573.png)![](https://caseyaccidental.com/wp-content/uploads/2021/05/Screen-Shot-2021-03-31-at-4.15.09-PM-1024x573.png)](https://caseyaccidental.com/wp-content/uploads/2021/05/Screen-Shot-2021-03-31-at-4.15.09-PM.png)

*Your development approach should change based on how ambiguous the problem and ideal solution are.*

When there is a lot of ambiguity about the problem or the solution, we should generally try to de-risk the project before investing a lot of time into it by using the approaches above. And we have many tools at our disposal to do this. With enough validation, teams should invest in building minimum viable products or features. Minimum viable product is probably the best known product development framework outside of perhaps Agile. It is about delivering value to users by building the smallest product you can to test your hypothesis. You ship to learn, which influences future product development. However, most things we build aren’t minimum viable products. It’s a product development framework for brand new products, and we rarely build brand new products. More likely, we are building features. These can be even more lightweight because you are building something on top of an existing product (you can think of a product as a bundle of features). The “Follow This Creator” feature was a great example of a minimum viable feature on the consumer side of our product. We didn’t know if consumers would adopt it, so we launched it just on Android without even building the push notification functionality. As we saw consumers adopt it, we built it for iOS and web and with email and push functionality.

The goal is usually to reduce the ambiguity around the product problem and solution so that you are not building an MVP/MVF, but instead doing phased delivery. This is a type of development where you have a strong vision and the problem and solution are validated, so the goal is to build toward that desired vision, and release incrementally as valuable pieces of that vision are complete.

MVP’s and MVF’s are to prove that our ideas actually solve a problem. If we prove that, we typically need to invest a lot more to reach the potential of the product or feature idea. Rarely do MVP’s or MVF’s crush expectations out the gate.

**OUR APPROACH MOVING FORWARD**

When projects are de-risked, we start building the desired product directly in phases. No shortcuts on design quality. No accumulation of technical debt to “get something out”. These are features we intend to be very valuable and support for a long time, so they should be built the right way. But how do you break up the product vision into phases when you have such a clear vision of the whole you want to build? Shouldn’t you just build it all upfront? There are a few reasons this is a bad idea. One is that if you wait to deliver some value to customers until all of the value you envisioned is completed, customers are dealing with sub-par experiences that do not improve for a long time. It is better to deliver some improvement over time than no improvement for a long time, and then a big reveal. Otherwise, you are holding back things that could add value to them today unnecessarily. Secondly, even with strong visions backed by data, usage of products can surprise you. It’s better to get the learning from usage incrementally over time to make micro-adjustments to the vision. Getting no feedback from customers on what you’re building for a long time is dangerous as customer preferences evolve. Lastly, releasing regularly allows you to de-risk your vision technically as well. You get to see how what you’ve built scales or breaks incrementally instead of all at once.

What if there is no way to break up the value delivered to the customer in phases, meaning it’s literally not valuable until all of the work is complete? It is generally still a good idea to release the code incrementally to de-risk the technical aspects of the project even if the customer doesn’t see it. One of my favorite recent examples of this is Apple. Hardware is usually very expensive to iterate on compared to software. Apple was working on a multi-year effort to launch Apple Pay using a customer’s fingerprint as the verification. Instead of launching a new way to authenticate and the credit card payment at the same time, it launched TouchID on the iPhone 5S to see if fingerprint authentication would be a successful interaction. That de-risked the launch of Apple Pay on the iPhone 6 using fingerprint for payment.

To bring it all home, product development is hard. You can’t read one article on the internet and all of sudden build great products, just like you can’t talk to one customer and know exactly what to build. We create frameworks not so that we can shut our brains off and follow an exact guide to building our product, but so that we can focus our brain power on the thousands of other very confusing and ambiguous questions we will undoubtedly face in trying to build this product over time. I hope these frameworks can help you understand how Eventbrite approaches situations it comes across, and gives you some things to think about as you build products.

*Thanks to Cody Evol for his help on these frameworks.*

*Currently listening to [Pool by Skee Mask](https://iliantape.bandcamp.com/album/itlp09-skee-mask-pool).*