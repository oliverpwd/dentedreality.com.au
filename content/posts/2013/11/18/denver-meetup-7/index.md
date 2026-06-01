---
title: Denver Meetup
date: '2013-11-18T08:58:39+00:00'
format: image
service: flickr
tags:
- automattic
- colorado
- Denver
- meetup
- mercury
- vision:clouds=0903
- vision:mountain=0627
- vision:outdoor=0957
- vision:sky=0964
image: http://i0.wp.com/dentedreality.com.au/wp-content/uploads/2013/11/12291286183_1b5e07da63_o.jpg?resize=607%2C455
---

[![Denver Meetup](http://i0.wp.com/dentedreality.com.au/wp-content/uploads/2013/11/12291286183_1b5e07da63_o.jpg?resize=607%2C455)](http://dentedreality.com.au/2013/11/18/denver-meetup-7/) 
# [Denver Meetup](http://dentedreality.com.au/2013/11/18/denver-meetup-7/)

Team Mercury meetup (and a few days after) in Denver, Colorado.





* #[automattic](http://dentedreality.com.au/tags/automattic/)
* #[colorado](http://dentedreality.com.au/tags/colorado/)
* #[Denver](http://dentedreality.com.au/tags/denver/)
* #[meetup](http://dentedreality.com.au/tags/meetup/)
* #[mercury](http://dentedreality.com.au/tags/mercury/)
* #[vision:clouds=0903](http://dentedreality.com.au/tags/visionclouds0903/)
* #[vision:mountain=0627](http://dentedreality.com.au/tags/visionmountain0627/)
* #[vision:outdoor=0957](http://dentedreality.com.au/tags/visionoutdoor0957/)
* #[vision:sky=0964](http://dentedreality.com.au/tags/visionsky0964/)

Posted on [Flickr](http://www.flickr.com/photos/borkazoid/12291286183/) [8:58 am, November 18, 2013](http://dentedreality.com.au/2013/11/18/denver-meetup-7/ "8:58 am") 
jQuery(document).ready(function(){
var gmap\_md71004b303f13ab40178c72a89d3772a = {
positions : {
692 : new google.maps.LatLng( '39.660861', '-105.203545' )
},
bounds : new google.maps.LatLngBounds(), // empty for now, we'll dynamically extend it later
map : new google.maps.Map(
document.getElementById( 'gmap\_md71004b303f13ab40178c72a89d3772a' ),
{
mapTypeId: google.maps.MapTypeId.ROADMAP,
center: new google.maps.LatLng( 0, 0 ),
zoom: 16 // Seems to be a good zoom for a single point
}
),
markers : {},
}; // end of gmap
// Extend the bounds of interest based on our positions
for ( var m in gmap\_md71004b303f13ab40178c72a89d3772a.positions ) {
gmap\_md71004b303f13ab40178c72a89d3772a.bounds.extend( gmap\_md71004b303f13ab40178c72a89d3772a.positions[m] );
}
// Render markers
for ( var m in gmap\_md71004b303f13ab40178c72a89d3772a.positions ) {
gmap\_md71004b303f13ab40178c72a89d3772a.markers[m] = new google.maps.Marker( {
clickable: true,
map : gmap\_md71004b303f13ab40178c72a89d3772a.map,
position : gmap\_md71004b303f13ab40178c72a89d3772a.positions[m]
} );
}
// Redraw map to fit our new marker-based bounds
gmap\_md71004b303f13ab40178c72a89d3772a.map.setCenter( gmap\_md71004b303f13ab40178c72a89d3772a.positions[692] );
});