---
title: Little’s law – Wikipedia
date: '2022-10-02T21:44:08-06:00'
format: link
service: instapaper
tags:
- read
external_url: https://en.wikipedia.org/wiki/Little%27s_law
---

[Little’s law – Wikipedia](https://en.wikipedia.org/wiki/Little%27s_law)  



In mathematical [queueing theory](https://en.wikipedia.org/wiki/Queueing_theory), **Little’s result**, **theorem**, **lemma**, **law**, or **formula** is a theorem by [John Little](https://en.wikipedia.org/wiki/John_Little_(academic)) which states that the long-term average number *L* of customers in a [stationary](https://en.wikipedia.org/wiki/Stationary_process) system is equal to the long-term average effective arrival rate *λ* multiplied by the average time *W* that a customer spends in the system. Expressed algebraically the law is

L  

=  

λ  

W  

.

{\displaystyle L=\lambda W.}

![](https://wikimedia.org/api/rest_v1/media/math/render/svg/0dad0c564990973535a7f5f5e7507a1dc727f904)![](https://wikimedia.org/api/rest_v1/media/math/render/svg/0dad0c564990973535a7f5f5e7507a1dc727f904)

Although it looks intuitively easy, it is quite a remarkable result, as the relationship is “not influenced by the arrival process distribution, the service distribution, the service order, or practically anything else.”

The result applies to any system, and particularly, it applies to systems within systems. So in a bank, the customer line might be one subsystem, and each of the [tellers](https://en.wikipedia.org/wiki/Bank_teller) another subsystem, and Little’s result could be applied to each one, as well as the whole thing. The only requirements are that the system be stable and [non-preemptive](https://en.wikipedia.org/wiki/Preemption_(computing)); this rules out transition states such as initial startup or shutdown.

In some cases it is possible not only to mathematically relate the *average* number in the system to the *average* wait but even to relate the entire *[probability distribution](https://en.wikipedia.org/wiki/Probability_distribution)* (and moments) of the number in the system to the wait.

## History

In a 1954 paper Little’s law was assumed true and used without proof. The form *L* = *λW* was first published by [Philip M. Morse](https://en.wikipedia.org/wiki/Philip_M._Morse) where he challenged readers to find a situation where the relationship did not hold. Little published in 1961 his proof of the law, showing that no such situation existed. Little’s proof was followed by a simpler version by Jewell and another by Eilon. Shaler Stidham published a different and more intuitive proof in 1972.

## Examples

### Finding response time

Imagine an application that had no easy way to measure [response time](https://en.wikipedia.org/wiki/Response_time_(technology)). If the mean number in the system and the throughput are known, the average response time can be found using Little’s Law:

mean response time = mean number in system / mean throughput


For example: A queue depth meter shows an average of nine jobs waiting to be serviced. Add one for the job being serviced, so there is an average of ten jobs in the system. Another meter shows a mean throughput of 50 per second. The mean response time is calculated as 0.2 seconds = 10 / 50 per second.

### Customers in the store

Imagine a small store with a single counter and an area for browsing, where only one person can be at the counter at a time, and no one leaves without buying something. So the system is roughly:

*entrance → browsing → counter → exit*


If the rate at which people enter the store (called the arrival rate) is the rate at which they exit (called the exit rate), the system is stable. By contrast, an arrival rate exceeding an exit rate would represent an unstable system, where the number of waiting customers in the store would gradually increase towards infinity.

Little’s Law tells us that the average number of customers in the store *L*, is the effective arrival rate *λ*, times the average time that a customer spends in the store *W*, or simply:

L  

=  

λ  

W

{\displaystyle L=\lambda W}

![](https://wikimedia.org/api/rest_v1/media/math/render/svg/c22b7178f025d29c130d89a539e44724438008e5)![](https://wikimedia.org/api/rest_v1/media/math/render/svg/c22b7178f025d29c130d89a539e44724438008e5)

Assume customers arrive at the rate of 10 per hour and stay an average of 0.5 hour. This means we should find the average number of customers in the store at any time to be 5.

L  

=  

10  

×  

0.5  

=  

5

{\displaystyle L=10\times 0.5=5}

![](https://wikimedia.org/api/rest_v1/media/math/render/svg/4950a8ba8fa9c3875479541fe6270b5c52d3a204)![](https://wikimedia.org/api/rest_v1/media/math/render/svg/4950a8ba8fa9c3875479541fe6270b5c52d3a204)

Now suppose the store is considering doing more advertising to raise the arrival rate to 20 per hour. The store must either be prepared to host an average of 10 occupants or must reduce the time each customer spends in the store to 0.25 hour. The store might achieve the latter by ringing up the bill faster or by adding more counters.

We can apply Little’s Law to systems within the store. For example, consider the counter and its queue. Assume we notice that there are on average 2 customers in the queue and at the counter. We know the arrival rate is 10 per hour, so customers must be spending 0.2 hours on average checking out.

W  

=

L  

λ

=

2  

10

=  

0.2

{\displaystyle W={\frac {L}{\lambda }}={\frac {2}{10}}=0.2}

![](https://wikimedia.org/api/rest_v1/media/math/render/svg/89ce5f596a77a3944a0940a55a70deaedf0f6a87)![](https://wikimedia.org/api/rest_v1/media/math/render/svg/89ce5f596a77a3944a0940a55a70deaedf0f6a87)

We can even apply Little’s Law to the counter itself. The average number of people at the counter would be in the range (0, 1) since no more than one person can be at the counter at a time. In that case, the average number of people at the counter is also known as the utilisation of the counter.

However, because a store in reality generally has a limited amount of space, it can eventually become unstable. If the arrival rate is much greater than the exit rate, the store will eventually start to overflow, and thus any new arriving customers will simply be rejected (and forced to go somewhere else or try again later) until there is once again free space available in the store. This is also the difference between the *arrival rate* and the *effective arrival rate*, where the arrival rate roughly corresponds to the rate at which customers arrive at the store, whereas the effective arrival rate corresponds to the rate at which customers *enter* the store. However, in a system with an infinite size and no loss, the two are equal.

## Estimating parameters

To use Little’s law on data, formulas must be used to estimate the parameters, as the result does not necessarily directly apply over finite time intervals, due to problems like how to log customers already present at the start of the logging interval and those who have not yet departed when logging stops.

## Applications

Little’s law is widely used in manufacturing to predict lead time based on the production rate and the amount of work-in-process.

Software-performance testers have used Little’s law to ensure that the observed performance results are not due to bottlenecks imposed by the testing apparatus.

Other applications include staffing emergency departments in hospitals.

## Distributional form

An extension of Little’s law provides a relationship between the steady state distribution of number of customers in the system and time spent in the system under a [first come, first served](https://en.wikipedia.org/wiki/First_come,_first_served) service discipline.

## See also

* [List of eponymous laws](https://en.wikipedia.org/wiki/List_of_eponymous_laws) (laws, adages, and other succinct observations or predictions named after persons)
* [Erlang (unit)](https://en.wikipedia.org/wiki/Erlang_(unit))

## Notes

1. Alberto Leon-Garcia (2008). *Probability, statistics, and random processes for electrical engineering* (3rd ed.). Prentice Hall. [ISBN](https://en.wikipedia.org/wiki/ISBN_(identifier)) [978-0-13-147122-1](https://en.wikipedia.org/wiki/Special:BookSources/978-0-13-147122-1).
2. Allen, Arnold A. (1990). [*Probability, Statistics, and Queueing Theory: With Computer Science Applications*](https://archive.org/details/probabilitystati0000alle/page/259). Gulf Professional Publishing. p. [259](https://archive.org/details/probabilitystati0000alle/page/259). [ISBN](https://en.wikipedia.org/wiki/ISBN_(identifier)) [0120510510](https://en.wikipedia.org/wiki/Special:BookSources/0120510510).
3. Simchi-Levi, D.; [Trick, M. A.](https://en.wikipedia.org/wiki/Michael_Trick) (2013). “Introduction to “Little’s Law as Viewed on Its 50th Anniversary””. *Operations Research*. **59** (3): 535. [doi](https://en.wikipedia.org/wiki/Doi_(identifier)):[10.1287/opre.1110.0941](https://doi.org/10.1287%2Fopre.1110.0941).
4. Serfozo, R. (1999). “Little Laws”. [*Introduction to Stochastic Networks*](https://archive.org/details/introductiontost00serf). pp. [135](https://archive.org/details/introductiontost00serf/page/n146)–154. [doi](https://en.wikipedia.org/wiki/Doi_(identifier)):[10.1007/978-1-4612-1482-3\_5](https://doi.org/10.1007%2F978-1-4612-1482-3_5). [ISBN](https://en.wikipedia.org/wiki/ISBN_(identifier)) [978-1-4612-7160-4](https://en.wikipedia.org/wiki/Special:BookSources/978-1-4612-7160-4).
5. [Keilson, J.](https://en.wikipedia.org/wiki/Julian_Keilson); Servi, L. D. (1988). [“A distributional form of Little’s Law”](https://dspace.mit.edu/bitstream/1721.1/47244/1/distributionalfo00keil.pdf) (PDF). *Operations Research Letters*. **7** (5): 223. [doi](https://en.wikipedia.org/wiki/Doi_(identifier)):[10.1016/0167-6377(88)90035-1](https://doi.org/10.1016%2F0167-6377%2888%2990035-1). [hdl](https://en.wikipedia.org/wiki/Hdl_(identifier)):[1721.1/5305](https://hdl.handle.net/1721.1%2F5305).
6. ^  [Little, J. D. C.](https://en.wikipedia.org/wiki/John_Little_(academic)); Graves, S. C. (2008). [“Little’s Law”](http://web.mit.edu/sgraves/www/papers/Little's%20Law-Published.pdf) (PDF). *Building Intuition*. International Series in Operations Research & Management Science. Vol. 115. p. 81. [doi](https://en.wikipedia.org/wiki/Doi_(identifier)):[10.1007/978-0-387-73699-0\_5](https://doi.org/10.1007%2F978-0-387-73699-0_5). [ISBN](https://en.wikipedia.org/wiki/ISBN_(identifier)) [978-0-387-73698-3](https://en.wikipedia.org/wiki/Special:BookSources/978-0-387-73698-3).
7. Cobham, Alan (1954). “Priority Assignment in Waiting Line Problems”. *Operations Research*. **2** (1): 70–76. [doi](https://en.wikipedia.org/wiki/Doi_(identifier)):[10.1287/opre.2.1.70](https://doi.org/10.1287%2Fopre.2.1.70). [JSTOR](https://en.wikipedia.org/wiki/JSTOR_(identifier)) [166539](https://www.jstor.org/stable/166539).
8. [Morse, Philip M.](https://en.wikipedia.org/wiki/Philip_M._Morse) (1958). *Queues, inventories, and maintenance: the analysis of operational system with variable demand and supply*. Wiley.
9. [Little, J. D. C.](https://en.wikipedia.org/wiki/John_Little_(academic)) (1961). “A Proof for the Queuing Formula: *L* = *λW*“. *[Operations Research](https://en.wikipedia.org/wiki/Operations_Research_(journal))*. **9** (3): 383–387. [doi](https://en.wikipedia.org/wiki/Doi_(identifier)):[10.1287/opre.9.3.383](https://doi.org/10.1287%2Fopre.9.3.383). [JSTOR](https://en.wikipedia.org/wiki/JSTOR_(identifier)) [167570](https://www.jstor.org/stable/167570).
10. Jewell, William S. (1967). “A Simple Proof of: *L* = *λW*“. *Operations Research*. **15** (6): 1109–1116. [doi](https://en.wikipedia.org/wiki/Doi_(identifier)):[10.1287/opre.15.6.1109](https://doi.org/10.1287%2Fopre.15.6.1109). [JSTOR](https://en.wikipedia.org/wiki/JSTOR_(identifier)) [168616](https://www.jstor.org/stable/168616).
11. Eilon, Samuel (1969). [“A Simpler Proof of *L* = *λW*“](https://doi.org/10.1287%2Fopre.17.5.915). *Operations Research*. **17** (5): 915–917. [doi](https://en.wikipedia.org/wiki/Doi_(identifier)):[10.1287/opre.17.5.915](https://doi.org/10.1287%2Fopre.17.5.915). [JSTOR](https://en.wikipedia.org/wiki/JSTOR_(identifier)) [168368](https://www.jstor.org/stable/168368).
12. Stidham Jr., Shaler (1974). [“A Last Word on *L* = *λW*“](https://doi.org/10.1287%2Fopre.22.2.417). *Operations Research*. **22** (2): 417–421. [doi](https://en.wikipedia.org/wiki/Doi_(identifier)):[10.1287/opre.22.2.417](https://doi.org/10.1287%2Fopre.22.2.417). [JSTOR](https://en.wikipedia.org/wiki/JSTOR_(identifier)) [169601](https://www.jstor.org/stable/169601).
13. Stidham Jr., Shaler (1972). “*L* = *λW*: A Discounted Analogue and a New Proof”. *Operations Research*. **20** (6): 1115–1120. [doi](https://en.wikipedia.org/wiki/Doi_(identifier)):[10.1287/opre.20.6.1115](https://doi.org/10.1287%2Fopre.20.6.1115). [JSTOR](https://en.wikipedia.org/wiki/JSTOR_(identifier)) [169301](https://www.jstor.org/stable/169301).
14. Kim, S. H.; [Whitt, W.](https://en.wikipedia.org/wiki/Ward_Whitt) (2013). [“Statistical Analysis with Little’s Law”](http://www.columbia.edu/~ww2040/LL_OR.pdf) (PDF). *Operations Research*. **61** (4): 1030. [doi](https://en.wikipedia.org/wiki/Doi_(identifier)):[10.1287/opre.2013.1193](https://doi.org/10.1287%2Fopre.2013.1193).
15. Correll, Nikolaus (June 13, 2021). [“Manufacturing Lead Time”](https://thesevendeadlywastes.com/lesson/lead-time/). Retrieved June 12, 2021.
16. [Software Infrastructure Bottlenecks in J2EE by Deepak Goel](http://www.onjava.com/pub/a/onjava/2005/01/19/j2ee-bottlenecks.html)
17. [Benchmarking Blunders and Things That Go Bump in the Night by Neil Gunther](https://arxiv.org/abs/cs/0404043)
18. [Little, J. D. C.](https://en.wikipedia.org/wiki/John_Little_(academic)) (2011). [“Little’s Law as Viewed on Its 50th Anniversary”](http://www.informs.org/content/download/255808/2414681/file/little_paper.pdf) (PDF). *Operations Research*. **59** (3): 536–549. [doi](https://en.wikipedia.org/wiki/Doi_(identifier)):[10.1287/opre.1110.0940](https://doi.org/10.1287%2Fopre.1110.0940). [JSTOR](https://en.wikipedia.org/wiki/JSTOR_(identifier)) [23013126](https://www.jstor.org/stable/23013126).
19. Harris, Mark (February 22, 2010). [“Little’s Law: The Science Behind Proper Staffing”](http://www.epmonthly.com/subspecialties/management/littles-law-the-science-behind-proper-staffing/). Emergency Physicians Monthly. Archived from [the original](http://www.epmonthly.com/subspecialties/management/littles-law-the-science-behind-proper-staffing/) on September 5, 2012. Retrieved September 4, 2012.
20. Bertsimas, D.; Nakazato, D. (1995). [“The Distributional Little’s Law and Its Applications”](http://web.mit.edu/dbertsim/www/papers/Queuing%20Theory/The%20distributional%20Little's%20law%20and%20its%20applications.pdf) (PDF). *[Operations Research](https://en.wikipedia.org/wiki/Operations_Research_(journal))*. **43** (2): 298. [doi](https://en.wikipedia.org/wiki/Doi_(identifier)):[10.1287/opre.43.2.298](https://doi.org/10.1287%2Fopre.43.2.298). [JSTOR](https://en.wikipedia.org/wiki/JSTOR_(identifier)) [171838](https://www.jstor.org/stable/171838).
## External links

* *[A Proof of the Queueing Formula L = λ W](http://www.columbia.edu/~ks20/stochastic-I/stochastic-I-LL.pdf)*, Sigman, K., Columbia University