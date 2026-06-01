---
title: How to Join a Team and Learn a Codebase
date: '2021-02-07T11:58:13-07:00'
format: link
service: instapaper
tags:
- read
external_url: https://www.samueltaylor.org/articles/how-to-learn-a-codebase.html
---

[How to Join a Team and Learn a Codebase](https://www.samueltaylor.org/articles/how-to-learn-a-codebase.html)  



[Home](https://www.samueltaylor.org/index.html) > [Articles](https://www.samueltaylor.org/articles/index.html) > new codebase, who dis? (How to Join a Team and Learn a Codebase)
# new codebase, who dis? (How to Join a Team and Learn a Codebase)

I have switched teams more often than I have had to implement an AVL tree, and you can guess which one of those two was taught in school. I wish someone had taught me how to join a new team! While learning a new codebase can be daunting, I’ve found a few things that work for me.

You should do at least three things when joining a new team. The order of these three can be whatever you like, but all three should be done as soon as reasonably possible.

**First**, you’ll likely set up the development environment. As you do this, pay attention to just what it is that you’re setting up. For instance, if you need to get Redis running locally, then that’s a good hint that there’s some caching happening somewhere. Noting the order in which you run internal projects helps you understand dependencies. If the feature store needs to be running before you bring up the model serving service, that’s a hint that the model serving service may depend upon the feature store. Such dependencies start to hint at the overall architecture.

Take notes on the exact commands you’re running and packages you’re installing. You’re bound to run into something that’s changed since the setup docs were written, and being able to correct them is a quick win you can provide to the new team. Plus, it’s good to know exactly how you ruined your system installation of Python.

Ideally, the code you’re working on should have some sort of automated test suite in place. A good way to start experimenting with and understanding the code is to get that test suite successfully running, then make changes to the codebase completely at random and see what breaks.

The **second** thing you should do is get some overview of the architecture. Some teams will have a document describing this, and if that document is an accurate depiction of reality then you should certainly work to understand it. In any case, asking a more senior person on the team to give you an overview is a good idea. They should know how up-to-date that document is (if it does exist) and also be able to describe and/or draw the architecture for you. Here are some sample questions you can consider asking:

* What repositories (or portions of repositories) do we own and/or work on most frequently? What do each of them do?
* Where does our code run? (e.g. EC2 Instances, Google’s Kubernetes Engine, on prem)
* What does the deployment pipeline look like? How does a feature get from my laptop to live in production?
* Do we have certain services, packages, classes, or files that are a real headache? Areas that are particularly unreliable or error-prone?
* Are there external API’s, vendors, or products that we use or rely on? (e.g. SendGrid, DataDog, MySQL)

Similar to environment setup, an easy thing you can do to help the team is to document that architectural overview (or update the existing document). Write down what you learned, take a picture of the diagrams that were drawn, and post that information somewhere visible to the team. Be sure to put an “as of” date on your changes. Even stable projects exhibit some change over a long enough time period, so this date will help future readers know if they can trust this document.

A **third** thing you should do when starting on a new team is start understanding the business. If you’re new to the company, figure out its mission, product offering(s), and goal(s). Then work to understand how your team fits into those things. Some sample questions include:

* How can our team make an impact on the company’s goals?
* If our code were to break horrifically, who would get angry? How fast would that happen?
* What other teams do we have the most interaction with? What services/codebases do they own? Do we share parts of our codebase with other teams?

Without an understanding of the team’s place in the company, you’re doomed. You won’t have sufficient context to execute your work well.

## Mindset

I strongly believe that learning a new codebase happens best through implementing real features (even if they are small to start with). The whole point of being on this team as an individual contributor is to build stuff, and there is no better way to learn how to do something than by spending quality time doing that exact thing. As you build skill and understanding, you can work on larger and larger projects over time.

Implementing something will require you to read the code. But “read” may be a misleading word here, because reading code is dramatically different from reading a novel. Code is typically organized with more related code being closer together (in the same directory, package, class, or file). Can you imagine a novel written in this way? If Tolkien had placed all scenes of two characters fighting each other in adjacent pages, while all scenes with magic in them occurred in a separate book? How absurd!

Though learning to code taught me the basics of reading code, nobody ever taught me how to read a large codebase. To do so, we must adopt a certain mindset. Balance understanding each intricate detail against making impact quickly. Quick impact helps establish your reputation on the team and gets you to that accurate/intricate understanding faster than trying to read everything up front.

The rule of thumb I use is to understand something just enough to express what it does without necessarily knowing exactly how it does that. This process is called “chunking,” and it relies on the fact that once you have a basic understanding of a unit of code, “you don’t need to remember all the little underlying details” (Oakley). If you’re worried about not understanding everything in minute detail, don’t be afraid to take a note to come back and understand that chunk more fully.

This understanding will grow recursively: first, you understand what the various services do. Then, you identify the particular service you need to modify and start to understand the various modules within that service. In the modules you modify, you’ll start to understand the classes contained. The base case of this recursive process is the individual line.

Keep in mind that different teams may implement the same concept or pattern in different ways. Understanding why your current team chose the way they did is another way new teammates can help the team. It’s totally possible that your new team hasn’t heard of the cool way to implement singletons that you like. It’s equally possible that your way is worse in some way you didn’t know. Either way, someone gets to learn something!

The last mindset recommendation I’ll give before we dive into the process is to try to understand the code both in terms of code paths and data flows. Think about which objects know what information and how that information flows between parts of the system.

## Process

I recommend this process for working in any codebase:

1. **Locate the portion of code most relevant to the immediate task** at hand.
2. Understand that code enough to **form a hypothesis** about the change you need to make.
3. Make that change and **test your hypothesis**. Sometimes the best way will be to click around in the UI or run a particular script. Sometimes the easiest path is to write a test that describes the behavior you’re after.
4. If your hypothesis was incorrect, return to step 2. Understand why that change didn’t do what you thought it would, and develop a new hypothesis.
5. Once you have working code, **improve its quality**. Write a test (or a few) that document the changes in behavior you made. Refactor your code for clarity and style.

This scientific approach guides us gradually toward correct, high quality code without having to understand each and every bit of code around our change.

## Tools

While you could certainly get by with just a text editor and some patience, a wide variety of tools exist that help us read code more effectively throughout the process identified above.

### Identifying relevant code

While step one gets easier over time as we build familiarity with some portion of code, we often begin step one completely lost. A few approaches are helpful here: running the code, project search, and code search.

Running the code helps you understand it. Before you start changing things, understand what already exists. This could mean reproducing a bug locally, finding the place in the UI where the new feature will go, or any number of other things. When you do, stepping through the execution in a debugger will give you a strong start on understanding what is going on.

By “project search,” I mean searching artifacts created as part of the software development lifecycle. Particularly useful are issue trackers like JIRA/Asana/Pivotal Tracker, pull requests and issues in tools like GitHub and GitLab, and the git history itself. Because few tasks are truly novel, we can often gain understanding by looking for similar past work. Try several different keywords. Sometimes you’ll find a pull request that implements something very similar to what you want to do, and you can use that as a guide. Trying to divine something from scratch, while sometimes necessary, requires significantly more effort than adapting from an example.

Code search is just what it sounds like. For code that you have checked out locally, I highly recommend using a tool specifically built for recursive search like ack, Silver Searcher (ag), or ripgrep. But you won’t always have every bit of code at the company checked out locally, and sometimes it’s useful to be able to search exhaustively. For this use case, tools like OpenGrok or Sourcegraph are super helpful. GitHub and GitLab also offer ways to search all code within a specific organization.

No matter which tool you’re using, try several keywords you think might be relevant. Consider changing case sensitivity. You may have better results filtering down to specific file types.

### Understanding code

Using these various search tools, we arrive at a set of relevant locations. Thus, we arrive into step two of our process: understanding the code just well enough to form a hypothesis about the necessary change. The search tools we’ve already discussed are helpful to this end (if you come across usage of an unfamiliar class, search for it and read what you find).

One other tool that is incredibly useful is a good IDE. I like JetBrains’ products (I have no affiliation with them), though I’m sure similar functionality exists in competing products. JetBrains IDE’s can help you navigate code much more efficiently by linking you straight through to the definition of a function or class. By default on Macs, hold down Cmd and hover over the function or class name, then click. Being able to immediately jump to the definition is a complete game changer.

Another super-useful JetBrains keyboard shortcut is (by default) tapping shift twice. This brings up a search bar that can find just about anything (classes, functions, file names).

As you read code, always try to decrease your cognitive load. Remember to create “chunks”, mental boxes inside of which you don’t need to remember all the details. Consider taking notes, writing down file names and line numbers, drawing little diagrams. Reading and writing code is the most cognitively demanding part of the job, so take any chance you can get to make it easier for yourself.

You may get stuck or lost during this process. It is OK to ask for help. Use `git blame` to see who has been working on some bit of code you find confusing, and ask them about it. You can also use `git blame` to find relevant pull requests or JIRA tickets that might help you gain context.

### Working with libraries

Sometimes as part of step three, we will need to work with an external library. In an ideal world, all libraries have excellent documentation that helps you understand the key abstractions and be productive quickly. Alas, we do not live in an ideal world! Many projects do have good documentation. But others may be more easily learned through the broader community. Consider searching the web with a tool like DuckDuckGo or Google. See if there are examples on StackOverflow.

A recent lightbulb moment for me was realizing that GitHub allows users to search all public code. Consequently, we can find realistic examples of people using libraries and API’s that we care about. Try searching for the particular method name you’re trying to use. Or search for the name of the package, then search within individual repositories that come up. Consider filtering to just the language you care about.

Anecdotally I have found that sorting GitHub search by “recently indexed” gives me more diverse, more helpful results than the default search (which largely gives me the same copy-pasted examples over and over again). If you’re unhappy with your results, do try different sort orders.

## Parting words

Not only do we learn faster when we orient that learning around real tickets, but we simultaneously make an impact and start building reputation on the team. By taking advantage of prior work (and using good tools to find that work) we can accelerate our learning and our impact. Know that while joining a new team is non-trivial, it doesn’t have to be hard! Use the scientific method. Follow these practices. Take a look at these tools. You’ll gain confidence in your abilities and make a good first impression while you’re at it.

*If you found this interesting, consider [following me on Twitter](https://twitter.com/SamuelDataT). Thanks to my friend Benjamin Cody for providing feedback on this post.*

*Update 2021-01-16:* @Coding\_Career on Twitter made an awesome “cheat  

sheet” from this post [available here](https://twitter.com/Coding_Career/status/1350445944395821056).

Citations:

Oakley, Barbara A. *A Mind for Numbers: How to Excel at Math and Science (Even If You Flunked Algebra)*. Jeremy P. Tarcher/Penguin, 2014.