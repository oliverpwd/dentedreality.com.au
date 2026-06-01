---
title: Tarmac Exit
date: '2011-05-20T11:15:39+00:00'
format: image
service: flickr
tags:
- meetup
- PDX
- Portland
- teamsocial
image: http://i2.wp.com/dentedreality.com.au/wp-content/uploads/2011/05/5802179217_8e07cc6b4e_o.jpg?resize=607%2C452
---

[![Tarmac Exit](http://i2.wp.com/dentedreality.com.au/wp-content/uploads/2011/05/5802179217_8e07cc6b4e_o.jpg?resize=607%2C452)](http://dentedreality.com.au/2011/05/20/tarmac-exit/) 
# [Tarmac Exit](http://dentedreality.com.au/2011/05/20/tarmac-exit/)

I love getting off planes directly onto the tarmac.





* #[meetup](http://dentedreality.com.au/tags/meetup/)
* #[PDX](http://dentedreality.com.au/tags/pdx/)
* #[Portland](http://dentedreality.com.au/tags/portland/)
* #[teamsocial](http://dentedreality.com.au/tags/teamsocial/)

Posted on [Flickr](http://www.flickr.com/photos/borkazoid/5802179217/) [11:15 am, May 20, 2011](http://dentedreality.com.au/2011/05/20/tarmac-exit/ "11:15 am") 
jQuery(document).ready(function(){
var gmap\_m3018aed38f1945531136f1403f18667d = {
positions : {
802 : new google.maps.LatLng( '45.586833', '-122.592834' )
},
bounds : new google.maps.LatLngBounds(), // empty for now, we'll dynamically extend it later
map : new google.maps.Map(
document.getElementById( 'gmap\_m3018aed38f1945531136f1403f18667d' ),
{
mapTypeId: google.maps.MapTypeId.ROADMAP,
center: new google.maps.LatLng( 0, 0 ),
zoom: 16 // Seems to be a good zoom for a single point
}
),
markers : {},
}; // end of gmap
// Extend the bounds of interest based on our positions
for ( var m in gmap\_m3018aed38f1945531136f1403f18667d.positions ) {
gmap\_m3018aed38f1945531136f1403f18667d.bounds.extend( gmap\_m3018aed38f1945531136f1403f18667d.positions[m] );
}
// Render markers
for ( var m in gmap\_m3018aed38f1945531136f1403f18667d.positions ) {
gmap\_m3018aed38f1945531136f1403f18667d.markers[m] = new google.maps.Marker( {
clickable: true,
map : gmap\_m3018aed38f1945531136f1403f18667d.map,
position : gmap\_m3018aed38f1945531136f1403f18667d.positions[m]
} );
}
// Redraw map to fit our new marker-based bounds
gmap\_m3018aed38f1945531136f1403f18667d.map.setCenter( gmap\_m3018aed38f1945531136f1403f18667d.positions[802] );
});