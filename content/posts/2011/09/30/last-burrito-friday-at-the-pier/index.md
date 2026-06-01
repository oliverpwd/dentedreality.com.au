---
title: Last Burrito Friday at the Pier
date: '2011-09-30T09:16:36+00:00'
format: image
service: flickr
tags:
- automattic
- burritofriday
- thepier
- wordpress
image: http://i1.wp.com/dentedreality.com.au/wp-content/uploads/2011/09/6958246979_4d2f526993_o.jpg?resize=607%2C452
---

[![Last Burrito Friday at the Pier](http://i1.wp.com/dentedreality.com.au/wp-content/uploads/2011/09/6958246979_4d2f526993_o.jpg?resize=607%2C452)](http://dentedreality.com.au/2011/09/30/last-burrito-friday-at-the-pier/) 
# [Last Burrito Friday at the Pier](http://dentedreality.com.au/2011/09/30/last-burrito-friday-at-the-pier/)

This was our last lunch #burritofriday at the Automattic Lounge/Pier 38





* #[automattic](http://dentedreality.com.au/tags/automattic/)
* #[burritofriday](http://dentedreality.com.au/tags/burritofriday/)
* #[thepier](http://dentedreality.com.au/tags/thepier/)
* #[wordpress](http://dentedreality.com.au/tags/wordpress/)

Posted on [Flickr](http://www.flickr.com/photos/borkazoid/6958246979/) [9:16 am, September 30, 2011](http://dentedreality.com.au/2011/09/30/last-burrito-friday-at-the-pier/ "9:16 am") 
jQuery(document).ready(function(){
var gmap\_m3f70801c9ca77744c0c78a4050860773 = {
positions : {
885 : new google.maps.LatLng( '37.782833', '-122.387834' )
},
bounds : new google.maps.LatLngBounds(), // empty for now, we'll dynamically extend it later
map : new google.maps.Map(
document.getElementById( 'gmap\_m3f70801c9ca77744c0c78a4050860773' ),
{
mapTypeId: google.maps.MapTypeId.ROADMAP,
center: new google.maps.LatLng( 0, 0 ),
zoom: 16 // Seems to be a good zoom for a single point
}
),
markers : {},
}; // end of gmap
// Extend the bounds of interest based on our positions
for ( var m in gmap\_m3f70801c9ca77744c0c78a4050860773.positions ) {
gmap\_m3f70801c9ca77744c0c78a4050860773.bounds.extend( gmap\_m3f70801c9ca77744c0c78a4050860773.positions[m] );
}
// Render markers
for ( var m in gmap\_m3f70801c9ca77744c0c78a4050860773.positions ) {
gmap\_m3f70801c9ca77744c0c78a4050860773.markers[m] = new google.maps.Marker( {
clickable: true,
map : gmap\_m3f70801c9ca77744c0c78a4050860773.map,
position : gmap\_m3f70801c9ca77744c0c78a4050860773.positions[m]
} );
}
// Redraw map to fit our new marker-based bounds
gmap\_m3f70801c9ca77744c0c78a4050860773.map.setCenter( gmap\_m3f70801c9ca77744c0c78a4050860773.positions[885] );
});