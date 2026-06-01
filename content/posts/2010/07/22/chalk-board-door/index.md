---
title: Chalk-board Door
date: '2010-07-22T08:45:32-06:00'
format: image
service: flickr
tags:
- chalkboard
- door
- drawing
- gravatar
- loopy
- madness
- scribbles
- wordpress
latitude: '45.522999'
longitude: '-122.656834'
image: https://dentedreality-content.s3.amazonaws.com/wp-content/uploads/2010/07/14185736/4854300175_f749925849_o-768x1024.jpg
---

[![Chalk-board Door](https://dentedreality-content.s3.amazonaws.com/wp-content/uploads/2010/07/14185736/4854300175_f749925849_o-768x1024.jpg)](https://dentedreality.com.au/2010/07/22/chalk-board-door/) 
# [Chalk-board Door](https://dentedreality.com.au/2010/07/22/chalk-board-door/)

[![Chalk-board Door](https://dentedreality-content.s3.amazonaws.com/wp-content/uploads/2010/07/14185736/4854300175_f749925849_o-768x1024.jpg)](http://www.flickr.com/photos/borkazoid/4854300175/)

At the Jupiter Hotel in Portland. Stuck in my room all week, needed to do something other than stare at my laptop once in a while.

45.522999-122.656834




* #[chalkboard](https://dentedreality.com.au/tags/chalkboard/)
* #[door](https://dentedreality.com.au/tags/door/)
* #[drawing](https://dentedreality.com.au/tags/drawing/)
* #[gravatar](https://dentedreality.com.au/tags/gravatar/)
* #[loopy](https://dentedreality.com.au/tags/loopy/)
* #[madness](https://dentedreality.com.au/tags/madness/)
* #[scribbles](https://dentedreality.com.au/tags/scribbles/)
* #[wordpress](https://dentedreality.com.au/tags/wordpress/)

Posted on [Flickr](http://www.flickr.com/photos/borkazoid/4854300175/) [8:45 am, July 22, 2010](https://dentedreality.com.au/2010/07/22/chalk-board-door/ "8:45 am") 
jQuery(document).ready(function(){
var gmap\_m18ccf909bd19e34ba31df07bb3027e43 = {
positions : {
945 : new google.maps.LatLng( '45.522999', '-122.656834' )
},
bounds : new google.maps.LatLngBounds(), // empty for now, we'll dynamically extend it later
map : new google.maps.Map(
document.getElementById( 'gmap\_m18ccf909bd19e34ba31df07bb3027e43' ),
{
mapTypeId: google.maps.MapTypeId.ROADMAP,
center: new google.maps.LatLng( 0, 0 ),
zoom: 16 // Seems to be a good zoom for a single point
}
),
markers : {},
}; // end of gmap
// Extend the bounds of interest based on our positions
for ( var m in gmap\_m18ccf909bd19e34ba31df07bb3027e43.positions ) {
gmap\_m18ccf909bd19e34ba31df07bb3027e43.bounds.extend( gmap\_m18ccf909bd19e34ba31df07bb3027e43.positions[m] );
}
// Render markers
for ( var m in gmap\_m18ccf909bd19e34ba31df07bb3027e43.positions ) {
gmap\_m18ccf909bd19e34ba31df07bb3027e43.markers[m] = new google.maps.Marker( {
clickable: true,
map : gmap\_m18ccf909bd19e34ba31df07bb3027e43.map,
position : gmap\_m18ccf909bd19e34ba31df07bb3027e43.positions[m]
} );
}
// Redraw map to fit our new marker-based bounds
gmap\_m18ccf909bd19e34ba31df07bb3027e43.map.setCenter( gmap\_m18ccf909bd19e34ba31df07bb3027e43.positions[945] );
});