---
title: 'DevEx Principles: Minimize Switching Contexts'
date: '2023-02-12T11:00:36-07:00'
format: link
service: instapaper
tags:
- read
external_url: https://kathykorevec.substack.com/p/devex-principles-minimize-switching
---

[DevEx Principles: Minimize Switching Contexts](https://kathykorevec.substack.com/p/devex-principles-minimize-switching)  



Recently someone asked me what my principles are for DevEx. Over the past 15 years shipping products for Heroku, GitHub, and now Vercel, I’ve learned a lot about what developers need to succeed. Still, I’ve never documented the principles I use daily to build developer tools, so I’ve decided to write it all down.

1. Interruptions matter even when it’s your tools that are doing it.
2. Respect the craft. The bar is higher because you’re building products for people who build products.
3. **Automate anything that can be automated:** Automation is king. Any task that can be run in the background should.
4. **Optimize for TTC (time to code):** Just as artists need to see paint on canvas in order to keep creating, developers need to see code running in order to test, get feedback, and ship.
5. **Be dependable:** Be mindful of breaking changes. People’s services depend on your services.
6. **Don’t bury the lede:** Show me what is possible and why it matters. Don’t hide pricing, don’t use convoluted marketing language, and don’t hide the documentation.

I’ll talk about each principle in detail over the next five posts. Minimizing switching contexts is the first and perhaps the most important, and I consider all of them when designing and building any new developer-focused product.

### Minimize switching contexts

[![](https://substackcdn.com/image/fetch/w_424%2Cc_limit%2Cf_auto%2Cq_auto:good%2Cfl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F806dbbe2-344c-40fc-9f14-9afd307bbae5_1058x1054.png)![](https://substackcdn.com/image/fetch/w_424%2Cc_limit%2Cf_auto%2Cq_auto:good%2Cfl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F806dbbe2-344c-40fc-9f14-9afd307bbae5_1058x1054.png)](https://substackcdn.com/image/fetch/f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F806dbbe2-344c-40fc-9f14-9afd307bbae5_1058x1054.png)

The key to building excellent tools for developers is understanding how often they have to switch contexts and how detrimental that can be to developer productivity and happiness. Developers interface with four main tools—an IDE, a console, a DVCS (distributed version control system), and documentation. When they need to use tools, build systems, a library or framework, or external documentation outside these four primary interfaces, their flow can be easily broken. I’ve seen many developer tools come to market that seem to rush to creating a website, whereas a plugin is much more appropriate.

The great thing is many of these developer interfaces are open to third-party plugins and extensions. For example, VSCode has [thousands of extensions](https://marketplace.visualstudio.com/vscode) offering vast amounts of customization. The hugely popular [GitHub Copilot](https://github.com/features/copilot) exists entirely within a third-party IDE. Vercel CD runs within the DVCS. There is quite a bit of flexibility on building rich featured products within existing developer tools. Don’t feel like you need to create a web interface to do that.

The more powerful you can make existing tools, the more effective you’ll make the developer. Intrinsically, developers know that minimizing context switching is the key to productivity. While there’s an opportunity to do more research on the effects of switching contexts, [this study](https://scholar.google.co.uk/citations?view_op=view_citation&hl=en&user=C5eTGe8AAAAJ&citation_for_view=C5eTGe8AAAAJ:maZDTaKrznsC) shows that “it takes an average of 23 minutes to fully mentally return to a task after an interruption.” That’s a lot of mental energy, and productivity lost throughout the day to constant context switches and interruptions.

### Why does it matter?

It all comes down to respecting your developer’s time. Don’t make them jump through hoops to use your product, “even minor context shifts are productivity poison.” 

[1](https://kathykorevec.substack.com/p/devex-principles-minimize-switching#footnote-1-99723243)

Developers know their tools best and are likelier to stay in the flow when using them efficiently. We all are skeptical of the n+1 tool. In fact, “interruptions are more disruptive than we think — and affect more than just our work. With minimal or no interruptions, developers had an 82% chance of having [a good day](https://github.blog/2021-05-25-octoverse-spotlight-good-day-project/), but when developers were interrupted the majority of the day, their chances of having a good day dropped to just 7%.” 

[2](https://kathykorevec.substack.com/p/devex-principles-minimize-switching#footnote-2-99723243)

Solve this by bridging the gap between what you provide and the environment where developers already work. For example, when we were building Vercel Comments, we decided to integrate notifications into Slack as well as GitHub and GitLab because these tools are what developers are already using to collaborate. This allowed us to minimize context switching and interruptions.

### What happens next?

In the future, we won’t be talking about one or two significant products that reduce context switching. Instead, the magic will be in the features that are thoughtfully automated or are powered by AI and weave intelligence throughout the workflow that will help developers stay in the flow the most. Our tools will get even more powerful. When you’re building a new website, you’ll soon be able to ask your favorite LLM to style it like Apple utilizing your favorite CSS framework and have AI create the database schema and test data. From your editor, AI will handle writing the code, opening a PR, and even do a first pass review. Developers will be able to change the entire look and feel of their app without ever switching apps.

AI is starting to democratize developer tools. We are moving development more and more towards AI as an abstraction layer to coding. Writing functions, interfacing with build systems, setting up architectures, will all feel magical, especially to people who are new to software development. It’s an exciting time to build developer tools. There are no shortages of problems to solve. By following good dx we can get there faster.

[![](https://substackcdn.com/image/fetch/w_424%2Cc_limit%2Cf_auto%2Cq_auto:good%2Cfl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F02fcc2c2-97df-49e7-b027-68778f443e80_1348x1316.png)![](https://substackcdn.com/image/fetch/w_424%2Cc_limit%2Cf_auto%2Cq_auto:good%2Cfl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F02fcc2c2-97df-49e7-b027-68778f443e80_1348x1316.png)](https://substackcdn.com/image/fetch/f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F02fcc2c2-97df-49e7-b027-68778f443e80_1348x1316.png)
### Stay tuned for more!

1. **[Minimize switching contexts](https://kathykorevec.substack.com/p/devex-principles-minimize-switching)**
2. **[Remember, you are a chef cooking for chefs](https://kathykorevec.substack.com/p/devex-principles-chef-cooking-for)**
3. **Automate anything that can be automated**
4. **Optimize for TTC (time to code)**
5. **Be dependable**
6. **Don’t bury the lede**

[1](https://kathykorevec.substack.com/p/devex-principles-minimize-switching#footnote-anchor-1-99723243)

https://www.nytimes.com/interactive/2023/01/23/magazine/cal-newport-interview.html



[2](https://kathykorevec.substack.com/p/devex-principles-minimize-switching#footnote-anchor-2-99723243)
> [Octoverse Spotlight 2021: The Good Day Project—Personal analytics to make your work days better](https://github.blog/2021-05-25-octoverse-spotlight-good-day-project/)

All images generated with Midjourney.