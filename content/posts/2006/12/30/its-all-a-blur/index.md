---
title: It’s all a blur
date: '2006-12-30T05:39:14+00:00'
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
image: http://i0.wp.com/dentedreality.com.au/wp-content/uploads/2006/12/349557078_17155b57d0_o.jpg?resize=607%2C455
---

[![It's all a blur](http://i0.wp.com/dentedreality.com.au/wp-content/uploads/2006/12/349557078_17155b57d0_o.jpg?resize=607%2C455)](http://dentedreality.com.au/2006/12/30/its-all-a-blur/) 
# [It’s all a blur](http://dentedreality.com.au/2006/12/30/its-all-a-blur/)

Punch, kick, knee, elbow, it’s all good.





* #[boxing](http://dentedreality.com.au/tags/boxing/)
* #[fight](http://dentedreality.com.au/tags/fight/)
* #[muaythai](http://dentedreality.com.au/tags/muaythai/)
* #[phuket](http://dentedreality.com.au/tags/phuket/)
* #[thaiboxing](http://dentedreality.com.au/tags/thaiboxing/)
* #[thailand](http://dentedreality.com.au/tags/thailand/)
* #[thailand06](http://dentedreality.com.au/tags/thailand06/)

Posted on [Flickr](http://www.flickr.com/photos/borkazoid/349557078/) [5:39 am, December 30, 2006](http://dentedreality.com.au/2006/12/30/its-all-a-blur/ "5:39 am") 
jQuery(document).ready(function(){
var gmap\_ma122e3c62761917765c593b613a2df1a = {
positions : {
151 : new google.maps.LatLng( '7.896794', '98.295879' )
},
bounds : new google.maps.LatLngBounds(), // empty for now, we'll dynamically extend it later
map : new google.maps.Map(
document.getElementById( 'gmap\_ma122e3c62761917765c593b613a2df1a' ),
{
mapTypeId: google.maps.MapTypeId.ROADMAP,
center: new google.maps.LatLng( 0, 0 ),
zoom: 16 // Seems to be a good zoom for a single point
}
),
markers : {},
}; // end of gmap
// Extend the bounds of interest based on our positions
for ( var m in gmap\_ma122e3c62761917765c593b613a2df1a.positions ) {
gmap\_ma122e3c62761917765c593b613a2df1a.bounds.extend( gmap\_ma122e3c62761917765c593b613a2df1a.positions[m] );
}
// Render markers
for ( var m in gmap\_ma122e3c62761917765c593b613a2df1a.positions ) {
gmap\_ma122e3c62761917765c593b613a2df1a.markers[m] = new google.maps.Marker( {
clickable: true,
map : gmap\_ma122e3c62761917765c593b613a2df1a.map,
position : gmap\_ma122e3c62761917765c593b613a2df1a.positions[m]
} );
}
// Redraw map to fit our new marker-based bounds
gmap\_ma122e3c62761917765c593b613a2df1a.map.setCenter( gmap\_ma122e3c62761917765c593b613a2df1a.positions[151] );
});