---
title: Memorial Day
date: '2010-05-30T13:49:09+00:00'
format: image
service: flickr
tags:
- bridge
- ggb
- goldengatebridge
- memorialday
- sanfrancisco
image: http://i0.wp.com/dentedreality.com.au/wp-content/uploads/2010/05/4746456673_c3cdc36c8c_o.jpg?resize=607%2C455
---

[![Memorial Day](http://i0.wp.com/dentedreality.com.au/wp-content/uploads/2010/05/4746456673_c3cdc36c8c_o.jpg?resize=607%2C455)](http://dentedreality.com.au/2010/05/30/memorial-day-2/) 
# [Memorial Day](http://dentedreality.com.au/2010/05/30/memorial-day-2/)





* #[bridge](http://dentedreality.com.au/tags/bridge/)
* #[ggb](http://dentedreality.com.au/tags/ggb/)
* #[goldengatebridge](http://dentedreality.com.au/tags/goldengatebridge/)
* #[memorialday](http://dentedreality.com.au/tags/memorialday/)
* #[sanfrancisco](http://dentedreality.com.au/tags/sanfrancisco/)

Posted on [Flickr](http://www.flickr.com/photos/borkazoid/4746456673/) [1:49 pm, May 30, 2010](http://dentedreality.com.au/2010/05/30/memorial-day-2/ "1:49 pm") 
jQuery(document).ready(function(){
var gmap\_m2209e65e7b4b3c9ed5efb04f2a33b45b = {
positions : {
237 : new google.maps.LatLng( '37.806333', '-122.469667' )
},
bounds : new google.maps.LatLngBounds(), // empty for now, we'll dynamically extend it later
map : new google.maps.Map(
document.getElementById( 'gmap\_m2209e65e7b4b3c9ed5efb04f2a33b45b' ),
{
mapTypeId: google.maps.MapTypeId.ROADMAP,
center: new google.maps.LatLng( 0, 0 ),
zoom: 16 // Seems to be a good zoom for a single point
}
),
markers : {},
}; // end of gmap
// Extend the bounds of interest based on our positions
for ( var m in gmap\_m2209e65e7b4b3c9ed5efb04f2a33b45b.positions ) {
gmap\_m2209e65e7b4b3c9ed5efb04f2a33b45b.bounds.extend( gmap\_m2209e65e7b4b3c9ed5efb04f2a33b45b.positions[m] );
}
// Render markers
for ( var m in gmap\_m2209e65e7b4b3c9ed5efb04f2a33b45b.positions ) {
gmap\_m2209e65e7b4b3c9ed5efb04f2a33b45b.markers[m] = new google.maps.Marker( {
clickable: true,
map : gmap\_m2209e65e7b4b3c9ed5efb04f2a33b45b.map,
position : gmap\_m2209e65e7b4b3c9ed5efb04f2a33b45b.positions[m]
} );
}
// Redraw map to fit our new marker-based bounds
gmap\_m2209e65e7b4b3c9ed5efb04f2a33b45b.map.setCenter( gmap\_m2209e65e7b4b3c9ed5efb04f2a33b45b.positions[237] );
});