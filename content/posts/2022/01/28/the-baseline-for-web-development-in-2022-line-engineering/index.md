---
title: The baseline for web development in 2022 – LINE ENGINEERING
date: '2022-01-28T19:40:55-07:00'
format: link
service: instapaper
tags:
- read
external_url: https://engineering.linecorp.com/en/blog/the-baseline-for-web-development-in-2022/
---

[The baseline for web development in 2022 – LINE ENGINEERING](https://engineering.linecorp.com/en/blog/the-baseline-for-web-development-in-2022/)  



**TL;DR:***The baseline for web development in 2022 is: low-spec Android devices in terms of performance, Safari from two years before in terms of Web Standards, and 4G in terms of networks. The web in general is not answering those needs properly, especially in terms of performance where factors such as an over-dependence on JavaScript are hindering our sites’ performance.*

Hello there! I’m Alan Dávalos, a front-end engineer at LINE. You might have thought this article’s title is just clickbait but bear with me for a while, I promise it’s worth it. The main reason for that is that there were some big changes in the web between 2021 and 2022 and those affect the way we should face web development as a whole.

So, today I would like to address those changes and how well we are adapting to them as web developers by analyzing many different data points.

## The biggest change that happened in 2021 ~ The retirement of Internet Explorer

There were many changes in 2021 but none were as big as the official retirement of Internet Explorer (IE). [Microsoft made the announcement in May 2021](https://blogs.windows.com/windowsexperience/2021/05/19/the-future-of-internet-explorer-on-windows-10-is-in-microsoft-edge/) and by August many Microsoft products including Microsoft 365 had officially dropped support for IE. The official retirement date for IE is scheduled for June 2022 but there are several other reasons why we can consider IE as fully retired by now.

### Some of the Web’s biggest sites drop support for IE

After Microsoft’s announcement, many other projects started dropping support for IE. Among them are sites most internet users interact with.

For example, [Google search dropped support for IE in October 2021](https://twitter.com/cramforce/status/1443962459723755533).

![](https://engineering.linecorp.com/wp-content/uploads/2022/01/Google-Support-1-1024x649.png)![](https://engineering.linecorp.com/wp-content/uploads/2022/01/Google-Support-1-1024x649.png)

Twitter @cramforce


In Japan, [Yahoo! JAPAN announced set IE as a non-recommended browser in September 2021](https://support.yahoo-net.jp/PccYjcommon/s/article/H000011350) (website in Japanese).

![](https://engineering.linecorp.com/wp-content/uploads/2022/01/Yahoo-Support-1.png)![](https://engineering.linecorp.com/wp-content/uploads/2022/01/Yahoo-Support-1.png)
> Yahoo! JAPAN had Internet Explorer 11 as a recommended browser. But following the end of support of Internet Explorer announcement by Microsoft Yahoo! JAPAN decided to set Internet Explorer 11 as a non-recommended browser starting from September 7th, 2021.
> 
> Furthermore, you can still use Internet Explorer 11 to use some of our services but you might face issues where the page doesn’t behave or render properly. We would also recommend any users using Internet Explorer 11 to use other of our recommended browsers as the official end-of-support date for Internet Explorer 11 is getting close.

Furthermore, WordPress, [which is used in about 33% of the Web](https://almanac.httparchive.org/en/2021/cms#top-cmss), also announced that [they would drop support for IE in WordPress version 5.8](https://wordpress.org/news/2021/05/dropping-support-for-internet-explorer-11/) released in July 2021.

![](https://engineering.linecorp.com/wp-content/uploads/2022/01/Wordpress-Support-1.png)![](https://engineering.linecorp.com/wp-content/uploads/2022/01/Wordpress-Support-1.png)

When WordPress 5.8 is released in July of this year, Internet Explorer 11 will no longer be supported.


### IE’s current market share

There is a good reason why the announcements above didn’t wait until IE’s official retirement. IE’s market share dropped sharply throughout 2021.

![](https://engineering.linecorp.com/wp-content/uploads/2022/01/Global-Browser-Share-Pie-1.svg)![](https://engineering.linecorp.com/wp-content/uploads/2022/01/Global-Browser-Share-Pie-1.svg)

Graph derivative of [“Browser Market Share Worldwide”](https://gs.statcounter.com/browser-market-share#monthly-202111-202111-bar) by Statcounter used under [CC BY-SA 3.0](https://creativecommons.org/licenses/by-sa/3.0/). This graph is licensed under [CC BY-SA 3.0](https://creativecommons.org/licenses/by-sa/3.0/) by Alan Dávalos.



![](https://engineering.linecorp.com/wp-content/uploads/2022/01/Japanese-Browser-Share-Pie-1.svg)![](https://engineering.linecorp.com/wp-content/uploads/2022/01/Japanese-Browser-Share-Pie-1.svg)

Graph derivative of [“Browser Market Share Japan”](https://gs.statcounter.com/browser-market-share/all/japan/#monthly-202111-202111-bar) by Statcounter used under [CC BY-SA 3.0](https://creativecommons.org/licenses/by-sa/3.0/). This graph is licensed under [CC BY-SA 3.0](https://creativecommons.org/licenses/by-sa/3.0/) by Alan Dávalos.


Globally, IE’s current market share is under 0.5%. And even in Japan, which has a higher market share of IE compared to other countries, IE’s market share is close to 2% and has a downward tendency.

## The new baseline for web development

Until now we kept supporting IE due to its market share. But now, there are basically no good reasons to keep supporting IE. However, this brings up a new problem, IE was the support baseline for many tools. IE’s development mostly stopped quite a while ago, so the web standards it supports are very different to those supported by modern browsers.

Now that IE is gone, that baseline has become blurry. So, I’ll take upon the task of defining a new baseline by analyzing the current status of our users’ devices.

### Users’ devices and browsers

#### The market share for browsers and OS

Let’s take a look at the browser market share chart in a different format.

![](https://engineering.linecorp.com/wp-content/uploads/2022/01/Global-Browser-Share-Bar-1.svg)![](https://engineering.linecorp.com/wp-content/uploads/2022/01/Global-Browser-Share-Bar-1.svg)

Graph derivative of [“Browser Market Share Worldwide”](https://gs.statcounter.com/browser-market-share#monthly-202111-202111-bar) by Statcounter used under [CC BY-SA 3.0](https://creativecommons.org/licenses/by-sa/3.0/). This graph is licensed under [CC BY-SA 3.0](https://creativecommons.org/licenses/by-sa/3.0/) by Alan Dávalos.



![](https://engineering.linecorp.com/wp-content/uploads/2022/01/Japanese-Browser-Share-Bar-1.svg)![](https://engineering.linecorp.com/wp-content/uploads/2022/01/Japanese-Browser-Share-Bar-1.svg)

Graph derivative of [“Browser Market Share Japan”](https://gs.statcounter.com/browser-market-share/all/japan/#monthly-202111-202111-bar) by Statcounter used under [CC BY-SA 3.0](https://creativecommons.org/licenses/by-sa/3.0/). This graph is licensed under [CC BY-SA 3.0](https://creativecommons.org/licenses/by-sa/3.0/%20target=) by Alan Dávalos.


There are two tendencies I want to highlight here:

1. There are 3 browser engines we need to support
   1. Chromium, the base for Chrome, Edge, Samsung Internet Browser, and Opera.
   2. Gecko, the base for Firefox.
   3. WebKit, the base for Safari.
2. The rate of Safari users in Japan is higher than the global average.

The reason for the latter of those points is easy to figure when looking at the following charts.

![](https://engineering.linecorp.com/wp-content/uploads/2022/01/Global-Mobile-OS-Share-1.svg)![](https://engineering.linecorp.com/wp-content/uploads/2022/01/Global-Mobile-OS-Share-1.svg)

Graph derivative of [“Mobile Operating System Market Share Worldwide”](https://gs.statcounter.com/os-market-share/mobile/worldwide/#monthly-202111-202111-bar) by Statcounter used under [CC BY-SA 3.0](https://creativecommons.org/licenses/by-sa/3.0/). This graph is licensed under [CC BY-SA 3.0](https://creativecommons.org/licenses/by-sa/3.0/%20target=) by Alan Dávalos.



![](https://engineering.linecorp.com/wp-content/uploads/2022/01/Japanese-Mobile-OS-Share-1.svg)![](https://engineering.linecorp.com/wp-content/uploads/2022/01/Japanese-Mobile-OS-Share-1.svg)

Graph derivative of [“Mobile Operating System Market Share Japan”](https://gs.statcounter.com/os-market-share/mobile/japan/#monthly-202111-202111-bar) by Statcounter used under [CC BY-SA 3.0](https://creativecommons.org/licenses/by-sa/3.0/). This graph is licensed under [CC BY-SA 3.0](https://creativecommons.org/licenses/by-sa/3.0/%20target=) by Alan Dávalos.


As you can see, Android has around 70% of the global mobile OS market share while iOS has 28%. On the other hand, the opposite applies in Japan, where Android has only 33% of market share compared to iOS’s 66%.

#### The difference in CPU performance

The difference in OS is not only on the software side, it also implies hardware differences. The biggest one could be considered the CPU performance.

![](https://engineering.linecorp.com/wp-content/uploads/2022/01/Performance-Multi-1-1024x663.png)![](https://engineering.linecorp.com/wp-content/uploads/2022/01/Performance-Multi-1-1024x663.png)

As seen in the charts above, iOS devices have had the best CPU performance scores every year for the past 10 years. Compared to that, high-tier Android devices have somewhat similar results, but mid-tier and low-tier devices perform quite worse than that. Quoting Alex Russel, [the author of the article the above two charts came from](https://infrequently.org/2021/03/the-performance-inequality-gap/#mind-the-gap%20target=):

> 2020’s high-end Androids sport the single-core performance of an iPhone 8, a phone released in Q3’17  
> Mid-priced Androids were slightly faster than 2014’s iPhone 6  
> Low-end Androids have finally caught up to the iPhone 5 from 2012

#### Browser’s alignment to web standards

The part of the different browsers that most affects web development is their implementation of the different web standards. As mentioned above, there are 3 browser engines we should care about. So, let’s take a look at how these different browsers implement web standards. The easiest way to check these difference is with the following data of the Web Platform Tests.

![](https://engineering.linecorp.com/wp-content/uploads/2022/01/WPT-1.svg)![](https://engineering.linecorp.com/wp-content/uploads/2022/01/WPT-1.svg)

Source: [“Browser Specific Failures”](https://ecosystem-infra.github.io/wpt-results-analysis/%20target=) – extracted on December 4th, 2021


This chart shows how many Web Platform Tests fail in only one browser. In other words, how many features the other two browsers have already implemented.

One fact becomes evident here, the number of web standards only Safari hasn’t implemented is many times bigger than those of Firefox and Chrome. To be precise, 2.4 times as much as Firefox and 4.7 times as much as Chrome.

Moreover, we should also take in consideration the close relationship Safari and iOS have. Specifically, these two points:

1. Other mobile browsers update independently from the OS, whereas Safari is only updated when there is an update to iOS. iOS devices that are no longer supported with newer versions of iOS cannot update to the latest version of Safari.
2. All browsers in iOS are based on Webkit: There are Chrome and Firefox versions for iOS but those use the same engine as Safari in iOS. This is because of [an Apple guideline](https://developer.apple.com/app-store/review/guidelines/#software-requirements%20target=) which mentions that all iOS browsers must use Webkit.

This relationship between iOS and Safari also means that we must also check how the market share of iOS versions changes with each new major iOS version release.

![](https://engineering.linecorp.com/wp-content/uploads/2022/01/iOS-Share-1.png)![](https://engineering.linecorp.com/wp-content/uploads/2022/01/iOS-Share-1.png)

Graph derivative of [“Mobile & Tablet iOS Version Market Share Worldwide”](https://gs.statcounter.com/ios-version-market-share/mobile-tablet/worldwide/#quarterly-201901-202104) by Statcounter used under [CC BY-SA 3.0](https://creativecommons.org/licenses/by-sa/3.0/). This graph is licensed under [CC BY-SA 3.0](https://creativecommons.org/licenses/by-sa/3.0/%20target=) by Alan Dávalos.


To have a deeper understanding on how the market share of each iOS version changes let’s take a look at how the market share for iOS 12 changed in the past 2 years:

* From Q1 to Q3 2019, iOS 12’s share was gradually growing, but that number plummets once the iPhone 11 and iOS 13 came out in Q3.
* From there, iOS 12’s share fell under 20% throughout the next year.
* Then, as soon as the iPhone 12 and iOS 14 came out in Q3 2020, iOS 12’s share had such a sharp decline, by Q2 2021 its share was negligible.
* The same pattern that happened to iOS 12 was also observed in later years with versions 13 and 14.

In conclusion, we can safely assume that over 90% of the iOS market share will be constantly made up of major versions released in the past 2 years. In other words, we only need to support Safari versions released in the last 2 years.

### Mobile networks

So far, we’ve mostly talked about devices and browsers, but now let’s take a look at one of the factors that has a big impact on the UX that web developers have no influence on: network connections. When connected to a Wi-Fi network, the connection is mostly stable but the same can’t be said for mobile networks. Let’s take a look at the current state of mobile networks.

#### 3G and 4G

When using lab tools such as Lighthouse, the network is tethered to simulate 3G, but mobile networks worldwide have changed recently. According to [a May 2020 report by Opensignal](https://www.opensignal.com/sites/opensignal-com/files/data/reports/pdf-only/data-2020-05/state_of_mobile_experience_may_2020_opensignal_3_0.pdf%20target=), the worldwide average availability for 4G is 86.8%. So, we can safely assume that most users will have access to a 4G network worldwide. And among the tested countries, Japan had the highest 4G availability with 98.5%.

#### 5G

However, 5G networks are still far from being a reality. According to [a November 2021 report by Opensignal](https://www.opensignal.com/2021/11/30/benchmarking-the-global-5g-experience-november-2021%20target=), the highest 5G availability worldwide was only 29.1% in South Korea.

### What’s the new baseline?

Taking all the data above in consideration, the new baseline for web development would be:

1. **Safari** is the baseline in terms of web standards: The sites we develop must work in Safari versions at least 2 years old.
2. **Low-tier Android devices** are the baseline in terms of performance: Low-tier Android devices have advanced little in the past few years so we must make sure our sites are super performant.
3. **4G** is the baseline in terms of networks: Mobile networks have become a lot faster and stabler worldwide in recent years.

## How well are we answering to user needs?

We have successfully defined the 3 parts that make up our baseline but that’s not enough. We need to take a look at how well we’re answering to user needs. However, an in-depth analysis would bring up different results for different projects. So, talking about a specific project in LINE wouldn’t be as helpful for most people.

With that in mind, I’ll go big and analyze the whole web. Fortunately, we have a great data source for it, the [Web Almanac 2021](https://almanac.httparchive.org/ja/2021/%20target=). This is an annual report created by the HTTP Archive. In it, they analyze over 8.2 million sites to create 24 chapters. For this article, we’ll take some data excepts from some of these chapters to see how well the current web is matching the baseline defined above.

### The median website in 2021

The median website in 2021 weights 1,923 KB. If we separate the size by file type we can see that images and JavaScript (JS) make up most of that size.

Looking at this data, it’s easy to focus on the images as those are the heaviest, but we should pay special attention to the JS size. The biggest reason for that is that processing images is not as complicated as processing JS. Images can basically be rendered as soon as they are downloaded but JS needs to be parsed and executed too. So, generally speaking, JS processing takes up more resources.

Furthermore, according to [the article by Alex Russell](https://infrequently.org/2021/03/the-performance-inequality-gap/%20target=) mentioned above, when testing a low-tier Android device on a 4G network, the budget for a website to keep a good performance is up to 100 KB of HTML and CSS and up to 350 KB of JS. In other words, the current median site meets the performance budget in terms of HTML and CSS but it goes way over it in terms of JS.

### HTML and CSS usage

The Web Almanac has a chapter on both [markup](https://almanac.httparchive.org/en/2021/markup) and [CSS](https://almanac.httparchive.org/en/2021/css%20target=) which contain plenty of information. I want to highlight a few key data points that I think serve to exemplify how we’re using HTML and CSS currently.

#### HTML

Let’s first talk about HTML, there are currently [112 non-deprecated HTML elements](https://html.spec.whatwg.org/multipage/indices.html#elements-3%20target=). But the median amount of HTML elements used in a page is 31. There’s obviously no need to use every single element in all pages, but these 31 elements include elements such as `<html>`, `<body>`, and `<script>`. That means that the number of elements we’re using to actually display content is actually smaller.

In the list of the most used HTML elements, `<div>` is 1st place, `<span>` is 3rd, and `<p>` is 7th. Moreover, the probability of a page having a `<div>` element is 98.9%; it’s definitely the most used element to display contents.

In contrast, the probability of the `<main>` element being used is only 27.9%. The reason why this is important is because `<main>`, along with other elements such as `<aside>` and `<header>`, is one of the elements that doesn’t have a special style applied to it but has a semantic meaning. In other words, the usage of `<main>` can be taken as an indicator of how many pages are proactively using semantic elements. This is why that 27.9% number is so important.

#### CSS

For CSS usage, I think there’s one data point that summarizes CSS usage very well. And that is the usage of the modern layout features: Flex and Grid.

![](https://engineering.linecorp.com/wp-content/uploads/2022/01/CSS-1.svg)![](https://engineering.linecorp.com/wp-content/uploads/2022/01/CSS-1.svg)

Source: [“CSS” – Web Almanac 2021](https://almanac.httparchive.org/en/2021/css#flexbox-and-grid-adoption%20target=)


As you can see, while Flex is used in 71% of pages, Grid is only used in 8%. The biggest reason for this difference lies in IE support. [IE only supports an old specification of Grid](https://caniuse.com/css-grid%20target=), so pages that want to support IE must take that fact in account. CSS features cannot be polyfilled as easily as JS features. This is probably the main reason why many developers are giving up on using Grid. However, now that we can cut support for IE, many modern CSS features such as Grid become usable.

### Performance

The way of measuring performance most commonly used nowadays is by measuring the [Core Web Vitals](https://web.dev/vitals/) (CWV). There are many reasons why this happened but CWV being [used as a ranking factor in Google search](https://developers.google.com/search/blog/2020/11/timing-for-page-experience%20target=) is probably one of the biggest. Let’s look at how the web is performing in terms of CWV.

Performance isn’t great overall, over half of the pages have bad CWV scores. Mobile pages scoring worse than desktop pages 12% of the time seems reasonable considering the difference in CPU power between devices. And this result also aligns with the fact that most sites have JS sizes higher than the performance budget.

We can also see that performance directly influences the number of users by looking at the next chart.

We can see that there is a correlation between good CWV scores and number of views. Perhaps partly influenced by the fact that CWV is a ranking factor in Google search. The top 1,000 sites in terms of views have good CWV scores 37% of the time while the overall amount is 32%. And when checking the top 10,000 or 100,000, we can see that sites ranked higher in terms of views tend to have better performance. It’s definitely not a stretch to say that improving performance is one of the ways we can directly increment revenue in our projects.

### JS libraries and frameworks

So far we’ve seen how the amount of JS we serve is having a bad influence in our sites’ performance. Most of the projects which use large amounts of JS will use a library or framework in one way or another. So, let’s take a look at the consequences that choice can have.

#### JS libraries and frameworks usage

According to [the Web Almanac’s JS chapter](https://almanac.httparchive.org/en/2021/javascript#libraries-usage%20target=), the most used library is jQuery with 84% of usage. The fact that WordPress is used in 33% of sites that we mentioned above is one of the big reasons for this.

Among frameworks, React is the most popular at 8%. But if you consider other frameworks don’t even get to the 4% mark, it’s safe to say framework usage is still the minority.

#### Comparing framework performance

While frameworks are still the minority, we have enough data on the most popular ones to make some performance comparisons. The data for this section comes from [this article from 2020 by Tim Kadlec](https://timkadlec.com/remembers/2020-04-21-the-cost-of-javascript-frameworks/%20target=).

Let’s first compare the JS size for sites using React, Angular, Vue, and jQuery to the general data:

* The median for both the overall data and jQuery are each 414 KB and 430 KB. This number is close to the median for 2021.
* However, the median for Vue and React are both around 690 KB. Over 250 KB above the overall median.
* Angular is even higher at 1,066 KB, the first number over 1 MB.
* Even looking at the 10th percentiles the story is similar: the overall 10th percentile is 93 KB, jQuery’s is 110 KB, Vue’s is 245 KB, React’s is 348 KB, and Angular’s is 445 KB.
* In other words, even the sites using frameworks with the least amount of JS barely meet the performance budget set above.

Naturally, while JS size is a big indicator for performance it’s definitely not the whole story. So, let’s now dive into some data regarding how these same sites perform in actual devices.

* To be as fair as possible, sites using multiple libraries or frameworks weren’t included.
* Looking at the median times for jQuery and Vue, they stand at 2.3 seconds and 3.2 seconds respectively. Doing simple math, the ratio for the size difference is close to the ratio for time difference.
* However, React and Angular don’t follow the same tendency. Angular’s median time is 3.7 seconds while React’s is a few seconds slower at 10.1 seconds.
* It’s evident that size is not the only metric that matters when comparing JS libraries.

#### Comparing framework performance in static sites

Frameworks are used frequently to create Single Page Applications (SPA), but they are also used to create static sites. Let’s compare how Static Site Generators (SSG) using frameworks perform to SSGs not using JS frameworks. We’ll compare [the top 5 SSGs](https://almanac.httparchive.org/en/2021/jamstack#which-ssgs-are-the-most-popular%20target=) whose usage is actually detectable.

* The median JS size for React-based Gatsby and Next.js and Vue-based Nuxt.js all stand at around 700 KB. This number is similar to the median for React and Vue in general.
* Compared to that, Go-based Hugo and Ruby-based Jekyll stand at 177 KB and 129 KB respectively.
* JS framework-based SSGs serve a median of over 500 KB of JS more than those not based in JS.

And since we mentioned that JS size is not everything in terms of performance, let’s look at the difference between CWV scores for mobile sites.

* Next.js and Nuxt.js have good CWV scores less than 15% of the time.
* Gatsby stands higher than fellow React-based Next.js at 21.9%.
* Non-framework-based Hugo and Jekyll have good CWV scores 31.8% and 34.3% of the time respectively.
* SSGs not using JS frameworks have better percentage of CWV scores than the overall average.

#### Comparing framework performance in lab tests

So far, we’ve looked at the usage data for the three most popular frameworks and compared their performance. However, there are many other frameworks besides these three. With that in mind, let’s compare those three with some other frameworks that might not be used enough to show up in the Web Almanac but are among the most popular ones.

Note:

* The data for these comparisons come from lab tests, performance might be different when used in actual projects.
* The frameworks added to the comparison are some that the author judged to be among those that have most momentum. You can see comparisons to other frameworks by going to the data sources for each comparison.

The table above compares frameworks to a hand-optimized vanilla JS implementation in three main categories: DOM Manipulation, Startup, and Memory Allocation. In it we can observe the following:

* React and Angular perform twice as bad as Vanilla JS on average.
* In contrast, Vue actually stands closer to Preact and Stencil at an average of 1.5 times. The main reason for the difference between this result and what we saw reported in the Web Almanac might be due to the performance improvements Vue had when version 3.0 released.
* And finally, Solid, Lit, and Svelte are all at around 1.2 times. They all perform very close to the Vanilla JS version.

Something that’s clearly influencing these results is IE. You might ask, “Why mention IE?” And for that we have to take a look at the history of both frameworks and the JS standards in general.

You can say that Edge’s release in 2015 was the point where new development for IE stopped for the most part. That year was also the year the ES 2015 (or ES6) standard came out; which was arguably the biggest revolution in JS history. ES 2015 included features such as promises and arrow functions. Later versions began adding even more features to JS that can achieve more things with less code. In other words, things developed for a pre-ES 2015 world differ greatly from those developed for ES 2015 forwards.

In the table above, the worst in terms of performance are Angular and React. These two, together with Vue, are the only frameworks on the table that had their first release before 2015. In other words, the performance difference can be attributed to the era they were developed in. The reason why this rule doesn’t seem to apply to Vue is because, as mentioned above, Vue 3.0 changed a lot of internal code in order to improve performance.

There’s one more way to fully understand the difference mentioned above: comparing Solid, Preact, and React. Solid and Preact are heavily influenced by React. In Preact’s case, they even have a compatibility module to use React code as Preact code. But looking at the table, Solid and Preact outperform React in every single parameter. This means that React’s performance problems don’t lie in its philosophy or the way you write code for React. They lie in React’s internals. To be precise, in React’s Virtual DOM and synthetic event system implementation, both of which have many considerations needed for IE. Preact and Solid instead prefer default to using APIs available in modern browsers. This might be the biggest reason for the performance deficit.

Finally, let’s take a look at one more chart.

This chart compares most of the aforementioned frameworks in a different metric: the bundle size when creating 30 components with the same framework. This comparison allows us to emulate how these frameworks would work when creating a full application with them.

* React ends up being the biggest again at 45.45 KB, but in terms of actual developer code it’s the smallest at 9.26 KB. It’s just that the library itself is a few times bigger than the rest.
* Vue did make a lot of improvements in version 3.0 but it still ends up being about twice as big as other libraries at 32.65 KB.
* The rest of the frameworks might differ in terms of how much developer code and library code is bundled, but they all end up having similar sizes in the 14-18 KB range.

## Accessibility

We’ve talked a lot about our users’ devices, but let’s now talk about the users themselves. According to the World Health Organization, [over 1 billion persons have some kind of disability](https://www.who.int/news-room/fact-sheets/detail/disability-and-health%20target=). There are many different kinds of disabilities but many of them influence how the user will interact with their devices. We usually use the term accessibility (a11y) to refer the actions needed to ensure disabled users can fully interact with our sites.

However, a11y is not only for disabled people. Actions to improve a11y have a positive impact on the UX for every user. The main reason for this is due to situational disabilities. Some examples of situational disabilities include trying to use your phone while eating or drinking something with one hand or device settings that places a black and white filter on the screen after a certain hour to improve sleep quality. Users faced with these situational disabilities will be able to use pages which are designed with a11y in mind as usual.

Moreover, not being accessible can also lead to legal problems. Depending on the legislation, users may even sue sites that don’t take a11y in account. Some famous cases include [both Beyonce and Domino’s Pizza being sued for not being accessible for visually impaired users](https://www.forbes.com/sites/jackgarson/2020/02/25/popstar-to-pizza-to-porn-complying-with-the-ada-in-the-digital-age/?sh=549f4a2d182c%20target=). So, not having proper a11y can be costly too.

### How accessible is the web?

Let’s now take a look at how accessible is the web. To do that, we’ll take out some representative data from the [Web Almanac’s a11y](https://almanac.httparchive.org/en/2021/accessibility%20target=) chapter. There are many more data points in there in case you want to take a deeper look.

* **77.8%** of sites don’t have good contrast between background and font color. This means, that some visually impaired users and users using filters such as the one mentioned above may not be able to fully use almost 80% of the web.
* **29.4%** of sites block zooming. Some browsers ignore this setting nowadays but this is still a very big number.
* **42%** of sites have improperly ordered headings. Cases such as using an `h2` element without using an `h1` element before. This lack of order might cause problems, especially for users using assistive technology.
* **29%** of sites use `role="button"`. Some people might think that having that role and a click listener might be enough, but buttons must also respond to keyboard events and have proper focus handling. While you might achieve this using JS, you don’t need JS at all if you just use the `button` element.
* **32.7%** of sites have `input` elements with no accessible label. In other words, they don’t have an associated `label` element, an `aria-label` attribute, or anything else. This is worrying because you might be losing revenue due to this. For example, if a credit card input isn’t labelled, you might have users that want to buy something but don’t know where to write the information needed.

## Conclusion

Let’s look at the report card.

* We’re not answering to the users’ needs: Especially in terms of performance and a11y.
* We’re overusing JS: Both in our dependencies and in our own code.
* We’re underusing HTML and CSS: This is partly due to IE support, but now that we don’t need to support IE there are many features that become usable.

Here are a few overall tips for people who want a starting point on how to improve:

* If you can do something using **CSS** use CSS: There are many things that previously were only achievable using JS that can be done with only CSS nowadays. By doing that you can partly reduce your JS code.
* Evaluate your **toolset**: Many newer tools have better performance baselines compared to older ones, and not every project needs to be an SPA. Some of the non-framework-based SSGs like Hugo, Jekyll, or 11ty work great for those use cases.
* Build for **modern** **browsers**: Drop IE support and set your build target to ES 2017 or even 2018. Just doing that might get you bundle size improvements of up to 20%.
* Consider **a11y** from the beginning: Having a11y in mind from the planning and design stages is the ideal scenario. Starting by improving things such as contrast rates, font sizes, semantic HTML usage, and keyboard navigation can make a great difference.

[#CSS](https://engineering.linecorp.com/en/blog/tag/css-2/) [#frontend](https://engineering.linecorp.com/en/blog/tag/frontend-en/) [#JavaScript](https://engineering.linecorp.com/en/blog/tag/javascript-en/) [#UIT](https://engineering.linecorp.com/en/blog/tag/uit/)