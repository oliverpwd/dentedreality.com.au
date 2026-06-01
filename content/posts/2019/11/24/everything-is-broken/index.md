---
title: Everything is Broken
date: '2019-11-24T10:38:19-07:00'
format: link
service: instapaper
tags:
- read
external_url: https://medium.com/@aallan/everything-is-broken-8627a848dcac
---

[Everything is Broken](https://medium.com/@aallan/everything-is-broken-8627a848dcac)  



Everything is broken, and it’s actually starting to sort of scare me that we’re not willing to acknowledge how bad things have become. It’s starting to scare me that the industry tends to have discussions about morals and ethics in bars, and sometimes in the hallways and dark corners at conferences, rather than in the harsh light of day. It’s really starting to scare me that nobody in the industry reads or understands history any more.

I’m beginning to think that courses in economics should be mandatory for all computer science students. Maybe history as well, real history, not the rote memorisation of lists of people and dates. It might add some sanity to the proceedings.

Because it’s almost back in pre-history now, at least when if you’re on Internet time, all the way back in 1972 in fact, when Alan Kay, one pioneers of the modern Internet, wrote,

![]()



Seventeen years before the invention of the World Wide Web, and thirty five years before the release of the first iPhone, which arguably really did change everything, Kay anticipated the black rectangle of glass and brushed aluminium that lives in all of our pockets today, and the ubiquity of ad blocking software we need to make the web even a little bit useable.

Yet, while Alan Kay’s prediction of the existence of the smartphone was almost prophetic, it was also in a way, naive.

Because Kay lived in a simpler time, without the ubiquitous panopticon of the modern world, and without the security threats ,which arguably shapes the modern Internet, and our view of it. Because the arrival of the web, broke the Internet that sits underneath it.

Because there really is only one business model on the web, and that’s advertising. People have consistently refused to subscribe to services or pay for content. Instead, advertising supports the services that sit underneath almost everything we do on the Web, and behind advertising is the data that makes it possible.

Think about how your day-to-day experience of the Web would be different if Google charged a monthly subscription fee for its search service, or perhaps worse yet, used a micro-payment based approach to charge on a search-by-search basis. It would change how and when you used the web.

A series of almost accidental decisions and circumstances have led to a world where most things on the web appear to be “free”. That doesn’t mean they are free, just that we pay for them in other ways. Our data and our attention are the currency we use to pay Google for our searches, and Facebook for keeping us in touch with our friends.

I used to argue that, one day, the idea that a stranger could make a bell ring in your home, and you would then be socially obligated to talk to them, would seem—when we look back on the twentieth century—laughable.

A retro-rotary phone powered by AIY Projects Voice Kit and a Raspberry Pi. (📹: Alasdair Allan)

Today, nobody I know answers their landline. I don’t even know anyone under the age of 30 that has one. Why bother?

Similarly I’m now beginning to wonder not if the Facebook-style model of social networking will seem similarly laughable in the future, but how long it’s going to be until that happens.

Recently Facebook announced that it would [no longer fact-check political speech](https://www.theguardian.com/technology/2019/oct/04/facebook-exempts-political-ads-ban-making-false-claims), including ads. This announcement has been met with [widespread condemnation](https://www.theguardian.com/technology/2019/oct/28/facebook-employees-strongly-object-to-policy-allowing-false-claims-in-political-ads), and in response a California man named Adriel Hampton [registered as a candidate for state governor](https://www.theguardian.com/technology/2019/oct/29/california-man-adriel-hampton-stands-governor-facebook-rules-lying), with a campaign promise that ever advert from him would be a lie.

In turn Facebook responded by saying that he will [not be allowed](https://www.theguardian.com/technology/2019/oct/30/facebook-to-keep-fact-checking-pac-boss-who-tried-to-skirt-rules) to run ‘false ads’ on their platform, “*…this person has made clear he registered as a candidate to get around our policies, so his content, including ads, will continue to be eligible for third-party fact-checking.*”

Here Facebook is declaring that it won’t decide what’s an outright lie in a political ad, but it will decide who is a legitimate political candidate, which is arguably worse.

While Twitter’s response, to [ban all political advertising](https://www.theguardian.com/technology/2019/oct/30/twitter-ban-political-advertising-us-election) from their platform is, at least on the surface, better. It means that while companies can advertise, political groups trying to stop them from doing harm, can’t.

Ten years ago Mark Zuckerberg [famously stated](https://www.theguardian.com/technology/2010/jan/11/facebook-privacy) that privacy should no longer be considered “*a social norm.*” It became the mantra of the Big Data age, and for the last ten years Silicon Valley has pursed it with vigour.

But the companies that we have entrusted with our data, in exchange for our free services, have not been careful with it. Back in April this year [more than 540 million records](https://slate.com/technology/2019/04/facebook-data-breach-540-million-users-privacy.html) about Facebook users were publicly exposed on Amazon’s cloud computing service by a third party app developer, and then again in September, [another 419 million records](https://www.forbes.com/sites/daveywinder/2019/09/05/facebook-security-snafu-exposes-419-million-user-phone-numbers/#413f3c781ab7) were found on an unsecured server, no password needed. This time the records contained phone numbers linked to Facebook user ids, and some included both the user’s gender and location details.

But it’s not just the social networks. Back in 2017 [the Equifax breach](https://www.theguardian.com/us-news/2017/sep/07/equifax-credit-breach-hack-social-security) exposed the details of 143 million people in the United States, millions of driver’s license numbers, phone numbers, and email addresses. Alongside this were people’s real names, their date of birth, and their US Social Security number.

While last year the Marriott/Starwood breach leaked details [of 500 million people](https://www.theguardian.com/world/2018/nov/30/marriott-hotels-data-of-500m-guests-may-have-been-exposed); name, gender, home address, phone number, email, nationality, passport number, date of birth, along with arrival and departure information. If you’ve ever stayed in Starwood property, like the Sheraton, or the Westin, your details are in this data.

These are not small companies. Neither Equifax or Marriott are startups throwing things on an AWS instance and figuring to fix everything once their Series A comes in and have the money, or the head count, to do it.

But it turns out that unintentional data breaches might be the least of our worries. Data leakage by design is a real problem.

For instance if you share a Dropbox Paper document publicly, any viewer can see the full name and email address of any other Dropbox user who has ever opened that document.

That’s a problem. Because it’s trivial to crawl for Dropbox Paper document public URLs, and harvest all the personal details of the tens, or hundreds, of thousands of people who have opened those documents.

Dropbox views this as a feature, not a bug.

Of course, things get more interesting when it comes to hardware. There was some [great work recently looking at RF leakage](https://www.hackster.io/news/building-an-rf-side-channel-attack-using-machine-learning-6544e691542e) from the Ledger Blue cryptocurrency wallet by carried out by by [Thomas Roth](https://twitter.com/stacksmashing), [Josh Datko](https://twitter.com/cryptotx), and [Dmitry Nedospasov](https://twitter.com/nedos).

![]()


RF at ~169 MHz leaking from the Ledger Blue cryptocurrency wallet. (📹: [leveldown security](https://leveldown.de/))

Now, there isn’t anything new about RF side-channel attacks. Recovering plain text from encrypted communications using leaked emissions from poorly shielded hardware dates all the way back to the Second World War, and the dawn of the information age.

It’s a sufficiently common problem that there are now well established standards for shielding devices to ensure that they don’t leak. However, not everybody pays attention to them.

Here each button press on the wallet creates a significant electro magnetic signal around the 169 MHz spectrum. However the really interesting thing here is that the team behind this attack [used machine learning](https://leveldown.de/blog/tensorflow-sidechannel-analysis/) to recover the PIN from the leaked RF signals. Which, as far as I know, is a first.

But just like software, hardware can leak data intentionally, by design, as well as unintentionally through mechanisms like an RF side channel attack.

For instance if you have an iPhone have you ever thought about how services like AirDrop work? Or how your MacBook sees you are running Safari on your phone, and is able to open the same web page? Or share a WiFi password?

Apple AirDrop mobile phone catcher. (📹: [hexway](https://www.youtube.com/channel/UCAmrk4PPgB-AszEWKZ2seng))

These features work due to something called [Apple Wireless Direct Link](https://stackoverflow.com/questions/19587701/what-is-awdl-apple-wireless-direct-link-and-how-does-it-work) (AWDL), a protocol that can work either via WiFi or BLE to interconnect and allow data transfers between devices. But the protocol is less anonymous than you might think.

But as well as things like phone and Wi-Fi status, [recent work by by security researchers at a company called Hexway](https://hexway.io/blog/apple-bleee/) show that AirDrop sends out a SHA256 hash of your phone number to all devices in range every time you hit “*Share.*” While only the first 3-bytes of the hash are advertised, phone numbers have pretty strict formatting, attackers can use pre-calculated hash tables to recover your actual phone number.

Again, this is a feature, not a bug.

Hardware can also be weaponised. A HID attack is where an attacker takes a programmable embedded development platform and [creates a USB device](https://mg.lol/blog/badusb-cables/) which when plugged into a computer will execute a pre-configured set of keystrokes to drop a malicious payload onto it.

These are now getting [really rather sophisticated](https://github.com/O-MG/DemonSeed), far beyond the classic ‘dropping a USB flash drive in the car park’ scenario. You can now embed this sort of attack hardware into a USB cable, that’s [entirely indistinguishable from the original](https://shop.hak5.org/products/o-mg-cable). Like the Lightning cable you use to charge your phone, or the USB cable you use to charge your laptop.

This is sufficiently easy now that I won’t plug my devices into publicly accessible charging sockets. All those convenient USB sockets on planes, and hotels? I won’t use them, and I wouldn’t recommend anyone else does either.

If you can’t compromise someone’s hardware directly, you can always [steal its identity](https://www.vice.com/en_uk/article/3kx4ej/sim-jacking-mobile-phone-fraud). SIM Jacking is the process where an attacker uses personal information, that they may have found in a separate data leak — like those from Equifax or Marriott that I mentioned earlier — to persuade your cellphone provider to transfer your number to a new SIM card.

Once the swap is complete, messages containing codes for two-factor authentication can be intercepted, and the fraudsters can hijack your email, social media, or even banking accounts. Your life.

SIM Jacking is a growing problem because it differs from other forms of hacking, in that it doesn’t require any technical know-how; all you need is skills of persuasion and a basic grasp of identity-theft.

Although if you do have the right skills, and physical access to hardware, the results can be spectacular. For instance there was [a spate of malware attacks against ATM machines](https://www.vice.com/en_us/article/7x5ddg/malware-that-spits-cash-out-of-atms-has-spread-across-the-world) in Germany back in 2017.

Referred to as ATM jackpotting, the [malware](https://www.cyber.nj.gov/threat-profiles/atm-malware-variants/cutletmaker) tricks the machines into ejecting all of its cash, no card required. Typically installed by opening a panel to reveal a USB port and the just plugging in a flash drive, the attack in Germany affected a machine model that is [still in use](https://www.businesswire.com/news/home/20031117005645/en/Wincor-Nixdorf-Introduces-New-xe-series-ProCash-ATMs) today. Freestanding ATM machines, often found in hotel lobbies and corner stores, are especially vulnerable.

Last year [the Secret Service started warning financial institutions](https://krebsonsecurity.com/2018/01/first-jackpotting-attacks-hit-u-s-atms/) of the first jackpotting attacks in the wild in the United States.

However perhaps the thorniest problems are those caused by a combination of hardware and software. Earlier in the year a man named Masamba Sinclair rented a Ford Expedition from Enterprise Rent-a-Car.

When he rented the car he connected it to his FordPass app. The app allows drivers to use their phones to remotely start and stop the engine, lock and unlock the doors, and continuously track the vehicle’s location.

Despite bringing it to the attention of both Enterprise, and Ford, we [learned last week](https://arstechnica.com/information-technology/2019/10/five-months-after-returning-rental-car-man-still-has-remote-control/) that five months after his returning rental car, and multiple renters later, he still has full remote control of the vehicle.

A couple of times now the CES technology show in Las Vegas has run a scavenger hunt. Based around [Beacon technology](https://makezine.com/2014/01/03/reverse-engineering-the-estimote/) — bluetooth beacons that is — participants needed to hunt for eight scattered around the vast halls, and all three venues, of the CES show in Las Vegas.

Both times they’ve run this hunt I’ve [managed to hack it](https://makezine.com/2014/01/03/hacking-the-ces-scavenger-hunt/), fooling the CES app into thinking I’ve found all the beacons, and won. Except that both times I wasn’t actually attending CES, I wasn’t even in Las Vegas at the time.

By [decompiling the CES app](https://makezine.com/2014/01/03/hacking-the-ces-scavenger-hunt/) you can get the identities, and locations, of the beacons it’s looking for, and then fake them, and fool the app. It’s actually a pretty easy. You can do it with a Raspberry Pi and half a dozen lines of Javascript.

However it turns out that the fact you can win the scavenger hunt from your desk isn’t the most interesting thing I found, at least not [the second time](https://makezine.com/2016/01/07/hacking-ces-scavenger-hunt-second-time/) I hacked the hunt.

![]()


*There are over 1,000 beacons scattered across the three CES venues back in 2016. (*📷: [Alasdair Allan](https://makezine.com/2016/01/07/hacking-ces-scavenger-hunt-second-time/))

Along with the identities of the eight hunt beacons came the latitude and longitude of over 1,000 other beacons scattered over the three CES venues that — so long as you had the app installed — would be picked up by the app on your phone as you made your way around the show.

Possibly intended for indoor navigation, the notifications they generated as you made your way around CES were at times [a bit creepy](https://makezine.com/2016/01/07/hacking-ces-scavenger-hunt-second-time/).

Looking at the decompiled code of the CES app it looked a lot like that, each time your phone saw a beacon, it “*called home*” to report your location. If that’s really the case then a minute-by-minute log of you position at CES could conceivably be saved in the cloud, and your location tracked the whole time you’re there.

Until recently this sort of mass deployment of beacon technology has been rare, and there has been very little debate about the privacy implications underlying it.

Connected devices, the Internet of Things, is a problem. There are so many moving parts, not necessarily physically moving parts, but rather interactions. Every time software talks to hardware, or other software, there is an attack surface.

A recent survey revealed that 1 in 5 security experts working with internet connected things [feared their smart toilet would be hacked](https://www.zdnet.com/article/1-in-5-it-professionals-fear-their-connected-toilets-will-be-hacked/). The only surprising part of that survey was that this many people had smart toilets?

But it’s not just your toilet you should be worrying about.

The status quo is increasingly being threatened by state actors seeking to exploit the vulnerabilities inherent in digitisation. Back in June US Cyber command [launched a retaliatory digital strike against an Iranian group](https://www.washingtonpost.com/national-security/us-military-carried-out-secret-cyber-strike-on-iran-to-prevent-it-from-interfering-with-shipping/2019/08/28/36202a4e-c9db-11e9-a1fe-ca46e8d573c0_story.html) that supported limpet mine attacks against oil tankers in the Straits of Hormuz.

While just last month they [launched a cyber operation against Iran](https://arstechnica.com/information-technology/2019/10/us-claims-cyber-strike-on-iran-after-attack-on-saudi-oil-facility/) in response to the September attacks on Saudi oil facilities. Of course that’s nothing new, the history of the US-Iran cyber-conflict dates all the way back to [the Stuxnet attack](https://en.wikipedia.org/wiki/Stuxnet) against the Iranian nuclear program back in 2010.

The government of the Netherlands [recently released a document](https://blog.lukaszolejnik.com/dutch-application-of-international-rules-to-cyberspace-warfare/) describing their views and position on the application of international law to cyberattacks. Unlike some previous documents I’ve seen it’s really a rather well reasoned. I highly recommend it.

At the start of last month [three US hospitals were forced to temporarily close their doors](https://www.bbc.com/news/technology-49905226) to “*all but the most critical new patients*” following ransomware outbreaks. Separately, seven hospitals in Australia also reported disruptive ransomware infections.

Also last month the city of Johannesburg was [held for ransom](https://www.bankinfosecurity.com/johannesburg-struggles-to-recover-from-ransomware-attack-a-13296). Initially, employees thought they were the victims of a ‘normal’ ransomware attack, like the one that hit the city’s power grid back in July, an attack that left many without electricity for days.

However, it was later discovered that city computers were not encrypted. Instead after providing proof, the attackers asked for 4 bitcoins—that’s roughly US$40,000 at today’s exchange rate—threatening to upload all the city’s stolen city on to the internet.

An interesting change of tactics there.

In an attempt to keep track of these incidents, StateScoop has developed an [interactive map](https://statescoop.com/ransomware-map/) of every known public-sector ransomware attack inside the continental United States going back nearly six years. More than 100 public-sector ransomware attacks have been reported in 2019 so far, compared to 51 reported in 2018. Things appear to be getting worse.

Ransomware attacks can be devastating, especially against utilities, or heavy industry. Where the increasing use of Internet connected machines mean loosing not just data, but capability.

Norsk Hydro ASA is a Norwegian aluminium and renewable energy company. It is one of the largest aluminium companies worldwide. Back in March [it was it was hit with a ransomware attack](https://www.wsj.com/articles/norsk-hydro-hit-by-extensive-cyberattack-11553004589). The entire workforce — 35,000 people — had to resort to pen and paper.

Production lines shaping molten metal were switched to manual, in some cases long-retired workers came back in to help colleagues run things “*the old fashioned way*”. In many cases though, production lines simply had to stop.

Concerned about their reputation damage, litigation. Evidence suggests that many, most even, large [companies or agencies hit by ransomware pay](https://www.zdnet.com/article/georgia-county-pays-a-whopping-400000-to-get-rid-of-a-ransomware-infection/). Norse Hydro didn’t, and in the first three months after the attack that decision cost them somewhere around 60 million US dollars.

What they’ve lost in revenue, they’ve arguably gained in reputation.

Under the weight of malware, botnets, rogue social media, and national paranoia, the global internet is [starting to fragment](https://www.bbc.com/future/article/20190514-the-global-internet-is-disintegrating-what-comes-next). The Great Firewall of China, Russia’s ‘sovereign internet’ law which is basically a parallel domain name system, coupled with deep packet inspection.These are the obvious signs.

But the malaise goes deeper. The global success of the Chinese TikTok app has been hailed as a “[*national security threat*](https://www.nytimes.com/2019/11/01/technology/tiktok-national-security-review.html)” by the United States government. Perhaps because this is the first time cultural creep has gone the other way. The Americans are used to us adopting their culture, not the other way around.

But there is also intriguing ripples, in part due to the fallout from the ongoing Chinese-American trade war that the common shared technological stack, which until recently we all shared, is [starting to split](https://www.hackster.io/news/splitting-the-technology-stack-9e8795186ae0).

One thing that’s driving that divide is magic.

Amongst other things, including inventing the idea of the geostationary satellite, Arthur C. Clarke is famous for saying that “*…any sufficiently advanced technology is indistinguishable from magic.*”

From the outside machine learning, artificial intelligence, looks like magic. But it’s not, it’s computer science, mathematics, statistics, and a dash of domain knowledge.

It’s also controversial, because as you might expect the industry is making the same privacy and security mistakes here as it has done with big data, and the internet of things.

Machine Learning applications driving digital surveillance are ubiquitous in China. In a country where every adult has an ID card with their face on it, and that data is in a government database, facial recognition can be [a powerful technology for surveillance](https://www.nytimes.com/2019/04/14/technology/china-surveillance-artificial-intelligence-racial-profiling.html), and repression.

But they’re still proving controversial here in the west. One recent pilot project in Germany saw [300 volunteers tracked over the course of a year](https://www.politico.eu/article/berlin-big-brother-state-surveillance-facial-recognition-technology/) during their morning commute in Berlin.

According to the German Interior Ministry, the system averaged 80% accuracy, meaning 1 in 5 of the volunteers went unnoticed. The average for false positives were significantly lower, it incorrectly identified 1 in 1,000 as a person of interest. That seems low, but if you think about a larger rollout, with more people, and consider the potentially grave consequences for an innocent person mistakenly identified by such a system. It’s worryingly high.

Especially since deep learning models are [incredibly easy to fool](https://arxiv.org/pdf/1707.08945.pdf). Adding a simple physical perturbation — just four stickers! —to a stop sign, something that could easily be disguised as real graffiti, can fool a model.

![]()


Adding stickers to a stop sign in an adversarial attack. *(*📷: [Eykholt et al., 2018](https://arxiv.org/pdf/1707.08945.pdf))

This is what is called an adversarial attack, and those four stickers makes machine vision network designed to control an autonomous car read that Stop sign — still obviously a stop sign to us humans — as saying the ‘Speed Limit’ is 45 miles an hour. Not only would the car not stop, it might instead speed up.

You can launch similar attacks against face and voice recognition machine learning networks. For instance you can [bypass the ‘liveness detection’](https://findbiometrics.com/biometrics-news-researchers-use-tape-and-glasses-to-spoof-face-id-liveness-detection/) of Apple’s FaceID system, albeit under constrained and limited circumstances, using a pair of glasses with tape over the lens.

More worrying that direct attacks perhaps is bias and ethics in machine learning. There is only really a small group of people making decisions about what data to collect, what algorithms to use, how they should be trained.

Most of us are middle aged white men.

For instance according to [recent research](https://www.washingtonpost.com/health/2019/10/24/racial-bias-medical-algorithm-favors-white-patients-over-sicker-black-patients/), algorithms developed to help decide which patients need of extra medical care are more likely to recommend relatively healthy white patients over sicker black patients.

The algorithm sorts patients according to what they had previously paid in health care fees, meaning those who have traditionally incurred more costs would get preferential treatment. That’s where the bias creeps in. When breaking down health care costs, the researchers found that the health care system is less inclined to give treatment to black patients dealing with similar chronic illnesses compared to white patients.

The press around machine learning, or rather artificial intelligence, paints a picture which is really not in line with our current understanding of how such systems are built today, or even in the foreseeable future.

Machine learning systems are trained to a specific task, we are nowhere near general intelligence, and most researchers would argue that we don’t really understand how to get from here to there.

Privacy, security, morals, and ethics around machine learning—all of this is now being debated, although for the most part it’s being done rather quietly.

So as not to scare the public.

But what scares me the most is that as an industry we’ve proven ourselves perhaps uniquely ill-suited to self-regulate. Ten years of big data has convinced me that the technology industry is arrogant and childish, “*…move fast and break something*” shouldn’t apply to our personal privacy. Or to our civilisation!

It is the arrival of the [GDPR](https://eugdpr.org/) in Europe, and to a lesser extent the [CPPA](https://oag.ca.gov/privacy/ccpa) in California, has changed the conversation. They gave us, as citizens, rights. They gave us, as developers, responsibilities.

The reaction from Silicon Valley was predictable, especially perhaps given the different view on privacy between the United States and Europe, something that is based in part on a good number Europeans having survived under repressive governments in living memory.

To me, and to a lot of developers who will quietly tell you the same—at least in private—the screams of anguish from the Valley show not that the GDPR is a poor law. Instead that it is doing exactly what it should be doing.

Just like [some US-based websites](https://www.engadget.com/2018/08/09/us-news-sites-unavailable-europe-gdpr/) who didn’t want to think about the implications of the GDPR, some ‘smart’ devices stopped providing service when the GDPR came into force.

One of these [was Yeelight](https://twitter.com/internetofshit/status/999619364541394944). You could still turn individual bulbs on or off, one at a time, in their app. But everything else got taken away if you told the app that you refused the accept their new privacy policy. Which makes me wonder what data, about when, and what, bulbs you’re turning on or off is the company behind the app selling on, or using in ways you don’t expect.

To be clear, I’m fairly sure this sort of response isn’t legal under the GDPR. You can’t refuse to provide the service just because the user refuses to let you have their data, unless that data is required to provide the service. I can’t conceive of a case where GDPR infringing data is necessary to turn light bulbs on or off, can you?

![]()


Mark Zuckerberg at Facebook’s F8 conference in 2019. (📷: Facebook)

Earlier this year, Zuckerberg [stood up on stage at Facebook’s F8 conference](https://www.theverge.com/2019/4/30/18524188/facebook-f8-keynote-mark-zuckerberg-privacy-future-2019) and said “…*the future is private.*” Even if you don’t believe him, and lets face it we haven’t been given any reason to, the idea that this man, the man that ten years ago stood up and sold us on the mantra of the big data age, that privacy was no longer a social norm said this, tells us something.

It tells us that that age is over.

I’ll leave you then with one more thought. I no longer believe the industry will solve all these problems. I believe legislation, like the GDPR, is the solution.

As developers we sit in meetings, and if someone asks us to do something that we feel is ethically bad, we should say no. But there is always pressure, pressure knowing that others might say “*…yes!*” That our job is on the line. That our company’s funding is on the line. Our lives, our families, our future.

We need laws that are digital native, laws that tell people that it is okay to say no, we need to know that you have our backs.

Don’t pass laws in anger, or god forbid [ignorance](https://www.wired.co.uk/article/what-is-article-13-article-11-european-directive-on-copyright-explained-meme-ban), do not be tempted yourself down the dark paths, the easy wins that technology offers. But I’m pleading with you, go back to your constituents, your agencies, and govern. It is past time, more than past time, for you to do so.

Ten years of big data, ten years of attempted technological fixes, rather than cultural ones, has proved that the industry cannot.

Please, help us. You’re our only hope.