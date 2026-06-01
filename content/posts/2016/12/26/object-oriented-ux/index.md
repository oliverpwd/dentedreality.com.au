---
title: Object-Oriented UX
date: '2016-12-26T00:01:54-07:00'
format: link
service: instapaper
tags:
- read
external_url: http://alistapart.com/article/object-oriented-ux
---

[Object-Oriented UX](http://alistapart.com/article/object-oriented-ux)  



![Dinosaurs setting up blocks.](http://alistapart.com/d/_made/d/SueLockwood-SophiaVoychehovski_960_440_81.jpg)![Dinosaurs setting up blocks.](http://alistapart.com/d/_made/d/SueLockwood-SophiaVoychehovski_960_440_81.jpg)[Issue № 431](http://alistapart.com/issue/431)

Illustration by

[Sue Lockwood](http://alistapart.com/author/slockwood)

# Object-Oriented UX

In June 2012, while working at [CNN.com](http://www.cnn.com), I was tasked with designing the user experience of election night. The next five months of my life would be dedicated to that single night—but success to me had nothing to do with who won. I was concerned with findability, data visualization, a shape-shifting canvas, and how the hell mouse-over flyouts were going to work on an iPhone. For the first time in history, CNN.com was releasing a responsive experience. And, for the first time in history, I was going to *design* a responsive experience.

The stakes were high. Election night is like Super Bowl Sunday for CNN.com. If well executed, it’s one of the highest revenue nights in a four-year cycle. To add to the pressure, we were on a tight timeline with a deadline that was not going to budge. November 6th or bust.

Then I learned that the first development sprint kicked off in four days. *Four days?!* My project manager calmly told me, “Don’t worry. The devs only need *one template* for the first sprint. While they are building the first template, you can move on to the next.”

Huh? How was I supposed to design a cog in a machine without first roughing out the design of the machine?

Thinking myopically worked okay when we were designing in pages on fixed screen sizes; we could get away with quilting together pieces designed in silos. I was pretty clueless about responsive design, but I did know that we’d need a clean and simple system, not pages strung together. And as all engineers and designers know, the more moving parts in a system, the more opportunities for disaster.

So during those first four days, I did not wireframe one disconnected template. Instead, I blocked out a holistic system made of reusable, interchangeable parts. Here’s what it looked like:

![Election night diagram](http://alistapart.com/d/431/image1-results.jpg)![Election night diagram](http://alistapart.com/d/431/image1-results.jpg)

The diagram of the proposed election night experience I first presented to the CNN.com team.

I presented this diagram to a conference room of stakeholders who expected to review a single “finished” template. I demonstrated that I had reduced the number of components and templates compared to our 2008 design, and that the new system was simple enough to fit on one 8.5 × 11 sheet of paper! Thankfully, a critical mass of people in the room saw the value of what I presented: less stuff to build.

The diagram I churned out in 2012 was far from perfect, mostly in that I was trying to do too much too soon. I jumped the gun on implementation, blocking out flyouts and bar graphs. I was still thinking desktop-first, worrying about *positioning*, as opposed to *prioritization*. I packed in a premature homepage, a cover sheet for the experience (which I would now design *last*). I took a stab at persistent top-level navigation, instead of focusing on the content modules first.

Although imperfect, the spirit of the diagram, and the thinking behind it, hit a chord with me. It wasn’t a sitemap; it showed no hierarchy. It wasn’t a storyboard; it didn’t block out a task flow. Instead, this diagram mapped out a system of things. And it changed the way I do UX.

Stripping away interaction, persistent navigation, homepage, and layout, here’s the diagram that I would have created then if I knew what I know now, showing a system of three objects: [States](http://www2.cnn.com/election/2012/results/state/TN/), [Races](http://www2.cnn.com/election/2012/results/race/senate/), and [State-Race Results](http://www2.cnn.com/election/2012/results/state/TN/senate/).

![An updated election night diagram](http://alistapart.com/d/431/image2-diagram.png)![An updated election night diagram](http://alistapart.com/d/431/image2-diagram.png)

How I’d present the election night experience if I were designing it today.

It worked: our responsive election night turned out to be the Super Bowl Sunday CNN executives hoped for. But we did it by the skin of our teeth, working late nights and weekends to make sure the design performed on a myriad of devices. I’m not sure we could have pulled it off with a design any more complex.

Today, I’ve evolved this trial-by-fire experience into a proven, structured object-based process. In this article, I will introduce object-oriented UX, share my process of object mapping, and help you start doing it yourself.

## Mobile first, content first, and objects first

> Always separate thinking about real-world things from the documents which describe those things. Resource before representation.



[Mike Atherton](http://www.slideshare.net/reduxd/modeling-structured-content-ias13-workshop)



It took me about about a year to retrain myself to truly think [mobile first](http://www.lukew.com/resources/mobile_first.asp), but today, I do so even when designing desktop-only software applications. To me, mobile first simply means forced prioritization. It means think about layout later. Start with a single column “design” (also known as a list), and force yourself to prioritize content and functionality with sequential ranking.

This approach dovetails nicely with the concept of content first: [“content-out design” as opposed to “canvas-in” design](https://adactio.com/journal/4523). You have to know what you’re saying before you can prioritize it.

Sometimes, this means having real-deal copy first—particularly when you’re working on a site with a critical mass of evergreen or instructional copy that can be organized, prioritized, analyzed, and updated before design work begins.

But if you are working on a site that is 99 percent *instantiated objects* (news articles, products, campaigns, donations), there’s no way to build a complete copy deck up front—or ever. Instead of prioritizing actual copy, I have to think in objects.

That’s OOUX: putting object design before procedural action design, and thinking about a system through the lens of the real-world objects in a user’s mental model (products, tutorials, locations), not digital-world actions (search, filter, compare, check out). We determine the actions after first defining the objects, as opposed to the traditional actions-first process that jumps straight into flows, interactions, and features.

## OOUX is powerful

Newsflash! This is how your backend engineers work. In the ’80s, the software engineering community began to transition from procedural languages to object-oriented languages, which have benefits like code reuse, data encapsulation, and easier software maintenance. Most programmers bring your designs to life using object-oriented languages like Java, Ruby, Python, C++ or C#.

Engineers start their process by mapping out the objects that make up the problem domain—something UXers should be doing from day one. When they look at your wireframes or prototypes, they first reverse-engineer your design to parse out the objects. They think, “How will object *X* talk to object *Y*? Will object *A* be made up of lots of object *B*s? Which attributes will each object have? Will this class of objects inherit from that class of objects?”

On the web, we develop object-orientedly, but still design procedurally, focusing on drill-down hierarchy or linear task flows. But there’s another option. In his 1995 book, [Designing Object Oriented User Interfaces](http://www.amazon.com/Designing-Object-Oriented-Interfaces-Addison-Wesley-Technology/dp/080535350X/ref=sr_1_1?s=books&ie=UTF8&qid=1441640610&sr=1-1&keywords=designing+object+oriented+user+interfaces), designer and engineer Dave Collins argues that basing both front-end and backend design on object-oriented principles “brings coherence to the software development process. Object-orientation reveals deep structural correspondences between the artifacts of analysis, design, and implementation.”

Defining objects that mimic the mental model of your users provides a scaffolding for team communication. It gives you a shared language. On top of team cohesion, designing object-orientedly can also help you:

* match your user’s mental model, improving their experience
* ensure simplicity, reducing any accidental complexity due to extraneous design elements
* grow and maintain your product: objects can be iterated on without affecting the rest of the system and new objects can be gracefully folded in (as opposed to tacking on features)
* build better APIs with portable, independent objects
* get SEO brownie points from structured content and valuable cross-linking

Then, there’s my favorite justification: OOUX helps you bake in more-crucial-than-ever contextual navigation. In other words, it helps users get to content through content.

Persistent navigation might be hidden, hamburgered out of sight when a user is on a small screen. But even on 17-inch monitor, the most beautiful pinned-to-the-top navigation might still get ignored. When a user visits a site for the first time, they often gravitate to the big shiny objects, using the navigation or search bar only as a backup plan. As [Val Jencks](https://www.linkedin.com/in/valeriejencks) neatly summed up, “We go to content on the page first. The top navigation is the fire escape.”

If a user is reading a recipe, where might they want to go next? We should anticipate how they might want to explore based on the recipe they are reading, and not leave it up to them to peck through a hierarchical menu or come up with a search term. And we certainly should not leave them with a few “related recipes” and consider our work done. They might want to see all the recipes that the chef has posted. Or maybe they want to see more recipes that use swiss chard, pivoting by ingredient?

If we are thinking object-orientedly, we will *experiment* with ways that each object might relate to other objects, looking beyond the obvious. Maybe chefs have favorite ingredients? In the object-oriented design below, a user can continually explore instances of these three objects (recipe, chef, ingredient) without ever hitting a dead end. The content is the navigation, and it’s all in context.

![An object model for a cooking site](http://alistapart.com/d/431/image3-recipes.png)![An object model for a cooking site](http://alistapart.com/d/431/image3-recipes.png)

In this object model, recipes, chefs, and ingredients are interconnected, allowing continuous exploration.

If this concept feels familiar, you’ve probably read about or practiced content modeling. In the past five years, many information architects (see [Mike Atherton’s work](http://www.slideshare.net/reduxd/modeling-structured-content-ias13-workshop)) and content strategists (see [Rachel Lovinger’s work](http://alistapart.com/article/content-modelling-a-master-skill)) have started focusing on systems of reusable content types, and becoming more involved in the design of CMSes: the content creator, not just the end-user, is a primary user.

In her book [Content Everywhere](http://rosenfeldmedia.com/books/content-everywhere/), Sara Wachter-Boettcher encourages us to model our content before diving into wireframes and interaction design:

> Content modeling gives you systematic knowledge; it allows you to see what types of content you have, which elements they include, and how they operate in a standardized way.

Unfortunately, the art of content modeling is still unfamiliar to many UX designers, who hear “content” and assume it doesn’t apply to them. This is especially true for UXers who deal with software as a service or product design: strategies involving *content* sometimes fall on deaf ears.

## Object mapping

Object mapping, my process behind OOUX, is content modeling for designers who do not deal with content in the traditional sense, but still need to design systems—and not just [systems of *implementation*](http://bradfrost.com/blog/post/atomic-web-design/). While a tight collection of reusable templates and modules is invaluable, those design patterns don’t hold meaning for a user unless they’re backed by a system of real-world objects that matches that user’s mental model. Focus first on designing the system of real-world objects, then on designing a system of implementation to bring it all to life. This is the linchpin of all my design work, because it transforms goals into an executable system that meets those goals.

Get out your sticky notes, grab your team, and clear some wall space—I’d like to walk you through my process.

### Step 1: Extract objects from goals

One of my favorite perks of object mapping is that it provides a perfect bridge from goals to design. Instead of haphazardly whiteboarding A Beautiful Mind-style, object mapping provides a neat framework to move from strategy to design. (Please continue to go all [John Nash](https://en.wikipedia.org/wiki/John_Forbes_Nash,_Jr.) at the whiteboard, but create an object map first. It will give your wild creativity a solid foothold.)

As an example, let’s say we are building an application to help home improvement brands connect to DIYers. After user interviews, a competitive analysis, and discussions with stakeholders, we have our brief:

> Give DIYers an outlet to post their home improvement challenges, soliciting potential solutions from product companies (brands). DIYers get expert solutions to their challenges and brands get exposure.
> 
> * DIYers can search and browse existing challenges, commenting on the proposed solutions.
> * Brands can search and browse for open challenges that might be a good fit for one of their products.
> * Brands can create solutions that feature one or more of their products.
> * DIYers can close a challenge after a solution has been chosen, and later follow-up on how well the solution worked.
> * Brands can create a library of solutions that can be reused on various challenges.

To extract the objects, we basically highlight the nouns.

![Image of the brief with nouns highlighted](http://alistapart.com/d/431/image4-goals.jpg)![Image of the brief with nouns highlighted](http://alistapart.com/d/431/image4-goals.jpg)

Highlighting the nouns in our project brief is the first step to mapping our objects.

Recognizing nouns is first-grade simple, but extracting objects does require some subtle art:

* We pay special attention to nouns that keep popping up, like *challenge* and *solution*. Those will be important objects.
* We ignore the abstract noun *exposure*, as this describes a fluffy concept we hope will emerge from our system, not a tangible object that will be part of our system.
* We ignore *library* because this is simply a collection of other objects (*solutions*). Watch out for words like *calendar*, *catalog*, or *map*. These are usually just fancy list-views of the core object: an *event*, *product*, or *location*, respectively. For example, most systems that deal with locations will have a single (perhaps filterable) map view. The map is a design mechanism, not an object itself.
* We infer an object from two actions: “commenting on” and “following up.” Obviously, we will need some sort of *comment* object.
* We note that a *challenge* object needs multiple states: posted, in progress, closed, and closed with feedback.

From this 10- to 15-minute exercise, we have the main building blocks of our system. Let’s write each object on a blue sticky.

![Blue sticky notes](http://alistapart.com/d/431/image5-stickynotes.png)![Blue sticky notes](http://alistapart.com/d/431/image5-stickynotes.png)

We write each object on its own sticky note to visualize the building blocks of our system.

Next, we need to define what the objects are made of.

### Step 2: Define core content of objects

> Content modeling requires you to simultaneously understand your goals at the highest level and get intimate with your content’s most minute attributes.



—Sara Wachter-Boettcher, Content Everywhere 



Quite. We just determined the macro building blocks of our system, and now we must determine the most granular elements of each. This activity is often reserved for eleventh-hour detailed design, but defining elements while in the medium of sticky notes is liberating—when you start sketching a little later on, you can focus on more creative aspects. Also, having early conversations about what makes up each object can help you avoid moments late in the game where an important element is left off (or extraneous) and the change needs to be made across several design documents.

Most importantly, you can have conversations with your team such as, “Should DIYers be able to add their budget onto a challenge?” *before* non-designers are looking at wireframes or layout. This helps keep conversations focused, rather than getting stuck on something like the icon for budget.

At this point in the process, I separate two types of elements: core content and metadata. Core content, like text and images, goes on yellow stickies. Metadata—any data that a user might sort or filter on—I put on red stickies.

![Blue, yellow, and red sticky notes](http://alistapart.com/d/431/image6-stickynotes.png)![Blue, yellow, and red sticky notes](http://alistapart.com/d/431/image6-stickynotes.png)

The granular elements of each of our objects are mapped out with additional sticky notes.

If your team isn’t sure about a potential piece of content, write it down anyway and just add a question mark. Move on and return to it later.

### Step 3: Nest objects for cross-linking

And now the system comes alive. Do a series of thought experiments for each object. Starting with one object, consider ways that each of the other objects can “nest” inside that given object. As you nest objects, you are defining the relationships between them, and, implicitly, the contextual navigation as well. Using blue stickies, experiment with how each object might nest its other sibling objects.

![The complete object model](http://alistapart.com/d/431/image7-stickynotes.png)![The complete object model](http://alistapart.com/d/431/image7-stickynotes.png)

We finish out the model by adding sticky notes that show how other content objects can “nest” within each object.

For example, here’s how that conversation might go for our *challenge* object:

* DIYer: “Easy, the DIYer is the author of the challenge.”
* Solution: “This is the main nested object of a challenge. We need to show all solutions posted to this challenge.”
* Brand: “Eh, not really? Brand will be a part of the solution modules (as an author of the solution), but probably not directly nested into a challenge.”
* Product: “Again, part of a solution, not directly nested. Huh. Unless DIYers can post the products they already have at home?”
* Comment: “Hmmm. Probably relegated to solution…should we keep all commenting on the solution? Or should brands and DIYers perhaps be able to post questions directly to the challenge? We need to explore this more.”

Note that not everything is figured out. Some items, like the commenting discussion, might be best resolved during sketching—but you will be intentionally exploring an identified design problem, as opposed to that problem catching you by surprise.

### Step 4: Forced ranking

Ugh. This is the most diabolically difficult step. In the prior steps, it’s very important that you wrote each element and nested object on *separate* stickies. Why? Because now we need to reorder the elements, from most to least important.

![A prioritized object model](http://alistapart.com/d/431/image8-stickynotes.png)![A prioritized object model](http://alistapart.com/d/431/image8-stickynotes.png)

Our object model, reordered based on how important each element is.

This ordered list does not necessarily provide a direct representation of what will be at the top and the bottom of the screen. In design, priority might manifest in size or color. Low-priority content might be placed at the top of the screen, but in a collapsed panel (yay, progressive disclosure!). So reassure your team that we are simply prioritizing and not *designing*.

While prioritizing, imagine which elements will be most important to your users. Which bits are must-have information and which are nice-to-have? When considering metadata, think about the most important sorting and filtering mechanisms. If the default sorting will be by “popularity,” then “number of DIYers who like this” will be high priority.

## A new foundation and framework

Now you have an object-based system derived straight from goals. But keep in mind that while this activity provides a foundation for designing an *implementation system*, interactions, and persistent navigation, it doesn’t carve any decisions in stone. It’s a first draft! As you iterate, objects and elements will be introduced, eliminated, and reprioritized. Your object map provides a framework for continued conversation and collaboration: with your client, your design team, and your developers.

OOUX is not a new end-to-end process; it’s a new ingredient to add to your current process. It adds clarity, simplicity, and cohesion—to how you design, and to the products you release into the world.

# About the Author

[![](http://alistapart.com/d/_made/pix/authors/photos/photo_140610_120_120_c1.png)![](http://alistapart.com/d/_made/pix/authors/photos/photo_140610_120_120_c1.png)](http://alistapart.com/author/sophiavoychehovski)

## [Sophia Voychehovski](http://alistapart.com/author/sophiavoychehovski)

Sophia Voychehovski is the founder of [Rewired](http://www.rewiredux.com/), a UX design studio based in Atlanta. Rewired consults to nonprofits, social entrepreneurs, and tech startups. A recovering perfectionist, Sophia specializes in MVPifying, complexity elimination, and ruthless prioritization. She is constantly reminding herself (and her clients) that done is better than perfect.
### More from this Author

* [OOUX: A Foundation for Interaction Design](http://alistapart.com/article/ooux-a-foundation-for-interaction-design)