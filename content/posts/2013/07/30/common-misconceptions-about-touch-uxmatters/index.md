---
title: 'Common Misconceptions About Touch :: UXmatters'
date: '2013-07-30T16:21:09-06:00'
format: link
service: instapaper
tags:
- read
external_url: http://www.uxmatters.com/mt/archives/2013/03/common-misconceptions-about-touch.php
---

[Common Misconceptions About Touch :: UXmatters](http://www.uxmatters.com/mt/archives/2013/03/common-misconceptions-about-touch.php)

> garbnzgh: Design guidelines for mobile: “Common Misconceptions About Touch” —UXmatters http://t.co/yyeAKaDgaG

[Design](http://www.uxmatters.com/topics/)
[Research](http://www.uxmatters.com/topics/)
## [Mobile Matters](http://www.uxmatters.com/columns/mobile-matters/)

### Designing for every screen

A column by [Steven Hoober](http://www.uxmatters.com/authors/archives/2012/04/steven_hoober.php)


March 18, 2013
> 44 pixels is *not* a physical size. … We cannot even translate 44 pixels, or points, to a single actual size.

Touchscreens have been with us for decades—and they’ve been the mobile input method of choice for many of us for about 5 years. In fact, many junior designers and developers—or at least those who were late to the mobile party—have never owned a mobile phone for which buttons were the primary input method.

But there are still very few designers who seem to know how touchscreens actually work or how people really interact with them. In my work as a UX design consultant, working for many different organizations, I’ve encountered lots of myths and half-truths about designing for touchscreens.




Sponsor Advertisement
 [![]()![]()](http://info.userzoom.com/build-a-better-experience.html?source=online%20advertising&llr=uxmatters&olr=uxmatters&medium=displayad)

Continue Reading…

## You Can’t Rely on Designing 44-Pixel Touch Targets

Even with iOS clearly in second place behind Android, the Apple standard size for touch targets sticks with us, but 44 pixels is *not* a physical size. And with several device operating systems on the market—and Apple converting pixels to a device-independent measurement they call a *point*—we cannot even translate 44 pixels, or points, to a single actual size.

Physical sizes matter, so all *good* guidelines are in millimeters, inches, typographers’ points, or other real-world scales.

Plus, a lot of the guidelines for operating systems and OEMs (Original Equipment Manufacturers) define touch targets that are smaller than the vast body of research indicates would be correct. For example, Nokia often insists that 7 millimeters is a fine size for touch targets, and so does Microsoft—sort of—but they also say that there should be 2-millimeter gaps between targets. Other guidelines are all over the place. ANSI/HFES 100-2007 recommends a button size of at least 9.5 millimeters.

When designing targets in touch user interfaces, we can neither define them using a single number of pixels nor consider only a single axis of their size.

## Do Different Finger Sizes Really Matter?

> Because our fingers are three-dimensional and compliant, or squishy, the contact patch varies by pressure and angle.

Looking at touch-target size differently, ISO 9241-9 recommends a button size equal to the breadth of the distal finger joint of a 95th percentile male, which is about 22 millimeters! But many people touch mobile-device screens with their thumbs.

A number of touch-target guidelines are based on measurements of the widths of people’s fingers, but such measurements are mostly irrelevant. Sure, we do have fingers of different sizes, but when using capacitive touch devices, only part of the finger or thumb makes contact with the screen, as Figure 1 shows.

Figure 1—Only part of a user’s thumb gets flattened against the screen

![](http://www.uxmatters.com/mt/archives/2013/03/images/Hoober-TaughtAboutTouch-Fig1.png)![](http://www.uxmatters.com/mt/archives/2013/03/images/Hoober-TaughtAboutTouch-Fig1.png)  

Because our fingers are three-dimensional and compliant, or squishy, the contact patch varies by pressure and angle. Some research has suggested that users slow down and use more precise touch methods when targets are smaller—such as touching screens with their fingertips. Plus, when trying to exert more control, users touch more lightly, so have a smaller contact patch. It may even be possible to sense and take advantage of this in the near future. In my own research, I have found that children seem to have less control than adults, so despite their having smaller fingers, they have a contact patch of about the same size as an adult’s.

You may be surprised to learn that current touchscreens sense only the geometric center of a user’s contact patch, or its *centroid,* rather than its entire area, as shown in Figure 2. So touchscreens *can’t* communicate the size of a user’s contact patch to a mobile phone—or your Web site or app. Because a device uses only the centroid to determine what a user is tapping, the extent of the contact patch doesn’t matter.

Figure 2—Centroid of the contact patch on a target

![](http://www.uxmatters.com/mt/archives/2013/03/images/Hoober-TaughtAboutTouch-Fig2.png)![](http://www.uxmatters.com/mt/archives/2013/03/images/Hoober-TaughtAboutTouch-Fig2.png)  

Luckily, people know their own hands well and are pretty good at centering a touch on a target, so they can generally place the centroid of contact where they mean to. In Figure 2, the contact patch overlaps the items **Nearby** *and* **Events**, but the centroid is clearly on **Nearby**, so that is the target that gets tapped.

Of course, finger size *can* matter when a user’s finger is obscuring a user interface, but this is a different problem from finger size as it relates to touch targets. In this case, the part of the screen that a hand obscures depends on [how users hold their phone](http://www.uxmatters.com/mt/archives/2013/02/how-do-users-really-hold-mobile-devices.php).

## Bigger Buttons Are Easier to Use—Up to a Point

> If buttons get too big, users start having problems perceiving them as clickable buttons—and sometimes even discerning them as discrete elements.

When the target is a button, the bigger, the better—but *only* up to a point. Over a certain size—and a surprisingly small size really—research tells us that there’s no improvement in the accuracy of touch interactions. If buttons get too big, users start having problems perceiving them as clickable buttons—and sometimes even discerning them as discrete elements.

The belief in big buttons is also troublesome because it makes plain the general perception that visible targets and touch targets are the same thing. While this may often be true in practice, this perception is where many design issues arise. In actuality, to get a bigger target, there’s no need to increase the size of the visible target. Instead, you can simply increase the dimensions of the clickable area around a link or button.

As for any interactive element, the sizes of the visible target and the touch target for a button can be different. More often than not, they *should* be.

## Designing Targets

There are, in fact, three facets of touch targets that we must understand and consider when designing touch interfaces:

* designing visual targets
* designing touch targets
* preventing interference errors

### Designing Visual Targets

> The visual target is the link text, icon, or other graphic element that affords an interaction. Visual targets need to be big enough and clear enough….

The visual target is the link text, icon, or other graphic element that affords an interaction. Visual targets need to be big enough and clear enough so:

* They attract the user’s eye.
* The user understands that they are actionable elements.
* They are readable, and the user can understand what action they will perform.
* The user is confident that he can easily tap them.

The most common issues with visual targets arise from users’ expectations of what a target should be. For example, in a list or table, if rows have visible backgrounds or separator lines, users generally expect the whole box—that is, the cell or row between those lines—to be the target. So don’t make just the text the target. Design containers and indicators to attract taps as well. And be sure to use separators or containers whenever possible.

Always design visible targets to display multiple states. Many errors arise from minor delays in responsiveness. If users don’t get immediate feedback that a tap was successful, they will assume a miss and try again. As soon as a device accepts a touch, the visible target should change to an active state that is clearly different from its default state. Don’t forget about the issue of the user’s thumb or finger obscuring the target. Ensure that the change of state occurs in a visible area that is large enough for the user to see it.

For human vision, what matters most is not font sizes, but the angle of vision, which is referred to as *angular resolution*. In Figure 3, the narrow cone shows the minimum size for legible type; the larger cone, the area of high-resolution vision where the user’s eyes are focused. Devices that a user is viewing from further away require larger text.

Figure 3—Angles of vision, or angular resolution

![](http://www.uxmatters.com/mt/archives/2013/03/images/Hoober-TaughtAboutTouch-Fig3.png)![](http://www.uxmatters.com/mt/archives/2013/03/images/Hoober-TaughtAboutTouch-Fig3.png)  

Minimum font sizes must meet three criteria: the text must be readable, legible, and tappable. Calculations of angular resolution and distance, as shown in Figure 3, indicate that a 6-point (pt), or 2.1-millimeter (mm), font size is generally the smallest that allows readability. Icons should not be smaller than about 8 points, or 2.8 millimeters, unless they directly reinforce the text—for example, an indicator that a link loads a page in a new window. People with low vision need larger visual targets.

There’s a maximum size for visual targets as well. It is convenient—though not completely accurate—to say that our area of attention is much smaller than our field of view. The cone representing our *foveal vision* is about 5 degrees across—or a circle that is approximately half the size of your fist at arm’s length. This is also—not by coincidence—the angular dimension of most mobile handsets, but is much smaller than a tablet’s screen. So buttons or other tappable elements that extend across the entire viewport are often so big that users cannot perceive them as actionable items.

If you think banner ads don’t have this problem, take a closer look. Most contain smaller call-to-action buttons or links for the express purpose of solving this problem. Make sure your visual targets are small enough to be within the user’s attention zone.

Note—Unless otherwise stated, the specific guidelines I’ve provided here are for mobile phones. People use tablets, computer screens, and video players at greater distances, so depending on the size of the screen and the expected use case, you’ll need to design larger visual targets for them. People generally hold smaller mobile devices—such as most feature phones—closer, so you can use even smaller sizes for visual targets. Be sure to calculate the angular resolution and test for readability on real hardware, with real people.

### Designing Touch Targets

> Since touchscreens sense only the *centroid**,* or geometric center of the contact patch, the contact patch of a user’s finger is not as relevant in determining touch targets as you might think.

An area on a screen that a user can touch to perform an action is a *touch target*. Touching a device’s screen outside a touch target does not activate the target.

As I mentioned earlier, a target’s visual design drives users’ expectation of its size. If users could reasonably expect an entire button or other element to be tappable, make it so. I encounter too many buttons where only the text is the touch target and tapping the rest of the button does nothing.

Since touchscreens sense only the *centroid,* or geometric center of the contact patch, the contact patch of a user’s finger is *not* as relevant in determining touch targets as you might think. To determine how small a touch target can be without impairing usability, I have reviewed much literature and done some math relating to what is called the *circular error of probability (CEP)*.

Any targeting has inherent inaccuracy. A user’s actual touches on an intended target are never all perfectly aligned; they’re distributed around the target. Their distribution is not random, but closely clustered around the visual target. By measuring their inaccuracy, you can determine the CEP as a certain percentage of hits and determine whether users can hit a target of a certain size with acceptable accuracy.

Over about a 95% accuracy, there begin to be diminishing returns—much larger targets are necessary for a small improvement—so I’ve used a CEP of R95 to determine sizes.

Text links are far too small to accurately target them. Some modern operating systems and browsers such as Google Chrome attempt to solve this problem by zooming in on small, ambiguous targets, to offer suitably large tappable areas.

Figure 4—Chrome makes excessively small links into links that are a good size

![](http://www.uxmatters.com/mt/archives/2013/03/images/Hoober-TaughtAboutTouch-Fig4.png)![](http://www.uxmatters.com/mt/archives/2013/03/images/Hoober-TaughtAboutTouch-Fig4.png)  

However, the visual target does *not* have to be the touch target—and usually should *not* be. For example, say a mobile site needs to have a very small, 6-point text link to a disclaimer or the full site. The text should be small because you don’t want people to notice it much; but since it’s small, it may be hard to activate.

No problem. First, not only should the visible link text be clickable, the normally invisible area around it should also be clickable. (You can see a link’s clickable area if you drag your finger across the text to select it.)

If a link were in 6-point Helvetica, a box corresponding to its clickable area would be 7.68 points, or 2.7 millimeters, tall. That is still far, far too small to be easily tappable. Users might encounter error rates as high as 50% with a target this small.

The absolute minimum for a reliable touch target is 6 millimeters, but this is suitable only when users are relatively still. If users may either be moving or distracted, use an 8-millimeter target. Smaller targets would cause a user to slow down, which might not be acceptable for your user interface. There is *never* any need to exceed 15 millimeters for a touch target.

Depending how you measure the centroid of a touch, it can sometimes appear that the centroid tends to be below the centerline of the visible target. Although this is technically accurate, calculations of the more useful interpretations of CEP (D2RMS or R95) don’t bear this out. There is not a statistically significant difference between measuring the number of equally distant high clicks and low clicks that are close to the center. I am comfortable adding this phenomenon to the myths of mobile design, because it has no influence on design.

### Preventing Interference Errors

> The error that has the most serious consequences is *interference*, the condition that happens when two or more touch targets are in such close physical proximity that the circular error of probability for one target includes another target as well.

Making sure a touch target is the right size means ensuring a user can tap it. When a user fails to tap a touch target accurately, it results in a miss, and the target doesn’t activate. What happens when users miss a touch target is a key factor to consider. People actually miss *every* target by a little, so planning for error is crucial.

But the error that has the most serious consequences is *interference*, the condition that happens when two or more touch targets are in such close physical proximity that the circular error of probability for one target includes another target as well.

Be sure to check for interference on each axis of a target. To avoid interference errors, make sure that touch targets are *at least* 8 millimeters apart on center—with 10-millimeter spacing being strongly preferable. *On center* is an engineering term that means when measured from the center of each touch target. In this way, you can be measure the distance between the centers of differently sized objects such as a link and a button, because neither the visual- nor the touch-target sizes matter in this measurement.

As a consequence, most touch targets will never be too closely adjacent to each other, and only small amounts of space are necessary between them. This space does not have to be visually apparent. A non-touch area need not necessarily be whitespace. For example, toolbars often comprise icons that have suitable spacing, but without *any* visual indication of the gap between them. And the height of a tab bar can be as narrow as you want visually, as long as no other targets are too close either above or below the tabs.

Whether on an actual screen or a scaled screenshot, overlay a circle on each target to check for interference, as shown in Figure 5. In this case, the outer circle is 10 millimeters, while the inner circle is the minimal 8 millimeters. The lists in both screenshots are minimally acceptable. But the very small tab bar in the screenshot on the left would cause interference errors because users could accidentally tap either the action icons above it or the list items below it.

Figure 5—Measuring to avoid interference between targets

![](http://www.uxmatters.com/mt/archives/2013/03/images/Hoober-TaughtAboutTouch-Fig5.jpg)![](http://www.uxmatters.com/mt/archives/2013/03/images/Hoober-TaughtAboutTouch-Fig5.jpg)  

Avoiding disaster is the other part of designing for interference. It is often impossible to space touch targets far enough apart to avoid accidental tapping altogether. In some cases, operating system standards demand overly small and immediately adjacent targets. Tactics to mitigate such problems are relatively easy to implement.

Never place buttons with catastrophic consequences—or even just hard to undo results—near those that have trivial results. For example, in a user interface that lets users compose an email message, the **Send** and **Delete** buttons should be far from each other, and nowhere near things like formatting features. Accidentally changing text to bold can be easily fixed by clicking the **Bold** button again. But there’s no way to unsend a message, and recovering a deleted message requires digging around in the trash, if it’s possible at all.

On mobile devices, interactive elements simply *are* close to each other, so making mistakes when tapping or performing other gestures *will* happen. Luckily, our usual design practices already remedy this problem to a great extent. We take the time to group functions by behavior. We avoid visual design errors that would place targets too close to each other or give items of dissimilar importance the same visual weight or proximate locations.

I encourage interested readers to further explore the technology of touchscreens to better understand their capabilities and limitations. To give you one example, inaccuracies can also arise from the design of touchscreens, which varies widely among devices. Some have notable errors on certain parts of the screen. As we begin to gain a better understanding of these technical limitations, this may enhance our ability to prevent errors by avoiding detailed touch interactions in low-resolution parts of the screen.




## Designing Gesture and Motion

> Gestural interactions require similar, but slightly different guidelines.

This article has focused on designing touch interactions that involve tapping—and perhaps, pressing and holding. There has been less research on how the ergonomic factors that I’ve described apply to gestures.

For example, designing a volume slider that would be easy to use would clearly have the same requirements as any basic touch interaction in regard to pressing and holding the control. But further considerations would immediately arise when a user moved his finger on the screen to drag the control. Specifically, it would be necessary to restrict the directional movement to a single axis—or a particular angle or type of motion. In the case of a horizontal volume slider, once the user activated the control, the application would ignore any finger movement in the vertical axis. This is a good way to let users move controls with greater precision.

Other types of gestural interactions require similar, but slightly different guidelines. As with design for touch, there are many misconceptions about best practices for the design of gestures, which are neither well defined nor well understood. So think carefully about the needs of users when designing gestures. Hopefully, in addition to an increasing body of actual best practices for the design of gestures, there will soon be more solid research that will let us learn more about designing gestures.

## Summary of Touchscreen Design Guidelines

> Evaluate touch targets for possible interference errors. If small targets are too close together, adjust their size and spacing.

I’ve explained a lot of different design considerations in this column, so I’ll summarize the key steps that you should take when designing or evaluating a design for a touch user interface:

1. Determine the size of each visual target.
2. Determine the size of each touch target—and define it in your design specification!
3. Evaluate touch targets for possible interference errors. If small targets are too close together, adjust their size and spacing.
4. Determine the consequences of accidental taps on adjacent targets. If they’re severe, protect users from them by rearranging targets or placing them further apart.

### Summary of Size Guidelines

For your easy reference, here is a summary of the size guidelines I’ve provided throughout this column—including minimum sizes for visual targets on devices of various sizes, in Table 1; sizes for touch targets; and the minimum and preferred spacing between adjacent targets—as measured on center, on either axis—to avoid interference errors.

Table 1—Minimum sizes for visual targets on various device sizes
 Target | 2.5-inch Phone | 3.5–5-inch Phone | 9–10-inch Tablet |

Text

4 pt / 1.4 mm

6 pt / 2.1 mm

8 pt / 2.8 mm

Icons

6 pt / 2.1 mm

8 pt / 2.8 mm

10 pt / 3.5 mm

* Touch targets:
  + Minimum—17 pt / 6 mm
  + Preferred—23 pt / 8 mm
  + Maximum—43 pt / 15 mm
* Spacing between targets to avoid interference errors, on center:
  + Minimum—23 pt / 8 mm
  + Preferred—28 pt / 10 mm ![](http://www.uxmatters.com/images/ux-bug.gif)![](http://www.uxmatters.com/images/ux-bug.gif)

#### References

Wikipedia. “[HP-150](http://en.wikipedia.org/wiki/HP-150).”[![](http://www.uxmatters.com/images/new-window-arrow.gif)![](http://www.uxmatters.com/images/new-window-arrow.gif)](http://en.wikipedia.org/wiki/HP-150) *Wikipedia.* Retrieved March 5, 2013—Probably the first commercially available touchscreen, the IR-grid style, all-in-one HP-150 desktop PC sold from 1983 onward, followed by an unbroken series of touchscreens in all sorts of devices and settings.

Apple. “[Platform Characteristics](http://developer.apple.com/library/IOS/#documentation/UserExperience/Conceptual/MobileHIG/Characteristics/Characteristics.html).”[![](http://www.uxmatters.com/images/new-window-arrow.gif)![](http://www.uxmatters.com/images/new-window-arrow.gif)](http://developer.apple.com/library/IOS/#documentation/UserExperience/Conceptual/MobileHIG/Characteristics/Characteristics.html) *Apple iOS Human Interface Guidelines.* Retrieved March 6, 2013—An Apple *point*—which is not the same as the typographer’s 1/72-inch point—is a device-independent pixel that was originally 44 pixels on the displays of the early iPhone and iPod Touch. On the iPhone, this point was somewhat too small at 6.74 millimeters—maybe because they were assuming fingertips instead of thumbs. The size of a point is increasingly variable because it is based on device-scaling ratios. Most critically, since late 2012, the iPad Mini has drawn everything by pretending it is a full-sized iPad, so all items appear smaller on the screen—even touch targets.

Nokia. “[UX Checklist](http://www.developer.nokia.com/Resources/Library/Symbian_Design_Guidelines/#!ux-checklist.html).”[![](http://www.uxmatters.com/images/new-window-arrow.gif)![](http://www.uxmatters.com/images/new-window-arrow.gif)](http://www.developer.nokia.com/Resources/Library/Symbian_Design_Guidelines/#!ux-checklist.html) *Symbian Design Guidelines.* Retrieved March 5, 2013—“The preferred minimum size of a UI element is 7 x 7 mm for index finger use and 8 x 8 mm for thumb use.” It is difficult to tell which digits a user might employ, but it’s best to assume thumbs. 8 millimeters is *almost* a suitable size, but a bit small.

Microsoft. “[Windows 8 Touch Guidance](http://download.microsoft.com/download/8/A/6/8A652B51-AF09-4A5A-888C-A0465D00FE5E/Windows%208%20Touch%20Guidance.pdf).”[PDF![](http://www.uxmatters.com/images/new-window-arrow.gif)![](http://www.uxmatters.com/images/new-window-arrow.gif)](http://download.microsoft.com/download/8/A/6/8A652B51-AF09-4A5A-888C-A0465D00FE5E/Windows%208%20Touch%20Guidance.pdf) Retrieved March 5, 2013—Microsoft suggests 7-millimeter targets for most uses; 9 millimeters for more important targets, but allows 5-millimeter targets “when it just won’t fit.” More important, they also advise putting 2 millimeters between targets. This gets their recommendation much closer to a proven usable size. They also discuss finger width as being 11 millimeters, but seem to do nothing with this measurement, which is good because that’s not important.

Human Factors & Ergonomics Society. *ANSI/HFES 100-2007 Human Factors Engineering of Computer Workstations*. Santa Monica, CA: Human Factors and Ergonomics Society, 2007—This standard suggests a button size of at least 9.5 millimeters, but these recommendations are for the design of “computer workstations,” or desktop computers.

International Organization for Standardization. *Ergonomic Requirements for Office Work with Visual Display Terminals (VDTs)—Part 9: Requirements for Non-keyboard Input Devices*. Geneva, Switzerland: International Organization for Standardization, 2000—This standard recommends a button size that is equal to the breadth of the distal finger joint of a 95th percentile male—that is, approximately 22 to 23 millimeters. This is extremely large, not to mention that contact patches are not the full width of a finger on most devices. However, some of these standards may derive from the use of interference touchscreens, which sense the entire finger size using a field in front of the screen. Technology matters, so use these standards with caution.

T., Anthony. “[Finger-Friendly Design: Ideal Mobile Touchscreen Target Sizes](http://uxdesign.smashingmagazine.com/2012/02/21/finger-friendly-design-ideal-mobile-touchscreen-target-sizes/).”[![](http://www.uxmatters.com/images/new-window-arrow.gif)![](http://www.uxmatters.com/images/new-window-arrow.gif)](http://uxdesign.smashingmagazine.com/2012/02/21/finger-friendly-design-ideal-mobile-touchscreen-target-sizes/) *Smashing Magazine*, February 21, 2012. Retrieved March 5, 2013—An example that, while it uses some data, also generally refers to finger sizes rather than contact patches. Logic works only if our basic data and assumptions are correct.

Meyer, John. “[The Pursuit of Tappiness: Six Easy Ways to Make Your Website Tablet-Friendly](http://uxmag.com/articles/the-pursuit-of-tappiness).”[![](http://www.uxmatters.com/images/new-window-arrow.gif)![](http://www.uxmatters.com/images/new-window-arrow.gif)](http://uxmag.com/articles/the-pursuit-of-tappiness) *UX Magazine*, January 2, 2013. Retrieved March 5, 2013—There is a terrific counter-example to the pixel-centric craze among the many comments.

Pavlus, John. “[Fat Thumb: A One-Handed Alternative to Pinch-to-Zoom](http://www.fastcodesign.com/1671741/fat-thumb-a-one-handed-alternative-to-pinch-to-zoom#1).”[![](http://www.uxmatters.com/images/new-window-arrow.gif)![](http://www.uxmatters.com/images/new-window-arrow.gif)](http://www.fastcodesign.com/1671741/fat-thumb-a-one-handed-alternative-to-pinch-to-zoom#1) *Fast Co Design,* February 4, 2013. Retrieved March 5, 2013—A possible near-future, commercial software product that may exploit the sensing of different sizes of contact patches to infer pressure.

Nielsen, Jakob, and Raluca Budiu. *Mobile Usability*. Berkeley, California: The Nielsen Norman Group, 2013—“Making feedback big enough to be seen around the user’s finger is a basic usability guidelines for visual design on mobile and tablets.”

Sesto, Mary E., Curtis B. Irwin, Karen B. Chen, Amrish O. Chourasia, and Douglas A. Wiegmann. “Effect of Touch Screen Button Size and Spacing on Touch Characteristics of Users With and Without Disabilities,” in *Human Factors: The Journal of the Human Factors and Ergonomics Society*, June 2012, Volume 54, Number 3—The study found that 20-millimeter buttons worked best and larger spacing didn’t help, but they measured the force used, not targeting accuracy—apparently because of a special need of the disabled cohort. While these findings are not directly applicable, the 20-millimeter size is reasonable when accounting for inaccuracy due to motor-function issues.

Parhi, Pekka, Amy K. Karlson, and Benjamin B. Bederson. “Target Size Study for One-handed Thumb Use on Small Touchscreen Devices,” in *Proceedings of the 8th Conference on Human-Computer Interaction with Mobile Devices and Services*. New York: ACM, 2006—The “target size of 9.2 mm for discrete tasks and targets of 9.6 mm for serial tasks should be sufficiently large for one-handed thumb use on touchscreen-based handhelds.” They used CEP-R95, and there was no improvement when increasing to 11.5 mm. This paper does conflate target and interference for the most part, very often putting test items adjacent to each other. Quoted by Nielsen in *Mobile Usability* as recommending a target size of around 10 mm, which I can agree with.

Lee, Seungyon, and Shumin Zhai. “The Performance of Touch Screen Soft Buttons,” in *Proceedings of the SIGCHI Conference on Human Factors in Computing Systems*. New York: ACM, 2009—10-millimeter buttons resulted in 98 to 99.4% accuracy. Reducing button size caused users to switch from thumb to finger. iPhone keyboard buttons resulted in high accuracy (90%), but a third slower typing speed, and there was a huge jump in necessary corrections when typing on the narrow keyboard. I think they measured accuracy as the ability to enter the right value, not the first-time ability to hit the right target and, therefore, missed critical interference issues.

Park, Yong S., Sung H. Han, Jaehyun Park, and Youngseok Cho. “Touch Key Design for Target Selection on a Mobile Phone,” in *Proceedings of the 10th International Conference on Human Computer Interaction with Mobile Devices and Services*. New York: ACM, 2008—Really interesting research because participants did hold the device and use their thumb to interact, and the results show the accuracy rate plotted by screen location. Size recommendations resulted from this study as well—specifically, that 10 millimeters is better than 7 millimeters, and 4 millimeters is sort of a disaster.

Schildbach, Bastian, and Enrico Rukzio. “Investigating Selection and Reading Performance on a Mobile Phone While Walking,” in *Proceedings of the 12th International Conference on Human Computer Interaction with Mobile Devices and Services*. New York: ACM, 2010—“Whilst performance decreases, cognitive load increases significantly when reading and selecting targets when walking. Furthermore, the results show that the negative effect regarding target selection can be compensated by increasing the target size, but the text reading task did not yield better performance results for a larger text size due to the increased demand for scrolling.” This study’s results: 6.74-millimeter buttons had an error rate of up to 23%; buttons of about 10 millimeters were much better; and 20-millimeter buttons solve almost all problems, even when walking. Small buttons make people slow down due to cognitive loading. Small, 6-point text results in no performance degradation when walking, but is perceived by some as being worse. There is a middle ground because of the need to scroll. Text sizes that are too large are also bad.

Henze, Niels, Enrico Rukzio, and Susanne Boll. “100,000,000 Taps: Analysis and Improvement of Touch Performance in the Large.” *Proceedings of the 13th International Conference on Human Computer Interaction with Mobile Devices and Services*. New York: ACM, 2011—There were several million somewhat-qualified clicks from a game on Android. “Below 15mm the error rate dramatically increases and jumps to over 40% for targets smaller than 8mm.” There are nice charts on error rates by position, showing basically that the edges are much worse, pretty symmetrically.

Gilbert, Juan E., Aqueasha M. Martin, Gregory Rogers, Jerome McClendon, and Josh Ekandem. “Hey, That’s Not Who I Voted For!: A Study on Touchscreen Ballot Design,” in *Interactions*, November 2012—This article conflates target and interference; all tested designs have buttons hard against each other. Interesting information on indicator and visual-target focus. Discusses labels attracting taps and checkmarks to indicate selection.

Sears, A. “Improving Touchscreen Keyboards: Design Issues and a Comparison with Other Devices,” in *Interacting with Computers*, Volume 3, 1991—This is fairly early research on mounted touchscreens, and many refer to it, but I’d be wary of almost any specifications that rely on this too strongly for mobile devices.

Hoober, Steven, and Eric Berkman. *Designing Mobile Interfaces.* Sebastopol, California: O’Reilly, 2012—See “Appendix D: Human Factors,” section “Size of the Stimulus: Visual Angle,” which includes a formula for calculating visual angle, or angular resolution.

Hoober, Steven, and Eric Berkman. “[Human Factors & Physiology](http://4ourth.com/wiki/Human%20Factors%20%26%20Physiology).”[![](http://www.uxmatters.com/images/new-window-arrow.gif)![](http://www.uxmatters.com/images/new-window-arrow.gif)](http://4ourth.com/wiki/Human%20Factors%20%26%20Physiology) *4ourth Mobile Patterns Wiki*, July 11, 2012. Retrieved March 18, 2013.

Plait, Phil. “[Resolving the iPhone Resolution](http://blogs.discovermagazine.com/badastronomy/2010/06/10/resolving-the-iphone-resolution/).”[![](http://www.uxmatters.com/images/new-window-arrow.gif)![](http://www.uxmatters.com/images/new-window-arrow.gif)](http://blogs.discovermagazine.com/badastronomy/2010/06/10/resolving-the-iphone-resolution/)  *Discover*, June 10, 2010. Retrieved March 16, 2013—In the guise of adding science to the hype around the original release of the Apple Retina display on an iPhone, *Discover* published an easy-to-read discussion of the math behind angular resolution and why it matters more than absolute size.

Wikipedia. “[Circular Error Probable](http://en.wikipedia.org/wiki/Circular_error_probable).”![](http://www.uxmatters.com/images/new-window-arrow.gif)![](http://www.uxmatters.com/images/new-window-arrow.gif) *Wikipedia*, undated*.* Retrieved March 5, 2013

Hoober, Steven. “[Web to Mobile – Testing How Well It Will Work](http://shoobe01.blogspot.com/2011/10/web-to-mobile-testing-how-well-it-will.html).”[![](http://www.uxmatters.com/images/new-window-arrow.gif)![](http://www.uxmatters.com/images/new-window-arrow.gif)](http://shoobe01.blogspot.com/2011/10/web-to-mobile-testing-how-well-it-will.html) *Don’t Touch Me*, October 28, 2011. Retrieved March 5, 2013—The first time I wrote about how to test for interference on actual devices, using a circle template.

4ourth Mobile Patterns Wiki. “[4ourth Mobile Touch Template](http://4ourth.com/wiki/4ourth%20Mobile%20Touch%20Template).”[![](http://www.uxmatters.com/images/new-window-arrow.gif)![](http://www.uxmatters.com/images/new-window-arrow.gif)](http://4ourth.com/wiki/4ourth%20Mobile%20Touch%20Template) *4ourth Mobile*, undated*.* Retrieved March 15, 2013—I’ve created this tool to increase awareness of the problems of touch interference and make it easy to test for it. The video demonstrates measuring for interference and explains why it’s important, as well as how to use the other features of the tool.

Carey, John. “[Getting in Touch with Capacitance Sensor Algorithms](http://www.embedded.com/design/embedded/4008781/Getting-in-touch-with-capacitance-sensor-algorithms).”[![](http://www.uxmatters.com/images/new-window-arrow.gif)![](http://www.uxmatters.com/images/new-window-arrow.gif)](http://www.embedded.com/design/embedded/4008781/Getting-in-touch-with-capacitance-sensor-algorithms) *Embedded*, September 9, 2009. Retrieved March 5, 2013—A good overview of how capacitive touchscreens work and how to make them work better. (This article is comprehensive and gets pretty technical, so you might want to skim past any parts you don’t understand.)

Ganapati, Priya. “[Finger Fail: Why Most Touchscreens Miss the Point](http://www.wired.com/gadgetlab/2010/03/touchscreens-smartphones/).”[![](http://www.uxmatters.com/images/new-window-arrow.gif)![](http://www.uxmatters.com/images/new-window-arrow.gif)](http://www.wired.com/gadgetlab/2010/03/touchscreens-smartphones/) *Wired*, March 4, 2010. Retrieved March 5, 2013—Good general overview of the issues of technical accuracy on capacitive touchscreens, which may be another good reason to use larger targets, because tolerance stacking means adding device inaccuracy to user inaccuracy. In fact, I used to suggest that, with bezel use, edge targets could be smaller; but because accuracy is poor at the edges of the screen, I no longer recommend this.

Hoober, Steven, and Eric Berkman. *Designing Mobile Interfaces.* Sebastopol, California: O’Reilly, 2012—See the section “Provide Constraints,” around page 317, which discusses how scrolling should typically lock to one axis once scrolling starts.

Hoober, Steven, and Eric Berkman. “[General Interactive Controls](http://4ourth.com/wiki/General%20Interactive%20Controls).”[![](http://www.uxmatters.com/images/new-window-arrow.gif)![](http://www.uxmatters.com/images/new-window-arrow.gif)](http://4ourth.com/wiki/General%20Interactive%20Controls) *4ourth Mobile Patterns Wiki*, December 13, 2011. Retrieved March 18, 2013.