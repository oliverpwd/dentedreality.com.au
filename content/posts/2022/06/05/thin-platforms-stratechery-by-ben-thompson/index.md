---
title: Thin Platforms – Stratechery by Ben Thompson
date: '2022-06-05T09:20:43-06:00'
format: link
service: instapaper
tags:
- read
external_url: https://stratechery.com/2022/thin-platforms/
---

[Thin Platforms – Stratechery by Ben Thompson](https://stratechery.com/2022/thin-platforms/)  



The Department of Justice’s [1998 complaint against Microsoft](https://www.justice.gov/atr/complaint-us-v-microsoft-corp) accused the company of, amongst other things, tying the Internet Explorer browser to the Windows operating system:

> Internet browsers are separate products competing in a separate product market from PC operating systems, and it is efficient to supply the two products separately. Indeed, Microsoft itself has consistently offered, promoted, and distributed its Internet browser as a stand-alone product separate from, and not as a component of, Windows, and intends to continue to do so after the release of Windows 98…
> 
> Microsoft’s tying of its Internet browser to its monopoly operating system reduces the ability of customers to choose among competing browser products because it forces OEMs and other purchasers to license or acquire the tied combination whether they want Microsoft’s Internet browser or not. Microsoft’s tying — which it can accomplish because of its monopoly power in Windows — impairs the ability of its browser rivals to compete to have their browsers preinstalled by OEMs on new PCs and thus substantially forecloses those rivals from an important channel of browser distribution.

In retrospect, the complaint feels quaint for three reasons:

First, Microsoft won the browser wars, and it didn’t matter; after peaking at 95% market share in 2004, Internet Explorer was first challenged by Firefox, which peaked at 32% market share in 2010, and then surpassed by Chrome in 2012:

The reasons ended up being both a condemnation and an endorsement of the libertarian defense of Microsoft’s actions, depending on your timeframe: sure, the company leveraged its operating system dominance to gain browser market share, but the company also made a great browser (I personally switched with the release of version 4). And then, with Version 6 and its position seemingly secured, the company just stopped development; that is what opened the door to first Firefox and then Chrome, both of which were downloaded and installed by end users looking for something better. The market worked, eventually.

Of course, the reason the market could work is that Windows was an open platform: sure, Microsoft controlled (and allegedly abused) what could be preinstalled on a new computer, but once said computer was in a user’s hands they could install whatever they wanted to, including alternative browsers. That gets to the second reason why the complaint feels quaint: today having a browser pre-installed is de rigueur for operating systems, and Apple’s iOS goes much further than simply pre-installing Safari: all alternative browsers must use Apple’s built-in rendering engine, which means they can only compete on user interface features, not fundamental functionality.[1](#ipfootnote0)

The third reason has to do with Microsoft itself.

#### Thick and Thin

As [I noted last week in an Update](https://stratechery.com/2022/microsoft-build-thick-versus-thin-ai-platforms/), one of the overarching themes of CEO Satya Nadella’s [Build developer conference keynote](https://news.microsoft.com/build2022/) was the seemingly eternal tech debate about thin versus thick clients (to dramatically simplify — and run the risk of starting of a flame war — thin clients are terminals for a centralized computer, while thick clients are computers in their own right, that sync):

> The biggest takeaway from this keynote is that for developers, at least the ones that Microsoft is courting, the thin client model has won — although the truth, as is so often the case with tech holy wars, has ended up somewhere in the middle. Here is the key distinction: there is and will continue to be a lot of work that happens locally; all of the assumptions around that work, though, will be as if the work is being done on the server. For example:
> 
> * GitHub Codespaces is an explicitly online environment that you can temporarily use locally.
> * Azure Arc provides the the Azure control plane for an on-premises development environment.
> * The Azure Container Apps service and Azure Kubernetes Service enable developers to write locally in the same environment they deploy to the cloud.
> 
> Moreover, several other of the announcements were about patching up limitations in cloud development relative to local: Microsoft Dev Box, for example, enables the deployment of cloud-based VM’s that mimic a local development environment for things like app development; Microsoft Cloud PC (which was previously announced) does the same thing for client applications.

What makes this shift so striking is that it is being articulated by Microsoft; after all, Windows (along with Intel) was the dominant winner of the thick client era. Yes, Windows Server was an integral part of Microsoft’s enterprise dominance, but the foundation of the company’s strategy — as evidenced by the tactics used in the fight against Netscape — was the fact that Windows was the operating system on the devices people used. That, by extension, was precisely why mobile was so disruptive to the company: suddenly Windows was only on *some* of the devices people used; iOS and Android were on a whole bunch of them as well.

I’ve spent [many articles](https://stratechery.com/company/microsoft/) writing about how Satya Nadella [weaned Microsoft off of its Windows-centric strategy](https://stratechery.com/2018/the-end-of-windows/); the pertinent point in terms of this Article comes from [Teams OS and the Slack Social Network](https://stratechery.com/2020/the-slack-social-network/):

> The end of Windows as the center of Microsoft’s approach, and the shift to the cloud, though, did not mean the end of Microsoft’s focus on integration, or its attempt to be an operating system; the company simply changed its definition of what an operating system was; Satya Nadella said at [a press briefing in 2019](https://stratechery.com/2019/satya-nadella-on-microsoft/):
> 
> > The other effort for us is what we describe as Microsoft 365. What we are trying to do is bring home that notion that it’s about the user, the user is going to have relationships with other users and other people, they’re going to have a bunch of artifacts, their schedules, their projects, their documents, many other things, their to-do’s, and they are going to use a variety of different devices. That’s what Microsoft 365 is all about.
> > 
> > Sometimes I think the new OS is not going to start from the hardware, because the classic OS definition, that Tanenbaum, one of the guys who wrote [the book on Operating Systems](https://en.wikipedia.org/wiki/Modern_Operating_Systems) that I read when I went to school was: “It does two things, it abstracts hardware, and it creates an app model”. Right now the abstraction of hardware has to start by abstracting *all* of the hardware in your life, so the notion that this is one device is interesting and important, it doesn’t mean the kernel that boots your device just goes away, it still exists, but the point of real relevance I think in our lives is “hey, what’s that abstraction of all the hardware in my life that I use?” – some of it is shared, some of it is personal. And then, what’s the app model for it? How do I write an experience that transcends all of that hardware? And that’s really what our pursuit of Microsoft 365 is all about.
> 
> This is where Teams thrives: if you fully commit to the Microsoft ecosystem, one app combines your contacts, conversations, phone calls, access to files, 3rd-party applications, in a way that “just works”…This is what Slack — and Silicon Valley, generally — failed to understand about Microsoft’s competitive advantage: the company doesn’t win just because it bundles, or because it has a superior ground game. By virtue of doing everything, even if mediocrely, the company is providing a whole that is greater than the sum of its parts, particularly for the non-tech workers that are in fact most of the market. Slack may have infused its chat client with love, but chatting is a means to an end, and Microsoft often seems like the only enterprise company that understands that.

Note that line about “3rd-party applications”: if Teams is the Windows of Microsoft’s new services strategy, then it follows that the platform opportunity for developers in Microsoft’s ecosystem is itself centered on Teams; that’s exactly what Nadella described in the Build keynote:

> Let’s talk about the future of work and how we’re making apps more contextual and people-centric, so you can build a new class of collaborative applications. It starts with Microsoft Graph, which underlies Microsoft 365 and makes available to you information about people, their relationships, and all of their artifacts. Today we are seeing developers around the world enriching their apps with Microsoft Graph. In fact, more than half of the Microsoft 365 tenant are using custom-built and 3rd-party apps powered by the Graph. With Graph connectors ISVs can extend their applications and have them be discovered as part of the user’s everyday tasks, whether they are writing an email, meeting on Teams, or doing a search. For example, data from an app can appear directly in an organization’s search results, as you can see in the experience Figma is building here. You can compose a mail and @-mention files from these apps in-line, and you can access them in Teams chat too. Another way that you can create interactive experiences is by building live actionable loop component using adaptive cards like partner Zoho does. Your users can make decisions and take action like updating the status of a ticket right in the flow of work, and updates are always live, like this one across Outlook, Teams, and Zoho.
> 
> When you combine the Microsoft Graph with Microsoft Teams, you combine the data that describes how people work together with the place they work together. It’s incredibly powerful, and developers are extending their apps into Teams and embedding Teams in their apps. In fact, monthly usage of 3rd-party apps and custom-built solutions on Teams has grown 10x over the last two years, and more and more ISVs are generating millions of [dollars in] revenue from customers using apps built on Teams.

“Graph connectors” are the new APIs.

#### Windows versus Teams

If the Windows platform looked like this…

![](https://i0.wp.com/stratechery.com/wp-content/uploads/2022/05/thinplatforms-2.png?resize=1024%2C535&ssl=1)![](https://i0.wp.com/stratechery.com/wp-content/uploads/2022/05/thinplatforms-2.png?resize=1024%2C535&ssl=1)

…then the new Teams platform looks like this:

![](https://i0.wp.com/stratechery.com/wp-content/uploads/2022/05/thinplatforms-3.png?resize=1024%2C579&ssl=1)![](https://i0.wp.com/stratechery.com/wp-content/uploads/2022/05/thinplatforms-3.png?resize=1024%2C579&ssl=1)

There are a few important observations to make about these differences.

First, in the PC era the monopoly that mattered was being the only operating system on a single device. This, to be clear, is a technical necessity — while a PC could dual-boot into different operating systems, only one can run at a time[2](#ipfootnote1) — but it was the foundation of Windows’ market monopoly. After all, whichever operating system was running on the most devices most of the time was the operating system that developers would target; the more developers on a particular operating system, the more popular that operating system would be amongst end users, resulting in a virtuous cycle, aka a two-sided network, aka lock-in, aka a monopoly.

Once mobile came along, though, not only did the number of devices proliferate, but so did the need for new user interfaces, power requirements, hardware re-imagining, etc.; this made it inevitable that [Microsoft would miss mobile](https://stratechery.com/2014/microsofts-mobile-muddle/), because the company was approaching the problem from the completely wrong perspective.[3](#ipfootnote2) At the same time, this proliferation of devices meant that the point of integration — which enterprises still craved — moved up the stack. I wrote in 2015’s [Redmond and Reality](https://stratechery.com/2015/redmond-reality/):[4](#ipfootnote3)

> That is because there is in fact a need for an integrated solution on mobile. Look at Box, for example: the company obviously has a cloud component, but they also have multiple apps for every relevant — and non-relevant! — platform resulting in much better functionality than what Microsoft previously had to offer. Multiply that advantage across a whole host of services and it starts to make sense for the CIO to modularize her backend services in order to achieve integration when it comes to how those services are accessed:
> 
> [![](https://i0.wp.com/stratechery.com/wp-content/uploads/2015/02/image-30.jpg?w=1024&ssl=1)![](https://i0.wp.com/stratechery.com/wp-content/uploads/2015/02/image-30.jpg?w=1024&ssl=1)](https://stratechery.com/2015/redmond-reality/)

This is exactly what Microsoft would go on to build with Teams: the beautiful thing about chat is that like any social product it is only as useful as the number of people who are using it, which is to say it only works if it is a monopoly — everyone in the company needs to be on board, and they need to not be using anything else. That, by extension, sets up Teams to play the Windows role, but instead of monopolizing an individual PC, it monopolizes an entire company.

Second, developers had much more power and flexibility in the old model, because they had direct access to the underlying PC. This had both advantages — anyone could make an app that could do anything, and users could install it directly — and disadvantages — anyone could make an app that could do anything, and users could install it directly. In other words, the same openness of the PC that presented an opportunity for Firefox and Chrome to dethrone Internet Explorer — and for Netscape to exist in the first place — also presented an opportunity for viruses, malware, and ransomeware.

This latter point is the justification that Apple returns to repeatedly for its App Store model, even though a significant portion of the increased security of mobile devices is due to fundamentally different architectural choices made in designing the underlying operating system. Then again, these arguments go hand-in-hand: it’s those architectural choices in iOS (and Android) design that make App Store control possible; the broader point is that mobile set the expectation that developer freedom — and by extension, opportunity — would be limited by the operating system owner.

A thin platform like Teams takes this even further, because now developers don’t even have access to the devices, at least in a way that matters to an enterprise (i.e. how useful is an app on your phone that doesn’t connect to the company’s directory, file storage, network, etc.). That means the question isn’t about what system APIs are ruled to be off-limits, but what “connectors” (to use Microsoft’s term) the platform owner deigns to build. In other words, not only did Microsoft build their new operating system as a thin platform, they ended up with far more control than they ever could have achieved with their old thick platform.

#### Stripe OS

Build wasn’t the only developer conference last week: Stripe also held [Stripe Sessions](https://sessions.stripe.com/keynote), and one of the tentpole sections of the keynote was called “Finance OS”. Here’s Stripe co-founder and President John Collison:

> We’ve talked about payments, and how they’re highly strategic, and rapidly fragmenting, and we’ve talked about the business model innovations of adaptive enterprises and fintech everywhere. These trends are great news for the Internet economy, but a challenge for finance and business operations teams. The rate limiter for so many new opportunities isn’t the idea for a great product; it’s the mundane foundations. “Can we build for this? Can we get international operations off of the ground? Can we expand when we’re still not closing our books on time?” It’s never just about having the idea for a great product, it’s about being able to operate it, and that’s why we’re building a modern operating system for finance, and like any good OS, we’re focused on nailing the basics.

Those basics included features like invoicing, billing, taxes, revenue recognition, and data pipelines, all of which sit on top of the various ways to gather, store, and distribute money that Stripe has abstracted away:

![](https://i0.wp.com/stratechery.com/wp-content/uploads/2022/05/thinplatforms-6.png?resize=1024%2C566&ssl=1)![](https://i0.wp.com/stratechery.com/wp-content/uploads/2022/05/thinplatforms-6.png?resize=1024%2C566&ssl=1)

This image, given its similarity to the one above, makes clear what was coming next:

> So we just heard about core revenue management capabilities, like invoicing, subscription billing, and handling tax. Even if you’re not using Stripe, these are the things you should want running like clockwork.
> 
> But what about everything else? It’s like any operating system: core functionality needs to work perfectly out of the box, but the breadth of functionality of the platform is also really important, having an app to solve every use case. For things like customer messaging, you might want to use something like Intercom; for contracts, DocuSign; or, you might just to build your own tool. But often these workflows are highly integrated, so for years our users have been asking us for the tools of their choice to interoperate with Stripe…
> 
> We’re thrilled to launch today Stripe Apps and the Stripe App Marketplace, where you can find or build best-of-breed tools that work naturally with Stripe.

There are the missing pieces!

![](https://i0.wp.com/stratechery.com/wp-content/uploads/2022/05/thinplatforms-4.png?resize=1024%2C566&ssl=1)![](https://i0.wp.com/stratechery.com/wp-content/uploads/2022/05/thinplatforms-4.png?resize=1024%2C566&ssl=1)

“Working naturally with Stripe” doesn’t simply mean access to Stripe’s APIs; it means fitting in to the Stripe dashboard — Stripe is even including pre-made UI components so that 3rd-party apps look like they were designed by the fintech company:

![](https://i0.wp.com/stratechery.com/wp-content/uploads/2022/05/thinplatforms-1.png?resize=1024%2C577&ssl=1)![](https://i0.wp.com/stratechery.com/wp-content/uploads/2022/05/thinplatforms-1.png?resize=1024%2C577&ssl=1)

This is another thin platform: developers don’t have access to the core financial data of a company, nor does IT want them to; instead the opportunity is to sit on top of an abstraction layer that covers all of a company’s money-moving pieces, and to fit in as best as you can.

On one hand, of course I am covering the Build and Stripe Sessions keynotes together because both happened the same week; at the same time, it was a fortuitous coincidence, because Stripe’s announcement brings important context to Microsoft’s approach. After all, I used the magic word “monopoly”; the truth, though, is that not only was an operating system monopoly inevitable, it also made perfect sense from a user perspective that important functionality — like browsing — became integrated with the core OS.

Collison made the case as to why similar considerations should be front-and-center for thin platforms — there are things “you should want running like clockwork.” Microsoft would make a similar argument about Teams and its incorporation of things like file storage and communications, and, I would argue, Teams’ success in the market relative to Slack is evidence that the argument is a compelling one to customers. That Microsoft has so often seemed like the only enterprise company actually building for an enterprise’s ends, instead of solipsistically obsessing over being best-of-breed for one specific means, seems worth celebrating and emulating, not condemning and complaining.

At the same time, it is also worth mourning the slow eclipse of the thick client model. Yes, things like malware were a pain and a drain on productivity, and the SaaS model has led to a plethora of new products that are accessible to companies without needing an IT department, but the big downside of the thick model in terms of what could go wrong and the necessity of IT created the conditions for massive upside, in this case the opportunity to make new apps — and by extension, new companies — without needing any permission, “connectors” or pre-made UI components. Alas, the tech industry is past [the end of the beginning](https://stratechery.com/2020/the-end-of-the-beginning/); welcome to middle age, where the only thickness is your waistline.

### *Related*

1. Apple argues, not without merit, that this is for security reasons; critics argue, [with considerable](https://infrequently.org/2021/04/progress-delayed/) | [merit](https://httptoolkit.tech/blog/safari-is-killing-the-web/), that this restricts innovation on iOS and meaningful competition with the App Store.
2. Absent virtualization, although that wasn’t really feasible on user-level PCs at the time Windows was establishing its dominance
3. This [interview with Tony Fadell](https://stratechery.com/2022/an-interview-with-father-of-the-ipod-tony-fadell/) includes an excellent discussion on this point in the context of Intel, which applies just as much to Microsoft.
4. With, I am ashamed to admit, probably the worst drawing in the history of Stratechery; as I recall I was late to a Chinese New Years’ Eve dinner!