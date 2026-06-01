---
title: ''
date: '2016-03-20T16:06:47+00:00'
format: image
service: instagram
tags:
- gardenbeds
- pavers
- paving
- veggiegarden
- yard
image: http://i2.wp.com/dentedreality.com.au/wp-content/uploads/2016/03/11934860_204306876601116_435617604_n.jpg?fit=640%2C640
---

[![Pretty happy with how the yard is coming together.](http://i2.wp.com/dentedreality.com.au/wp-content/uploads/2016/03/11934860_204306876601116_435617604_n.jpg?fit=640%2C640)](http://dentedreality.com.au/2016/03/20/pretty-happy-with-how-the-yard-is-coming-together/) 

Pretty happy with how the yard is coming together.





* #[gardenbeds](http://dentedreality.com.au/tags/gardenbeds/)
* #[pavers](http://dentedreality.com.au/tags/pavers/)
* #[paving](http://dentedreality.com.au/tags/paving/)
* #[veggiegarden](http://dentedreality.com.au/tags/veggiegarden/)
* #[yard](http://dentedreality.com.au/tags/yard/)

Posted on [Instagram](https://www.instagram.com/p/BDMOW-EimHN/) [4:06 pm, March 20, 2016](http://dentedreality.com.au/2016/03/20/pretty-happy-with-how-the-yard-is-coming-together/ "4:06 pm") 
jQuery(document).ready(function(){
var gmap\_m80ca23f52c8f0e1a5b1367d5bba67d13 = {
positions : {
569 : new google.maps.LatLng( '39.7392', '-104.984' )
},
bounds : new google.maps.LatLngBounds(), // empty for now, we'll dynamically extend it later
map : new google.maps.Map(
document.getElementById( 'gmap\_m80ca23f52c8f0e1a5b1367d5bba67d13' ),
{
mapTypeId: google.maps.MapTypeId.ROADMAP,
center: new google.maps.LatLng( 0, 0 ),
zoom: 16 // Seems to be a good zoom for a single point
}
),
markers : {},
}; // end of gmap
// Extend the bounds of interest based on our positions
for ( var m in gmap\_m80ca23f52c8f0e1a5b1367d5bba67d13.positions ) {
gmap\_m80ca23f52c8f0e1a5b1367d5bba67d13.bounds.extend( gmap\_m80ca23f52c8f0e1a5b1367d5bba67d13.positions[m] );
}
// Render markers
for ( var m in gmap\_m80ca23f52c8f0e1a5b1367d5bba67d13.positions ) {
gmap\_m80ca23f52c8f0e1a5b1367d5bba67d13.markers[m] = new google.maps.Marker( {
clickable: true,
map : gmap\_m80ca23f52c8f0e1a5b1367d5bba67d13.map,
position : gmap\_m80ca23f52c8f0e1a5b1367d5bba67d13.positions[m]
} );
}
// Redraw map to fit our new marker-based bounds
gmap\_m80ca23f52c8f0e1a5b1367d5bba67d13.map.setCenter( gmap\_m80ca23f52c8f0e1a5b1367d5bba67d13.positions[569] );
});