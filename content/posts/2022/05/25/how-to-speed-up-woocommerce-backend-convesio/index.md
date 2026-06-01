---
title: How to Speed Up WooCommerce Backend | Convesio
date: '2022-05-25T08:00:05-06:00'
format: link
service: instapaper
tags:
- read
external_url: https://convesio.com/blog/wordpress-performance/how-to-speed-up-woocommerce-backend/
---

[How to Speed Up WooCommerce Backend | Convesio](https://convesio.com/blog/wordpress-performance/how-to-speed-up-woocommerce-backend/)  



![](https://convesio.com/wp-content/uploads/2022/04/Speed-Up-WooCommerce-Backend-1.jpg)![](https://convesio.com/wp-content/uploads/2022/04/Speed-Up-WooCommerce-Backend-1.jpg)

A large part of running an online store requires managing the backend operations including product updates, order management, and shipment management. These tasks can easily overwhelm your staff and potentially disrupt business operations if the backend of your store becomes slow. The majority of WooCommerce users focus on speeding up the front-end of their store and do not pay attention to the performance of the backend which is equally important for the success of your online business.

In this article, we will highlight the drawbacks of having a slow WooCommerce backend and how they affect the efficiency of your business followed by the possible causes behind a slow WooCommerce backend, and finally, the remedies that are effective in speeding up the backend of your WooCommerce store.

#### Why is it Important Not to Have a Slow WooCommerce Backend

Your WooCommerce backend is where everything that appears at the front-end of your store is managed. The backend has many moving parts, both automated and manual. Your staff is busy processing the new orders, updating the inventory for new customers, managing shipments, and resolving order complaints. For everything to run smoothly and efficiently, it is crucial to avoid delays at all costs.

##### A Slow Backend Leads to a Slow Frontend

Both the front-end and back-end of your WooCommerce store draw power from the same server resources. That means when the backend of your WooCommece store becomes slow and clunky it also slows down the front-end of your store. The backend processes could involve many plugins sending concurrent requests back and forth for updating records to fetching large data for reports. All of these tasks are resource-intensive and slow down the WooCommerce backend.

Similarly, uploading new products, updating existing SKUs, filtering through customer’s orders, and generating monthly reports can put a strain on your server resources, ultimately causing slow loading times for both the front-end and back-end of your WooCommerce store. These requests are dynamic and can not be cached, therefore, optimizing them for performance is very important. Other online businesses like membership sites and eLearning sites should also consider optimizing the WordPress backend as users access it frequently for various tasks.

##### Counter-Productive for Staff

A slow loading WooCommerce backend dashboard can also annoy anybody working on it. It can affect the productivity of your staff who have to wait unnecessarily for a task to be completed before they can jump to another one. This is also not good for business, especially in a busy season where more customer orders need to be processed in a set period of time. A slow WooCommerce backend might not seem like a big issue today but over time it can kill productivity and increase the chances of error.

##### Less Efficient for the Business

All of the above makes your online business less efficient and less profitable. As a business owner, you should look for ways to make operations run smoother as your revenue depends on it. A slow WooCommerce backend could be your first warning of a slow online store, frustrated staff, and loss of revenue.

#### What Makes WooCommerce Backend Slow

The first step towards speeding up a WooCommerce backend is to understand the underlying problems that make your WooCommerce backend run slow.

##### Bloated Database

WooCommerce stores orders and products like posts data which means your database size increases over time and it takes longer to run searches and filters through this large database. This is the reason behind long delays while searching for a customer order from last month or running a search query based on a filter. In some cases, the server simply refuses to fetch results and throws a timeout error instead.

Sometimes, displaying a large number of items in the backend can also cause performance issues. So instead of displaying a list of fifty orders per page, shrink it down to just 20 and use the pagination feature instead. You won’t be working on fifty orders at a time anyway.

##### Too Many Plugins

Plugins are awesome but too many plugins are not! It is true that there is a plugin for everything but really you do not need to have everything on your WooCommerce store. Plugins are tempting and thousands of them are free to install but they too come with a price that your server pays in precious computing kilobytes currency. Of course, there are good and bad plugins but even the good ones need resources to run, and the bad ones can do a lot more damage.

Plugins that are constantly running in the background, especially the ones that track visitors’ activity and keep updating the database for generating reports or “giving a customized experience” to a user are often the reason behind a slow front-end as well as for cluttering the backend of your WooCommerce store. Plugins when activated can make multiple requests and run several database queries in order to serve their purpose whether you need them or not.

##### Third-party Services

Nowadays, almost every tool comes with a WordPress integration which is welcomed by its users. These third-party services include tracking services, payment gateways, shipment integrations, chatbots, [off-site backups](https://convesio.com/blog/wordpress-business/how-to-backup-wordpress-site/), etc. A common misconception is that these third-party services live outside of the online store, thus, are lightweight and have no impact on the performance. Which is not entirely true. Third-party services do make a lot of external calls and can load tons of client-side code at the expense of your server or user browser. All of that can slow down the backend of your WooCommerce store.

To make things worse, some third-party services are so poorly designed that they do more damage than good. Let me explain that with a real-world example. One of our clients was using an unconventional payment gateway mainly focused on their country. The site barely went live and crashed two times. It turned out that the website for that payment gateway was down and apparently they were using the same server for powering the licensing service inside their plugin. This triggered time-out errors in the licensing service preventing everything else on the page from loading.

##### Bad Custom Code

WooCommerce allows the flexibility of adding your own custom code to add the desired features. However, if the custom code is not written properly and does not follow the best practices as defined in [WordPress codex](https://codex.wordpress.org/Main_Page) can add unnecessary complexities that can slow down your WooCommerce backend.

It is important to ensure that the custom code does not use deprecated functions and only requests the database for the information where needed. For example, calling functions inside the *init* function unnecessarily can cause delays on every page load.

##### Bad Configurations

Similar to bad custom code, bad configurations, and design strategies can also slow down the WooCommerce backend. For example, one of our clients had an Order Detail page that was taking **30 seconds to load!** It turned out that they had a custom field on that page with multiple menu options and the database had to query through thousands of rows just to fetch these few menu options.

##### Outdated WordPress Core and PHP

Outdated PHP versions and WordPress core are also major reasons behind a slow dashboard. Still, a lot of WooCommerce stores run on PHP 5.x and miss out on the performance gains of switching to PHP 7 and above. The newer PHP versions are leaner, optimized, secure, and provide better compatibility with the rest of the hosting stack. Similarly, updated versions of WordPress and WooCommerce are lightweight and much more efficient than their predecessors. Depreciated functions and inefficient coding practices lead to errors and decrease the performance of the backend.

#### How to Speed Up WooCommerce Backend

Speeding up a WooCommerce backend is a lot simpler after you have identified the possible causes that slow it down in the first place. The process of speeding up the WooCommerce backend is different from speeding up the WooCommerce front-end. That is because, on the backend, the optimization is more like an elimination process where we shred the extra load and fix bugs in the code. We also need to dig a little deeper with the help of certain tools to find the real culprits behind slowing down the dashboard.

##### Install Query Monitor

Installing the [Query Monitor](https://en-gb.wordpress.org/plugins/query-monitor/) plugin should be the first step toward speeding up the WooCommerce backend. Query Monitor is a debugging and monitoring tool that gives you visibility of slow database queries, API requests, and AJAX calls that take longer times and make the WooCommerce dashboard slow. WordPress Query Monitor plugin is a great and convenient way of monitoring every transaction that happens between your WooCommerce store and server. It is a tool that helps you make sense of what’s going on and what actions you can take to fix the issues.

Let’s briefly look at the Query Monitor in action.

Inside your WordPress admin, go to Plugins and add a new plugin. Search for Query Monitor, install it, and activate it.

![](https://convesio.com/wp-content/uploads/2022/04/image5-1024x501.png)![](https://convesio.com/wp-content/uploads/2022/04/image5-1024x501.png)

Once the plugin is activated, you will notice a new option at the top bar of your admin panel. These numbers represent Page generation time, Peak PHP memory usage, Database query time, and the number of database queries made. This shows that the Query Monitor plugin has already started working and gathering useful data about your WooCommerce site.

![](https://convesio.com/wp-content/uploads/2022/04/image2-1024x595.png)![](https://convesio.com/wp-content/uploads/2022/04/image2-1024x595.png)

Click on these numbers and a complete Query Monitor dashboard will expand. The complete overview of this dashboard is out of the scope of this article, however, I will walk you through the two important sections that will help you speed up the WooCommerce backend. The first section is **Queries** which contains a list of all the database queries running on your site. Next to each query you can also see the time it takes to process it and the component requested that query.

![](https://convesio.com/wp-content/uploads/2022/04/image4-1024x500.png)![](https://convesio.com/wp-content/uploads/2022/04/image4-1024x500.png)

You can also filter the types of queries and the components. For example, if you wish to see just the queries made by a suspected plugin, select that plugin from the component’s list. Another useful feature of this plugin to help you speed up the WooCommerce backend is the **Scripts** feature.

![](https://convesio.com/wp-content/uploads/2022/04/image1-1024x499.png)![](https://convesio.com/wp-content/uploads/2022/04/image1-1024x499.png)

This gives you complete visibility of all the scripts running on your site. From this option, you can filter the scripts based on their host and identify third-party scripts. Similarly, you can also filter through the script’s dependencies and the corresponding elements depending on these scripts. This way you can see what features are dependent on what scripts and what will be the outcome of removing that script.

Query Monitor is an effective tool for monitoring database queries and API requests. Install it and start playing with it to understand what each section does and can help you make the right decisions in speeding up the WooCommerce backend.

##### Remove Unnecessary Plugins

After installing and understanding how Query Monitor works, getting rid of unnecessary and problematic plugins should not be an issue. Based on the Query Monitor’s report, you can identify the plugins that take a longer query time or make an unusual number of requests to your server or to a third-party service. At this point, you can either decide to deactivate them and activate them only when required or replace them with a better [WooCommerce plugin](https://convesio.com/blog/wordpress-ecosystem/must-have-plugins-for-woocommerce-website/) or simply uninstall them.

You can skip Query Monitor altogether and simply check the performance of your WooCommerce backend by deactivating and then activating each plugin one by one. Although this method might not give you very useful insights you can still use it to make a quick check especially if you have doubts about a particular plugin that you recently updated or installed.

##### Monitor Using New Relic

[New Relic](https://newrelic.com/) is a renowned Application Performance Management (APM) tool that gives far more in-depth performance analysis of your WooCommerce store than Query Monitor. It is free to use with 100GB of data and for 1 user which for the majority of small to mid-sized WooCommerce stores is sufficient. Let’s see how you can integrate this useful tool to speed up the backend of your WooCommerce store.

Go to the New [Relic WordPress Quickstart](https://newrelic.com/instant-observability/wordpress/59ba7d1f-7833-4d9b-893d-2b493e5ddac8) website and create your account. Once the account is created, add your data source which is the process of generating a command inside the New Relic dashboard that connects New Relic with your server and your WordPress application. This integration is beyond the scope of this guide as it can vary from host to host. Some hosting providers do not allow root access and you need to contact their support to get New Relic installed on your server.

After getting New Relic, you can begin exploring various features. The tool offers a huge range of options to analyze the performance of your WooCommrce store. The most important feature of New Relic is its Transaction traces feature which gives a detailed snapshot of all the transactions happening on your site. It allows you to filter through slow transactions, database calls, and external resources.

Similarly, it also gives a detailed usage breakdown of WordPress themes and plugins. From New Relic’s dashboard, you can see which theme or plugin takes a long time to respond and contributes to a slow WooCommerce backend.

![](https://convesio.com/wp-content/uploads/2022/04/image6-1024x597.png)![](https://convesio.com/wp-content/uploads/2022/04/image6-1024x597.png)

WordPress site transactions and their duration. Source: [New Relic](https://newrelic.com/blog/best-practices/web-performance-optimization-automation)