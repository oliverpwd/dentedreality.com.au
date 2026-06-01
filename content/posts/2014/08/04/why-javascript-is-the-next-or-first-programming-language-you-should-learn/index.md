---
title: Why JavaScript Is The Next (or first) Programming Language You Should Learn
date: '2014-08-04T15:18:43+00:00'
tags:
- codepen
- development
- grunt
- gulp
- javascript
- jsfiddle
- mentor
- node.js
- phonegap
- programming
categories:
- personal
- posts
- tech
---

I’ve been asked a few times recently what programming language I’d learn if I was just starting out. Right now, the answer is definitely JavaScript, and here’s why:

## Easiest Development Environment

I believe one of the biggest hurdles for people to get into programming is actually [all of the other stuff](http://dentedreality.com.au/2014/06/07/why-web-development-is-complex/ "Why Web Development Is Complex") around just writing code. Anything you can do to get to the point where you’re writing code faster (at least while you’re learning) is a win in my mind. Everyone has access to a web browser, which means everyone now has access to a simple development environment. If you’re using Chrome on a Mac, press cmd-opt-j. Welcome to the console, you’re now able to start writing JavaScript to manipulate the page you’re looking at. That’s pretty awesome. There are also a bunch of [online](https://c9.io/) [editors](https://codio.com/) and tools like [CodePen](http://codepen.io/pen/), [JSFiddle](http://jsfiddle.net/) which allow you to dive into a more complete development/testing/prototyping environment right in your browser.

## Simple

JavaScript makes it really easy to write simple code when you’re getting started, which is perfectly valid. Define a function, call it. Make a loop. Ignore the DOM (in fact, ignore the web almost entirely) and focus on simple logic and code. Start building objects and arrays. The OO-model in JS can be a little weird (especially around classes and inheritance), but that’s OK, you’re going to need to be flexible if you’re going to be a developer anyway. Once you get the basics figured out, you can start diving deeper and discover the full power of JavaScript.

## Flexible

The flip side of the previous argument is that JavaScript is also super flexible (arguably too much so!). Once you move on from a few functions embedded directly in script tags in your page to manipulate an image or a menu, you can quickly move towards a fully-architected web application with many files, larger object/class-style structures, complex single-page-applications and a whole lot more. JavaScript actually scales up quite nicely to handle bigger challenges, and is ideally suited to web applications, since it’s so tightly integrated with the DOM and the browser.

## Web-native

As much as native mobile app developers would have you believe that apps are the future, I still think that open web technologies are the key to the future. Give it a little time, and we’ll mostly be writing all of our mobile apps in HTML/JS, and deploying them in wrapper-apps to our phones. I consider this basically inevitable. Learning to develop for the web is super important. You’ll need to know it basically regardless of what main language you’re working with, because despite our [best efforts](http://wordpress.org), you will still end up manipulating CSS, tweaking some HTML tags, etc. That’s not going to go away any time soon I don’t think.

## Inevitable

This is pretty far down the list, but that’s mainly because of a thought progression more than anything else. I actually see this as a really important reason for why you should learn JavaScript. Here’s the deal — if you want to develop things for the web, you *will* end up writing JavaScript. There’s no avoiding it. There’s only so much you can do with a server-side language (PHP, Python, Ruby). At some point, your payload is delivered to a browser, and if you want to do anything remotely interesting there, you have to do it in JavaScript. So if you’re going to have to learn it anyway, why not optimize that process (and perhaps use JS in more places, rather than less?).

## Portable (browser/server/native)

Now that we have things like [Node.js](http://nodejs.org/), JavaScript has moved beyond the browser. Not only can you write server-side JS (so you can build the front and back-end of your web application in JS), you can also use something like [node-webkit](https://github.com/rogerwang/node-webkit) to bundle it up into a distributable desktop application, or use [PhoneGap](http://phonegap.com/) to package it as a mobile app for any platform. No other language can match that portability right now.

## Toolchain

If all of the above wasn’t enough, the exploding JavaScript community has really come a long way in the last few years as far as the developer’s toolchain goes. While we might not have the integrated, one-stop-shop approach of something like [XCode](https://developer.apple.com/xcode/) for Mac developers, we have tools like [Grunt](http://gruntjs.com/) and [Gulp](http://gulpjs.com/) which allow us to build our own asset pipelines. Every code editor known to man has support for JavaScript syntax highlighting and linting, and we don’t need a build process like other languages, so we’re lighter on our feet anyway. There’s also a bunch of [tools for testing](https://stackoverflow.com/questions/300855/javascript-unit-test-tools-for-tdd); everything from unit tests to functional tests, to fully automated simulations of users-in-browsers.

So anyway — [there’s never been a better time](https://medium.com/message/you-are-not-late-b3d76f963142) to get started with coding, and if you’re going to do it, I suggest starting with JavaScript. Start small, work your way up. View Source. Get on Github. Go nuts.