---
title: Free software maintenance – Adding Features
date: '2021-11-16T20:34:36-07:00'
format: link
service: instapaper
tags:
- read
external_url: https://ometer.com/features.html
---

[Free software maintenance – Adding Features](https://ometer.com/features.html)  



*This was written sometime in 2004, I think*

How does the maintainer of a free software project decide which features to  

add? The guiding principle is simple: ask “why,” rather than “why not.”

Let’s start with some mails from Linus Torvalds on the subject,  

since people are more likely to listen to him than me:  

[here](http://www.uwsg.iu.edu/hypermail/linux/kernel/0210.3/2128.html)  

and [here](http://www.uwsg.iu.edu/hypermail/linux/kernel/0210.3/2141.html)  

([local mirror if the links died](https://ometer.com/linus-on-features.html)).

All code is *presumed harmful*, because it will have bugs and  

maintenance costs, and introduce behaviors that will interact with other  

features. One feature often precludes or simplifies the implementation of some  

other feature, and these interactions can be unpredictable.

The basic job of a maintainer is to keep things on track, taking a  

long-term view. In practice this means saying “no” a lot.  

How do you convince a maintainer to add a feature? Provide a rationale  

which:

* Does not apply to all possible features.
* Contains facts or empirical data rather than speculation.
* Demonstrates that you’ve done your homework on alternative  
  
  solutions to the same problem.
* Demonstrates that you know what the *root* problem actually  
  
  is; what motivates the feature? How else could it be approached?
* Demonstrates that you’re thinking of all users in the big picture,  
  
  instead of just yourself and people like you.
* Improves things for a large percentage (50%?) of users, or makes the  
  
  impossible possible for a smaller percentage (5%?). “Easy things easy,  
  
  hard things possible.”
* Shows that the feature is genuinely important enough to be worth  
  
  maintaining some extra code.

Bad rationales which apply to all possible features include:

* Some other operating system had the feature.
* Some (unknown number of) people might like it (for some  
  
  unknown reason).
* “But the feature doesn’t hurt anyone who isn’t using it.”

These rationales *a priori* don’t count, because allowing all  

possible features destroys the software. Software can’t be infinite in  

size. All rationales must draw a line between what’s in and what’s  

out.

Important homework for any feature:

* What do other operating systems do?
* What other approaches were considered and rejected?
* Who else have you talked to and what did they say?
* Is the feature already present in custom vendor-specific patches?
* Are there any applicable standards?
* If the feature is performance-related, what is the current  
  
  performance, are performance problems user-visible, and what are the  
  
  possible gains?
* How does the feature interact with other features?
* Were there any mailing list threads?
* What does the UI team think about the UI for this feature?
* Is the feature designed around user concepts and goals or the implementation  
  
  details of the software?

Please don’t assume that the key issue for accepting a feature is whether  

there’s a patch. It isn’t. It’s easy to write a patch. It’s hard to maintain a  

software project over the long term. Maintainers absolutely have to  

*understand the rationale* for each feature, not just rubber stamp the  

patches. If they don’t understand a feature they can’t maintain it over  

time. There will be future decisions about how the feature works, or how related  

features work, and the maintainer will have to make those decisions.

Thus the maintainer must understand *why the feature exists, in detail.*  

If they just take your word for it, they aren’t doing their job.

See also [this argument](https://ometer.com/free-software-ui.html),  

specifically the part about preferences, which are especially likely  

to have poor rationales.

Please don’t bother flaming maintainers because your feature hasn’t  

gone in yet. Provide better rationale, yes. Randomly flame about the  

fact that maintainers have to say “no” a lot, no. Design by committee  

is far, far worse than rejecting a couple of patches. As Linus says,  

“If you don’t get it, don’t bother emailing me.”

Special bugzilla rule: if you move a bug from WONTFIX or NOTABUG to REOPENED,  

you had better add additional, quality rationale at the same time.

Here’s one way to look at it: If you’re too lazy to do the homework and think  

through the big-picture rationale, I’m too lazy to add the feature. On the other  

hand, patches that come with well-thought-through rationale are often applied  

right away.

In addition to saying “no,” maintainers have a couple of other  

obligations in my opinion:

* In the presence of good rationale, maintainers should be willing  
  
  to change their mind often.
* If you want to provide your own patch set or distribution of the  
  
  software with different features, the maintainer should not complain.

Making your own patch set or distribution is often a good way to  

demonstrate that a feature is useful and build the case for including  

it in the mainline. (Caveat: external interfaces/APIs should be  

marked as nonstandard or vendor-specific in some way, if included in a  

nonstandard distribution. e.g. if you create a nonstandard function,  

call it yoyodyne\_extension\_blahblah(), not  

standard\_namespace\_blahblah().)

Of course, if a custom patch set or distribution is only of  

interest to 1% of users, it should conceivably stay custom forever,  

instead of being merged. But if it proves its worth for a good number  

of people, probably it should be merged.

Will maintainers make mistakes? Yes. But occasionally screwing up  

the exact line between accepted and rejected patches is a much lesser  

evil than taking every patch immediately would be.