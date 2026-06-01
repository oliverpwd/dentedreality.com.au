---
title: Denver Meetup
date: '2013-11-21T13:03:42+00:00'
format: image
service: flickr
tags:
- automattic
- colorado
- Denver
- meetup
- mercury
- vision:car=0691
- vision:outdoor=0734
- vision:sky=0619
- vision:sunset=0598
- vision:text=0708
image: http://i2.wp.com/dentedreality.com.au/wp-content/uploads/2013/11/12291289583_618ab2e8d4_o.jpg?resize=607%2C809
---

[![Denver Meetup](http://i2.wp.com/dentedreality.com.au/wp-content/uploads/2013/11/12291289583_618ab2e8d4_o.jpg?resize=607%2C809)](http://dentedreality.com.au/2013/11/21/denver-meetup-3/) 
# [Denver Meetup](http://dentedreality.com.au/2013/11/21/denver-meetup-3/)

Team Mercury meetup (and a few days after) in Denver, Colorado.





* #[automattic](http://dentedreality.com.au/tags/automattic/)
* #[colorado](http://dentedreality.com.au/tags/colorado/)
* #[Denver](http://dentedreality.com.au/tags/denver/)
* #[meetup](http://dentedreality.com.au/tags/meetup/)
* #[mercury](http://dentedreality.com.au/tags/mercury/)
* #[vision:car=0691](http://dentedreality.com.au/tags/visioncar0691/)
* #[vision:outdoor=0734](http://dentedreality.com.au/tags/visionoutdoor0734/)
* #[vision:sky=0619](http://dentedreality.com.au/tags/visionsky0619/)
* #[vision:sunset=0598](http://dentedreality.com.au/tags/visionsunset0598/)
* #[vision:text=0708](http://dentedreality.com.au/tags/visiontext0708/)

Posted on [Flickr](http://www.flickr.com/photos/borkazoid/12291289583/) [1:03 pm, November 21, 2013](http://dentedreality.com.au/2013/11/21/denver-meetup-3/ "1:03 pm") 
jQuery(document).ready(function(){
var gmap\_mb403c78acec0ac634578f342e00d7885 = {
positions : {
363 : new google.maps.LatLng( '39.743466', '-104.980837' )
},
bounds : new google.maps.LatLngBounds(), // empty for now, we'll dynamically extend it later
map : new google.maps.Map(
document.getElementById( 'gmap\_mb403c78acec0ac634578f342e00d7885' ),
{
mapTypeId: google.maps.MapTypeId.ROADMAP,
center: new google.maps.LatLng( 0, 0 ),
zoom: 16 // Seems to be a good zoom for a single point
}
),
markers : {},
}; // end of gmap
// Extend the bounds of interest based on our positions
for ( var m in gmap\_mb403c78acec0ac634578f342e00d7885.positions ) {
gmap\_mb403c78acec0ac634578f342e00d7885.bounds.extend( gmap\_mb403c78acec0ac634578f342e00d7885.positions[m] );
}
// Render markers
for ( var m in gmap\_mb403c78acec0ac634578f342e00d7885.positions ) {
gmap\_mb403c78acec0ac634578f342e00d7885.markers[m] = new google.maps.Marker( {
clickable: true,
map : gmap\_mb403c78acec0ac634578f342e00d7885.map,
position : gmap\_mb403c78acec0ac634578f342e00d7885.positions[m]
} );
}
// Redraw map to fit our new marker-based bounds
gmap\_mb403c78acec0ac634578f342e00d7885.map.setCenter( gmap\_mb403c78acec0ac634578f342e00d7885.positions[363] );
});