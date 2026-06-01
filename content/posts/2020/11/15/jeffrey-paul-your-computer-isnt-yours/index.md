---
title: 'Jeffrey Paul: Your Computer Isn’t Yours'
date: '2020-11-15T16:17:47-07:00'
format: link
service: instapaper
tags:
- read
external_url: https://sneak.berlin/20201112/your-computer-isnt-yours/
---

[Jeffrey Paul: Your Computer Isn’t Yours](https://sneak.berlin/20201112/your-computer-isnt-yours/)  



It’s here. It happened. Did you notice?

I’m speaking, of course, of [the world that Richard Stallman predicted in 1997](https://www.gnu.org/philosophy/right-to-read.en.html). The one [Cory Doctorow also warned us about](https://craphound.com/pc/download/).

On modern versions of macOS, you simply can’t power on your computer, launch a text editor or eBook reader, and write or read, without a log of your activity being transmitted and stored.

It turns out that in the current version of the macOS, the OS sends to Apple a hash (unique identifier) of each and every program you run, when you run it. Lots of people didn’t realize this, because it’s silent and invisible and it fails instantly and gracefully when you’re offline, but today the [server got really slow](https://news.ycombinator.com/item?id=25074959) and it didn’t hit the fail-fast code path, and everyone’s apps failed to open if they were connected to the internet.

Because it does this using the internet, the server sees your IP, of course, and knows what time the request came in. An IP address allows for coarse, city-level and ISP-level geolocation, and allows for a table that has the following headings:

`Date, Time, Computer, ISP, City, State, Application Hash`

Apple (or anyone else) can, of course, calculate these hashes for common programs: everything in the App Store, the Creative Cloud, Tor Browser, cracking or reverse engineering tools, whatever.

This means that Apple knows when you’re at home. When you’re at work. What apps you open there, and how often. They know when you open Premiere over at a friend’s house on their Wi-Fi, and they know when you open Tor Browser in a hotel on a trip to another city.

“Who cares?” I hear you asking.

Well, it’s not just Apple. This information doesn’t stay with them:

1. These OCSP requests are transmitted *unencrypted*. Everyone who can see the network can see these, including your ISP and [anyone who has tapped their cables](https://en.wikipedia.org/wiki/Room_641A).
2. These requests go to a third-party CDN run by another company, Akamai.
3. Since October of 2012, Apple is a partner in [the US military intelligence community’s PRISM spying program](https://en.wikipedia.org/wiki/PRISM_(surveillance_program)), which grants the US federal police and military unfettered access to this data without a warrant, any time they ask for it. [In the first half of 2019 they did this over 18,000 times, and another 17,500+ times in the second half of 2019.](https://www.apple.com/legal/transparency/)

This data amounts to a tremendous trove of data about your life and habits, and allows someone possessing all of it to identify your movement and activity patterns. For some people, this can even pose a physical danger to them.

Now, it’s been possible up until today to block this sort of stuff on your Mac using a program called [Little Snitch](https://www.obdev.at/products/littlesnitch/index.html) (really, the only thing keeping me using macOS at this point). In the default configuration, it blanket allows all of this computer-to-Apple communication, but you can disable those default rules and go on to approve or deny each of these connections, and your computer will continue to work fine without snitching on you to Apple.

The version of macOS that was released today, 11.0, also known as Big Sur, has new APIs that prevent Little Snitch from working the same way. The new APIs don’t permit Little Snitch to inspect or block any OS level processes. Additionally, the [new rules in macOS 11 even hobble VPNs so that Apple apps will simply bypass them](https://appleterm.com/2020/10/20/macos-big-sur-firewalls-and-vpns/).

[@patrickwardle lets us know](https://twitter.com/patrickwardle/status/1327034191523975168) that `trustd`, the daemon responsible for these requests, is in the new `ContentFilterExclusionList` in macOS 11, which means it can’t be blocked by any user-controlled firewall or VPN. In his screenshot, it also shows that CommCenter (used for making phone calls from your Mac) and Maps will also leak past your firewall/VPN, potentially compromising your voice traffic and future/planned location information.

Those shiny new Apple Silicon macs that Apple just announced, three times faster and 50% more battery life? They won’t run any OS before Big Sur.

These machines are the first general purpose computers ever where you have to make an exclusive choice: you can have a fast and efficient machine, or you can have a private one. (Apple mobile devices have already been this way for several years.) Short of using an external network filtering device like a travel/vpn router that *you* can totally control, there will be no way to boot any OS on the new Apple Silicon macs that *won’t* phone home, and you can’t modify the OS to prevent this (or they won’t boot at all, due to hardware-based cryptographic protections).

Your computer now serves a remote master, who has decided that they are entitled to spy on you. If you’ve [the most efficient high-res laptop in the world](https://www.apple.com/macbook-air/), you *can’t turn this off*.

Let’s not think very much right now about [the additional fact that Apple can, via these online certificate checks, prevent you from launching any app they (or their government) demands be censored](https://lapcatsoftware.com/articles/revocation.html).

# Dear Frog, This Water Is Now Boiling

The day that Stallman and Doctorow have been warning us about has arrived this week. It’s been a slow and gradual process, but we are finally here. You will receive no further alerts.

# See Also

# Probably Unrelated

In other news, Apple has quietly backdoored the end-to-end cryptography of iMessage. Presently, modern iOS will prompt you for your Apple ID during setup, and will automatically enable iCloud and iCloud Backup.

iCloud Backup is not end to end encrypted: it encrypts your device backup to *Apple* keys. Every device with iCloud Backup enabled (it’s on by default) backs up the complete iMessage history to Apple, along with the device’s iMessage secret keys, each night when plugged in. Apple can decrypt and read this information without ever touching the device. Even if *you* have iCloud and/or iCloud Backup disabled: it’s likely that whoever you’re iMessaging with does not, and that your conversation is being uploaded to Apple (and, via PRISM, freely available to the US military intelligence community, FBI, et al—with no warrant or probable cause).

[Use Signal.](https://signal.org/)