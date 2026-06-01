---
title: Everything is Amazing, But Nothing is Ours
date: '2019-11-04T07:51:31-07:00'
format: link
service: instapaper
tags:
- read
external_url: https://alexdanco.com/2019/10/26/everything-is-amazing-but-nothing-is-ours/
---

[Everything is Amazing, But Nothing is Ours](https://alexdanco.com/2019/10/26/everything-is-amazing-but-nothing-is-ours/)  



Back in 2015, I wrote a blog post called [Dropbox: the First Dead Decacorn](https://alexdanco.com/2015/08/24/dropbox-the-first-dead-decacorn/). At the time, it was the most widely shared take I’d ever written. I learned several things from writing this piece, and none of them had to do with Dropbox: I learned, for instance, that a great way to get people to click on your blog post is to make them mad. I also learned about a company called Social Capital, after my soon-to-be-colleague Ray reached out to me about what I’d written. I’m certainly thankful I wrote it.

Today, Dropbox is not dead. I’m glad! I certainly never *wanted* the business to do poorly. I used it all the time back then, continue to have friends who work there, and generally would rather not cheer for companies to fail; that’s not a great look. But I think it’s fair to say that the take didn’t turn out to be egregiously wrong. (Dropbox had last raised at a $10 billion valuation the year before, and currently trade at an 8 billion dollar market cap. So over the last five years that’s a -4% annual return, compared to the S&P at around 10%. Not dead, but hardly what I think most people pictured the next 5 years to be like.)

Relatedly, I do believe that the main idea in the blog post turned out to be correct. Dropbox was the ultimate file product. But it also hit right at Peak Files. Files aren’t the focus going forward. At the time, I wrote:

*“Files are discrete objects that exist in a physical place; the internet is pretty much the opposite of that. … Dropbox might be the pinnacle of file management, but Slack is the beginning of what comes next. I don’t think files are going to completely disappear; not anytime soon, anyway. They’ll certainly still exist as data structures, deep inside our servers and our phones, for a very long time – and yet most people will be indifferent to their existence.”* 

![](https://alexdanco.files.wordpress.com/2019/10/dropbox.jpg)![](https://alexdanco.files.wordpress.com/2019/10/dropbox.jpg)

I got to thinking about all this the other week after hearing news that [Yahoo Groups was shutting down](https://www.vice.com/en_us/article/8xwe9p/yahoo-groups-is-winding-down-and-all-content-will-be-permanently-removed), and wiping out two decades of content – sending online communities and archivists into a scramble to preserve their spaces and history before it all disappears. It’s a huge bummer, for sure; and also a reminder of a hidden price we pay for modern technology. Everything is amazing, but nothing is ours.

Up until the mid 2000s or so, it felt like the collective goal of software and the internet was to create digital versions of all the stuff that worked well in real life – documents became Word, slides became Powerpoint, and mail became email. It’s also why files are called files, and why we got rid of them by dragging them into the trash can. Software was pretty [skeuomorphic](https://www.interaction-design.org/literature/topics/skeuomorphism) in design and in function. The file as an atomic unit for productivity made sense. It’s a solid, distinct object you could understand, and that was yours. You had to take care of it, name it properly, and save it in the right place, just like a paper file.

But for the last ten years, we’ve been undoing all of that. The constraints of mobile, plus a new generation of users that’ve never really known life without the internet, meant the benefits of skeuomorphism were no longer worth the cost. Ditching it as a philosophy, both in design and in function, freed us to go out and reinvent everything as a *service.* Abstract everything away into databases, links and logic, and provide it as a consumer service with all the topology and complexity hidden out of sight.

We love services. Services free us to be pure consumers, seeking [exactly what we want](https://medium.com/social-capital/understanding-abundance-part-1-its-caused-by-consumers-db7abb984e2e) for as little friction and overhead as possible. So long as everything works, trading ownership for access is an attractive deal: everything under the hood just gets magic-ed away, and provided for us as a service. No files, no updates, no maintenance; [just access](https://alexdanco.com/2015/02/02/the-rise-of-the-access-economy/%0A).

This isn’t just a software thing, by the way. New technology generally reorganizes our consumption away from ownership and towards access. 100 years ago, music came from a piano, then it came from the record store, and now it comes from Spotify. 100 years ago, food came from a farm, then it came for a grocery store, and now it comes from DoorDash. There’s no denying that this is forward progress for the consumer. You would not want to go backwards. But there’s a cost. The more you can access, the less it’s yours.

I joke sometimes that my generation’s version of “Sorry I’m late, the car broke down” is “Sorry I’m late, the car got lost.” It makes me laugh because cars are obviously better than they used to be: they don’t break down like they used to, they’re safer, and best of all, you don’t even have to drive it anymore. You just push the Uber button and somebody comes and picks you up. But it’s also not funny, because we’ve all experienced the particularly modern frustration of seeing the Uber drive in the opposite direction, spin around 4 times, then cancel. Access *feels* like the real thing, until it’s taken away from you.

Look, all technology breaks sometimes. I’m not saying that new is bad because it’s buggy; I promise you, the old stuff broke too. You probably do not want to go back. But there’s a difference between “the car broke down” and “the car got lost”. One is a fragility of *things*: if you drive a car, you need to take responsibility for keeping it in good shape. It’s a scarcity problem. But the latter feels more like an abundance problem: it’s fragility of *something,* I just couldn’t put my finger on what.

Right as I was thinking about all of this, I came across this fabulous post by Simon Pitt from a couple weeks ago that had the answer.

[Computer files are going extinct | Simon Pitt](https://onezero.medium.com/the-death-of-the-computer-file-doc-43cb028c0506)

The whole post is good, but one thing he wrote hit me as a perfect gem of an idea, not just about files and software systems but about technology in general:

*“The other day, I came across a website I’d written over two decades ago. I double-clicked the file, and it opened and ran perfectly. Then I tried to run a website I’d written 18 months ago and found I couldn’t run it without firing up a web server, and when I ran NPM install, one or two of those 65,000 files had issues that meant node failed to install them and the website didn’t run. When I did get it working, it needed a database. And then it relied on some third-party APIs and there was an issue with CORS because I hadn’t whitelisted localhost.*

*My website made of files carried on, chugging along. This isn’t me saying that things were better in the old days. I’m just saying that**years ago websites were made of files; now they are made of dependencies**.”*

The last line really hit a chord with me: that’s exactly it. Worlds of scarcity are made out of things. Worlds of abundance are made out of dependencies. That’s the software playbook: find a system made of costly, redundant objects; and rearrange it into a fast, frictionless system made of logical dependencies. The delta in performance is irresistible, and dependencies are a compelling building block: they seem like just a piece of logic, with no cost and no friction. But they absolutely have a cost: the cost is complexity, outsourced agency, and brittleness. The cost of ownership is up front and visible; the cost of access is back-dated and hidden.

Files feel like a good bellwether for what’s happening. We’re in this funny in-between time right now where our phones are fully in the future: apps are services kind of by definition, and it’s *really* hard to access the file system. But our computers are still kind of in the past: to me, at least, the two most important navigational anchors on my computer are the desktop and the downloads folder.

One of the funny outcomes of this half-mobile half-desktop world is where our de facto file system remerged. In absence of a coherent, logical file system across these two worlds, we trampled down a [desire path](https://en.wikipedia.org/wiki/Desire_path) and made our own: our email inboxes. I (and many of you, I’m sure) use my email inbox the way we’re all supposed to use Dropbox: it’s a ubiquitous, universally understood way to move stuff around, store and retrieve it. Gmail is the new Finder.

Email as a file system is inefficient, terribly designed, and full of friction. Repeatedly emailing yourself copy-and pasted information and attachments called presentation\_final, presentation\_final2 and presentation\_final\_final is nobody’s idea of a good time. But you know why it works? Dependency minimization. It’s air gapped from the rest of your work: no software update or edge case is going to screw things up so badly that it goes into your inbox and deletes your emails. You can always get to your email, and that attachment will always be there. It’s a universally adopted format. Most importantly, your inbox is *yours*.

I think there’s a really strong, counter-trend bet to be made here over the next few tech generations. If the world is going to get reorganized into services and dependencies, so be it; but find what’s air gapped, and find what’s ours. People are smart enough to tell what’s solid and what isn’t. Product teams who go out of their way to give us real, tangible objects we feel that we can own will find a great deal of success.

One example of a software company doing the right thing today is Figma. They’ve built an incredible user experience for multiplayer design software – a domain that’s been fully SaaSed – by taking *out* the excessive, “everything must be live access” type of dependencies [in favour of simpler, stabler architecture](https://www.figma.com/blog/how-figmas-multiplayer-technology-works/) that works fabulously and feels solid, like something you can trust. Meanwhile, the Bitcoin ecosystem is having a real effect on how people think about ownership versus access, as people learn about how to store and manage their private keys, and by extension, come to realize everything that access isn’t.

I’m fully confident that we’ll continue to invent great software that reimagines how the world can work. But I’d love to see more teams embrace the idea that less friction isn’t always best. If the current trend of technology is sweeping us in a direction of “everything is amazing, but nothing is ours”, *Technology that’s Actually Yours* could be the next great counter-trend.

*Like this post? [Get it in your inbox every week](http://danco.substack.com/) with Two Truths and a Take, my weekly newsletter enjoyed by thousands.*

  

[Uncategorized](https://alexdanco.com/category/uncategorized/)