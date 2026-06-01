---
title: Denver Meetup
date: '2013-11-17T12:16:22+00:00'
format: image
service: flickr
tags:
- automattic
- colorado
- Denver
- meetup
- mercury
- vision:face=099
- vision:outdoor=0756
- vision:people=099
image: http://i1.wp.com/dentedreality.com.au/wp-content/uploads/2013/11/12291142885_dda406d2a9_o.jpg?resize=607%2C455
---

[![Denver Meetup](http://i1.wp.com/dentedreality.com.au/wp-content/uploads/2013/11/12291142885_dda406d2a9_o.jpg?resize=607%2C455)](http://dentedreality.com.au/2013/11/17/denver-meetup-21/) 
# [Denver Meetup](http://dentedreality.com.au/2013/11/17/denver-meetup-21/)

Team Mercury meetup (and a few days after) in Denver, Colorado.





* #[automattic](http://dentedreality.com.au/tags/automattic/)
* #[colorado](http://dentedreality.com.au/tags/colorado/)
* #[Denver](http://dentedreality.com.au/tags/denver/)
* #[meetup](http://dentedreality.com.au/tags/meetup/)
* #[mercury](http://dentedreality.com.au/tags/mercury/)
* #[vision:face=099](http://dentedreality.com.au/tags/visionface099/)
* #[vision:outdoor=0756](http://dentedreality.com.au/tags/visionoutdoor0756/)
* #[vision:people=099](http://dentedreality.com.au/tags/visionpeople099/)

Posted on [Flickr](http://www.flickr.com/photos/borkazoid/12291142885/) [12:16 pm, November 17, 2013](http://dentedreality.com.au/2013/11/17/denver-meetup-21/ "12:16 pm") 
jQuery(document).ready(function(){
var gmap\_m61dfebfc6a2d484c79b2bbb8d7d06094 = {
positions : {
517 : new google.maps.LatLng( '39.712466', '-104.998559' )
},
bounds : new google.maps.LatLngBounds(), // empty for now, we'll dynamically extend it later
map : new google.maps.Map(
document.getElementById( 'gmap\_m61dfebfc6a2d484c79b2bbb8d7d06094' ),
{
mapTypeId: google.maps.MapTypeId.ROADMAP,
center: new google.maps.LatLng( 0, 0 ),
zoom: 16 // Seems to be a good zoom for a single point
}
),
markers : {},
}; // end of gmap
// Extend the bounds of interest based on our positions
for ( var m in gmap\_m61dfebfc6a2d484c79b2bbb8d7d06094.positions ) {
gmap\_m61dfebfc6a2d484c79b2bbb8d7d06094.bounds.extend( gmap\_m61dfebfc6a2d484c79b2bbb8d7d06094.positions[m] );
}
// Render markers
for ( var m in gmap\_m61dfebfc6a2d484c79b2bbb8d7d06094.positions ) {
gmap\_m61dfebfc6a2d484c79b2bbb8d7d06094.markers[m] = new google.maps.Marker( {
clickable: true,
map : gmap\_m61dfebfc6a2d484c79b2bbb8d7d06094.map,
position : gmap\_m61dfebfc6a2d484c79b2bbb8d7d06094.positions[m]
} );
}
// Redraw map to fit our new marker-based bounds
gmap\_m61dfebfc6a2d484c79b2bbb8d7d06094.map.setCenter( gmap\_m61dfebfc6a2d484c79b2bbb8d7d06094.positions[517] );
});