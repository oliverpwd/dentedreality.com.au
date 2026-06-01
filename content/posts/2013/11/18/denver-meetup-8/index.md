---
title: Denver Meetup
date: '2013-11-18T08:58:22+00:00'
format: image
service: flickr
tags:
- automattic
- colorado
- Denver
- meetup
- mercury
- vision:clouds=0903
- vision:mountain=0883
- vision:outdoor=099
- vision:sky=096
image: http://i0.wp.com/dentedreality.com.au/wp-content/uploads/2013/11/12291129585_8fe6ce4f24_o.jpg?resize=607%2C455
---

[![Denver Meetup](http://i0.wp.com/dentedreality.com.au/wp-content/uploads/2013/11/12291129585_8fe6ce4f24_o.jpg?resize=607%2C455)](http://dentedreality.com.au/2013/11/18/denver-meetup-8/) 
# [Denver Meetup](http://dentedreality.com.au/2013/11/18/denver-meetup-8/)

Team Mercury meetup (and a few days after) in Denver, Colorado.





* #[automattic](http://dentedreality.com.au/tags/automattic/)
* #[colorado](http://dentedreality.com.au/tags/colorado/)
* #[Denver](http://dentedreality.com.au/tags/denver/)
* #[meetup](http://dentedreality.com.au/tags/meetup/)
* #[mercury](http://dentedreality.com.au/tags/mercury/)
* #[vision:clouds=0903](http://dentedreality.com.au/tags/visionclouds0903/)
* #[vision:mountain=0883](http://dentedreality.com.au/tags/visionmountain0883/)
* #[vision:outdoor=099](http://dentedreality.com.au/tags/visionoutdoor099/)
* #[vision:sky=096](http://dentedreality.com.au/tags/visionsky096/)

Posted on [Flickr](http://www.flickr.com/photos/borkazoid/12291129585/) [8:58 am, November 18, 2013](http://dentedreality.com.au/2013/11/18/denver-meetup-8/ "8:58 am") 
jQuery(document).ready(function(){
var gmap\_m0b7d210f202ae1df0080e47ae3579dce = {
positions : {
179 : new google.maps.LatLng( '39.660841', '-105.203462' )
},
bounds : new google.maps.LatLngBounds(), // empty for now, we'll dynamically extend it later
map : new google.maps.Map(
document.getElementById( 'gmap\_m0b7d210f202ae1df0080e47ae3579dce' ),
{
mapTypeId: google.maps.MapTypeId.ROADMAP,
center: new google.maps.LatLng( 0, 0 ),
zoom: 16 // Seems to be a good zoom for a single point
}
),
markers : {},
}; // end of gmap
// Extend the bounds of interest based on our positions
for ( var m in gmap\_m0b7d210f202ae1df0080e47ae3579dce.positions ) {
gmap\_m0b7d210f202ae1df0080e47ae3579dce.bounds.extend( gmap\_m0b7d210f202ae1df0080e47ae3579dce.positions[m] );
}
// Render markers
for ( var m in gmap\_m0b7d210f202ae1df0080e47ae3579dce.positions ) {
gmap\_m0b7d210f202ae1df0080e47ae3579dce.markers[m] = new google.maps.Marker( {
clickable: true,
map : gmap\_m0b7d210f202ae1df0080e47ae3579dce.map,
position : gmap\_m0b7d210f202ae1df0080e47ae3579dce.positions[m]
} );
}
// Redraw map to fit our new marker-based bounds
gmap\_m0b7d210f202ae1df0080e47ae3579dce.map.setCenter( gmap\_m0b7d210f202ae1df0080e47ae3579dce.positions[179] );
});