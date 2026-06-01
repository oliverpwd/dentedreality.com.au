---
title: Denver Meetup
date: '2013-11-18T08:37:47+00:00'
format: image
service: flickr
tags:
- automattic
- colorado
- Denver
- meetup
- mercury
- vision:clouds=0594
- vision:mountain=0851
- vision:outdoor=0986
- vision:sky=0971
image: http://i1.wp.com/dentedreality.com.au/wp-content/uploads/2013/11/12291558534_a28d04f08e_o.jpg?resize=607%2C455
---

[![Denver Meetup](http://i1.wp.com/dentedreality.com.au/wp-content/uploads/2013/11/12291558534_a28d04f08e_o.jpg?resize=607%2C455)](http://dentedreality.com.au/2013/11/18/denver-meetup-13/) 
# [Denver Meetup](http://dentedreality.com.au/2013/11/18/denver-meetup-13/)

Team Mercury meetup (and a few days after) in Denver, Colorado.





* #[automattic](http://dentedreality.com.au/tags/automattic/)
* #[colorado](http://dentedreality.com.au/tags/colorado/)
* #[Denver](http://dentedreality.com.au/tags/denver/)
* #[meetup](http://dentedreality.com.au/tags/meetup/)
* #[mercury](http://dentedreality.com.au/tags/mercury/)
* #[vision:clouds=0594](http://dentedreality.com.au/tags/visionclouds0594/)
* #[vision:mountain=0851](http://dentedreality.com.au/tags/visionmountain0851/)
* #[vision:outdoor=0986](http://dentedreality.com.au/tags/visionoutdoor0986/)
* #[vision:sky=0971](http://dentedreality.com.au/tags/visionsky0971/)

Posted on [Flickr](http://www.flickr.com/photos/borkazoid/12291558534/) [8:37 am, November 18, 2013](http://dentedreality.com.au/2013/11/18/denver-meetup-13/ "8:37 am") 
jQuery(document).ready(function(){
var gmap\_m359511b318396fa1a5c21567cf3e8ab6 = {
positions : {
225 : new google.maps.LatLng( '39.66368', '-105.202912' )
},
bounds : new google.maps.LatLngBounds(), // empty for now, we'll dynamically extend it later
map : new google.maps.Map(
document.getElementById( 'gmap\_m359511b318396fa1a5c21567cf3e8ab6' ),
{
mapTypeId: google.maps.MapTypeId.ROADMAP,
center: new google.maps.LatLng( 0, 0 ),
zoom: 16 // Seems to be a good zoom for a single point
}
),
markers : {},
}; // end of gmap
// Extend the bounds of interest based on our positions
for ( var m in gmap\_m359511b318396fa1a5c21567cf3e8ab6.positions ) {
gmap\_m359511b318396fa1a5c21567cf3e8ab6.bounds.extend( gmap\_m359511b318396fa1a5c21567cf3e8ab6.positions[m] );
}
// Render markers
for ( var m in gmap\_m359511b318396fa1a5c21567cf3e8ab6.positions ) {
gmap\_m359511b318396fa1a5c21567cf3e8ab6.markers[m] = new google.maps.Marker( {
clickable: true,
map : gmap\_m359511b318396fa1a5c21567cf3e8ab6.map,
position : gmap\_m359511b318396fa1a5c21567cf3e8ab6.positions[m]
} );
}
// Redraw map to fit our new marker-based bounds
gmap\_m359511b318396fa1a5c21567cf3e8ab6.map.setCenter( gmap\_m359511b318396fa1a5c21567cf3e8ab6.positions[225] );
});