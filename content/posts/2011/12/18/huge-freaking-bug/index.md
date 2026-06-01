---
title: Huge Freaking Bug!
date: '2011-12-18T13:47:13+00:00'
format: image
service: flickr
tags:
- bug
- insect
image: http://i1.wp.com/dentedreality.com.au/wp-content/uploads/2011/12/6959402595_e2f0252448_o.jpg?resize=607%2C813
---

[![Huge Freaking Bug!](http://i1.wp.com/dentedreality.com.au/wp-content/uploads/2011/12/6959402595_e2f0252448_o.jpg?resize=607%2C813)](http://dentedreality.com.au/2011/12/18/huge-freaking-bug/) 
# [Huge Freaking Bug!](http://dentedreality.com.au/2011/12/18/huge-freaking-bug/)





* #[bug](http://dentedreality.com.au/tags/bug/)
* #[insect](http://dentedreality.com.au/tags/insect/)

Posted on [Flickr](http://www.flickr.com/photos/borkazoid/6959402595/) [1:47 pm, December 18, 2011](http://dentedreality.com.au/2011/12/18/huge-freaking-bug/ "1:47 pm") 
jQuery(document).ready(function(){
var gmap\_m6609cf5823551113f42d99152aed752f = {
positions : {
925 : new google.maps.LatLng( '37.743833', '-122.435667' )
},
bounds : new google.maps.LatLngBounds(), // empty for now, we'll dynamically extend it later
map : new google.maps.Map(
document.getElementById( 'gmap\_m6609cf5823551113f42d99152aed752f' ),
{
mapTypeId: google.maps.MapTypeId.ROADMAP,
center: new google.maps.LatLng( 0, 0 ),
zoom: 16 // Seems to be a good zoom for a single point
}
),
markers : {},
}; // end of gmap
// Extend the bounds of interest based on our positions
for ( var m in gmap\_m6609cf5823551113f42d99152aed752f.positions ) {
gmap\_m6609cf5823551113f42d99152aed752f.bounds.extend( gmap\_m6609cf5823551113f42d99152aed752f.positions[m] );
}
// Render markers
for ( var m in gmap\_m6609cf5823551113f42d99152aed752f.positions ) {
gmap\_m6609cf5823551113f42d99152aed752f.markers[m] = new google.maps.Marker( {
clickable: true,
map : gmap\_m6609cf5823551113f42d99152aed752f.map,
position : gmap\_m6609cf5823551113f42d99152aed752f.positions[m]
} );
}
// Redraw map to fit our new marker-based bounds
gmap\_m6609cf5823551113f42d99152aed752f.map.setCenter( gmap\_m6609cf5823551113f42d99152aed752f.positions[925] );
});