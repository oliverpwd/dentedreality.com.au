---
title: A new era of WordPress themes is finally here — Rich Tabor
date: '2022-03-30T23:11:11-06:00'
format: link
service: instapaper
tags:
- read
external_url: https://richtabor.com/a-new-era/
---

[A new era of WordPress themes is finally here — Rich Tabor](https://richtabor.com/a-new-era/)  



We all knew the landscape of [WordPress themes was shifting](https://richtabor.com/the-future-of-wordpress-themes/) with the introduction of Gutenberg.

What we didn’t know, was by how much.

With the arrival of the anticipated Full Site Editing experience into WordPress 5.9, themes are starting to look very different. This new class of block-based WordPress themes arguably introduces the biggest change to themes, since well… themes existed.

**These themes are built entirely with blocks.** That is, the headers, footers, blogroll, and page templates — literally every aspect of the theme. If it’s on the page, it’s a block.

A site running a block theme may not look any different on the front-end, but behind-the-scenes there are a number of key differences that hint at the future of WordPress: a future where site publishing happens in a block editor, not a code editor.

## What makes a block theme different?

There are four key differences between “classic” themes and this new class of theme. Block themes…

### 1. Built 100% with blocks

There are no PHP *template* files within block themes. They’re all straight HTML, with block content and comments. You can even create full block templates and export them to use on another site.

And then there are theme blocks.

![](https://cdn.richtabor.com/wp-content/uploads/2022/03/Frame-13-1024x683.png)![](https://cdn.richtabor.com/wp-content/uploads/2022/03/Frame-13-1024x683.png)

A look at theme blocks within the block editor

With the addition of “theme” blocks — that is, blocks that replace traditionally PHP-based functionality within a template — we can now build smart templates that fetch data, instead of requiring an input from the user adding the block.

### 2. No, or limited, CSS (theme.json)

The days of repeating gobs of CSS across themes is finally in our rear view. A block theme leans heavily on individual blocks for styling, instead of relying on a theme author’s unique custom CSS.

Now that doesn’t mean every block will look the same on every theme. Every block theme starts with the same structural styling provided by core WordPress, but can be customized quite a bit with the theme’s configuration theme.json file.

![](https://cdn.richtabor.com/wp-content/uploads/2022/03/block-themes-1024x683.jpg)![](https://cdn.richtabor.com/wp-content/uploads/2022/03/block-themes-1024x683.jpg)

Various block themes available on [WordPress.org](https://wordpress.org/themes/tags/full-site-editing/)

This not only leads to themes needing much less custom CSS, but also that people can more successfully switch between block themes – as the design components are *mostly* standardized between themes.

Now I don’t know for sure that we’ll get to a place where a block theme won’t need any custom CSS, but I like that as a goal to aim for. And with each subsequent WordPress release, we’ll get closer and closer to achieving that goal — as the core team and Gutenberg developers see more of what themes are doing.

### 3. Full Site Editing

By activating a block theme, you’re automatically opted into a new template editing experience, often referred to as [Full Site Editing](https://richtabor.com/full-site-editing/) – but formally called the Template editor within WordPress.

The Template editor lets you edit any [block template, or part](https://richtabor.com/gutenberg-block-templates/) (i.e. header and footer), provided by the theme.

![](https://cdn.richtabor.com/wp-content/uploads/2022/03/CleanShot-2022-03-29-at-12.07.18@2x-1024x729.png)![](https://cdn.richtabor.com/wp-content/uploads/2022/03/CleanShot-2022-03-29-at-12.07.18@2x-1024x729.png)

The Template editor, as seen on my blog

For example, as everything in a block theme is built with blocks, you can move your logo to the center of the header, add social links, change the header background color, and more. And if your theme has multiple header parts registered, you can swap between entirely different header variants. Too easy.

![](https://cdn.richtabor.com/wp-content/uploads/2022/03/CleanShot-2022-03-29-at-12.10.08@2x-1024x241.png)![](https://cdn.richtabor.com/wp-content/uploads/2022/03/CleanShot-2022-03-29-at-12.10.08@2x-1024x241.png)

Editing the header part of my blog

That’s just one flow of template editing, but this concept persists for other parts, like the site footer, and each block template as well *(i. e. home, archive, singular, page, etc*).

### 4. Style variants

The last key difference between block themes and classic themes, is the idea behind style variants. Within the Global Styles interface, they’re referred to as “Other Styles” and the idea behind these is just that — other style sets to apply to your site.

![](https://cdn.richtabor.com/wp-content/uploads/2022/02/wabi-dark-1024x683.jpg)![](https://cdn.richtabor.com/wp-content/uploads/2022/02/wabi-dark-1024x683.jpg)

These style variants are not CSS based, and are each driven by a single JSON file within a theme’s `/styles` directory.

Creating an alternate style can be as complex as changing the entire site’s vibe, or as simple as switching out the color palette. In either case, anything set within the theme’s top-level theme.json file, will be inherited within each style.

Let’s look at [my Wabi theme](https://richtabor.com/wabi/) for example, which I think is the first block theme on WordPress.org that supported style variants:

![](https://cdn.richtabor.com/wp-content/uploads/2022/02/wabi-block-theme-1-1024x683.jpg)![](https://cdn.richtabor.com/wp-content/uploads/2022/02/wabi-block-theme-1-1024x683.jpg)

I’ve included three alternate style variants, Aoi (*a blue, material-inspired color scheme*), Pinku (*a feminine palette, also inspired by material*), and Dark (*a luscious moody palette of the night*).

I’m honestly not changing much of the theme’s character, as I wanted to persist the design language between the styles. But if I wanted to, I could leverage this style variant concept to stretch Wabi to look and feel more minimal, or brutalist even, like this:

![](https://cdn.richtabor.com/wp-content/uploads/2022/03/wabi-minimal-1024x683.jpg)![](https://cdn.richtabor.com/wp-content/uploads/2022/03/wabi-minimal-1024x683.jpg)

Wabi, with a unique minimalist/brutalist style

**Style variants are certainly a game changer for block themes.** This concept is a huge advantage over classic themes, which require loads of heavy lifting to achieve a similar concept — I know because [I led the development on one of those](https://wordpress.org/themes/go/).

And for folks running a block theme, one click gets you an entirely different vibe for the site. That’s neat.

The concept of additional styles also begs the question of if we really need thousands of WordPress block themes… if one “theme” can be house any sort of design configuration with a single file…

I’ve tossed around the idea of a [parent theme within WordPress core](https://richtabor.com/the-future-of-wordpress-themes/) in the past — I’m not sure I’m 100% sold on it — but we’re getting to a point where we’re sort of crossing that line… at least where Gutenberg is *becoming* the default styles for every block theme.

I wonder if perhaps one day, instead of launching a new default block theme each year, core will add a new style for *the* default theme. 🤔

## The future of theme development

I’ve been writing a good bit on all the new block theme, Full Site Editing, and Block Editor concepts that have been landing quite speedily into WordPress.

In short, there are lots of changes — welcome changes for sure, but it’s a lot to grasp if you’re used to building classic themes.

In addition to these four key differences, block themes lean heavily on block patterns — which are groups of blocks that can be dropped in all at once. Patterns are a powerful concept that classic themes may leverage as well — if you’d like to lean in on patterns, I have [a guide on building patterns](https://richtabor.com/build-block-patterns/).

It’s more apparent than ever to me that the barriers of theme development are slowly becoming smaller and smaller. There may always be some level of technical skillset required to produce phenomenal block themes, but generally speaking designing, assembling and launching a theme has never been easier.

### Block theme development 🔥 tip

An important concept to grasp is that **when you do make changes to a template, or part, within the Template editor, those changes will immediately take precedence** over the theme’s bundled template files.

If you’re testing a custom theme of yours, you’ll first need to clear any customizations of a modified template or part, to see the theme’s assets loading directly. What I’ve personally found useful is to make my changes within the editor, then copy those blocks into my theme’s templates without saving the changes in the editor.

Creating block themes is very different flow than classic themes, but being able to configure a theme’s templates, then export/copy them into a proper theme package is exceptionally empowering to non-technical theme creators.

## Are you in?

The new era of WordPress themes is here, and it’s dominated by blocks. We knew this was coming, and now it’s landed.

So the question remains: are you in? Are you ready to jump into the latest WordPress has to offer, leaning into the future of WordPress with block themes? I, for one, sure am.

There are currently around 60 block themes available in the [WordPress themes directory](https://wordpress.org/themes/tags/full-site-editing/), give a few a spin and let me know what you think.

I’m also putting together a post of the more interesting and beautiful block themes I’ve found online. If you’ve launched a block theme, I’d love to check it out. [Find me on Twitter](https://twitter.com/richard_tabor).