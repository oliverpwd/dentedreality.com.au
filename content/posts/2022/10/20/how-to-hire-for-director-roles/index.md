---
title: How to Hire for Director+ Roles?
date: '2022-10-20T09:59:43-06:00'
format: link
service: instapaper
tags:
- read
external_url: https://stassajin.medium.com/how-to-hire-for-director-roles-bb0690f49a51
---

[How to Hire for Director+ Roles?](https://stassajin.medium.com/how-to-hire-for-director-roles-bb0690f49a51)  



Hiring folks in leadership roles is very challenging. One difficulty is that almost every candidate who gets to that level is generally good at communication, charismatic in their demeanor, and well trained to say the right things to get the job. Nonetheless, there is a huge difference between how people interview and how they deliver once they get hired. In my interactions with folks in Director+ roles, I generally find a very strong dichotomy, with a few individuals being superstars and a large majority having some level of non-pathological narcissism, where they got to a leadership position primarily because they knew how to play the game of visibility. Given all this, how do you break the level of information asymmetry in interviews and hire exceptional leaders for technical roles?

# Do they have an understanding of the P&L?

A good Director+ is able to look at a profit and loss statement and translate that into a technical direction. For example, a Head of Data could look at a financial statement and immediately ask questions:

* It looks like our cost of acquisition is high. Who is leading that work? What optimization has been done to make that more efficient? Nobody? I would like to assign a data scientist who specializes in optimization to work on it.
* It looks like our infrastructure costs are growing at a higher rate than revenue. What are the drivers of that cost? Who is responsible for infra? Nobody? I would like to personally lead a Cloud FinOps initiative.
* It looks like our runway is unhealthy. Is it time to make tough decisions?
* It looks like our business is growing, but operations work is not scaling. Who is responsible for automating that?

If you give a candidate a situational interview where you go over a simplified P&L and they are not able to ask questions and tie that to technical solutions, it should tell you two things:

1. They will have a hard time thinking of initiatives in terms of revenue, cost, and profitability drivers, so they’ll have challenges communicating with business partners. Instead, they might still be stuck thinking in terms of project-based work or lofty initiatives of unknown value to the business (e.g., “becoming self-serve” or “becoming AI leader in the industry”)

2. That they don’t have experience “being in the room.” In almost all companies there is a room where line-by-line item discussions around the P&L are being addressed. Almost everyone part of the M-team is in that room. Someone high up in Data is in that room together with a bunch of analysts. If your candidate has no P&L experience, they were likely not in that room.

# Backchannels

I first read about backchannels from Ben Horowitz’ book [The Hard Thing About Hard Things](https://www.amazon.com/Hard-Thing-About-Things-Building/dp/0062273205) and I saw them used to alleviate information asymmetry. I know that backchannels might be perceived as [unethical](https://emilytriplettlentz.medium.com/why-i-dont-provide-backchannel-references-3d26e82db307), and I think there are good reasons why they should not be done for non-critical roles. Nonetheless, I think you owe it to your team to protect them from a bad hire. For example, I once found through the grapevine that one of my previous bosses was actually let go from his previous job due to performance reasons. Suddenly a lot of things clicked: the absenteeism, the lack of care, the lack of vision, the empty promises. In the back of my mind, I found it very unfair that 150+ people at the company had to suffer because of a bad hiring mistake that could’ve been avoided if someone did a proper background check. This is why for very senior leadership roles I’m supportive of backchannels.

# The “lunch test”

My initial exposure to interviewing Director+ roles was when my previous company tried to hire a Head of Research. I was a junior data scientist and the technical interview was done together with someone who had a mid-level role in the Design team. Literally within one minute of our introductions, the Director candidate tried to commandeer the interview and acted with the attitude of “I can’t believe I’m interviewed by a bunch of interns.” During the round table, everyone except us had a polite and professional interaction. This was not an exception and about 10 out of ~35 director+ candidates I had the chance to interview behaved this way.

I call this the “lunch test” because it echoes back to the idea of taking a prospect to lunch and seeing how they behave toward folks who are in a position of less privilege or power. The reason why this test is helpful is that it can flag candidates that don’t approach leadership from a position of a servant leader. If your hiring team is all made up of senior folks, you’re not likely to get this signal. I generally find this test to have a higher fidelity when it is administered in technical interviews and not in values or culture-based interviews where the candidate is primed to give the right answer.

![]()

[Differences between traditional and servant leadership.](https://learnercenteredleadership.org/2021/06/06/everybody-has-the-potential-to-be-a-servant-leader/)

# Have a process

I once had an interesting interview experience. A data engineer and I were preparing to interview a potential Chief Data Officer. Our questions centered only around very broad topics: “What do you think are the main components of a data platform? What’s the purpose of a data warehouse? How do you evaluate an ML model developed by your team? How do you resolve technical disagreements?” Each question had follow-ups, but we expected any candidate to nail this interview.

The data engineer and I were waiting outside for the previous interview to end. When the door opened, we heard a lot of laughter and joking around the topic of sports between the CFO and the candidate. I already knew that something was wrong because 30 minutes is absolutely not sufficient to evaluate a candidate and it sounded like the CFO wasn’t in control of the interview. Nonetheless, we entered, and we started with introductions.

> **Data Engineer**: Hi, my name is Z. I worked here for Y years and I do ABC.
> 
> **Me**: Hi, my name is X. I worked here for Y years and I’m responsible for ABC. It would be nice if you can give us a 1 minute introduction after which we will lead with about 20 minutes of questions from us, leaving you with 5–10 minutes to ask questions.
> 
> **Candidate:** Sure, my name is T and I’m very happy to be here.
> 
> **Data Engineer:** Great, T. Our first question is, what do you think are some of the main components of a Data Platform?
> 
> **Candidate**: Before we go on…I just have one question?
> 
> **Data Engineer:** … Yes, sure.
> 
> **Candidate:** Ok, do you know what the Dunbar number is?

My colleague froze from confusion. At this point, I knew where things were heading, and the sleight of hand the candidate was playing. I knew I had a Jimmy McGill on my hands, who was trying to redirect the discussion.

![]()

[Jimmy McGill (aka Saul Goodman) the famous lawyer from Better Call Saul](https://www.wsj.com/articles/better-call-saul-refined-television-11659720932)

I quickly jumped in.

> **Me:** I know what the number is, but I don’t see the connection with the question my colleague asked. Given that we only have 20 minutes, could we discuss the Dunbar number at the end?

For the rest of the interview, the candidate completely failed. He didn’t know what a data warehouse is and never used one, it’s been a while since he used machine learning so he was not familiar with metrics, and he didn’t know what is a data platform. Basically, the interview was a disaster, and it took us less than five minutes to realize that we were dealing with a charlatan with a possibly questionable background. This candidate listed that they were Search and Recommendation Lead at Amazon at their first job out of undergraduate, followed by more than half a decade of creating startups that got acquired for which I could not find evidence that they existed. To top it off, the candidate was expecting cash compensation of close to $1 million at a startup with ~150 people.

During the round table, everyone had generally glowing reviews. CEO, CFO, Head of Risk, etc. The data engineer and I were the only strong dissenters and went point by point over the reasons why we think this person should not be hired. Luckily our voices were listened to.

What went wrong? The answer is that the hiring process was not followed consistently or even enforced. Folks went into interviews free-styling and followed a very loose structure. I know this because questions from interview to interview would differ and because scorecards were very sparse in details around what was asked and what the candidate answered. To have a process means to:

1. Understand what skills/areas need to be assessed. What you are looking for?
2. Design the funnel. How many interviews? What their length should be? Who should be present?
3. What questions should be asked? What is the rubric for each question? What are the potential good answers we expect for each question?
4. How much time should be given for deliberation? How quick should be the turnaround?
5. What are our compensation limits and when and why are we willing to make exceptions?
6. Enforce the process and remove people from the interview loop if they freestyle or fail to calibrate.

Without a process, you are only subjecting yourself to biases, such as hiring candidates based on charisma instead of experience and their execution ability. These will be folks that will be very nice people, very hard to fire, and wholly incompetent at their job.

# Company Size and Non-Tech Companies

If you hire people from larger non-tech companies for your startup, expect some cultural differences in how they may approach problem-solving. My impression from interviewing candidates from large companies is that their work is more reactive. These folks have 200+ direct and indirect reports. People come to them with problems and opportunities, and they basically just give their opinion or approval. The size of the org does not give them the freedom and the flexibility to engage and probe deeply into things. They might not be able to connect the dots, review products, or even use their own products. Note that this is a generalization and I have met many exceptions. I once interacted with a CFO of a 5000+ company who was very enjoyable to talk to and they went out of their way to understand the technical details behind some ML work the team was doing.

If you’re hiring from a non-tech company, be mindful that they might come from a culture where Engineering is treated as a subservient organization. [The Unicorn Project](https://www.amazon.com/Unicorn-Project-Developers-Disruption-Thriving-ebook/dp/B07QT9QR41) book does a good job of portraying these types of organizations. I recommend adding things in the interview loop that deal with prioritization and something that tests that the candidate is able and willing to push back. For example, I once met a candidate who said that “my team will burn the midnight candle to get things done” as an appropriate answer to a prioritization question.

# Job Hopping

Every Director+ candidate is ambitious and wants to make a mark. At my previous startup, we had 10+ Directors come and go. The average tenure was probably one year while for the rest of the employees it was about two years. Each Director+ wanted to make an impact and most of them did not spend time acquiring the right context. In the majority of cases, folks that failed to acquire the right context ended up failing and had no choice but to leave their job due to their spectacular lack of success. They came, they made a big splash, and then left the organization to drown in the aftereffects of their incompetence.

I like [Will’s idea](https://lethain.com/things-learned-hiring-data-science-leader/) of asking what a candidate plans to do in the first 90-days since it can reveal if their nature is to jump into things before reflecting. I would personally want to get to the bottom of why candidates leave before their two-year mark through backchannels and/or by asking the candidate directly.

# Fast career tracks

For candidates that have fast career tracks, where they have three promotions in four years, I generally see these two buckets:

* They are amazing superstars and you need to do everything to get them on board.
* They worked at a fast-growing company, but unfortunately, that tailwind growth generally led to title inflation. They lack both depth and breadth of experience to be effective in difficult situations.

During the recent IPO boom, many were able to jump on a rocketship which means that four years out of an undergrad, folks could be in very senior roles. Fast career progression by itself is not a bad thing, but it doesn’t give you enough signal to understand that the candidate can be effective when things get tough, when headcount is sparse, when business is stagnating, when money is not flush, when internal employees are unhappy, and when culture is broken. Many folks that benefited from that growth did not benefit from the lessons learned from a struggling company. If you suspect you deal with an inexperienced person, try to go one level lower in your evaluation and ask them things you might ask a manager or senior manager.

* Give me an example of when you negotiated a vendor contract.
* Give me an example of when you had to manage upwards.
* How do you perform 1:1 at your current company?
* How do you perform quarterly planning at your current company? What could be done better?
* Give me an example of when you had to handle a difficult employee and what did you do? Please don’t disclose identifying information.

# Hiring Views

Lastly, most people think that Director+ should be responsible for vision, roadmap, or any of the other non-personnel activities that unlock business value to the company. Personally, the most effective Directors+ I’ve seen were the ones who knew how to build great teams and let those teams handle the roadmap, execution, and vision. In most cases what they had to do is set good metrics, reward people fairly and timely, and sponsor projects/teams that would unlock large benefits. This is why the interview should get a signal on the candidates’ views on hiring, promotion, evaluation, and how they set metrics.

# Conclusion

A bad Director+ hire can very well make the difference between success and failure in an organization. I fully echo Jim Collins’ book [Good to Great](http://Good%20to%20Great), that the most important thing for successfully executing is to have the right people on the bus, the wrong people off the bus, and the right people in the right seats.