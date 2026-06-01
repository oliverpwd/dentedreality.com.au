---
title: An introduction to Wardley ‘Value Chain’ Mapping
date: '2019-07-26T05:53:27-06:00'
format: link
service: instapaper
tags:
- read
external_url: https://www.cio.co.uk/it-strategy/introduction-wardley-value-chain-mapping-3604565/
---

[An introduction to Wardley ‘Value Chain’ Mapping](https://www.cio.co.uk/it-strategy/introduction-wardley-value-chain-mapping-3604565/)  



![](https://www.cio.co.uk/cmsdata/features/3604565/Wardley_Mapping_08_thumb336.jpg)![](https://www.cio.co.uk/cmsdata/features/3604565/Wardley_Mapping_08_thumb336.jpg)  






This is about my journey, from a newly-minted yet confused CEO caught like a rabbit staring helpless into the oncoming headlights of change – to being voted one of the most influential people in IT within the UK. It took me a decade to first develop the techniques that I’m going to describe and a further 10 years to gain confidence with them through practice.

Every journey begins with a step, and in our case there were several. I’ll use an example throughout, and in this first foray I’m going to map a TV company that is part of a larger media conglomerate. I’ll be using an early draft, which took about two hours to develop, including the strategic play from a base understanding of nothing about the TV industry. The reason I’ve selected this example is because while it explains the process of mapping, anything of commercial value has long since left it and been exploited or discarded.

### Step 1. Focus on user needs

Critical to mapping is to first focus on what the user actually wants. There are various techniques for this from writing the press release to creating a user journey. In the case of the TV company, the users wanted to be entertained. There are two routes to satisfying this need; either through a branded online service that delivers the company’s programmes or through a content aggregator such as Netflix where the output from many TV companies is combined. Figure 1 below image shows the users’ needs.

![](https://www.cio.co.uk/cmsdata/features/3604565/Wardley_Mapping_01.jpg)![](https://www.cio.co.uk/cmsdata/features/3604565/Wardley_Mapping_01.jpg)

### Step 2. Create the value chain

Once you’ve determined the high level needs, the next step is to flesh this out with the components required to meet those needs. You do this by creating a chain of needs. I call this a ‘value chain’ because by meeting the needs of others, you hope to create value. At the top of any value chain should be the visible user need you are trying to serve and below this are the increasingly invisible (to the user) components that are necessary to serve those needs.



Figure 2 below provides a value chain for the TV company. In this diagram both branded and aggregator sites need content. That content needs a distribution mechanism (such as traditional media) but it also has to be created, which requires artistic direction. Naturally, artistic direction needs a creative studio to make the show but it also needs market analysis; for example, what sort of programs do people want to watch? And so the chain continues down to components such as compute and power.

![](https://www.cio.co.uk/cmsdata/features/3604565/Wardley_Mapping_02.jpg)![](https://www.cio.co.uk/cmsdata/features/3604565/Wardley_Mapping_02.jpg)

### Step 3. Create a map

Value chains on their own are practically useless for understanding an environment because they lack any form of context on how it is changing. If you think of a company such as Nokia, it started out as a paper mill, became a plastics manufacturer and then eventually a telecommunications company. During this time, its value chains radically altered. In order to understand an environment, we need to somehow capture this aspect of change and combine it with our value chain. The biggest problem is that the process of change and how things evolve cannot be measured over time. As uncomfortable as it is, you have to embrace the uncertainty of future change. Fortunately, there’s a neat trick because while evolution can’t be measured over time, it can be measured over certainty.

So, this is what you need to do. Take your value chain and plot the components along an evolution axis covering genesis, custom built, product (+rental) and commodity (+utility). This is what I’ve done in Figure 4 below for the TV company.

![](https://www.cio.co.uk/cmsdata/features/3604565/Wardley_Mapping_04.jpg)![](https://www.cio.co.uk/cmsdata/features/3604565/Wardley_Mapping_04.jpg)

All the components in the map are evolving from left to right due to supply and demand competition. As they evolve their characteristics change from an uncharted domain (the uncertain, rare and constantly changing) becoming more industrialised (the known, the common, the stable). For example, power supply is something commonplace and well understood. However, creative studios and the art of creating a TV show is less common and less well understood.



Once you have a map, examine it. In Figure 4, the content component of the TV company has an interesting distinction between creation and distribution; for example, there is a pipeline of content creation from commissioned shows to acquired formats along with separate distribution mechanisms such as traditional media and internet broadcast. To make this distinction more visible, you can add a pipeline to the map – see below (Figure 5).

![](https://www.cio.co.uk/cmsdata/features/3604565/Wardley_Mapping_05.jpg)![](https://www.cio.co.uk/cmsdata/features/3604565/Wardley_Mapping_05.jpg)

You now have something that you can start to discuss the environment in which a TV company operates.

### Step 4. Challenge

Three of the biggest issues within any organisation are bias, communication and duplication. Invariably when someone in a company tells me they want to build something such as a ‘rules engine’, then it doesn’t take long to discover at least half a dozen other projects building rules engines in the same company.

Duplication is rampant in most organisations because there is usually no means of effective communication within groups. Even if you do find another group that’s no guarantee they’ll want to work together – they tend to believe their rules engine is unique and different from everyone else’s. Everyone has bias.

One of the beautiful things about maps is that you can start to build up a portfolio of maps from different parts of the organisation and start to challenge this duplication and bias by sharing. Maps give you the communication mechanism to do this. When you start getting good at this, you can even challenge your own maps against the outside market and other competitors. The way that I normally do this is to start by aggregating maps; an example of which is given below in Figure 6.



![](https://www.cio.co.uk/cmsdata/features/3604565/Wardley_Mapping_06.jpg)![](https://www.cio.co.uk/cmsdata/features/3604565/Wardley_Mapping_06.jpg)

When you look at your map not every component will have a duplicate in the organisation. That said, many components will have multiple implementations. For example, if we take our aggregated view as typical of a media conglomerate, then there would be 13 different implementations of the website, five different implementations of a recommendation engine and 18 different implementations of compute in the same organisation. These are all examples of duplication.

Even if you find duplication, then not every group will treat the same component in the same way. For example, in Figure 6 above, the 14 different implementations of the web server will vary from one group believing it should be custom built to a larger group maintaining that it’s more of a commodity. This is the issue of bias.

By choosing clusters of points on an aggregated view (the red dots) – you can determine roughly how something should be treated like in our map (the blue dot) – we have market analysis as something relatively novel and best implemented with an early stage product. However, the majority (the cluster shown as red dots) has market analysis as something common, well-defined and best implemented with a commodity or utility like service. The use of the aggregated view can therefore tell us that we’re not the only group doing market analysis in the organisation but also that other groups are treating it in a much more effective and commodity-like manner.

### Step 5. Adjust

Once you’ve challenged the map by removing duplication and bias, you need to adjust it to suit the people involved. Hence, you take your map, point out all the areas where you can use the work of other groups and also provide the evidence that we’re going about things in the wrong way. This is always a fraught time because people may well have inertia to change and hence will resist.



Maps are also great for identifying what can be built as common services in an organisation and what can be reused from elsewhere. Hence don’t forget to use your maps to make agreements between groups; for example, this group will build the rules engine for all the other six groups, and so on. You can’t remove such duplication without a communication mechanism such as mapping. Relying on people to simply talk over the water cooler in a large organisation is how most companies get into a mess of duplication. Let us, however, assume that you have persuaded everyone on the adjustments necessary and made agreement to consume and supply components to other groups. I’ve provided an adjusted map here (Figure 7).

![](https://www.cio.co.uk/cmsdata/features/3604565/Wardley_Mapping_07.jpg)![](https://www.cio.co.uk/cmsdata/features/3604565/Wardley_Mapping_07.jpg)

From the map, we have identified the user need (the ‘visible’ elements at the top of the map), we know the components involved in creating those needs (the value chain), we’ve got some idea of the context and how evolved the components are, and we’ve challenged the map by identifying any bias we might have in the treatment of components. We’ve worked out that other groups have built several components and these are things we should consume from them. We’ve also agreed with other groups what components we could look to provide.

We now have a good understanding of the landscape and have removed potential duplication and bias. The next step is about putting some measurements in place (transaction costs and revenues) and sharing the maps with others. However, I thought I’d jump ahead to my next favourite topic, which is strategic play or the art of thinking.

### Step 6. Think

This is the stage in which we add a bit of strategy to the conversation. I tend to abolish the word strategy from the lexicon, because strategy without an understanding of the context (without situational awareness) is worthless.

The key step is to determine where to attack. Why is a relative statement – for example, why here over there. This is critical to understand because many companies try to determine why with no understanding of context.

There is a lot to strategy from anticipation of change to competitor moves, from inertia to tactical plays, and so on. Maps help you learn what works and what doesn’t over time through practice. As with military campaigns, maps are an incredibly useful tool for organisational learning.

The key to their use is to think about the environment (the board), to attempt to manipulate the environment (move pieces) and to practice. Don’t worry about being perfect, you’ll get better. So, back to our TV company example. There are numerous where’s that you could attack. I’m not going to list them all, but instead give a simple example known as ‘Fool’s mate’.

The problem is that the TV company has to commission shows from creative studios. These are limited in number and hence programs tend to be expensive. What we want to do is drive the creative studios to more of a commodity. Alas, the creative studios will resist this and hence have inertia to such a change (marked as a black bar below in Figure 8).

![](https://www.cio.co.uk/cmsdata/features/3604565/Wardley_Mapping_08.jpg)![](https://www.cio.co.uk/cmsdata/features/3604565/Wardley_Mapping_08.jpg)

Fortunately, creative studios themselves have constraints in terms of production talent and production systems. By driving production systems to more of a commodity (ideally through an open approach), you can reduce these constraints and encourage more creative studios to form, hence driving creative studios to more of a commodity. The beauty of this approach is that creative studios are likely to support you in your efforts because production systems will be seen as a cost to the business rather than a barrier protecting the business.

Of course, the vendors of production systems won’t be happy (they’ll have inertia), but with the creative studios backing you up, this can be overcome.

So, in the above, you have two wheres and the why now becomes easy to identify. You attack the production systems with an open source effort because this will ultimately commoditise creative studios hence further reducing your programme costs for commissioning. The benefit of attacking this space is that the creative studios are likely to support your effort rather than resist it. This is why you attack production system over attacking directly the creative studios.

In Figure 8 above there’s a range of potential points of attacks and some strategic games that can be played. However, it’s enough for the moment to simply understand the basics of where and why through the Fool’s mate example.

### Step 7. Methods

Once you have the map and the initial strategic play, you can start to examine how you’re going to do this. You’ll need multiple methods for any complex business. Remember that as things evolve their characteristics change and the techniques you need to use will evolve, too.

You could at this point create a map to represent your target operating model (TOM). I don’t tend to bother because your map will change with time and competitor moves. TOMs tend to be more wishful thinking and I have a preference to keep it adaptive.

In Figure 9 below, I’ve added method and use arrows to show a direction of intended travel (as opposed to a TOM). This gives a view of the environment based upon user needs, the components involved, the context (how things are changing), the strategic plays, how I can reduce duplication, what I can provide, a mechanism to overcome bias, and the methods involved (from agile to lean to six sigma).

![](https://www.cio.co.uk/cmsdata/features/3604565/Wardley_Mapping_09.jpg)![](https://www.cio.co.uk/cmsdata/features/3604565/Wardley_Mapping_09.jpg)

This map is something that I can discuss at the board level right down to individual project managers. Hence I tend to have a strong preference for maps within an organisation.

### Step 8. Organise

At this point, I normally break the map into teams. I tend to require a focus on FIST (Fast, Inexpensive, Simple and Tiny) principles and the use small, self – organising, cell-based teams (ideally less than 12 people) combined with small, focused contracts (see Figure 10 below).

![](https://www.cio.co.uk/cmsdata/features/3604565/Wardley_Mapping_10.jpg)![](https://www.cio.co.uk/cmsdata/features/3604565/Wardley_Mapping_10.jpg)

Once completed, I use a SWOT or Business Model Canvas (BMC) to refine a few more details or to validate the map and make sure I’ve not missed anything.

Once you become comfortable with the approach, the entire process of mapping out a line of business from user needs, removing duplication, removing bias, identifying strategic plays, putting in measurements, breaking out into methods and teams shouldn’t take more than a day or two. Given the scale of most projects, it’s usually time well spent.

At this point, I’ll move on to getting stuff done, often using Kanban as a scheduling tool and using the map as a guide. Obviously, maps evolve over time and there’s a lot to learn about mapping.

I prefer not to make grand claims of how much it’s going to save you or how much it’ll improve your strategic play. The proof of the pudding is in the eating, so I suggest you try it for a few days and make up your own mind.

### About the author:

Simon Wardley is a Researcher for the [Leading Edge Forum](http://leadingedgeforum.com/about-us/what-we-do) and his focus is on the intersection of IT strategy and new technologies. Simon’s most recent published research, entitled [*Of Wonders and Disruption*](http://leadingedgeforum.com/projects/118) where he attempts to predict the nature of technological and business change over the next 20 years. His previous published research covers topics including *The Future is More Predictable Than You Think – A Workbook for Value Chain Mapping, Beware of Geeks Bearing Gifts: Strategies for an Increasingly Open Economy, Learning from Web 2.0 and A Lifecycle Approach to Cloud Computing*.

Wardley has spent the last 15 years defining future IT strategies for companies in the FMCG, Retail and IT industries.

As a geneticist with a love of mathematics and a fascination in economics, Wardley has always found himself dealing with complex systems, whether it’s in behavioural patterns, environmental risks of chemical pollution, developing novel computer systems or managing companies. He is a passionate advocate and researcher in the fields of open source, commoditisation, innovation, organisational structure and cybernetics.