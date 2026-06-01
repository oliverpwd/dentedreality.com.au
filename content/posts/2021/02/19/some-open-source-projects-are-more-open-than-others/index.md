---
title: Some Open-Source Projects Are More Open Than Others
date: '2021-02-19T07:37:27-07:00'
format: link
service: instapaper
tags:
- read
external_url: https://builtin.com/software-engineering-perspectives/mergechance
---

[Some Open-Source Projects Are More Open Than Others](https://builtin.com/software-engineering-perspectives/mergechance)  



Piotr Zakrzewski is a sometime-contributor to open source projects. He’s not a regular on any one project, but more of a dabbler — a self-described “outsider contributor” who sometimes submits pull requests to projects he enjoys using.

In fact, Zakrzewski said, many contributors to open-source projects are outsiders.

“We are talking about people who usually use the project,” he said. “They don’t work on the project directly, they just use it for something else. And they found a bug or a missing feature, and because they were passionate about it and they like open source, they decided to give it a chance and make a contribution.”

But among the projects open to outside contribution, Zakrzewski found that some were a bit more open than others.

“There are some projects that are very eager to accept your contributions, that are more likely to merge it, that do whatever is needed to work with you to get it merged,” Zakrzewski said. “And there are also some projects that are more likely to ignore them, or they just don’t accept them.”

MORE ON ENGINEERING[Is an Open Web Still Possible?](https://builtin.com/software-engineering-perspectives/open-web)

## Open Source Isn’t Necessarily Open Collaboration

The definition of open source can be confusing. For instance, there’s a difference between open-source code and code that’s simply visible to the public, like code stored in public repositories on GitHub.

“You can inspect all open-source code, but not all code that you can inspect is immediately open source,” Zakrzewski said.

The exact definition of open source is squishy, but it generally means a project that is available to anyone to freely use.

“What determines that is a license,” Zakrzewski said. “There are certain types of licenses, like LGPL, GPL, MIT, FreeBSD, Apache and so forth, that, if you see them, means that this project is open source.”

These licenses state that projects are available for anyone to download, use and modify. For many open-source projects, there’s also an open collaboration aspect where anyone can contribute pull requests into the main branch of the codebase, but that’s not always the case.

> “There are projects that allow you to do anything you want with the code yourself — fork it, modify it, redistribute it, sell it — but they will not accept an outsider contribution into the main branch.”

“Just because something is open source, that does not necessarily mean that it’s open contribution,” Zakrzewski said. “There are projects that allow you to do anything you want with the code yourself — fork it, modify it, redistribute it, sell it — but they will not accept an outsider contribution into the main branch.”

Open-source projects closed to outside contributions are also easy to spot, because they usually say so explicitly in the project’s README file, Zakrzewski said. The real difficulty is figuring out just how open to contributions the remaining open-source, open-contribution projects really are.

“The problem is this gray zone in between,” Zakrzewski said. “They either don’t want to invest time anymore in interacting with the community, they simply cannot afford it — time-wise, mostly — or they just don’t want to do it for another reason but they don’t make it explicit. In other cases, they actually kind of would like some contributions, but they’re just very picky.”

That’s not an inherent problem — projects are different, and some may have characteristics that make pull requests difficult to get past review. But working on and submitting a pull request can take significant effort for developers, and Zakrzewski began to wish he knew the likelihood his suggestions would be accepted ahead of time.

“I didn’t know how to tell those apart for some time, and I found it a bit frustrating,” he said. “I felt that maybe other people find it [frustrating] too — it’s not easy to figure out how likely the contribution is ignored or not.”

At the time Zakrzewski was interested in learning to use the GraphQL programming language, so he combined his interests and built a tool that estimates the likelihood an outsider’s pull request on GitHub would be accepted, called [Merge Chance](https://merge-chance.info/).

## What Is Your Merge Chance?

Using GitHub’s documentation, Zakrzewski found APIs that gave him data from GitHub repositories, including those of some open-source projects he had unsuccessfully tried to contribute to.

“Once I fetched this data, I just calculated some very simple statistics,” Zakrzewski said. “How many pull requests are being merged in total, and what can I say about the people who merged them?”

He classified each project’s pull requests into two groups: those initiated by insider contributors and those initiated by outsider contributors. Insider contributors were considered to be people who owned repositories or belonged to organizations that owned the repositories. He then calculated the chance that a pull request has of getting approved for each project.

Zakrzewski found that most pull requests to open-source projects are accepted. “So open source mostly works,” he said.

> “It is a metric, it’s not necessarily a score that should be maximized.”

Zakrzewski was surprised to find that bigger open-source projects are more likely than smaller ones to accept outsider pull requests. This might be because larger projects have more people who can help review outside contributions.

“It is kind of counterintuitive that it is those big projects — usually backed by bigger companies — that are very dynamic, and they have enough people to really help you with approving your contribution,” Zakrzewski said. “A lot of small projects are those that are most likely to ignore you, or they just don’t have the resources to accept your contributions.”

Although Merge Chance calculates a percent likelihood of approval for each project, Zakrzewski said it’s important not to think of the number as a score.

“It is a metric, it’s not necessarily a score that should be maximized,” he said. “Whether every project should aspire to have 90 percent-plus merge chance — no, they shouldn’t. But it’s still useful to know what is the merge chance, because making a contribution to the project takes a lot of effort from the contributor, and also from those who accept it.”

## Some Contributions Are Actually Spam

Zakrzewski has tweaked the Merge Chance classifications to reflect feedback from developers. One adjustment affected how insider and outsider contributors are defined to better catch insiders who look like outsiders.

“There are a lot of different ways that people work with GitHub,” he said. “Some projects are very disciplined about adding insiders, and they give them official rights — those are very easy to detect. But more informal projects — or just projects that are organized differently, or from smaller companies — they don’t always do that. Contributors or even maintainers of a project, from a GitHub perspective, don’t differ at all from outsiders.”

In those cases, Merge Chance is likely to give the projects inflated likelihood values, because insider contributors get counted as outsiders. After Zakrzewski set a limit on how many contributions outsiders can have before being classified as insiders, the results gave a more accurate value.

Currently, he is working on something that will filter out spam pull requests, which artificially brings down a project’s Merge Chance value.

“For instance, Vue.js and React are very popular open-source projects, and they experience significant amounts of daily spam contributions,” Zakrzewski said. “Some developers — it’s hard to say why they do this — they just open frivolous contributions like Hello World, or they change one word in the README, and the maintainers immediately close them. So that inflates the metrics a bit for some repositories.”

Owners of open-source repositories who are interested in fostering more outsider contributions have also reached out to Zakrzewski about the project, in order to figure out how they can best help outsiders get involved in the community.

“They are interested in how the project they contribute to looks like,” he said. “Let’s say the product I work on accepts 60 percent. How do I feel about this? Should we maybe be more open? Should we be less critical? Or maybe it’s OK. It’s one more metric that developers might be interested in.”

MORE ON ENGINEERING[Could Tax Dollars Fund Smaller, Better Social Media?](https://builtin.com/software-engineering-perspectives/digital-public-infrastructure)