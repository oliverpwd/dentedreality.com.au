---
title: Sydney
date: '2011-01-23T08:45:06+00:00'
format: image
service: flickr
tags:
- australia
- sydney
image: http://i2.wp.com/dentedreality.com.au/wp-content/uploads/2011/01/5434192269_af1b60303e_o.jpg?resize=607%2C452
---

[![Sydney](http://i2.wp.com/dentedreality.com.au/wp-content/uploads/2011/01/5434192269_af1b60303e_o.jpg?resize=607%2C452)](http://dentedreality.com.au/2011/01/23/sydney-5/) 
# [Sydney](http://dentedreality.com.au/2011/01/23/sydney-5/)





* #[australia](http://dentedreality.com.au/tags/australia/)
* #[sydney](http://dentedreality.com.au/tags/sydney/)

Posted on [Flickr](http://www.flickr.com/photos/borkazoid/5434192269/) [8:45 am, January 23, 2011](http://dentedreality.com.au/2011/01/23/sydney-5/ "8:45 am") 
jQuery(document).ready(function(){
var gmap\_m11bc1f6abc97510688957914bbbf0fb8 = {
positions : {
876 : new google.maps.LatLng( '-31.933334', '115.9615' )
},
bounds : new google.maps.LatLngBounds(), // empty for now, we'll dynamically extend it later
map : new google.maps.Map(
document.getElementById( 'gmap\_m11bc1f6abc97510688957914bbbf0fb8' ),
{
mapTypeId: google.maps.MapTypeId.ROADMAP,
center: new google.maps.LatLng( 0, 0 ),
zoom: 16 // Seems to be a good zoom for a single point
}
),
markers : {},
}; // end of gmap
// Extend the bounds of interest based on our positions
for ( var m in gmap\_m11bc1f6abc97510688957914bbbf0fb8.positions ) {
gmap\_m11bc1f6abc97510688957914bbbf0fb8.bounds.extend( gmap\_m11bc1f6abc97510688957914bbbf0fb8.positions[m] );
}
// Render markers
for ( var m in gmap\_m11bc1f6abc97510688957914bbbf0fb8.positions ) {
gmap\_m11bc1f6abc97510688957914bbbf0fb8.markers[m] = new google.maps.Marker( {
clickable: true,
map : gmap\_m11bc1f6abc97510688957914bbbf0fb8.map,
position : gmap\_m11bc1f6abc97510688957914bbbf0fb8.positions[m]
} );
}
// Redraw map to fit our new marker-based bounds
gmap\_m11bc1f6abc97510688957914bbbf0fb8.map.setCenter( gmap\_m11bc1f6abc97510688957914bbbf0fb8.positions[876] );
});