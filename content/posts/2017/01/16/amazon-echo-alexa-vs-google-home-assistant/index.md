---
title: Amazon Echo (Alexa) vs Google Home (Assistant)
date: '2017-01-16T13:42:05+00:00'
format: link
service: jetpack
tags:
- Alexa
- amazon
- amazon echo
- automation
- voice
categories:
- personal
- posts
external_url: https://beau.blog/2017/01/amazon-echo-alexa-vs-google-home-assistant/
---

I have both of these devices at home, and have had them each for a few months (at least now). I got the Amazon Echo first, so have had it for a lot longer. I grabbed a Google Home because they were on sale and I wanted to compare the 2 systems. Here’s an outline of my experience thus far.

## Amazon Echo/Alexa

* Far superior audio quality. The speaker blows the Google Home away.
* Microphones/initial detection seem to be better, so you can yell from another room, from around a corner, etc, and Alexa will respond.
* Earlier to the game with a [developer program](https://developer.amazon.com/alexa-skills-kit), so there are [a lot of “skills” available](https://www.amazon.com/b?ie=UTF8&node=13727921011), although a lot (most?) of them are pretty useless trivia type games.
* Smart Home integration is much better so far. Includes an “internal” concept of devices, so you can create groups of devices natively within the Alexa app, and use them in commands, even if they’re different device types. For example I can group a [LIFX](http://www.lifx.com/) light bulb, and a light that’s controlled through [Wink](http://www.wink.com/), and have it all controlled as a single group via Alexa.
* Wink hub integration is nice, and I centralize as much as possible through there.
* Developing for Alexa is kind of cool. I built a few test skills using [Lambda](https://aws.amazon.com/lambda/) hosting, and was able to interact with [Car2Go](http://car2go.com/) and [WordPress.com](https://wordpress.com) pretty easily.
* Radio integration (via [TuneIn](https://beta.tunein.com/)) is pretty nice, and being able to just “play triple j radio” ([Australian station](http://www.abc.net.au/triplej/)) is awesome.
* I use [Spotify](https://www.spotify.com/us/) for all my music, and it gets a little tedious having to say “on Spotify” for everything (because Alexa will default to Amazon Prime music otherwise).
* It feels like total magic to walk into my house with music streaming from Spotify to [headphones](https://www.bragi.com/thedash/) (via my phone), and then say “Alexa, play from Spotify” and it’ll just take over mid-track and keep playing.

## Google Home/Assistant

* Linking it up with a [Chromecast](https://www.google.com/intl/en_us/chromecast/?utm_source=chromecast.com) allows for some really nice integrations.
* No Wink integration yet leaves me pretty sad. It means that basically none of the home automation stuff that I have is accessible directly through the Home. I have to set things up as a shortcut in Wink, then as an [IFTTT](https://ifttt.com) trigger against that shortcut. Pretty annoying.
* I turned to IFTTT pretty quickly to do any of the interesting home automation stuff I wanted to play with, because of the lack of Wink integration. It works reasonably well, but is a little slower than I’d like since it has to get to Google, IFTTT, then (in my case), Wink, and finally control something in my house.
* Integrations are only available for [Nest](https://nest.com/) (thermostat only), [Philips Hue](http://www2.meethue.com/en-us/) and [SmartThings](https://www.smartthings.com/) on the home automation front.
* I like the lights/interaction with the Google Home a bit more. The colored dots/animations feel “friendlier”.
* The touch-sensitive top of the Home is a nice addition. I have mine on my desk and find myself just tapping it quickly to pause, and sometimes using the spiral/swipe to adjust volume (although that’s a kind of awkward interaction).
* I haven’t built anything on it yet, but Google’s [API.ai](https://api.ai/) looks really interesting, and provides a pretty nice interface (and learning system) compared to having to write/generate a ton of utterances with Alexa.
* I don’t find the microphones/initial detection particularly good. I prefer to say “Hey Google” than “OK Google”, but either way I often find myself repeating it a few times to “get its attention”, and I also seem to see more “false-triggers” on the Google Home than I do on the Echo.
* The app prompts me to download separate apps, which I guess provide some level of integration? I tried downloading the TuneIn one, but couldn’t play JJJ radio because it “could not be found”.
* Setting Spotify as my default music source is nice, so now if I just ask for a track/artist, it always uses Spotify. I do find that often the first attempt to play music from Spotify doesn’t work though. Assistant will say “ok, playing from Spotify…” then just go quiet. If I repeat myself, it’ll work the next time. I have a feeling it’s related to the way Spotify handles multiple devices on the same account though, which seems to be a little bit funky with the Google Home in particular.
* Google seems generally better at answering “random” questions, and seems to come up with *something* for a lot more queries than Alexa.
* The set up process for the Home + Chromecast was a bit nicer than for the Echo.

*h/t to [Luca’s post](https://luca.blog/2017/01/15/first-impressions-on-google-home-and-alexa-dot/) that inspired me to write up my own experiences.*