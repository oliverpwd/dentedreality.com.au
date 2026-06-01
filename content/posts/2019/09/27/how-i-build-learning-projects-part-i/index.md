---
title: How I Build Learning Projects — Part I
date: '2019-09-27T13:47:03-06:00'
format: link
service: instapaper
tags:
- read
external_url: https://medium.com/@rchang/how-i-build-learning-projects-part-i-54dbaad68961
---

[How I Build Learning Projects — Part I](https://medium.com/@rchang/how-i-build-learning-projects-part-i-54dbaad68961)  



## A Little Bit of Slope Makes Up For A Lot of Y-Intercept


![](https://miro.medium.com/fit/c/96/96/1*EguVA0HsIGqUy0gaDS1VgA.png)![](https://miro.medium.com/fit/c/96/96/1*EguVA0HsIGqUy0gaDS1VgA.png)
Robert Chang
Jul 20 · 14 min read



![](https://miro.medium.com/max/6264/1*PNViZtLN_8qn0oX-55UKig.png)![](https://miro.medium.com/max/6264/1*PNViZtLN_8qn0oX-55UKig.png)

[Image credit](https://unsplash.com/photos/eMP4sYPJ9x0): When was the last time that you built a learning project?



# Motivation

Recently, I came across a [blog post](https://sirupsen.com/read/) written by Simon Hørup Eskildsen on how he approaches reading. It was an inspiring read because I did not know anyone this deliberate about the pursuit of reading. This kind of meticulous, thoughtful, system-level design thinking reminds me of [Ray Dalio’s Principle](https://www.principles.com/):

> Think of yourself as a machine operating within a machine and know that you have the ability to alter your machines to produce better outcomes

While I do not see myself as a machine, I did examine various aspects of my life and found that I tend to apply this type of thinking more rigorously when it comes to learning. In graduate school, I experimented with various studying strategies to make my day more effective. At work, I have been asked by my coworkers how I managed to find time to pursue learning projects.

Like many others, I am easily distracted by Netflix and are often bombarded by social media like Twitter and Facebook. Nevertheless, over the years, I have designed a system to make my self-directed learning easier and more effective. In this post, I will share my approach to building technical learning projects, and I hope it will inspire you to design your own as well. If you already have a system that works well for you, I would love to hear it!

# A Bit of Slope Makes Up For A Lot of Y-Intercept


![]()

[image credit](https://unsplash.com/photos/VfUN94cUy4o): Which slope are you climbing at the moment?



Before I go into the details of my still-evolving system, it’s useful to first talk about why I even pursue learning projects in the first place. Among my many reasons, the most important one came from Stanford professor [John Ousterhout](https://web.stanford.edu/~ouster/cgi-bin/home.php). In his “[Thoughts for the Weekend](https://www.quora.com/What-are-the-most-profound-life-lessons-from-Stanford-Professor-John-Ousterhout?share=1)” series, Professor Outsterhout once shared with his students a concept called “A little bit of slope makes up for a lot of Y-intercept”.

> If you have two lines, the red line and the blue line, and the red line has a lower Y-intercept but a greater slope […] then eventually the red line will cross the blue line. In a mathematical sense, it’s kind of obvious [a little bit of slope makes up for a lot of Y-intercept].
> 
> I think this is a pretty good guideline for life. What I mean is that how fast you learn is a lot more important than how much you know to begin with. So in general I say that people emphasize too much on how much they know and not how fast they’re learning.

When I took my first Data Science job in 2012, I barely knew git, SQL, and have never heard the term Data Engineering. I didn’t know how to design good experiments, and I know very little about Machine Learning beyond math and theory. Arguably, my Y-intercept was pretty low, but I focused on my slope anyway.

![]()



I love this philosophy, because it not only gives me more motivation to keep improving myself, but it also helps me to stay humble when working with less experienced people. We are all working along with our version of the slope, and in the long run, your learning rate is what determines your long-term success.

In this two-part series, I will talk about various strategies that I adopted along my journey climbing my slope. These include, but are not limited to:

* **How to choose a useful learning project**
* **How to design and iterate on a learning plan**
* How to execute on a learning project persistently
* How to internalize my learnings and make it useful for others

This post, part-I of the series, will explain several criteria I used when it comes to subject picking. Furthermore, I will talk about how to effectively design a learning plan, and explain why it is important to spend time doing so. In Part-II of this series, I will discuss the ingredients of good habits and how to leverage them to learn persistently. Finally, I will discuss why teaching and writing are the best ways to internalize what you have learned.

Let’s dive right in!

# 1. Choosing a Learning Project


![]()

[Image credit](https://unsplash.com/photos/KmGMMxVv0_Q): Which learning projects should you choose?



In an era where learning resources are easily accessible via MOOCs, Youtube, and blog posts, the question is now less about accessibility but more about what subjects to learn. Some advocates to learn what you love until you love learning, others suggest learning skills that can withstand the test of time. My strategy, especially for developing professional skills, is heavily influenced by [Scott Adams](http://dilbertblog.typepad.com/the_dilbert_blog/2007/07/career-advice.html), the creator of the Dilbert comic strip.

> If you want an average successful life, it doesn’t take much planning. Just stay out of trouble, go to school, and apply for jobs you might like. But if you want something extraordinary, you have two paths:
> 
> 1. Become the best at one specific thing.  
> 2. Become very good (top 25%) at two or more things.
> 
> The first strategy is difficult to the point of near impossibility. Few people will ever play in the NBA or make a platinum album. I don’t recommend anyone even try. The second strategy is fairly easy. Everyone has at least a few areas in which they could be in the top 25% with some effort […] Capitalism rewards things that are both rare and valuable. You make yourself rare by combining two or more “pretty goods” until no one else has your mix.

I adopted the second strategy because I enjoy having breath and diversity in my skill sets. As such, I spent a lot of time thinking about what my repertoire of skills should be, and they generally boil down to skills that are foundational, adjacent, and transferable. Let me explain each of them below.

## Prioritize Foundational Skills

In the present world, the rate of technological change is often far too fast for any single person to digest. In a growing field where many people are contributing and competing, there is often an unending streak of new updates and announcements. As an example, in Deep Learning, we often hear debates about which learning framework will be the *lingua franca* of AI. Many of the technologies in debate today were not even popularized until a few years ago.

![]()


A common mistake for skill building is to focus too much on the tooling and not the workflow underneath it

With this rate of change, I argue that the ability to use any particular framework or tool is **not** by itself a foundational skill. Instead, it is the *workflow patterns* that these tools enabled that are foundational. Frameworks and tooling are often useful because they abstract away tedious parts of our workflow, but without knowing why we are following these workflows in the first place, we are simply using the tools mechanically without souls.

I tried to follow this principle when pursuing my learning projects. For Deep Learning, instead of obsessing over whether to use Keras or PyTorch, I spent most of my time understanding the conceptual difference between shallow models v.s. deep models. I learned why Transfer Learning is a standard workflow in the era of deep modeling, and I investigated why certain embeddings are powerful for different learning tasks. Similarly, when I practiced Data Engineering, I looked beyond Airflow’s simple building blocks such as sensors, operators, and transfers. Instead, I tried to understand the core activities involved in doing good data engineering work — data modeling, backfilling, testing and monitoring, … etc.

Over time, I learned that by mastering the core concepts associated with a workflow, the mental model one develops can be easily re-applied when picking up new tools and frameworks. This is perhaps why great engineers can typically pick up new languages without too much struggle — they understand the core concepts underneath that are universally foundational.

## Explore Adjacent Skills

Once I feel I have mastered a particular skill, I often expanded it by tapping into [adjacent discipline](http://www.effectiveengineer.com/blog/master-adjacent-disciplines), a term coined by Steven Sinofsky and advocated by Edmond Lau. Accordingly to Steven, adjacent disciplines as those that are immediately to the left or right of your own core expertise. For example, if you are a data scientist, your adjacent disciplines might be Data Engineering or Data Visualization. As a product manager, your adjacent disciplines might be A/B testing or product design. As a musician, your adjacent disciplines might be music composition or music production, so on and so forth.

![]()


A few examples of Adjacent disciplines for becoming a [GM](https://blogs.msdn.microsoft.com/techtalk/2005/09/19/the-path-to-gm-some-thoughts-on-becoming-a-general-manager/) & [Data Scientist](https://mindfulmachines.io/blog/2018/3/17/the-flavors-of-data-science-and-data-engineering)

The first obvious advantage of exploring adjacent skills is that it will make you more self-sufficient on the job. If you are a data scientist who needs a feature pipeline for machine learning, having the skill to build your own ETL pipeline means that you can iterate on feature engineering more efficiently. If you are an analyst who needs to include more dimensional cuts for a report, having the ability to modify table schema can help you to deliver results faster. This is why I believe data scientists who learned data engineering can usually take on bigger and more ambitious data projects.

Aside from this first benefit, learning adjacent disciplines often mean your knowledge compounds. Having learned Python and Object-Oriented Programming, these skills enabled me to understand better how different Data Engineering frameworks are implemented under the hood. By learning the challenges of building ETL jobs, I can appreciate much better why feature engineering in Machine Learning can be so time-consuming. Adjacent disciplines not only help you to transition into new areas, but it also helps you to connect related knowledge together.

The last and more subtle advantage of learning adjacent discipline is that it makes you a better cross-functional partner. By understanding the complexities and intricacies of your colleagues’ works, you can better empathize with the challenges that they face on the job.

## Focus on Transferable Skills

A few years ago, I was interested in building a website using Flask and Python. While dabbling into the world of web development, I came across a template engine called [Jinja](http://jinja.pocoo.org/). I soon learned that it is commonly used by developers because it simplifies writing HTML significantly via control flow and inheritance. I was very impressed by the ingenuity of this template engine at the time, but I never really used it again as a data scientist, not until when I arrived at Airbnb.

![]()


[Source](https://multithreaded.stitchfix.com/blog/2017/07/06/one-weird-trick/): Jinja, originally invented for HTML, can be applied to SQL as well

At Airbnb, I learned from experienced data engineers that many of the ideas in Jinja can be [applied](https://multithreaded.stitchfix.com/blog/2017/07/06/one-weird-trick/) to Hive queries directly. By leveraging for-loop in Jinja, I can greatly shorten the SELECT statement. By using the if-else control flow, I can incorporate backfilling logic into the same SQL query.

When thinking about writing HTML and writing SQL, I realize that there’s a lot of similarity between the two activities. Both workflows leverage an expressive language to achieve certain tasks: HTML for rendering web pages, SQL for data computation, so it wasn’t surprising to see that the same technique can be transferred from one domain to another.

Transferable skills are like superpowers — learned once, and you get to apply it in several places. The initial cost of acquiring those skills might be high, but the variable cost for applying it elsewhere is relatively low. When thinking about what skills to master, focusing on transferable skill.

## Takeaways

* **Prioritize foundational skills:** you will learn activities associated with a workflow and appreciate how tooling can abstract them away for you
* **Explore adjacent disciplines:** you will become more self-sufficient on the job, can take on larger and more ambitious projects, and develop more empathy for your colleagues
* **Focus on transferable skills:** you can apply these skills in different domains without much extra costs

Our society values what’s rare and valuable, and by being selective of what to learn, you are more likely to develop your own *mix* that is unique and not easily replaceable.

# 2. Designing a Learning Plan


![]()

[Source](https://unsplash.com/photos/ZSPBhokqDMc): How much time do you spend designing your learning plan before learning something?



Once you have chosen a specific skill to focus on, the next step is to develop a learning plan. In my opinion, the biggest mind shift here is that you need to treat yourself not only as a student but also as your own teacher. Playing these dual roles can seem a little bit daunting at first, especially if you are used to learning from an authority figure like a teacher or professor.

However, imagine what a teacher has to do before teaching a course. She has to define learning objectives for her students first. He most likely needs to sample different learning materials and develop a curriculum. Finally, she would need to set milestones to make sure students are held accountable.

Similarly, as a designer of your learning project, you will also need to go through these exercises to design an effective learning plan. Let us go over each of these activities in more detail.

## Define Your Learning Objectives

One of the mistakes that I made in my earlier learning projects was that I rarely stated upfront what learning objectives I would like to achieve. I dived into one learning project after another haphazardly, with the hope that someday I will apply these skills to some problems — It never happened.

![]()


A comparison: (Left) a learning project without clear learning objectives v.s. one that does (Right)

It does not hurt to be biased to action, but following unguided actions also means you could spend a lot of energy wandering around aimlessly. Reflecting on the lessons learned from earlier failures, I now try to identify one or two learning objectives upfront before diving into a learning project.

For example, when I pursued my Python learning project, I wrote down the learning objective that I want to eventually converge all my Data Science work from R to Python by the end of the calendar year. When pursuing my Deep Learning project, I set the goal to understand how Airbnb’s [room classification model](https://www.youtube.com/watch?v=tPb2u9kwh2w) works under the hood. The key here is to set concrete, time-bounded, measurable goals. i.e. I can check exactly if I have achieved what I set out to do by a specific deadline.

For technical learning projects that are aimed to improve my professional skills, my learning objectives usually revolve around:

* adopting or making a specific change in how I work
* achieving a better understanding of a problem or solution, or
* generating learning materials that can be consumed by others

I will talk more about generating public work in Part-II of this series.

## Identify Project Milestones

If your learning objective is relatively ambitious, then it is important to break down your learning objectives into tangible and achievable milestones. This “divide and conquer” approach has proven to be very effective for me.

![]()


Source: A truncated list of project milestones that I defined for my Flask learning project (see the full list [here](https://github.com/robert8138/flask-google-calendar-api-project))

As a concrete example, for my Flask learning project, I defined a learning objective to deploy a website that will render my Google calendar time logs in an interactive [d3](https://d3js.org/) visualization. I identified specific milestones for this goal: from reading the [Google Calendar API](https://developers.google.com/calendar/), pulling and storing my data in a local database, to finally rendering the data in a d3 visualization. After completing many small milestones, I finally built a website that did exactly what I set out to you. I still remember the day when I rendered all the data on a heat map, it was magical!

![]()


Without setting project milestones, I might have never been able to build this beautiful heap map!

## Develop a Curriculum

In my experience, one of the most important but under-appreciated skills in learning is the ability to identify materials that are accessible and approachable to your learning patterns. For most of my learning projects, I usually spent about 2–3 weeks sampling materials until I develop a curriculum that I feel excited about. This is the period where I would browse the internet to identify any free or paid materials that are relevant to my topic — be it blog posts, online courses, books, or the like. I typically do this by creating a [new github repository](https://help.github.com/en/articles/create-a-repo) to keep track of all the materials that I find relevant, and slowly organize them into something more structured like below:

![]()


[Source](https://github.com/robert8138/deep-learning-deliberate-practice): Curriculum that I built for my Deep Learning project. You can find my Python one [here](https://github.com/robert8138/python-deliberate-practice).

There are two reasons why sampling and developing your curriculum is important. First, without a very strong mental model, it is hard to know exactly what are the important concepts to learn. By standing on the shoulders of people who understand the materials very well, you will start to see the same core concepts emerging again and again. In my opinion, this is the first step toward understanding.

The second reason is that as a life-long student, you are no longer constrained by the textbook or teaching style of any single teacher. Depending on your background, you might want to mix and match between different learning materials that help you learn better. Over and over again, I have seen how the same concept can be explained horribly but also articulately, and it makes a world of a difference. It’s up to you to find the resources that resonant with your learning patterns.

As an example, during my Deep Learning project, I simultaneously sample materials from Stanford’s [on-campus course](http://cs231n.stanford.edu/), Coursera’s [Deep Learning specialization](https://www.coursera.org/specializations/deep-learning), and a [fast.ai](http://fast.ai) course. I generally find Coursera’s material great for developing intuition at first, but almost always gravitated toward the Stanford course because I want to understand the math better. Furthermore, to practice with more hands-on exercise, I would usually go to the [fast.ai](http://fast.ai) course, where notebooks and code examples are abundantly available. It was quite common that I would study the same subject using three different materials in a given week.

One final note, if you are not yet confident in your ability to source your own learning materials, be sure to solicit feedback from friends or coworkers who are knowledgeable on the subject. This is a good way to make sure your curriculum has covered all the basic grounds.

## Takeaways

When it comes to self-directed learning, it is very important to design a learning plan. This includes:

* **Define your learning objectives**: set clear goals on what behaviors or outcomes you would like to achieve
* **Identify project milestones**: divide and conquer so you can make steady progress without getting intimidated
* **Develop a curriculum:** find materials that you would enjoy according to your learning patterns. Consult experts to validate your curriculum

By the end of this design process, you would have a pretty solid learning plan, and that’s really half of the job done! The common mistake is that people generally do not spend enough time in this step.

# Conclusion

Even if you have a strong desire to learn, it often still feels like a struggle to balance between self-directed learning and other important life priorities, just think about all the responsibilities, obligations, and distractions in life!

Without a system, chances are, we will not achieve our goals. In this post, I shared my approach to choosing and building a learning project, using my previous successes and failures. I hope by sharing some of my learnings, you will be inspire to design your own learning methods.

In the next post, I will talk about how to make steady progress on a learning project, and how to internalize your learnings by teaching others and producing public artifacts.

Happy learning!