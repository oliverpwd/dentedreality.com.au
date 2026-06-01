---
title: Bouncy Light Bridge
date: '2013-08-29T16:29:45+00:00'
format: image
tags:
- bridge
- brooklyn
image: http://i1.wp.com/dentedreality.com.au/wp-content/uploads/2013/08/9767970646_d1f69fb9c2_o.jpg?resize=607%2C452
---

[![Bouncy Light Bridge](http://i1.wp.com/dentedreality.com.au/wp-content/uploads/2013/08/9767970646_d1f69fb9c2_o.jpg?resize=607%2C452)](http://dentedreality.com.au/2013/08/29/bouncy-light-bridge/) 
# [Bouncy Light Bridge](http://dentedreality.com.au/2013/08/29/bouncy-light-bridge/)

Going over to Brooklyn Bridge Park





* #[bridge](http://dentedreality.com.au/tags/bridge/)
* #[brooklyn](http://dentedreality.com.au/tags/brooklyn/)

Posted on [Flickr](http://www.flickr.com/photos/borkazoid/9767970646/) [4:29 pm, August 29, 2013](http://dentedreality.com.au/2013/08/29/bouncy-light-bridge/ "4:29 pm") 
jQuery(document).ready(function(){
var gmap\_macdd59ef3c403f125a7984b980323fd6 = {
positions : {
87 : new google.maps.LatLng( '40.700666', '-73.996' )
},
bounds : new google.maps.LatLngBounds(), // empty for now, we'll dynamically extend it later
map : new google.maps.Map(
document.getElementById( 'gmap\_macdd59ef3c403f125a7984b980323fd6' ),
{
mapTypeId: google.maps.MapTypeId.ROADMAP,
center: new google.maps.LatLng( 0, 0 ),
zoom: 16 // Seems to be a good zoom for a single point
}
),
markers : {},
}; // end of gmap
// Extend the bounds of interest based on our positions
for ( var m in gmap\_macdd59ef3c403f125a7984b980323fd6.positions ) {
gmap\_macdd59ef3c403f125a7984b980323fd6.bounds.extend( gmap\_macdd59ef3c403f125a7984b980323fd6.positions[m] );
}
// Render markers
for ( var m in gmap\_macdd59ef3c403f125a7984b980323fd6.positions ) {
gmap\_macdd59ef3c403f125a7984b980323fd6.markers[m] = new google.maps.Marker( {
clickable: true,
map : gmap\_macdd59ef3c403f125a7984b980323fd6.map,
position : gmap\_macdd59ef3c403f125a7984b980323fd6.positions[m]
} );
}
// Redraw map to fit our new marker-based bounds
gmap\_macdd59ef3c403f125a7984b980323fd6.map.setCenter( gmap\_macdd59ef3c403f125a7984b980323fd6.positions[87] );
});