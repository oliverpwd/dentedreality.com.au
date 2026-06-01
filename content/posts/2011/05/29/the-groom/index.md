---
title: The Groom
date: '2011-05-29T11:03:37+00:00'
format: image
service: flickr
tags:
- owenswedding
- wedding
image: http://i0.wp.com/dentedreality.com.au/wp-content/uploads/2011/05/5802874777_858de1eebf_o.jpg?resize=607%2C813
---

[![The Groom](http://i0.wp.com/dentedreality.com.au/wp-content/uploads/2011/05/5802874777_858de1eebf_o.jpg?resize=607%2C813)](http://dentedreality.com.au/2011/05/29/the-groom/) 
# [The Groom](http://dentedreality.com.au/2011/05/29/the-groom/)





* #[owenswedding](http://dentedreality.com.au/tags/owenswedding/)
* #[wedding](http://dentedreality.com.au/tags/wedding/)

Posted on [Flickr](http://www.flickr.com/photos/borkazoid/5802874777/) [11:03 am, May 29, 2011](http://dentedreality.com.au/2011/05/29/the-groom/ "11:03 am") 
jQuery(document).ready(function(){
var gmap\_mc09cf308b63c5d54788c83149cab8c54 = {
positions : {
455 : new google.maps.LatLng( '37.771166', '-122.412834' )
},
bounds : new google.maps.LatLngBounds(), // empty for now, we'll dynamically extend it later
map : new google.maps.Map(
document.getElementById( 'gmap\_mc09cf308b63c5d54788c83149cab8c54' ),
{
mapTypeId: google.maps.MapTypeId.ROADMAP,
center: new google.maps.LatLng( 0, 0 ),
zoom: 16 // Seems to be a good zoom for a single point
}
),
markers : {},
}; // end of gmap
// Extend the bounds of interest based on our positions
for ( var m in gmap\_mc09cf308b63c5d54788c83149cab8c54.positions ) {
gmap\_mc09cf308b63c5d54788c83149cab8c54.bounds.extend( gmap\_mc09cf308b63c5d54788c83149cab8c54.positions[m] );
}
// Render markers
for ( var m in gmap\_mc09cf308b63c5d54788c83149cab8c54.positions ) {
gmap\_mc09cf308b63c5d54788c83149cab8c54.markers[m] = new google.maps.Marker( {
clickable: true,
map : gmap\_mc09cf308b63c5d54788c83149cab8c54.map,
position : gmap\_mc09cf308b63c5d54788c83149cab8c54.positions[m]
} );
}
// Redraw map to fit our new marker-based bounds
gmap\_mc09cf308b63c5d54788c83149cab8c54.map.setCenter( gmap\_mc09cf308b63c5d54788c83149cab8c54.positions[455] );
});