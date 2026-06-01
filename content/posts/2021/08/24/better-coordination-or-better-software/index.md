---
title: Better Coordination, or Better Software?
date: '2021-08-24T22:53:18-06:00'
format: link
service: instapaper
tags:
- read
external_url: https://jessitron.com/2021/08/02/better-coordination-or-better-software/
---

[Better Coordination, or Better Software?](https://jessitron.com/2021/08/02/better-coordination-or-better-software/)  



**TL;DR**: *When different parts of an organization need to coordinate, it seems like a good idea to help them coordinate smoothly and frequently. Don’t. Help them coordinate less — more explicitly, less often.*

Software systems get big, and they have lots of parts, and those parts need to talk to each other. Maybe we’re building a new customer portal, and the new web services need to talk with existing CRM, and with warehouse systems for returns, and with invoicing. The software crosses organizational boundaries.

If the software is going to talk to each other, the teams need to talk to each other. The new services need changes new APIs from the warehouse and from invoicing. Maybe there’s some customization going on in the CRM too. All of these need coordination.

## How can we make this coordination easier? (This seems like the question to ask.)

I know, let’s move all the departments to the same tracking tool! Everyone will use JIRA. That way we can roll up all the changes to one place, and warehousing and invoicing and the new customer portal teams can all see each others’ status.

This visibility enables deeper coupling. Now we have dependencies between individual tasks in completely different departments. Now everyone needs to keep up with everyone. So many project managers are so busy tracking everything! Every task can affect people across the company.

![](image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)![](image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

Within departments, various teams have essential coupling between the software systems they write. Enabling task-level coordination creates coupling on individual work items within teams. So much coordination! So many handoffs!

By making coordination easier, we enable more of it. This leads to optimizations like: the portal teams can do less coding if we wait to write the call to the warehouse until after the service is complete. And then CRM changes can wait on our change, which is waiting on something else — the coordination work balloons.

But coordination isn’t the work we wanted to do! We wanted to build software.

## Try this: instead of making coordination easier, imagine that it is really expensive. How would we do less?

To minimize coordination, establish boundaries and the few interfaces that cross them. Work carefully on those interfaces: document them thoroughly, and test on both sides. Change them sparingly and with effort: versioning, backwards compatibility, gradual deprecation.

Instead of asking when the other side of the boundary will be ready, assume we can’t know. Write contract tests, translation layers, and custom fakes for testing.

Treat the other department more like another company, like Software as a Service, where we can’t control their schedules. Where we can’t access their tracking tools.

Communicate heavily around the content of the interface. And nowhere else. This lets the departments work separately.

![](image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)![](image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

A strong boundary is like an extra component. It takes more work, but that work stays within the department, not across. There’s no task-level entanglement. Each team proceeds at its pace.

While some production releases may wait for all the components to be delivered, none of the components’ development is waiting on each other. That makes this *faster* than the highly-coordinated, tightly-coupled release. When difficulty increases with size (such as in software systems), [several smaller systems can work more effectively than one larger system](https://jessitron.com/2021/01/18/when-costs-are-nonlinear-keep-it-small/).

## This decoupling requires more work on the software.

It’s faster, but is it cheaper? This takes more work: writing tests and fakes, architecting ports and adapters, changing those adapters when our first guess at the interface was wrong. It takes more building software.

That isn’t the work we wanted to do! We wanted to build software — oh wait.

## The extra work to make clear boundaries makes better software.

The extra work of coordination only makes it take longer.

When we change the system later, strong boundaries make those changes faster. Deep coordination makes those changes harder: the tight coupling still exists but the armies have moved on, the armies of project managers who heroically held together that initial release.

The coordination is really expensive, too. More managers. Plus, software developers sitting on coordination calls, struggling to test, and waiting for dependencies are expensive (and unhappy).

Making coordination smoother increases coupling, requiring more coordination. The alternative is spending development effort on healthy boundaries. You can pay for better coordination, or better software.

## Don’t unify tracking tools. Don’t make coordination smoother. Make delivery smoother! by strengthening boundaries.