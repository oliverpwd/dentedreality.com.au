---
title: Progressing from tech to leadership
date: '2018-02-10T13:04:09+00:00'
format: link
service: instapaper
tags:
- read
external_url: http://lcamtuf.blogspot.com/2018/02/on-leadership.html
---

[Progressing from tech to leadership](http://lcamtuf.blogspot.com/2018/02/on-leadership.html)  



I’ve been a technical person all my life. I started doing vulnerability research in the late 1990s – and even today, when I’m not [fiddling with CNC-machined robots](http://lcamtuf.coredump.cx/rstory/) or [making furniture](http://lcamtuf.coredump.cx/woodworking/), I’m probably [clobbering together a fuzzer](http://lcamtuf.coredump.cx/afl/) or writing a [book about browser protocols and APIs](http://lcamtuf.coredump.cx/tangled/). In other words, I’m a geek at heart.

My career is a different story. Over the past two decades and a change, I went from writing CGI scripts and setting up WAN routers for a chain of shopping malls, to doing pentests for institutional customers, to designing a series of network monitoring platforms and handling incident response for a big telco, to building and running the product security org for one of the largest companies in the world. It’s been an interesting ride – and now that I’m on the hook for the well-being of about 100 folks across more than a dozen subteams around the world, I’ve been thinking a bit about the lessons learned along the way.

Of course, I’m a bit hesitant to write such a post: sometimes, your efforts pan out not because of your approach, but despite it – and it’s possible to draw precisely the wrong conclusions from such anecdotes. Still, I’m very proud of the culture we’ve created and the caliber of folks working on our team. It happened through the work of quite a few talented tech leads and managers even before my time, but it did not happen by accident – so I figured that my observations may be useful for some, as long as they are taken with a grain of salt.

But first, let me start on a somewhat somber note: what nobody tells you is that one’s level on the leadership ladder tends to be inversely correlated with several measures of happiness. The reason is fairly simple: as you get more senior, a growing number of people will come to you expecting you to solve increasingly fuzzy and challenging problems – and you will no longer be patted on the back for doing so. This should not scare you away from such opportunities, but it definitely calls for a particular mindset: your motivation must come from within. Look beyond the fight-of-the-day; find satisfaction in seeing how far your teams have come over the years.

With that out of the way, here’s a collection of notes, loosely organized into three major themes.

#### The curse of a techie leader

Perhaps the most interesting observation I have is that for a person coming from a technical background, building a healthy team is first and foremost about the subtle art of letting go.

There is a natural urge to stay involved in any project you’ve started or helped improve; after all, it’s your baby: you’re familiar with all the nuts and bolts, and nobody else can do this job as well as you. But as your sphere of influence grows, this becomes a choke point: there are only so many things you could be doing at once. Just as importantly, the project-hoarding behavior robs more junior folks of the ability to take on new responsibilities and bring their own ideas to life. In other words, when done properly, delegation is not just about freeing up your plate; it’s also about empowerment and about signalling trust.

Of course, when you hand your project over to somebody else, the new owner will initially be slower and more clumsy than you; but if you pick the new leads wisely, give them the right tools and the right incentives, and don’t make them deathly afraid of messing up, they will soon excel at their new jobs – and be grateful for the opportunity.

A related affliction of many accomplished techies is the conviction that they know the answers to every question even tangentially related to their domain of expertise; that belief is coupled with a burning desire to have the last word in every debate. When practiced in moderation, this behavior is fine among peers – but for a leader, one of the most important skills to learn is knowing when to keep your mouth shut: people learn a lot better by experimenting and making small mistakes than by being schooled by their boss, and they often try to read into your passing remarks. Don’t run an authoritarian camp focused on total risk aversion or perfectly efficient resource management; just set reasonable boundaries and exit conditions for experiments so that they don’t spiral out of control – and be amazed by the results every now and then.

#### Death by planning

When nothing is on fire, it’s easy to get preoccupied with maintaining the status quo. If your current headcount or budget request lists all the same projects as last year’s, or if you ever find yourself ending an argument by deferring to a policy or a process document, it’s probably a sign that you’re getting complacent. In security, complacency usually ends in tears – and when it doesn’t, it leads to burnout or boredom.

In my experience, your goal should be to develop a cadre of managers or tech leads capable of coming up with clever ideas, prioritizing them among themselves, and seeing them to completion without your day-to-day involvement. In your spare time, make it your mission to challenge them to stay ahead of the curve. Ask your vendor security lead how they’d streamline their work if they had a 40% jump in the number of vendors but no extra headcount; ask your product security folks what’s the second line of defense or containment should your primary defenses fail. Help them get good ideas off the ground; set some mental success and failure criteria to be able to cut your losses if something does not pan out.

Of course, malfunctions happen even in the best-run teams; to spot trouble early on, instead of overzealous project tracking, I found it useful to encourage folks to run a data-driven org. I’d usually ask them to imagine that a brand new VP shows up in our office and, as his first order of business, asks “why do you have so many people here and how do I know they are doing the right things?”. Not everything in security can be quantified, but hard data can validate many of your assumptions – and will alert you to unseen issues early on.

When focusing on data, it’s important not to treat pie charts and spreadsheets as an art unto itself; if you run a security review process for your company, your CSAT scores are going to reach 100% if you just rubberstamp every launch request within ten minutes of receiving it. Make sure you’re asking the right questions; instead of “how satisfied are you with our process”, try “is your product better as a consequence of talking to us?”

Whenever things are not progressing as expected, it is a natural instinct to fall back to micromanagement, but it seldom truly cures the ill. It’s probable that your team disagrees with your vision or its feasibility – and that you’re either not listening to their feedback, or they don’t think you’d care. It’s good to assume that most of your employees are as smart or smarter than you; barking your orders at them more loudly or more frequently does not lead anyplace good. It’s good to listen to them and either present new facts or work with them on a plan you can all get behind.

In some circumstances, all that’s needed is honesty about the business trade-offs, so that your team feels like your “partner in crime”, not a victim of circumstance. For example, we’d tell our folks that by not falling behind on basic, unglamorous work, we earn the trust of our VPs and SVPs – and that this translates into the independence and the resources we need to pursue more ambitious ideas without being told what to do; it’s how we game the system, so to speak. Oh: leading by example is a pretty powerful tool at your disposal, too.

#### The human factor

I’ve come to appreciate that hiring decent folks who can get along with others is far more important than trying to recruit conference-circuit superstars. In fact, hiring superstars is a decidedly hit-and-miss affair: while certainly not a rule, there is a proportion of folks who put the maintenance of their celebrity status ahead of job responsibilities or the well-being of their peers.

For teams, one of the most powerful demotivators is a sense of unfairness and disempowerment. This is where tech-originating leaders can shine, because their teams usually feel that their bosses understand and can evaluate the merits of the work. But it also means you need to be decisive and actually solve problems for them, rather than just letting them vent. You will need to make unpopular decisions every now and then; in such cases, I think it’s important to move quickly, rather than prolonging the uncertainty – but it’s also important to sincerely listen to concerns, explain your reasoning, and be frank about the risks and trade-offs.

Whenever you see a clash of personalities on your team, you probably need to respond swiftly and decisively; being right should not justify being a bully. If you don’t react to repeated scuffles, your best people will probably start looking for other opportunities: it’s draining to put up with constant pie fights, no matter if the pies are thrown straight at you or if you just need to duck one every now and then.

More broadly, personality differences seem to be a much better predictor of conflict than any technical aspects underpinning a debate. As a boss, you need to identify such differences early on and come up with creative solutions. Sometimes, all you need is taking some badly-delivered but valid feedback and having a conversation with the other person, asking some questions that can help them reach the same conclusions without feeling that their worldview is under attack. Other times, the only path forward is making sure that some folks simply don’t run into each for a while.

Finally, dealing with low performers is a notoriously hard but important part of the game. Especially within large companies, there is always the temptation to just let it slide: sideline a struggling person and wait for them to either get over their issues or leave. But this sends an awful message to the rest of the team; for better or worse, fairness is important to most. Simply firing the low performers is seldom the best solution, though; successful recovery cases are what sets great managers apart from the average ones.

Oh, one more thought: people in leadership roles have their allegiance divided between the company and the people who depend on them. The obligation to the company is more formal, but the impact you have on your team is longer-lasting and more intimate. When the obligations to the employer and to your team collide in some way, make sure you can make the right call; it might be one of the the most consequential decisions you’ll ever make.