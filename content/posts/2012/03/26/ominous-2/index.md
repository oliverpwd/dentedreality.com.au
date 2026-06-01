---
title: Ominous
date: '2012-03-26T07:59:36+00:00'
format: image
service: flickr
tags:
- clouds
- sky
image: http://i2.wp.com/dentedreality.com.au/wp-content/uploads/2012/03/7770423588_a34a9631c4_o.jpg?resize=607%2C452
---

[![Ominous](http://i2.wp.com/dentedreality.com.au/wp-content/uploads/2012/03/7770423588_a34a9631c4_o.jpg?resize=607%2C452)](http://dentedreality.com.au/2012/03/26/ominous-2/) 
# [Ominous](http://dentedreality.com.au/2012/03/26/ominous-2/)





* #[clouds](http://dentedreality.com.au/tags/clouds/)
* #[sky](http://dentedreality.com.au/tags/sky/)

Posted on [Flickr](http://www.flickr.com/photos/borkazoid/7770423588/) [7:59 am, March 26, 2012](http://dentedreality.com.au/2012/03/26/ominous-2/ "7:59 am") 
jQuery(document).ready(function(){
var gmap\_m027260c1325779382ef8bd413f150cdd = {
positions : {
150 : new google.maps.LatLng( '37.783833', '-122.391167' )
},
bounds : new google.maps.LatLngBounds(), // empty for now, we'll dynamically extend it later
map : new google.maps.Map(
document.getElementById( 'gmap\_m027260c1325779382ef8bd413f150cdd' ),
{
mapTypeId: google.maps.MapTypeId.ROADMAP,
center: new google.maps.LatLng( 0, 0 ),
zoom: 16 // Seems to be a good zoom for a single point
}
),
markers : {},
}; // end of gmap
// Extend the bounds of interest based on our positions
for ( var m in gmap\_m027260c1325779382ef8bd413f150cdd.positions ) {
gmap\_m027260c1325779382ef8bd413f150cdd.bounds.extend( gmap\_m027260c1325779382ef8bd413f150cdd.positions[m] );
}
// Render markers
for ( var m in gmap\_m027260c1325779382ef8bd413f150cdd.positions ) {
gmap\_m027260c1325779382ef8bd413f150cdd.markers[m] = new google.maps.Marker( {
clickable: true,
map : gmap\_m027260c1325779382ef8bd413f150cdd.map,
position : gmap\_m027260c1325779382ef8bd413f150cdd.positions[m]
} );
}
// Redraw map to fit our new marker-based bounds
gmap\_m027260c1325779382ef8bd413f150cdd.map.setCenter( gmap\_m027260c1325779382ef8bd413f150cdd.positions[150] );
});