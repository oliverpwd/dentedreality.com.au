---
title: I’m Campin’
date: '2006-11-25T08:55:57+00:00'
format: image
service: flickr
tags:
- appletree
- beau
- beaulebens
- bigsur
- bottchersgap
- california
- dayhike
- devilspeak
- hiking
- lospadresnationalpark
- me
- pinecreek
image: http://i2.wp.com/dentedreality.com.au/wp-content/uploads/2006/11/308098869_a9b65ebb3c_o.jpg?resize=607%2C455
---

[![I'm Campin'](http://i2.wp.com/dentedreality.com.au/wp-content/uploads/2006/11/308098869_a9b65ebb3c_o.jpg?resize=607%2C455)](http://dentedreality.com.au/2006/11/25/im-campin/) 
# [I’m Campin’](http://dentedreality.com.au/2006/11/25/im-campin/)

Day hike from near Apple Tree (up from Bottcher’s Gap), heading around past Devil’s Peak towards Pine Creek campsite.





* #[appletree](http://dentedreality.com.au/tags/appletree/)
* #[beau](http://dentedreality.com.au/tags/beau/)
* #[beaulebens](http://dentedreality.com.au/tags/beaulebens/)
* #[bigsur](http://dentedreality.com.au/tags/bigsur/)
* #[bottchersgap](http://dentedreality.com.au/tags/bottchersgap/)
* #[california](http://dentedreality.com.au/tags/california/)
* #[dayhike](http://dentedreality.com.au/tags/dayhike/)
* #[devilspeak](http://dentedreality.com.au/tags/devilspeak/)
* #[hiking](http://dentedreality.com.au/tags/hiking/)
* #[lospadresnationalpark](http://dentedreality.com.au/tags/lospadresnationalpark/)
* #[me](http://dentedreality.com.au/tags/me/)
* #[pinecreek](http://dentedreality.com.au/tags/pinecreek/)

Posted on [Flickr](http://www.flickr.com/photos/borkazoid/308098869/) [8:55 am, November 25, 2006](http://dentedreality.com.au/2006/11/25/im-campin/ "8:55 am") 
jQuery(document).ready(function(){
var gmap\_m9730f522126f51d384652b3c8369f27e = {
positions : {
448 : new google.maps.LatLng( '36.34389', '-121.776409' )
},
bounds : new google.maps.LatLngBounds(), // empty for now, we'll dynamically extend it later
map : new google.maps.Map(
document.getElementById( 'gmap\_m9730f522126f51d384652b3c8369f27e' ),
{
mapTypeId: google.maps.MapTypeId.ROADMAP,
center: new google.maps.LatLng( 0, 0 ),
zoom: 16 // Seems to be a good zoom for a single point
}
),
markers : {},
}; // end of gmap
// Extend the bounds of interest based on our positions
for ( var m in gmap\_m9730f522126f51d384652b3c8369f27e.positions ) {
gmap\_m9730f522126f51d384652b3c8369f27e.bounds.extend( gmap\_m9730f522126f51d384652b3c8369f27e.positions[m] );
}
// Render markers
for ( var m in gmap\_m9730f522126f51d384652b3c8369f27e.positions ) {
gmap\_m9730f522126f51d384652b3c8369f27e.markers[m] = new google.maps.Marker( {
clickable: true,
map : gmap\_m9730f522126f51d384652b3c8369f27e.map,
position : gmap\_m9730f522126f51d384652b3c8369f27e.positions[m]
} );
}
// Redraw map to fit our new marker-based bounds
gmap\_m9730f522126f51d384652b3c8369f27e.map.setCenter( gmap\_m9730f522126f51d384652b3c8369f27e.positions[448] );
});