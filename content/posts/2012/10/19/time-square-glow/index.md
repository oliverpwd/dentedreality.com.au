---
title: Time Square Glow
date: '2012-10-19T16:39:53+00:00'
format: image
service: flickr
tags:
- Manhattan
- newyork
- timessquare
image: http://i1.wp.com/dentedreality.com.au/wp-content/uploads/2012/10/8245864374_6fd2a47b6a_o.jpg?resize=607%2C813
---

[![Time Square Glow](http://i1.wp.com/dentedreality.com.au/wp-content/uploads/2012/10/8245864374_6fd2a47b6a_o.jpg?resize=607%2C813)](http://dentedreality.com.au/2012/10/19/time-square-glow/) 
# [Time Square Glow](http://dentedreality.com.au/2012/10/19/time-square-glow/)





* #[Manhattan](http://dentedreality.com.au/tags/manhattan/)
* #[newyork](http://dentedreality.com.au/tags/newyork/)
* #[timessquare](http://dentedreality.com.au/tags/timessquare/)

Posted on [Flickr](http://www.flickr.com/photos/borkazoid/8245864374/) [4:39 pm, October 19, 2012](http://dentedreality.com.au/2012/10/19/time-square-glow/ "4:39 pm") 
jQuery(document).ready(function(){
var gmap\_m5556e2e7ea57fe90043bc1d08bd4097c = {
positions : {
542 : new google.maps.LatLng( '40.760833', '-73.9835' )
},
bounds : new google.maps.LatLngBounds(), // empty for now, we'll dynamically extend it later
map : new google.maps.Map(
document.getElementById( 'gmap\_m5556e2e7ea57fe90043bc1d08bd4097c' ),
{
mapTypeId: google.maps.MapTypeId.ROADMAP,
center: new google.maps.LatLng( 0, 0 ),
zoom: 16 // Seems to be a good zoom for a single point
}
),
markers : {},
}; // end of gmap
// Extend the bounds of interest based on our positions
for ( var m in gmap\_m5556e2e7ea57fe90043bc1d08bd4097c.positions ) {
gmap\_m5556e2e7ea57fe90043bc1d08bd4097c.bounds.extend( gmap\_m5556e2e7ea57fe90043bc1d08bd4097c.positions[m] );
}
// Render markers
for ( var m in gmap\_m5556e2e7ea57fe90043bc1d08bd4097c.positions ) {
gmap\_m5556e2e7ea57fe90043bc1d08bd4097c.markers[m] = new google.maps.Marker( {
clickable: true,
map : gmap\_m5556e2e7ea57fe90043bc1d08bd4097c.map,
position : gmap\_m5556e2e7ea57fe90043bc1d08bd4097c.positions[m]
} );
}
// Redraw map to fit our new marker-based bounds
gmap\_m5556e2e7ea57fe90043bc1d08bd4097c.map.setCenter( gmap\_m5556e2e7ea57fe90043bc1d08bd4097c.positions[542] );
});