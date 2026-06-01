---
title: Perth Sky
date: '2011-01-02T15:16:00+00:00'
format: image
service: flickr
tags:
- australia
- perth
- sky
image: http://i0.wp.com/dentedreality.com.au/wp-content/uploads/2011/01/5434098895_bd18e1c308_o.jpg?resize=607%2C452
---

[![Perth Sky](http://i0.wp.com/dentedreality.com.au/wp-content/uploads/2011/01/5434098895_bd18e1c308_o.jpg?resize=607%2C452)](http://dentedreality.com.au/2011/01/02/perth-sky/) 
# [Perth Sky](http://dentedreality.com.au/2011/01/02/perth-sky/)





* #[australia](http://dentedreality.com.au/tags/australia/)
* #[perth](http://dentedreality.com.au/tags/perth/)
* #[sky](http://dentedreality.com.au/tags/sky/)

Posted on [Flickr](http://www.flickr.com/photos/borkazoid/5434098895/) [3:16 pm, January 2, 2011](http://dentedreality.com.au/2011/01/02/perth-sky/ "3:16 pm") 
jQuery(document).ready(function(){
var gmap\_m21bac9dc2e8f1b2d60b468887cce5c55 = {
positions : {
646 : new google.maps.LatLng( '-32.053', '115.846499' )
},
bounds : new google.maps.LatLngBounds(), // empty for now, we'll dynamically extend it later
map : new google.maps.Map(
document.getElementById( 'gmap\_m21bac9dc2e8f1b2d60b468887cce5c55' ),
{
mapTypeId: google.maps.MapTypeId.ROADMAP,
center: new google.maps.LatLng( 0, 0 ),
zoom: 16 // Seems to be a good zoom for a single point
}
),
markers : {},
}; // end of gmap
// Extend the bounds of interest based on our positions
for ( var m in gmap\_m21bac9dc2e8f1b2d60b468887cce5c55.positions ) {
gmap\_m21bac9dc2e8f1b2d60b468887cce5c55.bounds.extend( gmap\_m21bac9dc2e8f1b2d60b468887cce5c55.positions[m] );
}
// Render markers
for ( var m in gmap\_m21bac9dc2e8f1b2d60b468887cce5c55.positions ) {
gmap\_m21bac9dc2e8f1b2d60b468887cce5c55.markers[m] = new google.maps.Marker( {
clickable: true,
map : gmap\_m21bac9dc2e8f1b2d60b468887cce5c55.map,
position : gmap\_m21bac9dc2e8f1b2d60b468887cce5c55.positions[m]
} );
}
// Redraw map to fit our new marker-based bounds
gmap\_m21bac9dc2e8f1b2d60b468887cce5c55.map.setCenter( gmap\_m21bac9dc2e8f1b2d60b468887cce5c55.positions[646] );
});