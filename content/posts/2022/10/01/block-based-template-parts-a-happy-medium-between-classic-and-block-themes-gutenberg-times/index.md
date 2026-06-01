---
title: 'Block-Based Template Parts: A Happy Medium Between Classic and Block Themes
  – Gutenberg Times'
date: '2022-10-01T10:54:48-06:00'
format: link
service: instapaper
tags:
- read
external_url: https://gutenbergtimes.com/block-based-template-parts-for-classic-themes/
---

[Block-Based Template Parts: A Happy Medium Between Classic and Block Themes – Gutenberg Times](https://gutenbergtimes.com/block-based-template-parts-for-classic-themes/)  



I was one of the early adopters of the block editor as a developer. Despite the flak that the Gutenberg plugin was catching before it was merged into core WordPress, I could see the potential. Yes, I could see the bugs, the inconsistent UI, and every other thing that was “wrong” about it around four or five years ago.

But there was a vision for the future of theming that I latched onto.

At the time, there was a bit of a rumor floating around that theme authors would eventually be able to allow users to edit any part of their theme with the block editor. It’d work similarly to sidebars. Developers would register “block areas,” and users could drop whatever content they wanted in them.

That was *the* vision. It was the future of theming that I, along with several other developers, expected to see in the year or so following the block system’s launch in WordPress 5.0. It was a concept that sold us—*hook, line, and sinker*—on this newfangled editor all those years ago. It was such a simple but brilliant idea. We would finally consolidate some of the competing APIs, such as shortcodes and widgets, into a single standard. And themers would be dropping these block areas all over the place for highly-flexible themes.

Of course, not everything played out according to the timeline in my head. However, WordPress 6.1 is finally introducing this feature in the form of [block-based template parts](https://github.com/WordPress/gutenberg/pull/42729).

Frankly, I had nearly forgotten about it over time. I’ve already been firmly on block-theme wagon for well over a year, and the thought of going back and building a classic theme just to use this feature didn’t excite me quite as much as it once would have.

However, I still know that it is one of the most vital features for the theming community to land in WordPress. There are many reasons that developers have not made the full jump to block theming. It is not the ideal tool for every project yet, and that is an OK place to be. Whatever the reason, this is another tool for gradually adopting FSE features without going all in. It allows developers to retain control over their top-level, PHP-based templates and decide which specific areas they want to expose to users as block *capable*.

In some ways, block-based template parts may represent a stable medium for a while or even a new class of themes, those that are neither entirely classic nor block. It is the middle ground that the theming community has long needed.

Perhaps it will even put the [classic vs. block battle](https://masterwp.com/the-imaginary-block-vs-classic-battle-in-wordpress/) to rest, at least for the theming community. *Do themers really have to choose between being “all in” or “all out”?* No. No, they do not. Maybe that happy middle ground has been a long time coming, but it has been a priority for the project. We’ve seen that with the inclusion of block-based menus and widgets, theme-support additions, `theme.json` support, and now template parts.

## Putting Theory into Practice

I began drafting this post before I ever tested the feature out within an actual classic theme. It sounded like everything I wanted years ago, at least in theory, but a question remained. *Did it hold up in practice?*

The only way to find out was to grab a classic theme and convert part of its front-end output to a block-based template part. Fortunately, Twenty Twenty-One was already using PHP-based template parts, so it offered a starting point.

**Note:** This post is not a full tutorial on using block-based template parts in classic themes. I encourage readers who want to dig deeper into the technical aspects to read the [call for testing](https://make.wordpress.org/themes/2022/09/12/testing-and-feedback-for-using-block-based-template-parts-in-classic-themes/) on the Make Themes blog.

Most theme authors are aware of how template parts work in WordPress. Essentially, they are smaller templates (i.e., parts) that are included within larger ones. This can be anything from a header to footer or sidebar to comments form. There are no hard-and-fast rules, and the decisions about which parts exist come down to the theme authors themselves.

To use block-based template parts in classic themes, developers must add support for them via `functions.php`:

```
add_action( 'after_setup_theme', function() {
    add_theme_support( 'block-template-parts' );
} );Code language: JavaScript (javascript)
```

This creates a new “Template Parts” item under the “Appearance” admin menu:

![](image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)![](image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

Initial template parts screen when no parts are registered.

Out of the box, there will be nothing for users to do. However, once new parts are added, users will be able to edit them.

For my first true test of this feature, I decided to replace Twenty Twenty-One’s header template part. Headers are often the most complex pieces of a website design, so it will not be the ideal starting point for every theme author making this transition. However, I was pretty successful in replacing Twenty Twenty-One’s default header with a block-based version.

After adding support for `block-template-parts`, into the theme setup function in `functions.php`, I created a new `parts/header.html` file and proceeded to recreate the basic branding and navigation menu sections directly in the editor:

![](image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)![](image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

Recreating Twenty Twenty-One’s header as a block template part.

After getting the look I wanted (or, at least, close enough), I copied the block code from the editor into `parts/header.html` and deleted my customizations.

Then, in the theme’s `header.php` file, I replaced the following line of code with my own:

```
<?php get_template_part( 'template-parts/header/site-header' ); ?>Code language: HTML, XML (xml)
```

The new code was a call to the block-based template part, which would load the `parts/header.html` file (or the user-customized version):

```
<?php block_template_part( 'header' ); ?>Code language: HTML, XML (xml)
```

I would love to exclaim, “*Voila*!” and call it a day. I would love to say that this was a simple one-and-done action, but developers know it is never as straightforward as that. Most classic themes were not built to handle block output outside of the content area. Twenty Twenty-One is no different. I had to make some other changes to actually make this work.

The first thing was removing a max-width set by the Twenty Twenty-One’s `assets/css/style-editor.css` file that was keeping full-width blocks from stretching across the editor. So, I cut this bit of code from the file:

```
.wp-block {
    max-width: var(--responsive--aligndefault-width);
}Code language: CSS (css)
```

I also needed to add layout support via `theme.json`. Because the theme didn’t include this file, I created it and kept the settings as simple as possible using Twenty Twenty-One’s existing custom CSS properties:

```
{
    "version": 2,
    "settings": {
        "layout": {
            "contentSize": "var( --responsive--default-width )",
            "wideSize": "var( --responsive--alignwide-width )"
        }
    }
}Code language: JSON / JSON with Comments (json)
```

These were just quick fixes to ensure that the system worked. Each theme will be a bit different and each theme author will have some obstacles to overcome in development.

For a better user experience, I also defined my header template part via `theme.json`. This allowed me to create a internationalized version of its user-facing title. So, the final version of my JSON file became:

```
{
    "version": 2,
    "settings": {
        "layout": {
            "contentSize": "var( --responsive--default-width )",
            "wideSize": "var( --responsive--alignwide-width )"
        }
    },
    "templateParts": [
        {
            "name": "header",
            "title": "Header",
            "area": "header"
        }
    ]
}Code language: JSON / JSON with Comments (json)
```

This last bit is not a requirement, but it does create a better all-around experience. Theme authors shouldn’t skip it.

I’m not sure how well block-based template parts will truly work without also opting into some `theme.json` support. At minimum, layout settings are likely recommended. This is why it is vital that theme authors start testing before WordPress 6.1 launches. These little tips and tricks must become a part of our collective knowledge so that we can share and help one another.

## Was the Feature All That I Thought It Would Be?

Despite a couple of natural hiccups from having to change some style-related bits in the theme, it was a success. For good measure, I tested a few other template parts and felt good with the results. The process would have been much easier with one of my own themes, something I was intimately familiar with. However, I chose Twenty Twenty-One because it is more accessible to the WordPress extender community.

There are so many ways that themers can utilize this once WordPress 6.1 lands (or [you can start now using Beta 1](https://wordpress.org/news/2022/09/wordpress-6-1-beta-1-now-available/)). For example, an easy win is making an editable “404 page content” part. This is one of those areas that has long required developers to either build custom solutions for or just leave it to users to directly edit PHP files.

Theme authors can replace sidebars, headers, and footers. They can allow end-users to edit archive page queries. Or, go even more ambitious and create block-based template parts for everything but the outer structure of the front end. There are no right or wrong answers. Developers have the flexibility to choose the path that’s best for them and their users.