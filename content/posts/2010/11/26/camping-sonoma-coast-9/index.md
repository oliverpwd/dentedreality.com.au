---
title: Camping, Sonoma Coast
date: '2010-11-26T11:46:45+00:00'
format: image
service: flickr
tags:
- california
- camping
- sonomacoast
image: http://i1.wp.com/dentedreality.com.au/wp-content/uploads/2010/11/5434024315_74b936a328_o.jpg?resize=607%2C452
---

[![Camping, Sonoma Coast](http://i1.wp.com/dentedreality.com.au/wp-content/uploads/2010/11/5434024315_74b936a328_o.jpg?resize=607%2C452)](http://dentedreality.com.au/2010/11/26/camping-sonoma-coast-9/) 
# [Camping, Sonoma Coast](http://dentedreality.com.au/2010/11/26/camping-sonoma-coast-9/)





* #[california](http://dentedreality.com.au/tags/california/)
* #[camping](http://dentedreality.com.au/tags/camping/)
* #[sonomacoast](http://dentedreality.com.au/tags/sonomacoast/)

Posted on [Flickr](http://www.flickr.com/photos/borkazoid/5434024315/) [11:46 am, November 26, 2010](http://dentedreality.com.au/2010/11/26/camping-sonoma-coast-9/ "11:46 am") 
jQuery(document).ready(function(){
var gmap\_m5c523361d931bde249f3398e4632603f = {
positions : {
604 : new google.maps.LatLng( '38.412166', '-123.101167' )
},
bounds : new google.maps.LatLngBounds(), // empty for now, we'll dynamically extend it later
map : new google.maps.Map(
document.getElementById( 'gmap\_m5c523361d931bde249f3398e4632603f' ),
{
mapTypeId: google.maps.MapTypeId.ROADMAP,
center: new google.maps.LatLng( 0, 0 ),
zoom: 16 // Seems to be a good zoom for a single point
}
),
markers : {},
}; // end of gmap
// Extend the bounds of interest based on our positions
for ( var m in gmap\_m5c523361d931bde249f3398e4632603f.positions ) {
gmap\_m5c523361d931bde249f3398e4632603f.bounds.extend( gmap\_m5c523361d931bde249f3398e4632603f.positions[m] );
}
// Render markers
for ( var m in gmap\_m5c523361d931bde249f3398e4632603f.positions ) {
gmap\_m5c523361d931bde249f3398e4632603f.markers[m] = new google.maps.Marker( {
clickable: true,
map : gmap\_m5c523361d931bde249f3398e4632603f.map,
position : gmap\_m5c523361d931bde249f3398e4632603f.positions[m]
} );
}
// Redraw map to fit our new marker-based bounds
gmap\_m5c523361d931bde249f3398e4632603f.map.setCenter( gmap\_m5c523361d931bde249f3398e4632603f.positions[604] );
});