---
title: OOPS Writeups
date: '2021-11-28T17:22:57-07:00'
format: link
service: instapaper
tags:
- read
external_url: https://surfingcomplexity.blog/2021/11/21/oops-writeups/
---

[OOPS Writeups](https://surfingcomplexity.blog/2021/11/21/oops-writeups/)  



A couple of people have asked me to share how I structure my [OOPS](https://www.learningfromincidents.io/blog/oops-learning-from-the-incident-you-didnt-have) write-ups. Here’s what they look like when I write them. This structure in this post is based on the OOPS template that has evolved over time inside of Netflix, with contributions from current and former members of the CORE team.

My personal outline looks like this (the bold sections are the ones that I include in every writeup)

* **Title**
* **Executive summary**
* Background
* **Narrative description**
  + Prologue
  + The trigger
  + Impact
  + Epilogue
* Contributors/enablers
* Mitigators
* Risks
* Challenges in handling

## Title: OOPS-NNN: How we got here

Every OOPS I write up has the same title, “how we got here”. However, the name of the Google doc itself (different from the title) is a one-line summary, for example: “*Server groups stuck in ‘deploying’ state”*.

## Executive summary

I start each write-up with a summary section that’s around three paragraphs. I usually try to capture:

* When it happened
* The impact
* Explanation of the failure mode
* Aspects about this incident that were particularly difficult

*On <date>, from <start time> to <end time>, users were unable to <symptom>* 

*The failure mode was triggered by an unintended change in <service> that led to <surprising behavior>.*

*The issue was made more difficult to diagnose/remediate due to a number of factors:*

* *<first factor>*
* *<second factor>*
* …

I’ll sometimes put the trigger in the summary, as in the example above. It’s important not to think of the trigger as the “root cause”. For example, if an incident involves TLS certificates expiring, then the trigger is the passage of time. I talk more about the trigger in the “narrative description” section below.

## Background

It’s almost always the case that the reader will need to have some technical knowledge about the system in order to make sense of the incident. I often put in a background section where I provide just enough technical details to help the reader understand the rest of the writeup. Here’s an example background section:

*Managed Delivery (MD) supports a GitOps-style workflow. For apps that are on Managed Delivery, engineers can make delivery-related changes to the app by editing a file in their app’s Stash repository called the delivery config.* 

*To support this workflow, Managed Delivery must be able to identify when a new commit has happened to the default branch of a managed app, and read the delivery config associated with that commit.*

*The initial implementation of this functionality used a custom Spinnaker pipeline for doing these imports. When an application was onboarded to Managed Delivery, newt would create a special pipeline named import-delivery-config. This pipeline was triggered by commits to the default branch, and would execute a custom pipeline stage that would retrieve the delivery config from Stash and push it to **keel**, the service that powers Managed Delivery.*

 *This solution, while functional, was inelegant: it exposed an implementation detail of Managed Delivery to end-users, and made it more difficult for users to identify import errors. A better solution would be to have **keel** identify when commits happen to the repositories of managed apps and import the delivery config directly. This solution was implemented recently, and all apps previously using pipelines were automatically migrated to the native git integration. As will be revealed in the narrative, an unexpected interaction involving the native git integration functionality contributed to this OOPS.*

## Narrative description

The narrative is the heart of the writeup. If I don’t have enough time to do a complete writeup, then I will just do an executive summary and a narrative description, and skip all of the other sections.

Since the narrative description is often quite long (over ten pages, sometimes many more), I break it up into sections and sub-sections. I typically use the following top-level sections.

* Prologue
* The trigger
* Impact
* Epilogue

### Prologue

In every OOPS I’ve ever written up, implementation decisions and changes that happen well before the incident play a key role in understanding how the system got into a dangerous state. I use the *Prologue* section to document these, as well as describing how those decisions were reasonable when they happened.

I break the prologue up into subsections, and I include timeline information in the subsection headers. Here are some examples of prologue subsection headers I’ve used (note: these are from different OOPS writeups).

* *New apps with delivery configs, but aren’t on MD (5 months before impact)*
* *Implementing the git integration (4 months before impact)*
* *Always using the latest version of a platform library* (*4 months before impact*)
* *A successful <foo> plugin deployment test* *(8 days before impact)*
* *A weekend fix is deployed to staging (4 days before impact)*
* *Migrating existing apps (3-4 days before impact)*
* *A dependency update eludes dependency locking (1 day before impact)*

I often use foreshadowing in my prologue section writeups. Her are some examples:

*It will be several months before keel launches its first **Titus Run Job** orca task. Until one of those new tasks fails, nobody will know that a query against orca for task status can return a payload that keel is incapable of deserializing.*

*The scope of the query in step 2 above will eventually interact with another part of the system, which will broaden the blast radius of the operational surprise. But that won’t happen for another five months.*

*Unknown at the time, this PR introduced two bugs:*  
*1. <description of first bug>  
2. <description of second bug>  
Note that the first bug masks the second. The first bug will become apparent as soon as the code is deployed to production, which will happen in three days. The second bug will lay unnoticed for eleven days.*

### The trigger

The “trigger” section is the shortest one, but I like to have it as a separate section because it acts as what my colleague J. Paul Reed calls a “pivot point”, a crucial moment in the story of the incident. This section should describe how the system transitions into a state where there is actual customer impact. I usually end the trigger section with some text in red that describes the hazardous state that the system is now in.

Here’s an example of a trigger section:

***Trigger: a submitted delivery config***

*On <date>, at <time>, <name> commits a change to their delivery config that populates the artifacts section. With the delivery config now complete, they submit it to Spinnaker, then point their browser at the environments view of the <app> app, where they can observe Spinnaker manage the app’s deployment.*

*When <name> submits their delivery config, keel performs the following events:*

1. *receives the delivery config via REST API.*
2. *deserializes the delivery config from YAML into POJOs.*
3. *serializes the config into JSON objects.*
4. *writes the JSON objects to the database.*

**At this point, *keel* has entered a bad state: it has written JSON objects into the resource table that it will not be able to deserialize.** 

### Impact

The impact section is the longest part of the narrative: it covers everything from the trigger until the system has returned to a stable state. Like the prologue section, I chunk it into subsections. These act as little episodes to make it easier for the reader to follow what’s happening.

Here are examples of some titles for impact subsections I’ve used:

* *User reports access denied on unpin*
* *Pinning the library back*
* *Maybe it’s gate?*
* *Deploying the version with the library pinned back*
* *Let’s try rolling back staging*
* *Staging is good, let’s do prod*
* *Where did the <X> headers go?*
* *Rollback to main is complete*
* *We’re stable, but why did it break?*

For some incidents, I’ll annotate these headers with the timing, like I did in the prologue (e.g., *“45 minutes after impact”*).

Because so much of our incident coordination is over Slack these days, my impact section will typically have pasted screeenshots of Slack conversation snippets, interspersed with text. I’ll typically write some text that summarizes the interaction, and then paste a screenshot, e.g.:

*<name> notes something strange in keel’s gradle.properties: it has multiple version parameters where it should only have one:*

*[Slack screenshot here]*

The impact section is mostly written chronologically. However, because it is chunked into episodic subsections, sometimes it’s not strictly in chronological order. I try to emphasize the flow of the narrative over being completely faithful to the ordering of the events. The subsections often describe activities that are going on in parallel, and so describing the incident in the strict ordering of the events would be too difficult to follow.

### Epilogue

I’ll usually have an epilogue section that documents work done in the wake of the incident. I split this into subsections as well. An example of a subsection: *Fixing the dependency locking issue*

## Contributors/enablers

Here’s the guidance in the template for the contributors and enablers section:

*Various* ***contributors and enablers*** *create vulnerabilities that remain latent in the system (sometimes for long periods of time). Think of these as things that had to be true in order for the incident to take place, or somehow made it worse.*

This section is broken up into subsections, one subsection for each contributor. I typically write these at a very low-level of abstraction, where my colleague J. Paul Reed writes these at a higher level.

I think it’s useful to call the various contributors out explicitly because it brings home how complex the incident really was.

Here are some example subsection titles:

* *Violated assumptions about version strings*
* *Scope of SQL query*
* *Beans not scanned at startup after Titus refactor*
* *Incomplete TitusClusterSpecDeserializer*
* *Metadata field not populated for PublishedArtifact objects*
* *Resilience4J annotations and Kotlin suspend functions*
* *Transient errors immediately before deploying to staging*
* *Artifact versioning complexity*
* *Production pinned for several days*
* *No attempts to deploy to production for several days*
* *Three large-ish changes landed at about the same time*
* *Holidays and travel*
* *Alerts focus on keel errors and resource checks*

## Mitigators

The guidance we give looks like this:

*Which factors helped reduce the impact of this operational surprise?*

Like the contributors/enablers section, this is broken up into subsections. Here are some examples of subsection titles:

* *RADAR alerts caught several issues in staging*
* *<name> recognized Titus API refactor as a trigger for an issue in production*
* *<name> quickly diagnoses artifact metadata issue*
* *<name>’s hypothesis about transactions rolling back due to error*
* *<name> recognized query too broad*
* *<name> notices spike in actuations*

## Risks

Here’s the guidance for this section from the template:

*Risks are items (technical architecture or coordination/team related) that created danger in the system. Did the incident reveal any new risks or reinforce the danger of any known risks? (Avoid hindsight bias when describing risks.)*

The risks section is where I abstract up some of the contributors to identify higher-level patterns. Here are some example risk subsection titles:

* *Undesired mass actuation*
* *Maintaining two similar things in the codebase*
* *Problems with dynamic configuration that are only detectable at runtime*
* *Plugins that violate assumptions in the main codebase*
* *Not deploying to prod for a while*

## Challenges in handling

Here’s the guidance for this section from the template:

*Highlight the obstacles we had to overcome during handling. Was there anything particularly novel, confusing, or otherwise difficult to deal with? How did we figure out what to do? What decisions were made? (Capturing this can be helpful for teaching others how we troubleshoot and improvise).* 

*In particular, were there unproductive threads of action? Capture avenues that people explored and mitigations that were attempted that did not end up being fruitful.*

Sometimes it’s not clear what goes into a contributor and what goes into a challenge. You could put all of these into “contributors” and not write this section at all. However, I think it’s useful to call out what explicitly made the incident difficult to handle. Here are some example subsection headers:

* *Long time to diagnose and remediate*
* *Limited signals for making sense of underlying problem*
* *Error checking task status as red herring*

## Other sections

The template has some other sections (incident artifacts, follow-up items, timeline and links), but I often don’t include those in my own writeups. I’ll always do a timeline document as input for writing up the OOPS, and I will typically link it for reference, but I don’t expect anybody to read it. I don’t see the OOPS writeup as the right vehicle for tracking follow-up work, so I don’t put a section in it.