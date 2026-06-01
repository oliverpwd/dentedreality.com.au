---
title: Thanksgiving, 2010
date: '2010-11-25T13:01:43+00:00'
format: image
service: flickr
tags:
- thanksgiving
- turkey
image: http://i1.wp.com/dentedreality.com.au/wp-content/uploads/2010/11/5434636668_d72966d865_o.jpg?resize=607%2C452
---

[![Thanksgiving, 2010](http://i1.wp.com/dentedreality.com.au/wp-content/uploads/2010/11/5434636668_d72966d865_o.jpg?resize=607%2C452)](http://dentedreality.com.au/2010/11/25/thanksgiving-2010/) 
# [Thanksgiving, 2010](http://dentedreality.com.au/2010/11/25/thanksgiving-2010/)

Chris and Marci hosted an amazing dinner.





* #[thanksgiving](http://dentedreality.com.au/tags/thanksgiving/)
* #[turkey](http://dentedreality.com.au/tags/turkey/)

Posted on [Flickr](http://www.flickr.com/photos/borkazoid/5434636668/) [1:01 pm, November 25, 2010](http://dentedreality.com.au/2010/11/25/thanksgiving-2010/ "1:01 pm") 
jQuery(document).ready(function(){
var gmap\_maf30b9f35a479d26c620f36a40557ed8 = {
positions : {
378 : new google.maps.LatLng( '37.795666', '-122.425167' )
},
bounds : new google.maps.LatLngBounds(), // empty for now, we'll dynamically extend it later
map : new google.maps.Map(
document.getElementById( 'gmap\_maf30b9f35a479d26c620f36a40557ed8' ),
{
mapTypeId: google.maps.MapTypeId.ROADMAP,
center: new google.maps.LatLng( 0, 0 ),
zoom: 16 // Seems to be a good zoom for a single point
}
),
markers : {},
}; // end of gmap
// Extend the bounds of interest based on our positions
for ( var m in gmap\_maf30b9f35a479d26c620f36a40557ed8.positions ) {
gmap\_maf30b9f35a479d26c620f36a40557ed8.bounds.extend( gmap\_maf30b9f35a479d26c620f36a40557ed8.positions[m] );
}
// Render markers
for ( var m in gmap\_maf30b9f35a479d26c620f36a40557ed8.positions ) {
gmap\_maf30b9f35a479d26c620f36a40557ed8.markers[m] = new google.maps.Marker( {
clickable: true,
map : gmap\_maf30b9f35a479d26c620f36a40557ed8.map,
position : gmap\_maf30b9f35a479d26c620f36a40557ed8.positions[m]
} );
}
// Redraw map to fit our new marker-based bounds
gmap\_maf30b9f35a479d26c620f36a40557ed8.map.setCenter( gmap\_maf30b9f35a479d26c620f36a40557ed8.positions[378] );
});