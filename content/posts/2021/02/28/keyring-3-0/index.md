---
title: Keyring 3.0
date: '2021-02-28T13:16:27-07:00'
service: jetpack
tags:
- keyring
- wordpress
categories:
- posts
---

Well it’s been a while, but I’ve just pushed a [3.0 release](https://github.com/beaulebens/keyring/releases/tag/v3.0) of [Keyring](https://dentedreality.com.au/projects/wp-keyring/).

> Keyring is a generalized framework for WordPress which handles authentication with, and authenticated requests to remote services. It provides a set of predefined “Services” which describe how to communicate with a collection of popular platforms, and also makes it easy for you to plug into that framework and define your own Services for other systems.

This version includes a bunch of improvements and compatibility updates, including all sorts of contributions from other folks. There are a lot of fixes and tweaks that have come back into the project as part of it being used on WordPress.com, and as part of the hiring process at Automattic.

[Download the latest Keyring](https://wordpress.org/plugins/keyring/)

Here’s the full changelog:

* **CHANGE: Default branch has been renamed to `trunk` to match WordPress projects. [Update your refs](https://docs.github.com/en/github/administering-a-repository/renaming-a-branch).**
* Enhancement: **BREAKING**: Removed delicious service (they have shut down completely). Props [@sanmai](https://github.com/sanmai).
* Enhancement: **BREAKING**: LinkedIn now uses OAuth2. Props [@glendaviesnz](https://github.com/glendaviesnz).
* Enhancement: `fetch_profile_picture` method added to Twitter service. Props [@glendaviesnz](https://github.com/glendaviesnz).
* Enhancement: Added a GitHub Service definition, props [@alperakgun](https://github.com/alperakgun).
* Enhancement: Added a Google Drive Service definition, props [@scruffian](https://github.com/scruffian).
* Enhancement: Trim spaces off API keys etc to avoid mistakes when copy/pasting. Props [@kbrown9](https://github.com/kbrown9).
* Enhancement: Allow all 2xx response codes to be considered “Success” for all requests, for all protocols. Props [@bgrgicak](https://github.com/bgrgicak) for the proposal.
* Enhancement: Add translator comments. Props [@scruffian](https://github.com/scruffian).
* Enhancement: Define the `self` endpoint for Tumblr, and add helper methods to retrieve user info. Props [@glendaviesnz](https://github.com/glendaviesnz).
* Enhancement: Add a `keyring_{service}_request_scope` filter for OAuth2 services, matching the existing filter for OAuth1 services. Props [@glendaviesnz](https://github.com/glendaviesnz).
* Enhancement: Add a `'full_response'` param to `Keyring_Service_OAuth2::request()`, which will cause the method to return the full HTTP response object. Props [@glendaviesnz](https://github.com/glendaviesnz).
* Enhancement: Some services (looking at you, Strava) seem to double-encode redirect URIs, resulting in “corrupted” parameter names. Added a method to clean that up.
* Bugfix: Make the Google services always request a refresh token for offline access. Props [@kbrown9](https://github.com/kbrown9) and [@atrniv](https://github.com/atrniv) for input.
* Bugfix: Update Strava to use refresh tokens and offline access, per their new API requirements. Props [@mdrovdahl](https://github.com/mdrovdahl) for pointing it out.
* Bugfix: Update use of add\_submenu\_page() to comply with WP 5.3. Props @jhwwp (wp.org) for the fix.
* Bugfix: Apply the keyring\_access\_token filter consistently in Google Services. Props [@pablinos](https://github.com/pablinos).
* Bugfix: Use static “Cancel” URIs in UIs. Props [@pgl](https://github.com/pgl).
* Bugfix: Remove some WordPress.com-specific code from Eventbrite.
* Bugfix: Ensure that `PUT` requests have a `Content-Length` header set. Props [@glendaviesnz](https://github.com/glendaviesnz).
* Bugfix: Compatibility with more recent versions of PHP7, and PHP8.
* Bugfix: Apply keyring\_access\_token filter properly in Instapaper.
* Bugfix: Remove redunant `is_service` check (enforced via method call signature). Props [@sanmai](https://github.com/sanmai).
* Bugfix: Remove hover event on action links in Service listing UI.