---
title: Ouch
date: '2006-12-30T04:11:02+00:00'
format: image
service: flickr
tags:
- boxing
- fight
- muaythai
- phuket
- thaiboxing
- thailand
- thailand06
image: http://i2.wp.com/dentedreality.com.au/wp-content/uploads/2006/12/349559451_f2c7b772cf_o.jpg?resize=607%2C455
---

[![Ouch](http://i2.wp.com/dentedreality.com.au/wp-content/uploads/2006/12/349559451_f2c7b772cf_o.jpg?resize=607%2C455)](http://dentedreality.com.au/2006/12/30/ouch-3/) 
# [Ouch](http://dentedreality.com.au/2006/12/30/ouch-3/)





* #[boxing](http://dentedreality.com.au/tags/boxing/)
* #[fight](http://dentedreality.com.au/tags/fight/)
* #[muaythai](http://dentedreality.com.au/tags/muaythai/)
* #[phuket](http://dentedreality.com.au/tags/phuket/)
* #[thaiboxing](http://dentedreality.com.au/tags/thaiboxing/)
* #[thailand](http://dentedreality.com.au/tags/thailand/)
* #[thailand06](http://dentedreality.com.au/tags/thailand06/)

Posted on [Flickr](http://www.flickr.com/photos/borkazoid/349559451/) [4:11 am, December 30, 2006](http://dentedreality.com.au/2006/12/30/ouch-3/ "4:11 am") 
jQuery(document).ready(function(){
var gmap\_m6c3138949ebd817eb50fb7dd3ff64346 = {
positions : {
523 : new google.maps.LatLng( '7.896794', '98.295879' )
},
bounds : new google.maps.LatLngBounds(), // empty for now, we'll dynamically extend it later
map : new google.maps.Map(
document.getElementById( 'gmap\_m6c3138949ebd817eb50fb7dd3ff64346' ),
{
mapTypeId: google.maps.MapTypeId.ROADMAP,
center: new google.maps.LatLng( 0, 0 ),
zoom: 16 // Seems to be a good zoom for a single point
}
),
markers : {},
}; // end of gmap
// Extend the bounds of interest based on our positions
for ( var m in gmap\_m6c3138949ebd817eb50fb7dd3ff64346.positions ) {
gmap\_m6c3138949ebd817eb50fb7dd3ff64346.bounds.extend( gmap\_m6c3138949ebd817eb50fb7dd3ff64346.positions[m] );
}
// Render markers
for ( var m in gmap\_m6c3138949ebd817eb50fb7dd3ff64346.positions ) {
gmap\_m6c3138949ebd817eb50fb7dd3ff64346.markers[m] = new google.maps.Marker( {
clickable: true,
map : gmap\_m6c3138949ebd817eb50fb7dd3ff64346.map,
position : gmap\_m6c3138949ebd817eb50fb7dd3ff64346.positions[m]
} );
}
// Redraw map to fit our new marker-based bounds
gmap\_m6c3138949ebd817eb50fb7dd3ff64346.map.setCenter( gmap\_m6c3138949ebd817eb50fb7dd3ff64346.positions[523] );
});