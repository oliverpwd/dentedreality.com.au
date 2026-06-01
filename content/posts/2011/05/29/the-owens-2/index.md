---
title: The Owens’
date: '2011-05-29T13:52:38+00:00'
format: image
service: flickr
tags:
- owenswedding
- wedding
image: http://i1.wp.com/dentedreality.com.au/wp-content/uploads/2011/05/5803433000_46934c93ec_o.jpg?resize=607%2C452
---

[![The Owens'](http://i1.wp.com/dentedreality.com.au/wp-content/uploads/2011/05/5803433000_46934c93ec_o.jpg?resize=607%2C452)](http://dentedreality.com.au/2011/05/29/the-owens-2/) 
# [The Owens’](http://dentedreality.com.au/2011/05/29/the-owens-2/)





* #[owenswedding](http://dentedreality.com.au/tags/owenswedding/)
* #[wedding](http://dentedreality.com.au/tags/wedding/)

Posted on [Flickr](http://www.flickr.com/photos/borkazoid/5803433000/) [1:52 pm, May 29, 2011](http://dentedreality.com.au/2011/05/29/the-owens-2/ "1:52 pm") 
jQuery(document).ready(function(){
var gmap\_m553dbec45e9f1953e2bdd4de3a77cef6 = {
positions : {
417 : new google.maps.LatLng( '37.776333', '-122.393834' )
},
bounds : new google.maps.LatLngBounds(), // empty for now, we'll dynamically extend it later
map : new google.maps.Map(
document.getElementById( 'gmap\_m553dbec45e9f1953e2bdd4de3a77cef6' ),
{
mapTypeId: google.maps.MapTypeId.ROADMAP,
center: new google.maps.LatLng( 0, 0 ),
zoom: 16 // Seems to be a good zoom for a single point
}
),
markers : {},
}; // end of gmap
// Extend the bounds of interest based on our positions
for ( var m in gmap\_m553dbec45e9f1953e2bdd4de3a77cef6.positions ) {
gmap\_m553dbec45e9f1953e2bdd4de3a77cef6.bounds.extend( gmap\_m553dbec45e9f1953e2bdd4de3a77cef6.positions[m] );
}
// Render markers
for ( var m in gmap\_m553dbec45e9f1953e2bdd4de3a77cef6.positions ) {
gmap\_m553dbec45e9f1953e2bdd4de3a77cef6.markers[m] = new google.maps.Marker( {
clickable: true,
map : gmap\_m553dbec45e9f1953e2bdd4de3a77cef6.map,
position : gmap\_m553dbec45e9f1953e2bdd4de3a77cef6.positions[m]
} );
}
// Redraw map to fit our new marker-based bounds
gmap\_m553dbec45e9f1953e2bdd4de3a77cef6.map.setCenter( gmap\_m553dbec45e9f1953e2bdd4de3a77cef6.positions[417] );
});