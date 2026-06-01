---
title: Things I Learned the Hard Way
date: '2023-11-10T12:50:08-07:00'
format: link
service: instapaper
tags:
- read
external_url: https://speakerdeck.com/bcantrill/things-i-learned-the-hard-way
---

[Things I Learned the Hard Way](https://speakerdeck.com/bcantrill/things-i-learned-the-hard-way)  



1. Things I Learned the  
   Hard Way  
   Bryan Cantrill  
   Oxide Computer Company
   
   [View Slide](https://files.speakerdeck.com/presentations/f7736dc4a6e9421ea6c477671cc7aece/slide_0.jpg)
2. OXIDE  
   The imperative to learn  
   • The thrill of being a software engineer is that we are always learning  
   • Learning is clearest with respect to our craft: learning new languages,  
   new technologies – or new aspects of developing or deploying them  
   • Learning extends beyond craft: software creation sits at the conﬂuence  
   of the technical and the creative, at once solitary and collaborative  
   • The way we organize is not formulaic; we are always learning new ways  
   of organizing ourselves and working with one another
   
   [View Slide](https://files.speakerdeck.com/presentations/f7736dc4a6e9421ea6c477671cc7aece/slide_1.jpg)
3. OXIDE  
   How we learn  
   • Even though it can feel diﬃcult at the time, learning is actually easiest  
   when it’s highly structured – as in one’s formal education  
   • But a formal education often suﬀers from being impractical – and much  
   of the learning of an engineer will in fact happen on the job  
   • Learning on the job will come from peers, from the organization, etc.  
   • In this regard, it is an organization eﬀectively teaching what it knows –  
   and it’s the easy way to learn
   
   [View Slide](https://files.speakerdeck.com/presentations/f7736dc4a6e9421ea6c477671cc7aece/slide_2.jpg)
4. OXIDE  
   Things I learned the easy way  
   • Coming up in OS kernel development at Sun Microsystems in the late  
   1990s and early 2000s, I learned a bunch of stuﬀ the easy way:  
   ○ The craft of C – and the importance of enforced standards  
   ○ Source code control (and the bringover/modify/merge model)  
   ○ Rigorous, ﬁrst principles thinking – and the need to explain that  
   thinking in the code itself (“Big Theory Statements”)  
   ○ The primacy of postmortem debugging
   
   [View Slide](https://files.speakerdeck.com/presentations/f7736dc4a6e9421ea6c477671cc7aece/slide_3.jpg)
5. OXIDE  
   The hard way  
   • But some wisdom comes from a gorier place: from doing it wrong  
   • This is where an organization itself is often learning – and the imperative  
   of the organization is not merely to teach but to learn  
   • This is the hard way – and I have learned a lot the hard way!  
   • Perhaps unsurprisingly: the human side of engineering has proven to  
   have the hardest lessons
   
   [View Slide](https://files.speakerdeck.com/presentations/f7736dc4a6e9421ea6c477671cc7aece/slide_4.jpg)
6. OXIDE  
   The hard way: The primacy of testing  
   • An operating system can be hard to test – and despite rigorous thinking,  
   the diﬃculty of testing often prevents any unit testing whatsoever  
   • In some early projects in my career we were far too late to develop a  
   comprehensive test suite – and even then we made the mistake of  
   eﬀectively outsourcing the development of tests  
   • The test suite became essential for us, but many tests needed to be  
   rewritten (and some remain brittle to this day!)  
   • Think about testing early and write your own tests
   
   [View Slide](https://files.speakerdeck.com/presentations/f7736dc4a6e9421ea6c477671cc7aece/slide_5.jpg)
7. OXIDE  
   The hard way: Invest in tooling  
   • Tools are the things we build that we don’t ship – but that very much  
   aﬀect the artifact that we develop  
   • It can be tempting to either shy away from developing tooling entirely or  
   (in larger organizations) to dedicate an entire organization to it  
   • In my experience, tooling should be built by those using it  
   • This is especially true for tools that improve the artifact by improving  
   understanding: the best time to develop a debugger is when debugging!
   
   [View Slide](https://files.speakerdeck.com/presentations/f7736dc4a6e9421ea6c477671cc7aece/slide_6.jpg)
8. OXIDE  
   The hard way: Debug by asking questions  
   • We (unfortunately) do not really teach debugging methodology: more or  
   less everyone learns debugging by doing it (often poorly)  
   • It is tempting to believe that we engage in a kind of scientiﬁc method  
   when we debug – but this is (in my experience) a myth  
   • Instead of forming hypotheses, focus instead on informed questions:  
   what do you want to ask of the system?  
   • Summon creativity (and tooling!) to answer the questions – and then use  
   the answers to questions to inform tighter questions
   
   [View Slide](https://files.speakerdeck.com/presentations/f7736dc4a6e9421ea6c477671cc7aece/slide_7.jpg)
9. OXIDE  
   The hard way: Understanding odd behavior  
   • Computers are – at root – deterministic; software systems aren’t magic!  
   • When something odd happens, it can be tempting to ignore it –  
   especially true when it feels somewhat ancillary!  
   • But odd behavior is worth understanding: at worst, it enhances our  
   own understanding (that is, that the behavior is in fact expected)…  
   • …but odd behavior can be an indicator of something much more deeply  
   amiss – and in fact has represents an otherwise innocuous presentation  
   of an important defect!
   
   [View Slide](https://files.speakerdeck.com/presentations/f7736dc4a6e9421ea6c477671cc7aece/slide_8.jpg)
10. OXIDE  
    The hard way: Half-measures on vexing problems  
    • If a problem is reproducible, it can be debugged – however psychotic!  
    • If a problem is not reproducible, it can also be debugged by asking  
    questions of the state it left behind (core dumps, log ﬁles, etc.)  
    • But what if a problem is both psychotic and non-reproducible?  
    • On these (blessedly rare!) problems, take half-measures: change the  
    system to leave more state behind, such that an additional occurrence  
    of the problem will help bifurcate the search space for the root cause
    
    [View Slide](https://files.speakerdeck.com/presentations/f7736dc4a6e9421ea6c477671cc7aece/slide_9.jpg)
11. OXIDE  
    The hard way: Making technology choices  
    • I have gotten in the most trouble when I am not deliberate about  
    technology decisions – and choose something because it feels like a  
    “safe” choice (“everyone uses it”) or because it wasn’t a choice at all  
    • However, it can also be easy to overly deliberate on technology choices!  
    • Technologies (and the decisions that they embody) reﬂect the values of  
    their inventors, developers, users and proponents  
    • When choosing technologies, weigh values heavily!
    
    [View Slide](https://files.speakerdeck.com/presentations/f7736dc4a6e9421ea6c477671cc7aece/slide_10.jpg)
12. OXIDE  
    The hard way: Predictions reﬂect the present  
    • Many who make predictions – or are paid to make them! – do not revisit  
    their past predictions; they are conﬁdently wrong  
    • The future is simply too dynamic to predict with repeatable accuracy  
    • Many years of making, recording and revisiting predictions taught me  
    that predictions tell you more about the present than the future  
    • Be very careful about giving someone else’s predictions too much  
    weight – especially if/when they feel wrong!
    
    [View Slide](https://files.speakerdeck.com/presentations/f7736dc4a6e9421ea6c477671cc7aece/slide_11.jpg)
13. OXIDE  
    The hard way: Bind a team with mutual trust  
    That fall West had put a new term in his vocabulary. It was  
    trust. “Trust is risk, and risk avoidance is the name of the  
    game in business,” West said once, in praise of trust. He  
    would bind his team with mutual trust, he had decided.  
    When a person signed up to do a job for him, he would in  
    turn trust that person to accomplish it; he wouldn’t break it  
    down into little pieces and make the task small, easy and  
    dull.  
    – Soul of New Machine by Tracy Kidder (1981)
    
    [View Slide](https://files.speakerdeck.com/presentations/f7736dc4a6e9421ea6c477671cc7aece/slide_12.jpg)
14. OXIDE  
    The hard way: Fear causes introspection gaps  
    • Fear is a base human emotion – and it causes us to take our most  
    disruptive, most rash actions (ﬁght-or-ﬂight!)  
    • Much conﬂict has fear at its root; when conﬂict erupts, it can be helpful  
    to elucidate those fears  
    • Must watch: Rachel Stephens’s excellent Monktoberfest 2022 talk!
    
    [View Slide](https://files.speakerdeck.com/presentations/f7736dc4a6e9421ea6c477671cc7aece/slide_13.jpg)
15. OXIDE  
    The hard way: Use values as a lens for hiring  
    • It is essential for an organization to articulate its shared values  
    • The most grievous mistakes I have made in my career are mishires  
    • Interviews are deeply ﬂawed as the sole mechanism for evaluating hires!  
    • I have found that it is important that new hires help to reinforce and  
    amplify shared values – and for that, values must be a lens in hiring  
    • This is not easy! We have found a written process to be very helpful in  
    this regard, and has helped inform our conversations
    
    [View Slide](https://files.speakerdeck.com/presentations/f7736dc4a6e9421ea6c477671cc7aece/slide_14.jpg)
16. OXIDE  
    Make the hard way the easy way?  
    • We can make the hard way the easy way by articulating our experience  
    • I have done this through talks over the years, but I have found that to be  
    insuﬃciently dynamic…  
    • We have found social audio (e.g., Discord) to be a great way to allow  
    technologists to discuss their experiences – and convey their wisdom!  
    • Check out the back catalog of our Oxide and Friends podcast…  
    • …and if you start your own, let me know so I can like-and-subscribe!
    
    [View Slide](https://files.speakerdeck.com/presentations/f7736dc4a6e9421ea6c477671cc7aece/slide_15.jpg)