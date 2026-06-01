---
title: Denver Meetup
date: '2013-11-21T05:57:39+00:00'
format: image
service: flickr
tags:
- automattic
- colorado
- Denver
- meetup
- mercury
- vision:mountain=0512
- vision:outdoor=0964
- vision:sky=0724
- vision:snow=0805
image: http://i1.wp.com/dentedreality.com.au/wp-content/uploads/2013/11/12291691326_79af5e0bc4_o.jpg?resize=607%2C455
---

[![Denver Meetup](http://i1.wp.com/dentedreality.com.au/wp-content/uploads/2013/11/12291691326_79af5e0bc4_o.jpg?resize=607%2C455)](http://dentedreality.com.au/2013/11/21/denver-meetup-4/) 
# [Denver Meetup](http://dentedreality.com.au/2013/11/21/denver-meetup-4/)

Team Mercury meetup (and a few days after) in Denver, Colorado.





* #[automattic](http://dentedreality.com.au/tags/automattic/)
* #[colorado](http://dentedreality.com.au/tags/colorado/)
* #[Denver](http://dentedreality.com.au/tags/denver/)
* #[meetup](http://dentedreality.com.au/tags/meetup/)
* #[mercury](http://dentedreality.com.au/tags/mercury/)
* #[vision:mountain=0512](http://dentedreality.com.au/tags/visionmountain0512/)
* #[vision:outdoor=0964](http://dentedreality.com.au/tags/visionoutdoor0964/)
* #[vision:sky=0724](http://dentedreality.com.au/tags/visionsky0724/)
* #[vision:snow=0805](http://dentedreality.com.au/tags/visionsnow0805/)

Posted on [Flickr](http://www.flickr.com/photos/borkazoid/12291691326/) [5:57 am, November 21, 2013](http://dentedreality.com.au/2013/11/21/denver-meetup-4/ "5:57 am") 
jQuery(document).ready(function(){
var gmap\_m529e990bc86278469c3af840971132b6 = {
positions : {
391 : new google.maps.LatLng( '39.737136', '-104.98327' )
},
bounds : new google.maps.LatLngBounds(), // empty for now, we'll dynamically extend it later
map : new google.maps.Map(
document.getElementById( 'gmap\_m529e990bc86278469c3af840971132b6' ),
{
mapTypeId: google.maps.MapTypeId.ROADMAP,
center: new google.maps.LatLng( 0, 0 ),
zoom: 16 // Seems to be a good zoom for a single point
}
),
markers : {},
}; // end of gmap
// Extend the bounds of interest based on our positions
for ( var m in gmap\_m529e990bc86278469c3af840971132b6.positions ) {
gmap\_m529e990bc86278469c3af840971132b6.bounds.extend( gmap\_m529e990bc86278469c3af840971132b6.positions[m] );
}
// Render markers
for ( var m in gmap\_m529e990bc86278469c3af840971132b6.positions ) {
gmap\_m529e990bc86278469c3af840971132b6.markers[m] = new google.maps.Marker( {
clickable: true,
map : gmap\_m529e990bc86278469c3af840971132b6.map,
position : gmap\_m529e990bc86278469c3af840971132b6.positions[m]
} );
}
// Redraw map to fit our new marker-based bounds
gmap\_m529e990bc86278469c3af840971132b6.map.setCenter( gmap\_m529e990bc86278469c3af840971132b6.positions[391] );
});