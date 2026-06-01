---
title: Denver Meetup
date: '2013-11-17T12:30:46+00:00'
format: image
service: flickr
tags:
- automattic
- colorado
- Denver
- meetup
- mercury
- vision:car=0622
- vision:sky=0597
image: http://i1.wp.com/dentedreality.com.au/wp-content/uploads/2013/11/12291561604_f865e82d4a_o.jpg?resize=607%2C455
---

[![Denver Meetup](http://i1.wp.com/dentedreality.com.au/wp-content/uploads/2013/11/12291561604_f865e82d4a_o.jpg?resize=607%2C455)](http://dentedreality.com.au/2013/11/17/denver-meetup-19/) 
# [Denver Meetup](http://dentedreality.com.au/2013/11/17/denver-meetup-19/)

Team Mercury meetup (and a few days after) in Denver, Colorado.





* #[automattic](http://dentedreality.com.au/tags/automattic/)
* #[colorado](http://dentedreality.com.au/tags/colorado/)
* #[Denver](http://dentedreality.com.au/tags/denver/)
* #[meetup](http://dentedreality.com.au/tags/meetup/)
* #[mercury](http://dentedreality.com.au/tags/mercury/)
* #[vision:car=0622](http://dentedreality.com.au/tags/visioncar0622/)
* #[vision:sky=0597](http://dentedreality.com.au/tags/visionsky0597/)

Posted on [Flickr](http://www.flickr.com/photos/borkazoid/12291561604/) [12:30 pm, November 17, 2013](http://dentedreality.com.au/2013/11/17/denver-meetup-19/ "12:30 pm") 
jQuery(document).ready(function(){
var gmap\_m4d9ef89a40af09f584e2ef292dd0f5b8 = {
positions : {
63 : new google.maps.LatLng( '39.712452', '-104.99865' )
},
bounds : new google.maps.LatLngBounds(), // empty for now, we'll dynamically extend it later
map : new google.maps.Map(
document.getElementById( 'gmap\_m4d9ef89a40af09f584e2ef292dd0f5b8' ),
{
mapTypeId: google.maps.MapTypeId.ROADMAP,
center: new google.maps.LatLng( 0, 0 ),
zoom: 16 // Seems to be a good zoom for a single point
}
),
markers : {},
}; // end of gmap
// Extend the bounds of interest based on our positions
for ( var m in gmap\_m4d9ef89a40af09f584e2ef292dd0f5b8.positions ) {
gmap\_m4d9ef89a40af09f584e2ef292dd0f5b8.bounds.extend( gmap\_m4d9ef89a40af09f584e2ef292dd0f5b8.positions[m] );
}
// Render markers
for ( var m in gmap\_m4d9ef89a40af09f584e2ef292dd0f5b8.positions ) {
gmap\_m4d9ef89a40af09f584e2ef292dd0f5b8.markers[m] = new google.maps.Marker( {
clickable: true,
map : gmap\_m4d9ef89a40af09f584e2ef292dd0f5b8.map,
position : gmap\_m4d9ef89a40af09f584e2ef292dd0f5b8.positions[m]
} );
}
// Redraw map to fit our new marker-based bounds
gmap\_m4d9ef89a40af09f584e2ef292dd0f5b8.map.setCenter( gmap\_m4d9ef89a40af09f584e2ef292dd0f5b8.positions[63] );
});