---
title: Finding the point of human leverage
date: '2019-05-15T23:04:57-06:00'
format: link
service: instapaper
tags:
- read
external_url: https://www.ben-evans.com/benedictevans/2019/4/8/mechanical-turks
---

[Finding the point of human leverage](https://www.ben-evans.com/benedictevans/2019/4/8/mechanical-turks)  



One of the paradoxes of today’s internet platforms is they are vastly automated, and have no human control or interaction over what any given person sees, and yet they are also totally dependent on human behavior, because what they’re really doing is observing, extracting and inferring things from what hundreds of millions or billions of people do.

The genesis of this was PageRank. Instead of relying on hand-crafted rules to understand what each page might be about, or indexing the raw text, PageRank looks at what people have done or have said about that page. Who linked to it, what text did they use, and who linked to the people who linked to it? And at the other end of the pipe, Google gets every user to curate every set of search results by hand: it gives you 10 blue links and you tell Google which one was right. The same thing for Facebook: Facebook doesn’t know really *know* who you are, or what you’re interested in, or what that piece of content is. It knows who you follow, what you press ‘like’ on, who else liked that and what else they liked and followed. Facebook is PageRank for people. The same applies, by extension, to YouTube: it never knew what the video was, only what people typed next to it and what else they watched and liked.

In effect, these systems are vast mechanical Turks. They don’t know what anything is of itself – rather, they try to create, capture and channel human annotation around those things. They’re vast distributed computing systems in which the CPUs are people and the platform is the router and the interconnections. (This reminds me a little of the idea in the Hitchhiker’s Guide to the Galaxy that the whole Earth is actually a vast purpose-built computer and our daily lives are part of the calculations.)

This means that a lot of the system design is around finding the right points of leverage to apply people to an automated system. Do you capture activity that’s already happening? Google began by using the links that already existed. Do you have to stimulate activity in order to capture the value within it? Facebook had to create behaviors before it could use them. Can you apply your own people to some point of extreme leverage? This is Apple Music’s approach, with manually curated playlists matched automatically to tens of millions of users. Or do you have to pay people to do ‘all’ of it?

The original Yahoo internet directory was an attempt at the ‘pay people to do all of it’ approach – Yahoo paid people to catalogue the whole of the web. To begin with this looked feasible, but as the web took off it quickly became an impossibly large problem, and when Yahoo gave up gave up the directory had passed 3m pages. The answer was PageRank. Conversely, Google Maps has humans (for now) driving cars with cameras along almost every street on earth and other humans looking at the pictures, and this is not an impossibly large problem – it’s just an expensive one. Google Maps is a private mechanical Turk. We’re exploring the same question now with human moderation of social content – how many tens of thousands of people do you need to look at every post, and how much can you automate that? Is this an impossibly large problem or just an expensive one?

If you look at these platforms as using billions of human beings to do the actual computation, this prompts two interesting questions: what does this tell us about abuse of the platforms, and how much might machine learning change all of this?

In the past, when we thought about abuse of computer systems, we thought about technical exploits of various kinds – stolen or weak passwords, unpatched systems, bugs, buffer overruns and SQL injection. We thought about ‘hackers’ finding gaps in the software engineering. But if YouTube or Facebook are distributed computer systems where the routers are old-fashioned software but the CPUs are people, then a bad actor thinks of finding exploits in the the people as well as the software. [Common cognitive biases](https://en.m.wikipedia.org/wiki/List_of_cognitive_biases) become as important as common programming errors.

That is, there are two ways to rob a bank – you can bypass the alarm and pick the lock on the safe, or you can con the manager. These are both ways that your processing systems are failing, but now one of the processing systems is us. Hence, as I wrote [here](https://www.ben-evans.com/benedictevans/2019/3/13/0mboxl0imfh636ggky829vnweu2qpv) looking at Facebook’s recent strategic pivot to privacy and security, human moderation of the data on these platforms is conceptually very similar to the software virus scanners that boomed in response to malware on Windows two decades ago. One part of the computer watches another part to see if it’s doing something it shouldn’t.

Even without thinking about deliberate abuse there are other problems inherent in using human activity to analyse human activity. Once you start using the computer to analyse the computer, you risk creating feedback cycles. You can see this in the idea of filter bubbles, or ‘YouTube radicalisation’, or even SEO spam. Meanwhile, one of the problems that Facebook has faced is that sometimes having or generating more data degrades the value of the data. This is the newsfeed overload problem: you add 50 or 150 friends, and you share 5 or 10 things every day or so, but so do all of them, and so you have 1,500 items in your feed every day. Dunbar’s number + Zuckerberg’s law = overload … which gets us to Goodhart’s Law.

*“Any observed statistical regularity will tend to collapse once pressure is placed upon it for control purposes.” –* [*Charles Goodhart*](https://en.m.wikipedia.org/wiki/Goodhart%27s_law)

Then, how might machine learning change this? I said earlier that the challenge is to work out how to add people to the right point of leverage in the computer, but there is of course another option – get the computer do all of it. Until very recently, the challenge, and the reason these systems existed in the first place, was that there were large classes of problem that computers couldn’t solve but that any human could do very easily. We used to call this ‘things that are easy for people but hard for computers’, but really, it was things that are easy for people to do but hard for people to *describe* to computers. The breakthrough of machine learning is that it gives us a way for the computer to work out the description.

The cartoon below (from 2014, just after machine learning computer vision systems started taking off), is a good illustration of this change. The first problem is easy but the second was not – until machine learning.



![](https://i1.wp.com/static1.squarespace.com/static/50363cf324ac8e905e7df861/t/5cad8a3415fcc044d7b97fd6/1554876994435/Screen+Shot+2019-04-09+at+11.16.09+PM.png?w=607&ssl=1)![](https://i1.wp.com/static1.squarespace.com/static/50363cf324ac8e905e7df861/t/5cad8a3415fcc044d7b97fd6/1554876994435/Screen+Shot+2019-04-09+at+11.16.09+PM.png?w=607&ssl=1)




The old way to solve this problem would have been to find a way to get people label the picture – to crowdsource this in some way. In other words, a mechanical Turk. But now, we might not need anyone to look at that picture – with machine learning we can very often automate exactly this request.

So: how many problems could you previously only solve if you applied the aggregate behavior of millions or hundreds of millions of people, which you now could solve with machine learning, without having any users of your own?

The contradiction in this, of course, is that machine learning is all about having lots of data. Clearly, one could suggest that having a big platform means you have lots of data and so your machine learning will be better as well. That’s certainly true, at least to begin with, but I think it’s interesting to wonder how many things could *only* be done with all those users. In the past, if you had a photo of a cat, it would only be labeled ‘cat’ if you had enough users that someone would look at and label that particular image. Today, you don’t need any users to see that particular cat picture – you just need some other users, somewhere else, at some point in the past, to have labeled enough *other* cat pictures to generate a decent recognition model.

This is just another form of leveraging people: you need people to do the labelling (and to write the rules for how the people do the labelling). But we move the point of leverage, and change, perhaps radically, how many people we need, and so we change some of the ‘winner takes all’ effects. After all, these giant social platforms are vast collections of manually labeled data, so is the glass half empty or half full? Glass half full: they have the world’s largest collection of manually label data (in their chosen domain). Glass half empty: it’s manually labeled.

Even where that data might be concentrated in a big platform (and very often it won’t – not at all – [as I wrote here](https://www.ben-evans.com/benedictevans/2018/12/19/does-ai-make-strong-tech-companies-stronger)), this becomes, well, a platform. Just as AWS became an enabler for startups, who no longer needed millions of users to get economies of scale in infrastructure, a lot of equivalent tools will mean you no longer need millions or billions of users to recognise a cat. You can automate the Turk.