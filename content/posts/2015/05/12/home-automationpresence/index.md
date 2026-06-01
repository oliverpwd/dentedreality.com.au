---
title: Home Automation/Presence
date: '2015-05-12T10:14:46+00:00'
tags:
- automation
- bluetooth
- home automation
- ibeacon
categories:
- posts
- tech
---

I’ve been thinking about home automation a bit recently, and I realized that what I want as a big part of a system is some sort of generic presence-system. I’m imagining something along the lines of:

* Small/cheap nodes that can be plugged in around a house/space
* The nodes would form a mesh and talk to each other
* Nodes would determine the strength of a signal (Bluetooth LE?) and “discuss” it amongst each other to determine which one you’re closest to, and thus roughly “where” you are (triangulate your location based on signal strengths)
* Nodes would all connect to a server/service (could be locally-hosted), where they would broadcast your current location somehow. Maybe something like a [Socket.IO](http://socket.io/) server, so that other services could connect and receive live updates of location changes?

I wonder if this could be hacked together from [iBeacons](https://en.wikipedia.org/wiki/IBeacon) somehow, or if it’s too much the reverse of what they’re intended for? Does this already exist? Is there a better/simpler solution already available?