---
title: Epic Australian Adventure, 2014
date: '2014-03-25T18:00:25+00:00'
format: image
service: flickr
tags:
- Melbourne
image: http://i2.wp.com/dentedreality.com.au/wp-content/uploads/2014/03/13904757992_4a3f6ac199_o.jpg?resize=607%2C455
---

[![Epic Australian Adventure, 2014](http://i2.wp.com/dentedreality.com.au/wp-content/uploads/2014/03/13904757992_4a3f6ac199_o.jpg?resize=607%2C455)](http://dentedreality.com.au/2014/03/25/epic-australian-adventure-2014-30/) 
# [Epic Australian Adventure, 2014](http://dentedreality.com.au/2014/03/25/epic-australian-adventure-2014-30/)

Perth, Mooloolaba and Melbourne





* #[Melbourne](http://dentedreality.com.au/tags/melbourne/)

Posted on [Flickr](http://www.flickr.com/photos/borkazoid/13904757992/) [6:00 pm, March 25, 2014](http://dentedreality.com.au/2014/03/25/epic-australian-adventure-2014-30/ "6:00 pm") 
jQuery(document).ready(function(){
var gmap\_m259ce9b9848909c250ec30cf9494c47b = {
positions : {
42 : new google.maps.LatLng( '-37.819028', '144.967955' )
},
bounds : new google.maps.LatLngBounds(), // empty for now, we'll dynamically extend it later
map : new google.maps.Map(
document.getElementById( 'gmap\_m259ce9b9848909c250ec30cf9494c47b' ),
{
mapTypeId: google.maps.MapTypeId.ROADMAP,
center: new google.maps.LatLng( 0, 0 ),
zoom: 16 // Seems to be a good zoom for a single point
}
),
markers : {},
}; // end of gmap
// Extend the bounds of interest based on our positions
for ( var m in gmap\_m259ce9b9848909c250ec30cf9494c47b.positions ) {
gmap\_m259ce9b9848909c250ec30cf9494c47b.bounds.extend( gmap\_m259ce9b9848909c250ec30cf9494c47b.positions[m] );
}
// Render markers
for ( var m in gmap\_m259ce9b9848909c250ec30cf9494c47b.positions ) {
gmap\_m259ce9b9848909c250ec30cf9494c47b.markers[m] = new google.maps.Marker( {
clickable: true,
map : gmap\_m259ce9b9848909c250ec30cf9494c47b.map,
position : gmap\_m259ce9b9848909c250ec30cf9494c47b.positions[m]
} );
}
// Redraw map to fit our new marker-based bounds
gmap\_m259ce9b9848909c250ec30cf9494c47b.map.setCenter( gmap\_m259ce9b9848909c250ec30cf9494c47b.positions[42] );
});