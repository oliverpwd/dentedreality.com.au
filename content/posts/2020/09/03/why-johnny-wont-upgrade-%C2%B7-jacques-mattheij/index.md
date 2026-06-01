---
title: Why Johnny Won’t Upgrade · Jacques Mattheij
date: '2020-09-03T18:20:36-06:00'
format: link
service: instapaper
tags:
- read
external_url: http://jacquesmattheij.com/why-johnny-wont-upgrade/
---

[Why Johnny Won’t Upgrade · Jacques Mattheij](http://jacquesmattheij.com/why-johnny-wont-upgrade/)  



Software distribution has over the years gone through an enormous revolution in efficiency. Originally, software was developed on things called ‘plug boards’, a matrix of sockets that allowed quick (or so they thought) re-configuration of computing hardware to adapt it to different problems. This was soon followed by papertape, then the punched card deck, a stack of paper cards that contained the program code in a series of holes punched into the paper. Special readers and writers took care of reading, ordering and punching the cards. Woe to you if you dropped a deck of such cards or if your reader jammed or you spilled coffee all over a deck. (From personal experience: if you don’t *immediately* copy such a deck; within 10 minutes or so the cards will swell to the point that the reader will jam, this will not make your boss happy.) That principle plus miniaturization caused a quick succession of hardware based software distribution models culminating in ROM cartriges, a physical device that you buy which contains the program.

Once written a ROM is impossible to rewrite, it literally stands for Read-Only-Memory. So any kind of fix of the software is going to be very expensive and will require a physical device to be distributed to all of the customers for that particular program. This is prohibitively expensive for many applications, so many solutions were developed that made this process more cost effective and quicker. Tapes with software sent to customers followed, quickly superceded by various disks and other magnetic carriers.

Enter the 90’s when the software distribution medium of choice was the 3.5” floppy disk. A typical large software package would require you to sit for an afternoon swapping disks in and out of the drives; to deal with the occasional read error and to curse a lot if you dropped the stack of floppies by accident (hey, but better than those punched cards). For a brief period the CD-ROM reigned supreme, at 600 MB a single CD held as much data and code as 400 floppy disks. Then the internet came along and it all changed, overnight.

I don’t actually remember what the last time was when I bought a shrink wrapped piece of software, it probably was Microsoft Office around 1997. Since then almost all software distribution has gone online. And that’s great right? No more hauling physical media around for bits that you might as well teleport around the world instantaneously.

The benefits are obvious: fast turnaround time between spotting a problem and getting it to the customer, very low cost of distribution and last but definitely not least: automatic updates are now a thing, your software *knows* when it is outdated and will be more than happy to install a new version of itself while you aren’t looking.

And that’s exactly the downside: your software will be more than happy to install a broken, changed, reduced, functionally no longer equivalent, spyware, malware, data loss inducing or outright dangerous piece of software right over the top of the one that you were using happily until today. More often than not automatic updates are not done with the interest of the user in mind. They are abused to the point where many users – me included – would rather forego all updates (let alone automatic ones) simply because we apparently can not trust the party on the other side of this transaction to have our, *the users*, interests at heart.

It isn’t rare at all to be greeted by a piece of software that no longer reads the data that was perfectly legible until yesterday because of an upgrade (I had a CAD system like that). Regressing back to the previous version and you’ll find that it tells you the data is also no longer legible by that version because the newer one has touched it. Restore from backup and get caught in an automatic update war that you can only stop by telling your computer that the automatic update host does not exist any more. It shouldn’t take that level of sophistication to keep a system running reliably, especially not when your livelihood depends on it.

It also – unfortunately – isn’t rare at all to find the user interface of the program that you are familiar with drastically messed up after an automatic upgrade. Familiar menu items may have been moved around, renamed or have been removed entirely. New functionality that you weren’t looking for may have been added, prominently so, taking up valuable screen space. Bundled software may have been installed without your knowledge or consent.

It gets worse. In some cases such automatic updates render your whole system unusable, requiring a re-installation, which – if you are lucky – will get you back to a state that you were already in. During work on a deadline this can cause very serious problems.

Sometimes upgrades will ostensibly be because of security reasons, something that tends to get even reluctant users to agree that this time it probably is worth it. Only to be screwed over by a free malware rider; or some kind of tracking or telemetry installed without your consent or knowledge.

The list of these transgressions is endless, and software vendors the world over still don’t seem to get it. If updating software is so easy, why are users so reluctant to do it?

That’s because all you software vendors collectively royally messed it up. You’ve burned your users trust on so many occasions, not thinking from *their* perspective but from your own almost exclusively leading to people locking down their systems and foregoing critical security updates because they are scared that they will end up with a lot of extra work or a much worse situation if they let you have your way.

So, software vendors, automatic updates:

* should always keep the user centric
* should be incremental and security or bug fixes only
* should *never* update a user interface without allowing the previous one to be used as the default
* should *never* be used to install telemetry or spyware or to re-enable it if it was previously switched off
* should *never* be used to install other software packages without the users explicit consent and knowledge
* should *never* change the format of data already stored on the system
* should *never* cause a system to become unusable or unstable
* *must* allow a revert to the previous situation
* *must* be disablable, in an easy and consistent manner for instance on mobile devices
* should *never* cause the system to become inaccessible or restarted without user consent
* should *always* be signed by the vendor to ensure that the update mechanism does not become a malware vector
* should *never* cause commercial messages or other fluff to be included
* should *never* cause configuration details to be lost
* should *always* be backwards compatible with previous plug-ins or other third party add ons

If we can agree to those terms I’ll be more than happy to update my software, automatic or manual. But until then you’re all on probation, too much misery and lost days on my end on account of these and I highly doubt that I’m alone in that, Johnny agrees.

This is in all our best interest: software updates are a very important mechanism in keeping the internet secure but because vendors routinely botch it users end up using old and insecure software far longer than they should having been bitten by the update bug a couple of times. That’s a very important mechanism squandered for the worst of reasons and if we could just agree on the above basic rules of engagment it would be a tremendous improvement over the current situation. Security and bug fixes are the reason we have automatic updates, not to satisfy the marketing or the design department.