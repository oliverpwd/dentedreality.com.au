---
title: Snowshoeing in Tahoe
date: '2011-04-22T10:30:29+00:00'
format: image
service: flickr
tags:
- beau
- beaulebens
- california
- me
- snow
- snowshoeing
- tahoe
image: http://i0.wp.com/dentedreality.com.au/wp-content/uploads/2011/04/5802703976_e195648dee_o.jpg?resize=607%2C813
---

[![Snowshoeing in Tahoe](http://i0.wp.com/dentedreality.com.au/wp-content/uploads/2011/04/5802703976_e195648dee_o.jpg?resize=607%2C813)](http://dentedreality.com.au/2011/04/22/snowshoeing-in-tahoe/) 
# [Snowshoeing in Tahoe](http://dentedreality.com.au/2011/04/22/snowshoeing-in-tahoe/)





* #[beau](http://dentedreality.com.au/tags/beau/)
* #[beaulebens](http://dentedreality.com.au/tags/beaulebens/)
* #[california](http://dentedreality.com.au/tags/california/)
* #[me](http://dentedreality.com.au/tags/me/)
* #[snow](http://dentedreality.com.au/tags/snow/)
* #[snowshoeing](http://dentedreality.com.au/tags/snowshoeing/)
* #[tahoe](http://dentedreality.com.au/tags/tahoe/)

Posted on [Flickr](http://www.flickr.com/photos/borkazoid/5802703976/) [10:30 am, April 22, 2011](http://dentedreality.com.au/2011/04/22/snowshoeing-in-tahoe/ "10:30 am") 
jQuery(document).ready(function(){
var gmap\_mf73637f77899b32c3ed7f74c9c287e2f = {
positions : {
267 : new google.maps.LatLng( '39.366166', '-120.264834' )
},
bounds : new google.maps.LatLngBounds(), // empty for now, we'll dynamically extend it later
map : new google.maps.Map(
document.getElementById( 'gmap\_mf73637f77899b32c3ed7f74c9c287e2f' ),
{
mapTypeId: google.maps.MapTypeId.ROADMAP,
center: new google.maps.LatLng( 0, 0 ),
zoom: 16 // Seems to be a good zoom for a single point
}
),
markers : {},
}; // end of gmap
// Extend the bounds of interest based on our positions
for ( var m in gmap\_mf73637f77899b32c3ed7f74c9c287e2f.positions ) {
gmap\_mf73637f77899b32c3ed7f74c9c287e2f.bounds.extend( gmap\_mf73637f77899b32c3ed7f74c9c287e2f.positions[m] );
}
// Render markers
for ( var m in gmap\_mf73637f77899b32c3ed7f74c9c287e2f.positions ) {
gmap\_mf73637f77899b32c3ed7f74c9c287e2f.markers[m] = new google.maps.Marker( {
clickable: true,
map : gmap\_mf73637f77899b32c3ed7f74c9c287e2f.map,
position : gmap\_mf73637f77899b32c3ed7f74c9c287e2f.positions[m]
} );
}
// Redraw map to fit our new marker-based bounds
gmap\_mf73637f77899b32c3ed7f74c9c287e2f.map.setCenter( gmap\_mf73637f77899b32c3ed7f74c9c287e2f.positions[267] );
});