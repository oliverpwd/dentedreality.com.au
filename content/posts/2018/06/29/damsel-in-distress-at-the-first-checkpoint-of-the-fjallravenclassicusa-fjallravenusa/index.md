---
title: ''
date: '2018-06-29T18:47:16-07:00'
format: image
service: instagram
tags:
- fjallravenclassicusa
latitude: '39.3214'
longitude: '-106.311'
image: https://dentedreality.com.au/wp-content/uploads/2018/06/34648727_199830734053345_8074223313125113856_n.jpg
---

[![Damsel in distress at the first checkpoint of the #fjallravenclassicusa @fjallravenusa](https://dentedreality.com.au/wp-content/uploads/2018/06/34648727_199830734053345_8074223313125113856_n.jpg)](https://dentedreality.com.au/2018/06/29/damsel-in-distress-at-the-first-checkpoint-of-the-fjallravenclassicusa-fjallravenusa/) 

[![Damsel in distress at the first checkpoint of the #fjallravenclassicusa @fjallravenusa](https://dentedreality.com.au/wp-content/uploads/2018/06/34648727_199830734053345_8074223313125113856_n.jpg)](https://www.instagram.com/p/BkoRThRFjSb/)

Damsel in distress at the first checkpoint of the #fjallravenclassicusa @fjallravenusa

39.3214-106.311




* #[fjallravenclassicusa](https://dentedreality.com.au/tags/fjallravenclassicusa/)

Posted on [Instagram](https://www.instagram.com/p/BkoRThRFjSb/) [6:47 pm, June 29, 2018](https://dentedreality.com.au/2018/06/29/damsel-in-distress-at-the-first-checkpoint-of-the-fjallravenclassicusa-fjallravenusa/ "6:47 pm") 
jQuery(document).ready(function(){
var gmap\_ma0c4eae541e2abccfaf8aaea47d87e90 = {
positions : {
649 : new google.maps.LatLng( '39.3214', '-106.311' )
},
bounds : new google.maps.LatLngBounds(), // empty for now, we'll dynamically extend it later
map : new google.maps.Map(
document.getElementById( 'gmap\_ma0c4eae541e2abccfaf8aaea47d87e90' ),
{
mapTypeId: google.maps.MapTypeId.ROADMAP,
center: new google.maps.LatLng( 0, 0 ),
zoom: 16 // Seems to be a good zoom for a single point
}
),
markers : {},
}; // end of gmap
// Extend the bounds of interest based on our positions
for ( var m in gmap\_ma0c4eae541e2abccfaf8aaea47d87e90.positions ) {
gmap\_ma0c4eae541e2abccfaf8aaea47d87e90.bounds.extend( gmap\_ma0c4eae541e2abccfaf8aaea47d87e90.positions[m] );
}
// Render markers
for ( var m in gmap\_ma0c4eae541e2abccfaf8aaea47d87e90.positions ) {
gmap\_ma0c4eae541e2abccfaf8aaea47d87e90.markers[m] = new google.maps.Marker( {
clickable: true,
map : gmap\_ma0c4eae541e2abccfaf8aaea47d87e90.map,
position : gmap\_ma0c4eae541e2abccfaf8aaea47d87e90.positions[m]
} );
}
// Redraw map to fit our new marker-based bounds
gmap\_ma0c4eae541e2abccfaf8aaea47d87e90.map.setCenter( gmap\_ma0c4eae541e2abccfaf8aaea47d87e90.positions[649] );
});