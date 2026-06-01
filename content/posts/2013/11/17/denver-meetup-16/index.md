---
title: Denver Meetup
date: '2013-11-17T15:33:49+00:00'
format: image
service: flickr
tags:
- automattic
- colorado
- Denver
- meetup
- mercury
- vision:flower=0709
- vision:plant=0748
- vision:sky=0616
image: http://i0.wp.com/dentedreality.com.au/wp-content/uploads/2013/11/12291297983_f1d09183d5_o.jpg?resize=607%2C607
---

[![Denver Meetup](http://i0.wp.com/dentedreality.com.au/wp-content/uploads/2013/11/12291297983_f1d09183d5_o.jpg?resize=607%2C607)](http://dentedreality.com.au/2013/11/17/denver-meetup-16/) 
# [Denver Meetup](http://dentedreality.com.au/2013/11/17/denver-meetup-16/)

Team Mercury meetup (and a few days after) in Denver, Colorado.





* #[automattic](http://dentedreality.com.au/tags/automattic/)
* #[colorado](http://dentedreality.com.au/tags/colorado/)
* #[Denver](http://dentedreality.com.au/tags/denver/)
* #[meetup](http://dentedreality.com.au/tags/meetup/)
* #[mercury](http://dentedreality.com.au/tags/mercury/)
* #[vision:flower=0709](http://dentedreality.com.au/tags/visionflower0709/)
* #[vision:plant=0748](http://dentedreality.com.au/tags/visionplant0748/)
* #[vision:sky=0616](http://dentedreality.com.au/tags/visionsky0616/)

Posted on [Flickr](http://www.flickr.com/photos/borkazoid/12291297983/) [3:33 pm, November 17, 2013](http://dentedreality.com.au/2013/11/17/denver-meetup-16/ "3:33 pm") 
jQuery(document).ready(function(){
var gmap\_m746e3fa8bbbc8d012f853b965ae406d8 = {
positions : {
209 : new google.maps.LatLng( '39.7486', '-105.0075' )
},
bounds : new google.maps.LatLngBounds(), // empty for now, we'll dynamically extend it later
map : new google.maps.Map(
document.getElementById( 'gmap\_m746e3fa8bbbc8d012f853b965ae406d8' ),
{
mapTypeId: google.maps.MapTypeId.ROADMAP,
center: new google.maps.LatLng( 0, 0 ),
zoom: 16 // Seems to be a good zoom for a single point
}
),
markers : {},
}; // end of gmap
// Extend the bounds of interest based on our positions
for ( var m in gmap\_m746e3fa8bbbc8d012f853b965ae406d8.positions ) {
gmap\_m746e3fa8bbbc8d012f853b965ae406d8.bounds.extend( gmap\_m746e3fa8bbbc8d012f853b965ae406d8.positions[m] );
}
// Render markers
for ( var m in gmap\_m746e3fa8bbbc8d012f853b965ae406d8.positions ) {
gmap\_m746e3fa8bbbc8d012f853b965ae406d8.markers[m] = new google.maps.Marker( {
clickable: true,
map : gmap\_m746e3fa8bbbc8d012f853b965ae406d8.map,
position : gmap\_m746e3fa8bbbc8d012f853b965ae406d8.positions[m]
} );
}
// Redraw map to fit our new marker-based bounds
gmap\_m746e3fa8bbbc8d012f853b965ae406d8.map.setCenter( gmap\_m746e3fa8bbbc8d012f853b965ae406d8.positions[209] );
});