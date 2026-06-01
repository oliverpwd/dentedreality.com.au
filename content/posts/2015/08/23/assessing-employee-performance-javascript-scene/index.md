---
title: Assessing Employee Performance — JavaScript Scene
date: '2015-08-23T15:30:36-06:00'
format: link
service: instapaper
tags:
- read
external_url: https://medium.com/javascript-scene/assessing-employee-performance-1a8bdee45c1a
---

[Assessing Employee Performance — JavaScript Scene](https://medium.com/javascript-scene/assessing-employee-performance-1a8bdee45c1a)  



# Assessing Employee Performance

## You’re Doing it Rong







Code Monkey — YJ Soon (CC BY-NC-ND 2.0)


I’m gonna give it to you straight. If you’re not **listening closely to the employee you’re evaluating,** & **interviewing their peers** about **how helpful and knowledgable that employee is…**

And if the sum of that feedback is anything less than your **primary gauge of performance**…




> ***You SUCK at judging  
> employee performance.***




Whatever else you’re doing is costing you dearly. Stop right now.

**Ask your employee directly** what value they have contributed to the company, and what evidence or corroboration is available to **prove it.** Then take your time. **Follow up.** **Learn about it.** The experience will be eye-opening.

This is something that **almost all companies are terrible at**. With the popularity of quantitative tools like **kanban software** and **job ticket trackers**, it’s very easy to simply look at the **number of tickets an employee closes** and base assessment on that, secure in your knowledge that you did the right thing, because **tracking told you so.**

The problem is, **your most productive employees** are the ones who **help all your other employees be more productive** — and those helpful employees are **busy helping other employees** improve or close tickets faster, or they’re in the deep think tank **painstakingly crafting your app’s architecture and designing quality library APIs.** Or they’re busy **sharing experience and knowledge** with the rest of your team.

They may also spend a lot of their time **contributing to the open source software your company relies on,** fixing bugs or performance issues in GitHub **tickets you never see.**

None of those **tremendously valuable contributions** show up on software dashboards, or the number of lines of code contributed to your app’s codebase.




> True value doesn’t appear overnight.  
> Keep your eye on the end game.




**Talk to your employees frequently**, but **assess their performance annually** in order to give their contributions **time to produce value.** The **more experience** your employee has, the **longer you should allow** for their contributions to be assessed.

**Why?**

Your best employees may take days or weeks to contribute code to your application, and **that’s OK.** They’re making **long term investments** that will **significantly impact your company’s bottom line.** They’re **making the decisions** that will spell the difference between **$1 million dollars** per year in profit, or **$10 million dollars** per year in profit. If you use in-house software to make money (why else would you hire developers?), **you need people like this on your team.**

For example, I once **stopped contributing any code to an app for a whole week** in order to conduct a usability study. I conducted a survey of 1,000 early access customers and asked them to report back. I collected log records of user actions in the shopping cart. I then combed through all of that data looking for patterns.

I discovered our shopping cart abandonment rate was much higher than expected. Double digits higher. That could have been a disaster.

I then brought inexperienced users into the office and asked them to browse our products and use our shopping cart. I recorded video of their sessions. I asked them to shop and say out-loud what they were thinking as they did. I didn’t give them any feedback or help. Just watched and listened.

I discovered that the primary cause of abandonment was that users were struggling with entering payment and shipping information in the checkout form, and I learned **exactly why they were struggling.**

I used what I’d learned to make subtle changes to the behavior of the **open-source** form validation library that we were using. I made the changes, put them up on GitHub for the whole world to use, and carried on.

For an entire week, my employer didn’t see **any ticket-tracking evidence** of my software contribution to their project. I closed just one ticket that week.

It was also the **most profitable time** for the duration of my employment. When I conducted the follow up study to measure results the cart abandonment rate was **reduced by double digits.**




> Reduced cart abandonment by double digits:  
> More than $1 Million in revenue  
> **per month.**




I made a blog post of the study details, and linked to the form validation software we used. In spite of its age, it’s still used in thousands of shopping carts grossing **millions of dollars per month** all over the world. The net global productivity gain is likely to be measured in the **$ billions.**

Not bad for a week’s work.




> Different tickets contribute  
> extremely different value  
> to the organization.




When I shared the study results with my manager, he told me:

> ***“We don’t think about how much money we add to the company’s bottom line.” ~*** *Terrible Manager*

That is the most horrible career advice I have ever heard.




> If you’re not thinking about  
> your impact on the company’s bottom line,  
> **you’re not doing your job.**




Another example: Yesterday I spent the entire day grappling with the ES6 spec to get to the bottom of [a common problem](http://blog.getify.com/es6-concise-methods-lexical-or-not/). I thought it was a bug in Babel, a tool that lets you use **time saving features** in the latest version of JavaScript even though most browsers & mobile devices don’t support those features yet.

The result? It wasn’t a bug at all. It was (in my opinion) awkward design in the JavaScript specification. Babel and other JavaScript engines are just following the specification even when it doesn’t make sense. My output for the entire day was **a lot of documentation on the issue,** and a **simple style guide rule** to **help developers avoid it** or **easily diagnose the issue** if they stumble across it.

I didn’t close a single ticket on the project I was working on yesterday. Instead, there are **two tickets** for **two open source projects** on GitHub, a **blog post** describing the issue in-depth, **several code samples** demonstrating the issue and its workarounds, and a lengthy twitter discussion that involved the author of a book on the new features of JavaScript, and Brendan Eich, the inventor of JavaScript.

*Thankfully, everybody was very patient with my misinterpretation of the spec, and disagreed with me respectfully. I’m really glad that we have a community that can argue and come out friends on the other side.*

None of this shows up in **my own project’s issue tracker,** but the work I did yesterday may prevent **hundreds or thousands of developers** from being similarly confused, and may prevent **hard to find bugs** in many projects.

A manager looking at tickets might think **I wasted the entire day** and had **nothing to show for it.**

Those managers are missing a very important point:




> **The best way to be a 10x developer**  
> is to help 5 other developers be  
> 2x developers.




> Ironically,***the best way to get fired***for underperformance***is to be a 10x developer.***




Likewise, many **junior developers**, are incorrectly **assessed as 10x developers** simply because **they close 10x more tickets** than another employee.

The problem is, without enough **experienced mentors** on the team **reviewing other people’s tickets,** and tackling deep issues in the software’s architecture, **you’re paying people to slow the rest of the team down.**

People who **focus primarily on the number of tickets** they close often do so **at the expense of quality.**

They bolt awkward additions onto already brittle code. When something new comes along that does **almost the same thing** as something that already exists, rather than recognize it as a repeating pattern and making it more reusable, they **copy and paste existing code**, which means that if there is a bug in that code, they’re spreading the bug around the codebase like a disease, instead of creating a safe quarantined space where the bug can be addressed and fixed one time instead of six or ten times.

**Drive by coders:** They stick their head out the window, throw a quick fix in the general direction of the problem, and move on to the next thing.




> Mediocre coders  
> *leave heaping piles of* ***technical debt*** in their wake.

> *And* ***you think they’re 10x developers***  
> because **tickets.**




You’re rewarding people who are just too early in their career to **recognize technical debt**, let alone specialize and **dive really deep** into issues that **really move the needle** for long-term organizational **software development productivity.**

### How do You Judge Performance?

Closed job tickets is the **least significant factor.**




> *Ticket based performance evaluation  
> is the* ***worst idea*** *in the history**of software development.*




Instead of being blinded by closed tickets, **treat your employees like human beings instead of numbers.**

Unsure whether or not they’re working out? **The worst thing you could do is show them that you don’t value them.** The moment you do that, **you’ve lost them.** It’s only a matter of time before they find somebody who will **appreciate them.**

Employees need to feel **appreciated, valued,** and **productive.** The best managers **learn from their employees** and **mentor employees** (in that order) to maximize the value they bring to the organization. That starts with **listening.**

**Before you express your doubts,** ***talk to them.***

Look at their **total contribution.**

Learn to value the **things you can’t track and count directly.**




> Like word of mouth advertising,  
> the things you can’t trackare the most valuable.




**Ask coworkers** to rate the employee’s helpfulness and knowledge. **Ask for the employee’s help** to find evidence of his or her contributions, not just in your codebase, but also in **open source you depend on,** **documentation, mentorship for other employees, design advice** and **architecture documentation,** **talks they gave,** **how they represent your company to the public,** and on and on…

**The employee you are evaluating is the best source** of this information. It’s up to you to decide how you value the sum of those contributions.

The best organizations build **listening, learning, and mentorship** deep into the company’s cultural DNA.

#### Numbers aren’t all evil

Google provides managers with standard forms and guidance on the subjects of candidate and employee valuation, and those forms and guidance get measured against quantitative organizational value. That’s worth emulating.

It’s a very good idea to **measure changes in your company value and revenue per employee,** and **track how those numbers correlate with candidate and employee assessment measurements.**

Measurements of guidelines must be evaluated over the span of ***years.*** It takes time to change cultural behaviors, and it takes much more time to measure the impact of that work. *But it’s worth it.*




> Your people make such a big impact,  
> you can’t afford to take shortcuts.




You can use those numbers to **evaluate your evaluations.** Learn to **recognize the mistakes** you’re making and **fine tune your guidelines** to point your managers, employees and recruits in positive directions.

*TL;DR: How do you measure an employee’s performance? Listen to them.*




> Want to learn how to become a 10x developer?

> [Learn JavaScript  
> with Eric Elliott](https://ericelliottjs.com/)




***Eric Elliott*** *is the author of* [*“Programming JavaScript Applications”*](http://pjabook.com) *(O’Reilly), host of the documentary film-in-production,* [***“Programming Literacy”***](http://www.programmingliteracy.com/)*. He has contributed to software experiences for* ***Adobe Systems****,* ***Zumba Fitness****,* ***The Wall Street Journal****,* ***ESPN****,* ***BBC****, and top recording artists including* ***Usher****,* ***Frank Ocean****,* ***Metallica****, and many more.*

*He spends most of his time in the San Francisco Bay Area with the most beautiful woman in the world.*