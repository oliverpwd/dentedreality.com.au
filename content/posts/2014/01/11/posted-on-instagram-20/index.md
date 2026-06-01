---
title: ''
date: '2014-01-11T18:30:42+00:00'
format: image
tags:
- photo
image: http://i0.wp.com/dentedreality.com.au/wp-content/uploads/2014/01/5e0a27987b1811e3b69812d07c665925_8.jpg?resize=640%2C640
---

[![Posted on Instagram](http://i0.wp.com/dentedreality.com.au/wp-content/uploads/2014/01/5e0a27987b1811e3b69812d07c665925_8.jpg?resize=640%2C640)](http://dentedreality.com.au/2014/01/11/posted-on-instagram-20/) 




* #[photo](http://dentedreality.com.au/tags/photo/)

Posted on [Instagram](http://instagram.com/p/jDA0cyCmJm/) [6:30 pm, January 11, 2014](http://dentedreality.com.au/2014/01/11/posted-on-instagram-20/ "6:30 pm") 
jQuery(document).ready(function(){
var gmap\_m2775f9b156cfa9d76cb436d7068f937f = {
positions : {
600 : new google.maps.LatLng( '23.006943231', '-109.71449141' )
},
bounds : new google.maps.LatLngBounds(), // empty for now, we'll dynamically extend it later
map : new google.maps.Map(
document.getElementById( 'gmap\_m2775f9b156cfa9d76cb436d7068f937f' ),
{
mapTypeId: google.maps.MapTypeId.ROADMAP,
center: new google.maps.LatLng( 0, 0 ),
zoom: 16 // Seems to be a good zoom for a single point
}
),
markers : {},
}; // end of gmap
// Extend the bounds of interest based on our positions
for ( var m in gmap\_m2775f9b156cfa9d76cb436d7068f937f.positions ) {
gmap\_m2775f9b156cfa9d76cb436d7068f937f.bounds.extend( gmap\_m2775f9b156cfa9d76cb436d7068f937f.positions[m] );
}
// Render markers
for ( var m in gmap\_m2775f9b156cfa9d76cb436d7068f937f.positions ) {
gmap\_m2775f9b156cfa9d76cb436d7068f937f.markers[m] = new google.maps.Marker( {
clickable: true,
map : gmap\_m2775f9b156cfa9d76cb436d7068f937f.map,
position : gmap\_m2775f9b156cfa9d76cb436d7068f937f.positions[m]
} );
}
// Redraw map to fit our new marker-based bounds
gmap\_m2775f9b156cfa9d76cb436d7068f937f.map.setCenter( gmap\_m2775f9b156cfa9d76cb436d7068f937f.positions[600] );
});