---
title: Replacing Wink with Home Assistant
date: '2020-09-13T15:57:03-06:00'
service: jetpack
tags:
- home assistant
- home automation
- smart home
- wink
categories:
- posts
---

I used to have [Wink](https://www.wink.com/) set up, managing some smart home devices throughout our house. I liked it because the app UI was quite nicely done, and it seemed to be compatible with “everything”. I had even upgraded from their version 1 hub, to the version 2. But then a few months ago they decided (somewhat out of the blue) that they were going to start charging a subscription fee. Coupled with some recent outages and frequent command delays, and it was the “motivation” I needed to invest in a [Home Assistant](https://www.home-assistant.io/) system, and move away from Wink entirely.

## Set Up + Config

I chose to install everything on a Raspberry Pi 4, and am using the official images and [recommended way of configuring things](https://www.home-assistant.io/getting-started/). Things mostly worked as expected, although I had some trouble getting Z-Wave working, and also getting used to YAML in general. I also wrestled with getting DuckDNS and SSL working for a while, but some of that ended up just being me port-forwarding the wrong ports. Here are a few details on some of the things I’ve got running which I think are useful:

1. **[HACS](https://hacs.xyz/):** Great for adding all sorts of “unofficial” bits and pieces. I’ve got a few integrations ([Wyze](https://github.com/kevinvincent/ha-wyzesense), [Orbit b-hyve](https://github.com/sebr/bhyve-home-assistant), and [Tempest weather](https://github.com/briis/smartweatherudp)) and some frontend additions ([Mini Media Player](https://github.com/kalkih/mini-media-player), [Custom Header](https://github.com/maykar/custom-header), and [auto-entities](https://github.com/thomasloven/lovelace-auto-entities)).
2. Add-Ons (available via Supervisor)
   1. **Dropbox Sync**: Back up your system snapshots to Dropbox, for safe keeping. I have an automation which syncs daily, and then only retain the most recent 3 on my HA install locally.
   2. **DuckDNS**: This is how I get external access to my install, which is nice especially for the iOS app, so that I can control things from a distance.
   3. **FTP**: I turn this on/off when I need it, but it’s nice to just get quick access to files for editing things via a real editor.
   4. **File editor**: When I’m making quick tweaks to config, this is an embedded/browser-based file editor that gives you full access to everything.
3. **[Alexa Smart Home integration](https://www.home-assistant.io/integrations/alexa.smart_home/)**: Pretty tedious to set up, but it’s working smoothly and allows me to easily add/remove devices and control all sorts of things.

I configured static IPs for as many of the “permanent” devices as I could (HA host, Lutron bridge, Roomba, MyQ, Tempest weather, and our AppleTV), which has made it a little easier to keep track of things. I also forwarded ports 8123 and 443 into local 443 on the HA host, which is required for getting external access (and Alexa control) working.

## Platform Details

I’ve ended up with a few key pieces to my configuration, namely:

1. **Z-Wave:** 2 Schlage door locks and 1 (relay) switch, controlled via an Aeotec USB stick (I’ve had the most trouble with Z-Wave devices, and currently don’t have one of those locks added to the system).
2. **Zigbee:** Aqara buttons and climate sensors, controlled via a ConBee II USB stick.
3. **Wyze Sense:** Door open/close and motion sensors, controlled via the Wyze USB hub.
4. **Lutron Caseta:** dimmer light switches, controlled via their separate hub.

There are also a few other pieces (like a MyQ garage door controller) and some native integrations (HomeKit, SONOS, Roomba) that round things out.

## Automations + Smarts

The point of all of this is to add some “intelligence” or convenience to your home, so this is where things get fun. Here are a few of the things I’ve been able to do (so far!):

1. **Mailbox Sensor**: I added an open/close sensor to the mailbox, so that we get push notifications and an indicator in the HA dashboard when we (probably) have mail. I also have an NFC sticker near the mailbox that allows me to clear the sensor easily.
2. **After dark door/lock notifications**: If we leave a door or lock open for 15 minutes after a specified time, we’ll get a reminder to make sure we close things.
3. **Goodnight button** (via [Python script](https://www.home-assistant.io/integrations/python_script/)): I have a button next to the bed that locks and turns things off when we’re ready for bed. If something is left open we get a verbal warning via SONOS speaker.
4. **Door announcements**: We get a verbal announcement when a door is opened.
5. **Doorbell**: I replaced our doorbell with an Aqara switch. Now when someone presses it, a door chime is played on our SONOS speakers, and we get a push notification with a snapshot from our security camera at the front door.
6. **Garmin HassIQ**: I have a Garmin Fenix 5, and I found a neat little integration that allows me to control most “switching” devices directly from my watch!
7. **Motion controlled lights**: I’ve configured various lights to turn on automatically based on motion, and to turn off after periods of inactivity.
8. **Garage Car Door left open**: If we leave the car door of the garage open for more than a few minutes, we get a push notification to make sure that it’s intentional. If it’s not, there’s a button included in the notification that allows you to close it immediately.
9. **Automated chores**: I control our Roomba via HA now, and run it a few times a week. We get a notification when the bin is full. We also have some automated sprinklers that are now controlled via HA. If/when the integration controlling my weather station is fixed, I’ll also add in some smarts around temperature and rain (delays and increased watering).

## Shopping List

Here are all the pieces I’ve purchased so far in building out our system.

* [Raspberry Pi 4 Model B 2019 Quad Core 64 Bit WiFi Bluetooth (4GB)](https://www.amazon.com/gp/product/B07TC2BK1X/ref=ppx_yo_dt_b_asin_title_o01_s02?ie=UTF8&psc=1)
* [Argon One RPi Case + Power](https://www.amazon.com/gp/product/B07WP9P8VW/ref=ppx_yo_dt_b_asin_title_o00_s00?ie=UTF8&psc=1)
* [USB Card reader](https://www.amazon.com/gp/product/B07N192W13/ref=ppx_yo_dt_b_asin_title_o01_s01?ie=UTF8&psc=1)
* [SanDisk Extreme Pro 64GB SD Card](https://www.amazon.com/gp/product/B07G3GMRYF/ref=ppx_yo_dt_b_asin_title_o01_s00?ie=UTF8&psc=1)
* [Aeotec Z-Wave Gen5 Stick](https://www.amazon.com/gp/product/B00X0AWA6E/ref=ppx_yo_dt_b_asin_title_o01_s03?ie=UTF8&psc=1)
* [5-port Switch](https://www.amazon.com/gp/product/B00A128S24/ref=ppx_yo_dt_b_asin_title_o09_s00?ie=UTF8&psc=1)
* [Lutron Caseta bridge](https://www.amazon.com/gp/product/B00XPW67ZM/ref=ppx_yo_dt_b_asin_title_o01_s02?ie=UTF8&psc=1)
* [Z-Wave switch](https://www.amazon.com/gp/product/B0781XZYWR/ref=ppx_yo_dt_b_asin_title_o05_s00?ie=UTF8&psc=1) (intended to work as a relay, seems to be pretty flakey)
* [8 Outlet Surge Protector Power Strip](https://www.amazon.com/gp/product/B013FCSHB8/ref=ppx_yo_dt_b_asin_title_o04_s00?ie=UTF8&psc=1)
* [Dual 120mm USB Fans](https://www.amazon.com/gp/product/B00JLV4BWC/ref=ppx_yo_dt_b_asin_title_o03_s00?ie=UTF8&psc=1) (to keep the whole mess of things cool)
* [Wyze Sense Motion Sensor](https://wyze.com/wyze-sense.html)
* [Wyze Sense Hub](https://wyze.com/wyze-sense.html)
* [Wyze Sense Door Sensor](https://wyze.com/wyze-sense.html)
* [USB Hub](https://www.amazon.com/gp/product/B07L32B9C2/ref=ppx_yo_dt_b_asin_title_o02_s00?ie=UTF8&psc=1) + [extension cables](https://www.amazon.com/gp/product/B07RQRMGKB/ref=ppx_yo_dt_b_asin_title_o08_s00?ie=UTF8&psc=1)
* [MyQ Garage controller](https://www.amazon.com/gp/product/B075H7Z5L8/ref=ppx_yo_dt_b_asin_title_o06_s00?ie=UTF8&psc=1)
* [ConBeeII Stick](https://www.amazon.com/gp/product/B07PZ7ZHG5/ref=ppx_yo_dt_b_asin_title_o03_s00?ie=UTF8&psc=1)
* [Aqara Button](https://www.amazon.com/gp/product/B07D19YXND/ref=ppx_yo_dt_b_asin_title_o03_s01?ie=UTF8&psc=1)
* [Aqara Climate Sensor](https://www.amazon.com/gp/product/B07D37FKGY/ref=ppx_yo_dt_b_asin_title_o03_s00?ie=UTF8&psc=1)
* [Tempest Weather Station](https://weatherflow.com/tempest-weather-system/) ([here’s my weather!](https://tempestwx.com/station/20182/))
* I also ended up adding an (excessive) [UPS](https://www.amazon.com/gp/product/B003Y24DEU/ref=ppx_yo_dt_b_asin_title_o09_s00?ie=UTF8&psc=1) and [extra battery](https://www.amazon.com/gp/product/B0047E5B90/ref=ppx_yo_dt_b_asin_title_o09_s01?ie=UTF8&psc=1) to keep things running smoothly.
* I’ve got a few [iSP5 switches](https://www.ihomeaudio.com/isp5wc/) connected via HomeKit as well, which I had from my previous set up

It’s been a pretty big and long-running project, but I’m happy with the results. I love that it’s (almost) all local (no external internet connection required for most pieces of the system), and it’s been quite fun tinkering around. I’m also able to dial in automations to a level that wasn’t possible with Wink, and the sheer scope of compatibility I have now is pretty impressive. It has been nowhere near as hard as I expected to get it all working (I was expecting a ton of command-line mucking around, but it’s mostly UI-driven).

There’s still a bunch I’d like to do, especially around UI and control, and setting up a tablet or 2 to have around the house to control things, but overall I’m really happy with it. Open source FTW!