---
title: Write Better Docs With a Product Thinking Mindset
date: '2022-08-01T22:35:47-06:00'
format: link
service: instapaper
tags:
- read
external_url: https://thisisimportant.net/2022/07/25/write-better-docs-with-a-product-thinking-mindset/
---

[Write Better Docs With a Product Thinking Mindset](https://thisisimportant.net/2022/07/25/write-better-docs-with-a-product-thinking-mindset/)  



I’ve frequently seen product thinking discussed in product management and user experience design contexts, but haven’t seen it applied to technical writing and documentation. And yet, by applying product thinking to documentation, we can write more useful, relevant, high quality documentation.

## What is product thinking?

Product management thought leader [Shreyas Doshi defines product thinking as follows in a Twitter thread](https://twitter.com/shreyas/status/1471650411341750273?utm_source=labnotes.org):

> “Product Thinking is about understanding motivations, conceiving solutions, simulating their effects, and picking a path based on the effects you want to create.”

![](https://lh4.googleusercontent.com/Ofq2I8Z8MUm3I1zE2XpR1BnpztIJtTd1XOyNyCIsXD6ZEYssodw7cae2MRErzmdOicfXsTzrnPnKu2iXTWe77vJgbHUUAW_eZ0szLvQiPm25DQLlZNjYoA_yQeeC8_rUhGEfIcKcEJGzAsSR67sRQMo)![](https://lh4.googleusercontent.com/Ofq2I8Z8MUm3I1zE2XpR1BnpztIJtTd1XOyNyCIsXD6ZEYssodw7cae2MRErzmdOicfXsTzrnPnKu2iXTWe77vJgbHUUAW_eZ0szLvQiPm25DQLlZNjYoA_yQeeC8_rUhGEfIcKcEJGzAsSR67sRQMo)

As a technical writer, I focus on user problems and the customer journey as a central part of my job, so it seems obvious to adopt product thinking for documentation. While I was working at Splunk, the documentation culture fostered a product thinking mindset, enshrined in the Splunk docs book, [The Product is Docs](https://www.amazon.com/Product-Docs-technical-documentation-development-ebook/dp/B085KHTV95).

Despite being immersed in that culture and caring deeply about helping users, I still found it easy to fall into a “just get it done” mindset, or what Doshi calls project thinking:

> “Project Thinking is about understanding expectations, formulating plans, marshaling resources, and coordinating actions to meet those expectations.”

![](https://lh4.googleusercontent.com/Q0i8rVtM6o27t3C6OptcawPfnbxHNVAbA8xmCcp-chK5MOZPXuAlAMQCK27VSS08haRuhkFIZPva36KZvsEZOB141Nvi1QzBj1pDEDsfO-dJZ2e5f4iv6q5IS3ZbTjXcHFU0-2KBxCWgtna9_4QQCjI)![](https://lh4.googleusercontent.com/Q0i8rVtM6o27t3C6OptcawPfnbxHNVAbA8xmCcp-chK5MOZPXuAlAMQCK27VSS08haRuhkFIZPva36KZvsEZOB141Nvi1QzBj1pDEDsfO-dJZ2e5f4iv6q5IS3ZbTjXcHFU0-2KBxCWgtna9_4QQCjI)

Where project thinking focuses on the steps and process for creating a product, product thinking focuses on the motivation for creating a product and the possible outcomes of that motivation.

## Why project thinking is pervasive in technical writing

Technical writers are often short on time and resources. Forced to keep track of multiple teams and projects, we often spend what energy we can on the priorities that seem most urgent. Even with sufficient resources and planning, time crunches still happen. With these limitations, it’s easy to focus solely on churning out documentation and just keeping up.

![](https://lh4.googleusercontent.com/_L5fV5RaQggg_qBZoeqX8bMNGQ5iF-mMJIf2R1rQhliPb5ggr7Nb6N89X6J40fapQk_CllPahUtWtgPIgOePkg8m58L4AcNxHuG-QGY8hI-Xcbvwc_VgFTvgrcv36eqhtiw-0E7lkMfaS0srkvx0jHw)![](https://lh4.googleusercontent.com/_L5fV5RaQggg_qBZoeqX8bMNGQ5iF-mMJIf2R1rQhliPb5ggr7Nb6N89X6J40fapQk_CllPahUtWtgPIgOePkg8m58L4AcNxHuG-QGY8hI-Xcbvwc_VgFTvgrcv36eqhtiw-0E7lkMfaS0srkvx0jHw)

Sprinting alongside engineers, we often adopt engineering practices like breaking our work down into small parts, writing tickets and adding them to sprints to track with developers. With the widespread adoption of CI/CD pipelines in product development, these practices seep further into our documentation processes.

It feels like an optimization shortcut to consider documentation projects in terms of “feature coverage”, much like how quality assurance projects are considered in terms of “test coverage”. Documentation can become another box to tick, making sure that every pull request deployed has sufficient test coverage and documentation coverage for the product functionality.

This “coverage” mindset is ruled by project thinking. What if we took a product thinking approach?

## Project thinking vs Product thinking

While project thinking leads us to write documentation that ensures coverage a specific product feature, product thinking helps us focus on what needs to be written and why. Embracing product thinking lets us write higher quality documentation that is more relevant to customers.

That probably seems too good to be true, so let’s look at a specific example—a product making changes to the API endpoints available to developers as part of a versioning change.

### Project thinking for API endpoint deprecation

Taking a project thinking approach to the documentation might look like the following:

* documenting each new endpoint
* making sure each deprecated endpoint has a link to the relevant new endpoint

There might be also be a deprecation plan in the project that includes “Add a banner to the old endpoints with a link to the new endpoints indicating that they are deprecated and will be removed in the future”.

As a project thinker, this approach has the essentials:

**Expectations**Document the new API**Planning**Docs and engineering work together to produce updated documentation  
Provide deprecation information to users**Resources**Docs and engineering**Delivered Output**Documentation available with new API release and shared deprecation plan
![](https://lh5.googleusercontent.com/A7j4gVnnqRKR8YO9MwZxCMCweH8TgWUSMywRzgsuwwYeEhrF4nJRxGYLog5prLhhxZ_-cNrZsELttJCfhM5s9EpbvjjfjiQ1AcNfpuaA6Y7XRMmJG1IcbNZwliqgBGYct1se0nRLqsPEoQw8cIjjmyY)![](https://lh5.googleusercontent.com/A7j4gVnnqRKR8YO9MwZxCMCweH8TgWUSMywRzgsuwwYeEhrF4nJRxGYLog5prLhhxZ_-cNrZsELttJCfhM5s9EpbvjjfjiQ1AcNfpuaA6Y7XRMmJG1IcbNZwliqgBGYct1se0nRLqsPEoQw8cIjjmyY)

This approach focuses primarily on coverage for the new functionality, and offers some form of continuity for users using the old functionality by alerting them to the change.

### Product thinking for API endpoint deprecation

Taking a product thinking approach to the documentation might instead look like the following:

* As soon as you know API endpoints will be changing, write learning outcomes such as the following examples:
  + As a developer, after reading the API docs I can successfully update my code to use the new endpoints.
  + As a developer, after reading the API docs I am confident that I won’t lose any data and am correctly handling data formats sent by the new endpoints.
  + As a developer, after reading the API docs I can explain to my colleague who was on vacation which endpoints changed.
  + As a developer, I want to explain to my boss when I need to deploy my new script (when the API changes become permanent).
* Documenting each new endpoint.
* Making sure each deprecated endpoint has a link to the migration guide.
* Writing a guide for users of the v1 API to help them migrate to the v2 API, that addresses the specific learning outcomes you defined by including the following:
  + A note or caution that calls out any changes to data formats.
  + Specific code examples comparing API calls using the deprecated endpoints with the API calls using the equivalent new endpoints and parameters.
  + Clear dates or communication methods where developers can find out when the v1 API stops working.

From a product thinking perspective, this list of steps covers the essentials:

MotivationsIdentify the customer motivations by writing learning outcomesSolutionsMake a list of documentation options that address customer motivations.SimulationsWrite a migration guide and draft specific code examples to validate with engineering and product management.Desired OutcomesCustomer achieves business continuity and engineering can deprecate old API endpoints and stop maintaining the code. 
![](https://lh6.googleusercontent.com/V9KGaomUWsz3JycgZH2JSdOXKWx5bXdXqhoMQSJoVhGtRDaEouA6Eu8AHWaU4Pzz41lad6a07sZsx3Nseg2QrFz735ieEqHR9VJck7FpjhKi6jyH_nDvwuJHrUyQ0d5TBRXrd0C-zt5du8gir11yiUg)![](https://lh6.googleusercontent.com/V9KGaomUWsz3JycgZH2JSdOXKWx5bXdXqhoMQSJoVhGtRDaEouA6Eu8AHWaU4Pzz41lad6a07sZsx3Nseg2QrFz735ieEqHR9VJck7FpjhKi6jyH_nDvwuJHrUyQ0d5TBRXrd0C-zt5du8gir11yiUg)

This approach focuses primarily on customer outcomes, rather than optimizing for producing a specific type of documentation or specific output that can be checked off a plan.

### Comparing the results

If project thinking optimizes for coverage and output, product thinking optimizes for outcomes. The documentation written from a product thinking mindset seems like it’s a lot more detailed, but also slow and resource intensive to create. And it is.

But product thinking is only slow in the short term. If you focus on coverage (and output) instead of outcomes (and customer success), you might have complete documentation, but it’s not as useful to customers. Over time, you might not have many of those to worry about.

![](https://lh3.googleusercontent.com/QPJ2xFRsFtCJbUJVEQDzlE7TmcNa4p_-FXbj9jEEP7f8_57-PsDhtu3-3fdRPO0NlC7hMqk01oUMOOF-WXZ0YSLrB6n6pWHZbnXIw6utnwyBBT-X9E_8uEG79oty8vOKfJliyH2GaAN4bLdLnDf5ZIg)![](https://lh3.googleusercontent.com/QPJ2xFRsFtCJbUJVEQDzlE7TmcNa4p_-FXbj9jEEP7f8_57-PsDhtu3-3fdRPO0NlC7hMqk01oUMOOF-WXZ0YSLrB6n6pWHZbnXIw6utnwyBBT-X9E_8uEG79oty8vOKfJliyH2GaAN4bLdLnDf5ZIg)

I’m not advocating for abandoning project thinking entirely. We can’t neglect resource considerations or the content delivery timing of what we’re writing, especially if we’re working as lone writers. But just as it’s crucial to consider the timing of what we write, we need to consider the usefulness of what we write. Cultivating a product thinking mindset is essential to writing useful documentation.

## Applying product thinking to documentation

It’s easy to fall into the habit of being a “reactive” documentarian, responding to requests for information and rotely updating page after page after page with more information. As technical writers, our priority lists are often shifting or shuffling around. So how do you go about applying product thinking to your documentation?

Approach the documentation itself like a product.

[![](https://sarahkmoir.files.wordpress.com/2022/07/productthinkingdocs.png?w=1024)![](https://sarahkmoir.files.wordpress.com/2022/07/productthinkingdocs.png?w=1024)](https://sarahkmoir.files.wordpress.com/2022/07/productthinkingdocs.png)

Create cues in your writing process, get access to people with essential information, write learning outcomes for your documentation, consider the content design of your documentation, and test everything about your proposed changes!

### Create process cues

To make sure you don’t spend too much time on “getting the writing done”, add cues to your documentation process that can help you maintain user-centricity in your writing. What kind of cues? It depends on how you do your writing, but here are some that have worked for me:

**Follow a template for documentation tickets.** On one fast-paced development project, I made sure that every documentation ticket I filed included the following:

* the audience of the content
* the technical SMEs that knew more about the feature
* the learning outcome(s) for the content

If I couldn’t fill out those details, I knew I couldn’t work on the documentation request without producing poor quality content.

**Review and plan your work regularly.** On another project, I embraced the essentials of project thinking by spending some time on Friday afternoons reviewing what I’d accomplished in the last week and planning out my tasks for the following week. An output-focused approach that I combined with an outcomes-oriented approach by identifying the key product outcomes or customer goals associated with each documentation task I planned to work on.

### Get access to people

It’s impossible to write product-focused documentation with customer outcomes in mind if you don’t have the access to the product managers, engineers, and customers to understand and validate those outcomes.

Make sure you can talk to the product managers, engineers, and UX designers working on your product, but especially take steps to build relationships with sales and customer support representatives that interact directly with customers every day.

![](https://lh4.googleusercontent.com/iTl72XlipMDXTFXzAxFNpxypgq2xUUia2gga1q1tkvczBMAszIiCnb499yC06iF2Lmqrlj0JLTf_cE65ZutC36OM4G15qQBFXl1qgH7EqurIVM6B28UdEzcO2ZizzB2_WkM9xLlixp6M__TosVa7HFI)![](https://lh4.googleusercontent.com/iTl72XlipMDXTFXzAxFNpxypgq2xUUia2gga1q1tkvczBMAszIiCnb499yC06iF2Lmqrlj0JLTf_cE65ZutC36OM4G15qQBFXl1qgH7EqurIVM6B28UdEzcO2ZizzB2_WkM9xLlixp6M__TosVa7HFI)

With access to product experts and customer experts, you can more readily identify and validate the customer motivations driving the development of specific product functionality. This is especially crucial in an agile development environment, where the functionality that you’re documenting might only be a small building block of a larger solution, but in isolation it seems clunky and broken. For example, an incident management feature that adds the ability to store information about an incident, but neglects a status field to denote the state of the incident.

With a deep understanding of the *why* and *why now* behind product development decisions, you can structure and write your content in a way that accommodates customer goals alongside these possible product limitations. For example, you can write an incident management workflow that includes options for adding a status to an incident. In this way, you’re writing documentation that addresses the existing feature, the customer’s desired outcome, and leaves room to showcase future product functionality.

### Write learning outcomes

It’s crucial to understand the customer’s desired outcome when using a product. As the technical writer for a product, however, you also want to establish the customer’s outcomes when using your documentation.

When you write a learning outcome, you want to use active words and be specific. These aren’t abstract user stories, but rather concrete outcomes that customers can achieve.

Don’t write this:

* After reading the docs, I understand how to call the API.
* After reading the docs, I understand how to create an incident in the product.

Instead, be specific about the desired customer outcomes:

* After reading the docs, I can successfully update my code to call the new API endpoint
* After reading the docs, I can confidently create an incident based on a phone call from DevOps.

You need to write specific learning outcomes for your documentation so that your documentation can also be specific and useful to customers.

If you can’t write a compelling and specific learning outcome for a feature, several things could be true:

* You might not need to document it. If there aren’t any associated customer outcomes, it probably doesn’t need documentation.
* You might not understand the customer motivations well enough. Check in with product management and the technical SMEs for the feature to dig into why the feature is being added to the product to uncover the motivations driving development.

Writing learning outcomes for every piece of documentation you produce (including the small ones) helps shift you to a product thinking mindset and reminds you why your documentation is important.

### Consider content design

Another element of the product thinking mindset is considering new ideas. Content creation can feel routine and straightforward, but it involves design just as much as it involves writing.

Considering the content design of your writing can make your writing [more accessible](https://docs.splunk.com/Documentation/StyleGuide/current/StyleGuide/Overview), [more inclusive](https://docs.splunk.com/Documentation/StyleGuide/current/StyleGuide/Inclusivity), and more useful. If you include more headers or change paragraphs to a table or a list, your content is easier to scan and therefore more helpful to anyone easily bored, in a hurry, and with dyslexia and/or ADD.

You can also break up paragraphs with visuals such as diagrams or screenshots, with [helpful alt text](https://support.microsoft.com/en-us/office/everything-you-need-to-know-to-write-effective-alt-text-df98f884-ca3d-456c-807b-1a1fa82f5dc2), which can reinforce your content and provide extra learning opportunities for more visual learners.

In addition to adjusting the design of your text, you can also change how and where you present your content. Consider the following alternatives to text documentation:

* An interactive product tour
* A blog post
* A 2-3 minute video
* An interactive tutorial that uses a demo environment

For example, you could write a blog post to walk through incident management functionality in your product using a common IT incident or a security exploit from the news. This alternate form of content provides a tangible relevant example to customers in a dated blog post that you won’t have to keep updated.

### Test everything

To continue treating documentation like a product, you need to test out the decisions that you make along the way. Validate the product motivations you’ve identified, the customer learning outcomes you’ve defined, and take advantage of any and all testing options available to you.

* Get a review from technical SMEs about the accuracy of your content.
* Ask a peer for feedback on the presentation of your content, especially if you’re trying something new.
* Send your writing to get edited, if you have the luxury of access to an editor.
* Check your writing for style guide adherence and completion, using a tool like [Vale](https://github.com/errata-ai/vale) or similar. I’m guilty of publishing docs with broken links and unfinished sentences. Automated or manual checklists are crucial to make sure your work is finished.
* Perform UX testing on the content. If you restructured the information architecture, use [tree testing to test out the intuitiveness of your changes](https://www.nngroup.com/articles/tree-testing/).

With a product thinking mindset, you build a clear understanding of *why* you are documenting something. In the end, that clear understanding produces documentation that provides a valuable resource to customers and can even prove to be a differentiator from your competitors.

![](https://lh3.googleusercontent.com/KSKJ_u_292fKVXsHa4ryseS09MfKMff9bz1I4SO8vfDGKShy5uzRB_r-rAtFpEDFopjYTKuo0I4fYGogmRJMBWTpZkF1R8FcDPfC_7vewtUyYSkBjelV4Xyu48cDSoVISlvNIb-xGRl9BmAsVdLxAMk)![](https://lh3.googleusercontent.com/KSKJ_u_292fKVXsHa4ryseS09MfKMff9bz1I4SO8vfDGKShy5uzRB_r-rAtFpEDFopjYTKuo0I4fYGogmRJMBWTpZkF1R8FcDPfC_7vewtUyYSkBjelV4Xyu48cDSoVISlvNIb-xGRl9BmAsVdLxAMk)