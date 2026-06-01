---
title: My Smart Home 2021
date: '2021-12-24T15:35:54-07:00'
format: link
service: instapaper
tags:
- read
external_url: https://jorisroovers.com/posts/my-smart-home-2021
---

[My Smart Home 2021](https://jorisroovers.com/posts/my-smart-home-2021)  



**Hi! It’s me, Joris.**

It looks like I’ve linked you here myself. Linking people to a blogpost I wrote is often a bit  

akward, especially at work.

I likely shared this blog in an attempt to further a conversation. Usually the post does a better  

job at succinctly sharing information  

than I could by talking.

In any case, I hope me sharing this post doesn’t come across as  

[humblebragging](https://www.merriam-webster.com/dictionary/humblebrag), that’s  

really the opposite of what I’m trying to achieve.

**Thanks for reading!**

## A Home Assistant Love Story

**TLDR**: I made a bunch of changes to my Home Assistant setup. A high-level overview of the changes (and rationale) is provided in this post. Details, code and config can be found in my [casa repository on github](https://github.com/jorisroovers/casa).

It’s been a year since [I presented at the first Home Assistant conference](https://github.com/jorisroovers/casa/blob/master/docs/Ultimate-Morning-Routine.md) and 18 months since I wrote about [My Favorite Home Automations](https://jorisroovers.com/posts/my-favorite-home-automations). A lot has changed since then – time for an update.

# I ❤️ Home Assistant Operating System

![](https://jorisroovers.com/assets/articles/my-smart-home-2021/mbp-server.jpg)![](https://jorisroovers.com/assets/articles/my-smart-home-2021/mbp-server.jpg)


 Enlarge

After starting out on a Raspberry Pi, I hosted Home Assistant from this 2011 Macbook Pro – running Ubuntu – for over 4 years. Over the years it also ran a bunch of supporting software: Prometheus, InfluxDB, Logstash, Sensu, Monit, HA Dashboard, Elasticsearch and at least half a dozen others. I’ve kept [all the related ansible roles in a legacy folder on Github](https://github.com/jorisroovers/casa/tree/master/legacy/roles).




![](https://jorisroovers.com/assets/articles/my-smart-home-2021/mbp-server.jpg)![](https://jorisroovers.com/assets/articles/my-smart-home-2021/mbp-server.jpg)



After starting out on a Raspberry Pi, I hosted Home Assistant from this 2011 Macbook Pro – running Ubuntu – for over 4 years. Over the years it also ran a bunch of supporting software: Prometheus, InfluxDB, Logstash, Sensu, Monit, HA Dashboard, Elasticsearch and at least half a dozen others. I’ve kept [all the related ansible roles in a legacy folder on Github](https://github.com/jorisroovers/casa/tree/master/legacy/roles).





When I started playing with [Home Assistant](https://www.home-assistant.io/) in early 2016, it already showed great potential.

Yet over the years I found myself spending a lot of times working around limitations, writing custom scripts and installing additional supporting software on an old Macbook Pro I had turned into a makeshift server. I even had [the entire setup process automated using ansible](https://github.com/jorisroovers/casa/tree/master/legacy).

While this worked, this approach was no longer scaling:

1. **Maintenance time sink**: Keeping the whole setup up-to-date started taking a lot of time.
2. **Divergence**: Over time, my setup was starting to diverge more and more from *vanilla* Home Assistant which became a vicious circle as I tried patching my way around it. It also meant I was missing out on some of the newer, very powerful features (more on that below).
3. **Aging hardware**: Software was sometimes slow due to the older CPU and spinning hard drive.
4. **Fire Safety**: Macbooks aren’t meant to be running for years on end on wall power, often under high load and without additional cooling. I had already been pushing my luck for too long.

## Enter Home Assistant Blue 🟦

So when [Home Assistant Blue](https://www.home-assistant.io/blue/) – a compact all-in-one hardware platform running the [Home Assistant Operating System](https://github.com/home-assistant/operating-system) – was announced, I was immediately enticed and quickly ordered one. While it took me a few months to find the time and appetite to migrate, I regret not having done so sooner because the difference is so massive.

![](https://jorisroovers.com/assets/articles/my-smart-home-2021/ha-blue.jpg)![](https://jorisroovers.com/assets/articles/my-smart-home-2021/ha-blue.jpg)


 Enlarge

Home Assistant Blue, banana for scale.




![](https://jorisroovers.com/assets/articles/my-smart-home-2021/ha-blue.jpg)![](https://jorisroovers.com/assets/articles/my-smart-home-2021/ha-blue.jpg)



Home Assistant Blue, banana for scale.





The benefits:

* **One-click upgrades**: Upgrading has become a single button-click task, often done on mobile and from the couch. I’ve yet to encounter any issue.
* **Editing from mobile**: The Home Assistant Mobile app is amazing. Not only for controlling, but also for quickly making edits as you think of improvements (from the couch, toilet, bed, on the road. I’ve done all those things).
* **Remote control using [Nabu Casa](https://www.nabucasa.com/)**: This cloud service to remotely control Home Assistant (from the founders of Home Assistant itself) is great. It works really well, is [secure](https://www.nabucasa.com/config/remote/#security), has been very stable and at 5 USD/month is dirt-cheap for what it provides.
* [**Home Assistant Add-Ons**](https://www.home-assistant.io/addons/): The ease of installing and managing other systems like Grafana, AdGuard Home, ZWave JS, VS Studio Code Server (and much more) is awesome. So, much, time and effort saved.
* [**HACS**](https://hacs.xyz/): Unofficial (i.e. community supported) Home Assistant customization store. This has allowed me to cut back a ton on building my own customizations.
* [**Google Drive Backups**](https://github.com/sabeechen/hassio-google-drive-backup): Given the amount of time I spend on tweaking my Home Assistant configuration, backing it up regularly is critical. This solution works so well it’s worth calling out separately.

While I’m running on Home Assistant Blue, I’ve already pre-ordered **[Home Assistant Yellow](https://www.crowdsupply.com/nabu-casa/home-assistant-yellow)**, the successor to Blue. If you’re just starting out, I recommend pre-ordering Home Assistant Yellow and [using a Raspberry Pi running Home Assistant Operating System](https://www.home-assistant.io/installation/raspberrypi) in the meantime.

![](https://jorisroovers.com/assets/articles/my-smart-home-2021/updating-ha.png)![](https://jorisroovers.com/assets/articles/my-smart-home-2021/updating-ha.png)


 Enlarge

Upgrading Home Assistant and managing add-ons is so easy when running Home Assistant Operating System. I’m still getting over how much easier this is than what I had to do in the past.




![](https://jorisroovers.com/assets/articles/my-smart-home-2021/updating-ha.png)![](https://jorisroovers.com/assets/articles/my-smart-home-2021/updating-ha.png)



Upgrading Home Assistant and managing add-ons is so easy when running Home Assistant Operating System. I’m still getting over how much easier this is than what I had to do in the past.






![](https://jorisroovers.com/assets/articles/my-smart-home-2021/hacs-frontend.png)![](https://jorisroovers.com/assets/articles/my-smart-home-2021/hacs-frontend.png)


 Enlarge

[HACS](https://hacs.xyz/) front-end customizations I have installed at the time of writing. HACS has made it so easy for people to share their workarounds and dashboard cards, I’m glad I can finally make use of them!




![](https://jorisroovers.com/assets/articles/my-smart-home-2021/hacs-frontend.png)![](https://jorisroovers.com/assets/articles/my-smart-home-2021/hacs-frontend.png)



[HACS](https://hacs.xyz/) front-end customizations I have installed at the time of writing. HACS has made it so easy for people to share their workarounds and dashboard cards, I’m glad I can finally make use of them!






# Bye-Bye Hubs 👋, it’s been fun

![](https://jorisroovers.com/assets/articles/my-smart-home-2021/zigbee-network.png)![](https://jorisroovers.com/assets/articles/my-smart-home-2021/zigbee-network.png)


 Enlarge

Visualization of my zigbee network (> 80 devices), using [ZHA](https://www.home-assistant.io/integrations/zha/).




![](https://jorisroovers.com/assets/articles/my-smart-home-2021/zigbee-network.png)![](https://jorisroovers.com/assets/articles/my-smart-home-2021/zigbee-network.png)



Visualization of my zigbee network (> 80 devices), using [ZHA](https://www.home-assistant.io/integrations/zha/).





When I started out with home automation in 2016, I wasn’t as savvy nor comfortable going “all in” on Home Assistant without trying it for a while. As a result, I mostly bought smart devices that supported multiple ecoystems (Apple HomeKit, Google Home *and* Home Assistant) as a way to hedge against Home Assistant not working out.

In practice, this translated to my setup heavily relying on Philips Hue and Ikea Trådfri hubs. While this worked fairly well (and the Home Assistant integrations became a lot more reliable over the years), the indirection of using hubs remained suboptimal. I was also using a few TP Link Wifi smartplugs that I wanted to get rid off.

So earlier this year, I decided to go all-in on [Zigbee](https://en.wikipedia.org/wiki/Zigbee) and re-paired all my devices with a [Conbee 2 Zigbee Gateway](https://phoscon.de/en/conbee2), while also adding a bunch more sensors and replacing some older bulbs and switches. I also added a few [Z-Wave](https://en.wikipedia.org/wiki/Z-Wave) smartplugs for power monitoring use-cases.

Overall, I’m extremely happy with that move and can highly recommend it; in general devices are more responsive and automations more reliable.

On caveat is that I have started running into some reliability issues (occasional device unavailability) once I exceeded 50 or so devices. This seems to be common for Zigbee networks, and I’m still exploring a few options on how to improve that.

I’m excited about the upcoming [Matter and Thread](https://www.theverge.com/22787729/matter-smart-home-standard-apple-amazon-google) standards which are likely to replace/augment Zigbee (and Z-wave) as true interoperable home automation connectivity standards. While some upgradeability has been promised for existing Zigbee setups, I fully expect having to buy (some) new devices. Regardless, the next 2 years are set to be bring disruption and innovation – I can’t wait 😁

![](https://jorisroovers.com/assets/articles/my-smart-home-2021/hubs.jpg)![](https://jorisroovers.com/assets/articles/my-smart-home-2021/hubs.jpg)


 Enlarge

**Philips Hue** (bottom left) and **Ikea Trådfri** (bottom right) hubs which I’m longer using, together with the **Homematic** hub I still use for radiator valve control.




![](https://jorisroovers.com/assets/articles/my-smart-home-2021/hubs.jpg)![](https://jorisroovers.com/assets/articles/my-smart-home-2021/hubs.jpg)



**Philips Hue** (bottom left) and **Ikea Trådfri** (bottom right) hubs which I’m longer using, together with the **Homematic** hub I still use for radiator valve control.






![](https://jorisroovers.com/assets/articles/my-smart-home-2021/aeotec-wallplug.jpg)![](https://jorisroovers.com/assets/articles/my-smart-home-2021/aeotec-wallplug.jpg)


 Enlarge

For power monitoring use-cases, I use Z-Wave power plugs like this [Aeotec Smart Switch 7](https://aeotec.com/z-wave-plug-in-switch/index.html). I use Z-Wave instead of Zigbee because Zigbee plugs with power monitoring are not as common and I’ve read about various reporting issues with them.




![](https://jorisroovers.com/assets/articles/my-smart-home-2021/aeotec-wallplug.jpg)![](https://jorisroovers.com/assets/articles/my-smart-home-2021/aeotec-wallplug.jpg)



For power monitoring use-cases, I use Z-Wave power plugs like this [Aeotec Smart Switch 7](https://aeotec.com/z-wave-plug-in-switch/index.html). I use Z-Wave instead of Zigbee because Zigbee plugs with power monitoring are not as common and I’ve read about various reporting issues with them.






# Sensing 📊 and Actuating 🤖

Of course, home automation is all about sensors and actuators. With my full embrace of Zigbee and Z-Wave, I also went on a bit of a sensor purchasing spree: motion sensors, temperature+humidity sensors, door/window contact sensors, leak sensors, power monitoring plugs. While I dream of having every room fully *sensorized,* it seems I can always think of another sensor to add.

All this data allows for setting up all sorts of useful notifications:

* **Door contact sensor**: *Front door left open for more than 5 minutes!*
* **Window contact sensor**: *It’s been more than 2 days since the kids’ bedroom windows were opened, time for some ventilation?*
* **Motion sensor**: *Motion detected in the house while house set to Away!*
* **Cameras**: *A person detected in the back garden while house set to Away!*
* **Leak sensor**: *Leak detected in Laundry room!*
* **Power Monitoring**: *Washer/Dryer has finished!*
* **Temperature sensors**: *It’s getting cold in the kids’ rooms, maybe turn on central heating?*
* **Air Quality**: *The concentration of CO2 is getting high in the office, maybe open a window?*
* **Vibration sensor**: *(automation) Dining table chair moved, turn on dining table lights!*
* **Apple [AirTags](https://www.apple.com/airtag/)**: *Wallet left behind when not at home! (not in Home Assistant)*

![](https://jorisroovers.com/assets/articles/my-smart-home-2021/aqara-sensors.jpg)![](https://jorisroovers.com/assets/articles/my-smart-home-2021/aqara-sensors.jpg)


 Enlarge

Various [Aqara](https://www.aqara.com/eu/products.html) Zigbee sensors I use. A big benefit of Zigbee over Z-wave is price. Each of these sensors costs less than 25 EUR, often considerably less when ordered in bulk and/or from China.




![](https://jorisroovers.com/assets/articles/my-smart-home-2021/aqara-sensors.jpg)![](https://jorisroovers.com/assets/articles/my-smart-home-2021/aqara-sensors.jpg)



Various [Aqara](https://www.aqara.com/eu/products.html) Zigbee sensors I use. A big benefit of Zigbee over Z-wave is price. Each of these sensors costs less than 25 EUR, often considerably less when ordered in bulk and/or from China.






![](https://jorisroovers.com/assets/articles/my-smart-home-2021/software-sensors.png)![](https://jorisroovers.com/assets/articles/my-smart-home-2021/software-sensors.png)


 Enlarge

Software sensors for presence detection and more, via the Home Assistant mobile app.




![](https://jorisroovers.com/assets/articles/my-smart-home-2021/software-sensors.png)![](https://jorisroovers.com/assets/articles/my-smart-home-2021/software-sensors.png)



Software sensors for presence detection and more, via the Home Assistant mobile app.






And of course, you can build a bunch of cool dashboards with all that data as well:

![](https://jorisroovers.com/assets/articles/my-smart-home-2021/ha-dashboard-energy.png)![](https://jorisroovers.com/assets/articles/my-smart-home-2021/ha-dashboard-energy.png)


 Enlarge

Home Assistant 2021.08 (August 2021) introduced [energy management](https://www.home-assistant.io/blog/2021/08/04/home-energy-management/). To get this data, I use a Raspberry Pi hooked up to my Smart Energy meter which supports [DSMR](https://www.home-assistant.io/integrations/dsmr/). I’ll be switching to [SlimmeLezer+](https://www.zuidwijk.com/product/slimmelezer-plus/) in the near future.




![](https://jorisroovers.com/assets/articles/my-smart-home-2021/ha-dashboard-energy.png)![](https://jorisroovers.com/assets/articles/my-smart-home-2021/ha-dashboard-energy.png)



Home Assistant 2021.08 (August 2021) introduced [energy management](https://www.home-assistant.io/blog/2021/08/04/home-energy-management/). To get this data, I use a Raspberry Pi hooked up to my Smart Energy meter which supports [DSMR](https://www.home-assistant.io/integrations/dsmr/). I’ll be switching to [SlimmeLezer+](https://www.zuidwijk.com/product/slimmelezer-plus/) in the near future.






![](https://jorisroovers.com/assets/articles/my-smart-home-2021/ha-dashboard-environment.png)![](https://jorisroovers.com/assets/articles/my-smart-home-2021/ha-dashboard-environment.png)


 Enlarge

Environment dashboard. Usefulness? Limited. Cool-factor? **A+** 😎




![](https://jorisroovers.com/assets/articles/my-smart-home-2021/ha-dashboard-environment.png)![](https://jorisroovers.com/assets/articles/my-smart-home-2021/ha-dashboard-environment.png)



Environment dashboard. Usefulness? Limited. Cool-factor? **A+** 😎






Sensing is awesome, but where home automation ***really*** shines is when it can do physical things around the house. This is an area where I’ve been doubling down, actuating all sorts of things:

* **Motion-based lights**: The majority of the lights in our home are now motion activated, with *smart* behavior depending on time-of-day and activity (working, watching TV, eating, sleeping, etc).
* **Curtains**: The office and hallway curtains are [fully automated](https://github.com/jorisroovers/casa/tree/master/projects/curtain-opener).
* **Window Blinds**: Similarly, the office blinds [will tilt automatically](https://twitter.com/jorisroovers/status/1460272092214145025) in the evening or when leaving home.
* **Window Opener**: The master bedroom window will intelligently open and close based on time-of-day and weather. [Detailed write-up](https://jorisroovers.com/posts/window-opener).
* **Thermostat:** These are pretty common, we use a Nest for downstairs heat control.
* **Radiator valves:** To control the heating of rooms upstairs.
* **Air purifier and humidifier**: A [Dyson Pure Humidify+Cool](https://www.dyson.com/air-treatment/air-purifier-humidifiers/pure-humidify-cool-ph01) does automatic air filtering and humidity control.
* **Diaper Station**: Automated lights based on weight sensing (i.e. when a baby is being changed).
* **Bathroom Mirror Heating:** A heating pad behind the mirror prevents it fogging up while showering. [Pictures in my Home Assistant Conference presentation.](https://github.com/jorisroovers/casa/blob/master/docs/Creating%20the%20Ultimate%20Morning%20Routine%20-%20Joris%20Roovers.pdf)
* **Boiling water tap:** We have a *[5-in-1 (warm, cold, cooking, carbonated, filtered) water tap](https://www.quooker.nl/international)* in the kitchen that saves a lot of time when making tea and cooking.
* **Smart Sauna**: I build a small infrared sauna and [equipped it with some smarts](https://jorisroovers.com/posts/my-smart-sauna).

Video Player is loading.
Current Time 0:00
/

Duration 0:22
Loaded: 0.00%


Stream Type LIVE

Remaining Time –0:22
 
1x

* Chapters


* descriptions off, selected


* captions off, selected



This is a modal window.


Beginning of dialog window. Escape will cancel and close the window.

Text

ColorTransparency


Background

ColorTransparency


Window

ColorTransparency



Font Size

Text Edge Style

Font Family


End of dialog window.



[Automated Curtains](https://github.com/jorisroovers/casa/tree/master/projects/curtain-opener) in the office.




Video Player is loading.
Current Time 0:00
/

Duration 0:51
Loaded: 0.00%


Stream Type LIVE

Remaining Time –0:51
 
1x

* Chapters


* descriptions off, selected


* captions off, selected



This is a modal window.


Beginning of dialog window. Escape will cancel and close the window.

Text

ColorTransparency


Background

ColorTransparency


Window

ColorTransparency



Font Size

Text Edge Style

Font Family


End of dialog window.



[Custom-built window opener](https://jorisroovers.com/posts/window-opener) in the bedroom.





![](https://jorisroovers.com/assets/articles/my-smart-home-2021/radiator-valve.jpg)![](https://jorisroovers.com/assets/articles/my-smart-home-2021/radiator-valve.jpg)


 Enlarge

Smart radiator valves, [HomeMatic HM-CC-RT-DN](https://www.eq-3.com/products/homematic/detail/homematic-wireless-radiator-thermostat.html).




![](https://jorisroovers.com/assets/articles/my-smart-home-2021/radiator-valve.jpg)![](https://jorisroovers.com/assets/articles/my-smart-home-2021/radiator-valve.jpg)



Smart radiator valves, [HomeMatic HM-CC-RT-DN](https://www.eq-3.com/products/homematic/detail/homematic-wireless-radiator-thermostat.html).






Video Player is loading.
Current Time 0:00
/

Duration 1:00
Loaded: 0.00%


Stream Type LIVE

Remaining Time –1:00
 
1x

* Chapters


* descriptions off, selected


* captions off, selected



This is a modal window.


Beginning of dialog window. Escape will cancel and close the window.

Text

ColorTransparency


Background

ColorTransparency


Window

ColorTransparency



Font Size

Text Edge Style

Font Family


End of dialog window.



Smart Diaper Station, using an ESP32, ESPHome and an HX711 sensor. Inspired by [a video from Everything Smart Home](https://www.youtube.com/watch?v=VCEgeDN0RLw).




# Smarter Dashboards and Notifications 🔔

As part of my move to Home Assistant Blue, I also fully adopted [Lovelace](https://www.home-assistant.io/lovelace/) for my wall-mounted control dashboards (running on iPad minis). I had been using [AppDaemon HA Dashboard](https://appdaemon.readthedocs.io/en/latest/DASHBOARD_INSTALL.html) before which served me really well for the last few years, but it’s clear that Lovelace is the superior solution these days (richer widgets, UI editing, less maintenance, frequent updates).

![](https://jorisroovers.com/assets/articles/my-smart-home-2021/appdaemon-dashboard.jpg)![](https://jorisroovers.com/assets/articles/my-smart-home-2021/appdaemon-dashboard.jpg)


 Enlarge

The [AppDaemon HA Dashboard](https://appdaemon.readthedocs.io/en/latest/DASHBOARD_INSTALL.html) I had been using for the last few years.




![](https://jorisroovers.com/assets/articles/my-smart-home-2021/appdaemon-dashboard.jpg)![](https://jorisroovers.com/assets/articles/my-smart-home-2021/appdaemon-dashboard.jpg)



The [AppDaemon HA Dashboard](https://appdaemon.readthedocs.io/en/latest/DASHBOARD_INSTALL.html) I had been using for the last few years.






![](https://jorisroovers.com/assets/articles/my-smart-home-2021/wallmount-ipad-annotated.jpg)![](https://jorisroovers.com/assets/articles/my-smart-home-2021/wallmount-ipad-annotated.jpg)


 Enlarge

The main [Lovelace](https://www.home-assistant.io/lovelace/) dashboard we use today, annotated.




![](https://jorisroovers.com/assets/articles/my-smart-home-2021/wallmount-ipad-annotated.jpg)![](https://jorisroovers.com/assets/articles/my-smart-home-2021/wallmount-ipad-annotated.jpg)



The main [Lovelace](https://www.home-assistant.io/lovelace/) dashboard we use today, annotated.






While improving my dashboards is something I want to spent a lot more time on, one thing I’ve been focussing on already is building *“smarter”* dashboards. Rather than showing dozens of sensors and controls at once, such dashboards only show ***what’s relevant at the time it is relevant*** (using a combination of [conditional cards](https://www.home-assistant.io/lovelace/conditional/), [custom button card](https://github.com/custom-cards/button-card), [card mod](https://github.com/thomasloven/lovelace-card-mod)).

![](https://jorisroovers.com/assets/articles/my-smart-home-2021/ios-notifications.png)![](https://jorisroovers.com/assets/articles/my-smart-home-2021/ios-notifications.png)


 Enlarge

Mobile notifications via the [Home Assistant mobile app](https://companion.home-assistant.io/) (also available for Android).




![](https://jorisroovers.com/assets/articles/my-smart-home-2021/ios-notifications.png)![](https://jorisroovers.com/assets/articles/my-smart-home-2021/ios-notifications.png)



Mobile notifications via the [Home Assistant mobile app](https://companion.home-assistant.io/) (also available for Android).





To goal here is to avoid **dashboard fatigue***,* where you stop looking at a dashboard because it’s always showing the same information. Examples include indicators for trash pickup, open windows/doors, a running dryer/washer and vacation days.

Similarly, I’ve been paying more attention to avoid **notification fatigue***,* where I stop looking at notifications on my phone because there’s so many of them and most have become irrelevant (e.g. window opened and closed hours ago). Most of this is done by auto-hiding messages after a few minutes or intelligently cleaning them up (e.g. remove a *Window Opened* notification when the window is closed).

For device control, I actually try to use the wall mounted dashboards as little as possible, instead relying on automations, voice control and a limited amount of physical (smart) wall switches. Wall mounted dashboards are really cool, but nothing beats a physical switch to toggle lights.

Dashboard building is a bit of a rabbit hole on its own: there are always things to improve. For inspiration, I’ve been looking at [ha-floorplan](https://github.com/ExperienceLovelace/ha-floorplan), [Dwains dashboard](https://github.com/dwainscheeren/dwains-lovelace-dashboard) and [Mattias Persson](https://github.com/matt8707/hass-config)’s work.

# The State of Home Automation

My personal home automation journey will likely never be done. I’ve got plenty of things on my list that I’d still like to automate: door locks, remaining windows/curtains/blinds, doorbell, sense infuser, garden irrigation, the list goes on. I know what to do to keep busy 🙂

Meanwhile, the home automation space is maturing rapidly. Compared to just a few years ago, things have gotten much better:

* **Stability and responsiveness**: while it still happens daily that a lightbulb or sensor doesn’t properly respond, overall stability and responsiveness has improved massively.
* **Standardization**: While Matter seems to be perpetually a few months out, the fact that the industry is working towards a single widely adopted standard is a game-changer.
* **Smart Device availability**: the number of available smart devices has exploded and the prices have come down a lot. Smart lamps and sensors are now plentiful and more approachable solutions are coming to market for things that used to be hard or expensive.
* **Influencers**: the number of youtube channels, twitter accounts and blogs seems to have exploded. I particularly like [The Hook Up](https://www.youtube.com/c/TheHookUp) and [Everything Smart Home](https://www.youtube.com/channel/UCrVLgIniVg6jW38uVqDRIiQ), but there are [a bunch of others](https://www.awesome-ha.com/#online-resources).

Most of all, Home Automation (and [Home Assistant](https://www.home-assistant.io/)) is crossing the barrier where it’s no longer only attainable for IT folk and tech enthusiasts, but becoming mainstream. For me, that’s a child’s dream come through.

Comments, questions, feedback? I’m [@jorisroovers](https://twitter.com/jorisroovers)  

on twitter.

Enjoyed reading this?   
Read one of [my other posts](https://jorisroovers.com/posts).

Get notified of new posts by [subscribing to my newsletter](https://jorisroovers.com/newsletter).