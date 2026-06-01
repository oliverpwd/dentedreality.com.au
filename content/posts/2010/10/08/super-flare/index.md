---
title: Super Flare!
date: '2010-10-08T11:37:39+00:00'
format: image
service: flickr
tags:
- iphone4
- lensflare
- sun
image: http://i1.wp.com/dentedreality.com.au/wp-content/uploads/2010/10/5183766628_ec9771026f_o.jpg?resize=607%2C452
---

[![Super Flare!](http://i1.wp.com/dentedreality.com.au/wp-content/uploads/2010/10/5183766628_ec9771026f_o.jpg?resize=607%2C452)](http://dentedreality.com.au/2010/10/08/super-flare/) 
# [Super Flare!](http://dentedreality.com.au/2010/10/08/super-flare/)





* #[iphone4](http://dentedreality.com.au/tags/iphone4/)
* #[lensflare](http://dentedreality.com.au/tags/lensflare/)
* #[sun](http://dentedreality.com.au/tags/sun/)

Posted on [Flickr](http://www.flickr.com/photos/borkazoid/5183766628/) [11:37 am, October 8, 2010](http://dentedreality.com.au/2010/10/08/super-flare/ "11:37 am") 
jQuery(document).ready(function(){
var gmap\_m42aac7c53e97b366c82d7f020fa9e91d = {
positions : {
993 : new google.maps.LatLng( '37.784', '-122.390667' )
},
bounds : new google.maps.LatLngBounds(), // empty for now, we'll dynamically extend it later
map : new google.maps.Map(
document.getElementById( 'gmap\_m42aac7c53e97b366c82d7f020fa9e91d' ),
{
mapTypeId: google.maps.MapTypeId.ROADMAP,
center: new google.maps.LatLng( 0, 0 ),
zoom: 16 // Seems to be a good zoom for a single point
}
),
markers : {},
}; // end of gmap
// Extend the bounds of interest based on our positions
for ( var m in gmap\_m42aac7c53e97b366c82d7f020fa9e91d.positions ) {
gmap\_m42aac7c53e97b366c82d7f020fa9e91d.bounds.extend( gmap\_m42aac7c53e97b366c82d7f020fa9e91d.positions[m] );
}
// Render markers
for ( var m in gmap\_m42aac7c53e97b366c82d7f020fa9e91d.positions ) {
gmap\_m42aac7c53e97b366c82d7f020fa9e91d.markers[m] = new google.maps.Marker( {
clickable: true,
map : gmap\_m42aac7c53e97b366c82d7f020fa9e91d.map,
position : gmap\_m42aac7c53e97b366c82d7f020fa9e91d.positions[m]
} );
}
// Redraw map to fit our new marker-based bounds
gmap\_m42aac7c53e97b366c82d7f020fa9e91d.map.setCenter( gmap\_m42aac7c53e97b366c82d7f020fa9e91d.positions[993] );
});