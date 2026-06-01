---
title: Stanky Leg!
date: '2012-01-12T06:18:35+00:00'
format: image
service: flickr
tags:
- automattic
- hawaii
- jjj
- johnjamesjacoby
- kailua
- meetup
- teamsocial
image: http://i2.wp.com/dentedreality.com.au/wp-content/uploads/2012/01/6959542275_3626b6ffba_o.jpg?resize=607%2C813
---

[![Stanky Leg!](http://i2.wp.com/dentedreality.com.au/wp-content/uploads/2012/01/6959542275_3626b6ffba_o.jpg?resize=607%2C813)](http://dentedreality.com.au/2012/01/12/stanky-leg/) 
# [Stanky Leg!](http://dentedreality.com.au/2012/01/12/stanky-leg/)

J-tripped.





* #[automattic](http://dentedreality.com.au/tags/automattic/)
* #[hawaii](http://dentedreality.com.au/tags/hawaii/)
* #[jjj](http://dentedreality.com.au/tags/jjj/)
* #[johnjamesjacoby](http://dentedreality.com.au/tags/johnjamesjacoby/)
* #[kailua](http://dentedreality.com.au/tags/kailua/)
* #[meetup](http://dentedreality.com.au/tags/meetup/)
* #[teamsocial](http://dentedreality.com.au/tags/teamsocial/)

Posted on [Flickr](http://www.flickr.com/photos/borkazoid/6959542275/) [6:18 am, January 12, 2012](http://dentedreality.com.au/2012/01/12/stanky-leg/ "6:18 am") 
jQuery(document).ready(function(){
var gmap\_m66ab27c64170bbd27b5673fd08ac4ade = {
positions : {
476 : new google.maps.LatLng( '21.410999', '-157.742334' )
},
bounds : new google.maps.LatLngBounds(), // empty for now, we'll dynamically extend it later
map : new google.maps.Map(
document.getElementById( 'gmap\_m66ab27c64170bbd27b5673fd08ac4ade' ),
{
mapTypeId: google.maps.MapTypeId.ROADMAP,
center: new google.maps.LatLng( 0, 0 ),
zoom: 16 // Seems to be a good zoom for a single point
}
),
markers : {},
}; // end of gmap
// Extend the bounds of interest based on our positions
for ( var m in gmap\_m66ab27c64170bbd27b5673fd08ac4ade.positions ) {
gmap\_m66ab27c64170bbd27b5673fd08ac4ade.bounds.extend( gmap\_m66ab27c64170bbd27b5673fd08ac4ade.positions[m] );
}
// Render markers
for ( var m in gmap\_m66ab27c64170bbd27b5673fd08ac4ade.positions ) {
gmap\_m66ab27c64170bbd27b5673fd08ac4ade.markers[m] = new google.maps.Marker( {
clickable: true,
map : gmap\_m66ab27c64170bbd27b5673fd08ac4ade.map,
position : gmap\_m66ab27c64170bbd27b5673fd08ac4ade.positions[m]
} );
}
// Redraw map to fit our new marker-based bounds
gmap\_m66ab27c64170bbd27b5673fd08ac4ade.map.setCenter( gmap\_m66ab27c64170bbd27b5673fd08ac4ade.positions[476] );
});