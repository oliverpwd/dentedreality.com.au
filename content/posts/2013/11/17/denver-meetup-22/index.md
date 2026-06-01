---
title: Denver Meetup
date: '2013-11-17T12:14:52+00:00'
format: image
service: flickr
tags:
- automattic
- colorado
- Denver
- meetup
- mercury
- vision:outdoor=0691
image: http://i1.wp.com/dentedreality.com.au/wp-content/uploads/2013/11/12291701506_4d41207ddf_o.jpg?resize=607%2C455
---

[![Denver Meetup](http://i1.wp.com/dentedreality.com.au/wp-content/uploads/2013/11/12291701506_4d41207ddf_o.jpg?resize=607%2C455)](http://dentedreality.com.au/2013/11/17/denver-meetup-22/) 
# [Denver Meetup](http://dentedreality.com.au/2013/11/17/denver-meetup-22/)

Team Mercury meetup (and a few days after) in Denver, Colorado.





* #[automattic](http://dentedreality.com.au/tags/automattic/)
* #[colorado](http://dentedreality.com.au/tags/colorado/)
* #[Denver](http://dentedreality.com.au/tags/denver/)
* #[meetup](http://dentedreality.com.au/tags/meetup/)
* #[mercury](http://dentedreality.com.au/tags/mercury/)
* #[vision:outdoor=0691](http://dentedreality.com.au/tags/visionoutdoor0691/)

Posted on [Flickr](http://www.flickr.com/photos/borkazoid/12291701506/) [12:14 pm, November 17, 2013](http://dentedreality.com.au/2013/11/17/denver-meetup-22/ "12:14 pm") 
jQuery(document).ready(function(){
var gmap\_m7979aa0555fca778f9c45b356407f08f = {
positions : {
35 : new google.maps.LatLng( '39.7122', '-104.998681' )
},
bounds : new google.maps.LatLngBounds(), // empty for now, we'll dynamically extend it later
map : new google.maps.Map(
document.getElementById( 'gmap\_m7979aa0555fca778f9c45b356407f08f' ),
{
mapTypeId: google.maps.MapTypeId.ROADMAP,
center: new google.maps.LatLng( 0, 0 ),
zoom: 16 // Seems to be a good zoom for a single point
}
),
markers : {},
}; // end of gmap
// Extend the bounds of interest based on our positions
for ( var m in gmap\_m7979aa0555fca778f9c45b356407f08f.positions ) {
gmap\_m7979aa0555fca778f9c45b356407f08f.bounds.extend( gmap\_m7979aa0555fca778f9c45b356407f08f.positions[m] );
}
// Render markers
for ( var m in gmap\_m7979aa0555fca778f9c45b356407f08f.positions ) {
gmap\_m7979aa0555fca778f9c45b356407f08f.markers[m] = new google.maps.Marker( {
clickable: true,
map : gmap\_m7979aa0555fca778f9c45b356407f08f.map,
position : gmap\_m7979aa0555fca778f9c45b356407f08f.positions[m]
} );
}
// Redraw map to fit our new marker-based bounds
gmap\_m7979aa0555fca778f9c45b356407f08f.map.setCenter( gmap\_m7979aa0555fca778f9c45b356407f08f.positions[35] );
});