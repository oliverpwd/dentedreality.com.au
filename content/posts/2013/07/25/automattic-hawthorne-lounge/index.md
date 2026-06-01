---
title: Automattic, Hawthorne Lounge
date: '2013-07-25T18:57:37+00:00'
format: image
service: flickr
tags:
- automattic
- hawthorne
- sanfrancisco
image: http://i0.wp.com/dentedreality.com.au/wp-content/uploads/2013/07/9437615327_c2b482b3a5_o.jpg?resize=607%2C452
---

[![Automattic, Hawthorne Lounge](http://i0.wp.com/dentedreality.com.au/wp-content/uploads/2013/07/9437615327_c2b482b3a5_o.jpg?resize=607%2C452)](http://dentedreality.com.au/2013/07/25/automattic-hawthorne-lounge/) 
# [Automattic, Hawthorne Lounge](http://dentedreality.com.au/2013/07/25/automattic-hawthorne-lounge/)

Our office space/lounge on Hawthorne St, in SF.





* #[automattic](http://dentedreality.com.au/tags/automattic/)
* #[hawthorne](http://dentedreality.com.au/tags/hawthorne/)
* #[sanfrancisco](http://dentedreality.com.au/tags/sanfrancisco/)

Posted on [Flickr](http://www.flickr.com/photos/borkazoid/9437615327/) [6:57 pm, July 25, 2013](http://dentedreality.com.au/2013/07/25/automattic-hawthorne-lounge/ "6:57 pm") 
jQuery(document).ready(function(){
var gmap\_m7e11a380b615ffc24af411523a6491af = {
positions : {
241 : new google.maps.LatLng( '37.784333', '-122.397' )
},
bounds : new google.maps.LatLngBounds(), // empty for now, we'll dynamically extend it later
map : new google.maps.Map(
document.getElementById( 'gmap\_m7e11a380b615ffc24af411523a6491af' ),
{
mapTypeId: google.maps.MapTypeId.ROADMAP,
center: new google.maps.LatLng( 0, 0 ),
zoom: 16 // Seems to be a good zoom for a single point
}
),
markers : {},
}; // end of gmap
// Extend the bounds of interest based on our positions
for ( var m in gmap\_m7e11a380b615ffc24af411523a6491af.positions ) {
gmap\_m7e11a380b615ffc24af411523a6491af.bounds.extend( gmap\_m7e11a380b615ffc24af411523a6491af.positions[m] );
}
// Render markers
for ( var m in gmap\_m7e11a380b615ffc24af411523a6491af.positions ) {
gmap\_m7e11a380b615ffc24af411523a6491af.markers[m] = new google.maps.Marker( {
clickable: true,
map : gmap\_m7e11a380b615ffc24af411523a6491af.map,
position : gmap\_m7e11a380b615ffc24af411523a6491af.positions[m]
} );
}
// Redraw map to fit our new marker-based bounds
gmap\_m7e11a380b615ffc24af411523a6491af.map.setCenter( gmap\_m7e11a380b615ffc24af411523a6491af.positions[241] );
});