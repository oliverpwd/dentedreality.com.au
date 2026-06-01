---
title: Crabs
date: '2013-07-14T14:11:44+00:00'
format: image
service: flickr
tags:
- beau
- beaulebens
- costarica
- crab
- hermitcrab
- me
image: http://i0.wp.com/dentedreality.com.au/wp-content/uploads/2013/07/9437410377_c4acc8ae15_o.jpg?resize=607%2C455
---

[![Crabs](http://i0.wp.com/dentedreality.com.au/wp-content/uploads/2013/07/9437410377_c4acc8ae15_o.jpg?resize=607%2C455)](http://dentedreality.com.au/2013/07/14/crabs/) 
# [Crabs](http://dentedreality.com.au/2013/07/14/crabs/)





* #[beau](http://dentedreality.com.au/tags/beau/)
* #[beaulebens](http://dentedreality.com.au/tags/beaulebens/)
* #[costarica](http://dentedreality.com.au/tags/costarica/)
* #[crab](http://dentedreality.com.au/tags/crab/)
* #[hermitcrab](http://dentedreality.com.au/tags/hermitcrab/)
* #[me](http://dentedreality.com.au/tags/me/)

Posted on [Flickr](http://www.flickr.com/photos/borkazoid/9437410377/) [2:11 pm, July 14, 2013](http://dentedreality.com.au/2013/07/14/crabs/ "2:11 pm") 
jQuery(document).ready(function(){
var gmap\_mda837abd167613e2f4b68c251ecd112c = {
positions : {
416 : new google.maps.LatLng( '9.880066', '-85.529864' )
},
bounds : new google.maps.LatLngBounds(), // empty for now, we'll dynamically extend it later
map : new google.maps.Map(
document.getElementById( 'gmap\_mda837abd167613e2f4b68c251ecd112c' ),
{
mapTypeId: google.maps.MapTypeId.ROADMAP,
center: new google.maps.LatLng( 0, 0 ),
zoom: 16 // Seems to be a good zoom for a single point
}
),
markers : {},
}; // end of gmap
// Extend the bounds of interest based on our positions
for ( var m in gmap\_mda837abd167613e2f4b68c251ecd112c.positions ) {
gmap\_mda837abd167613e2f4b68c251ecd112c.bounds.extend( gmap\_mda837abd167613e2f4b68c251ecd112c.positions[m] );
}
// Render markers
for ( var m in gmap\_mda837abd167613e2f4b68c251ecd112c.positions ) {
gmap\_mda837abd167613e2f4b68c251ecd112c.markers[m] = new google.maps.Marker( {
clickable: true,
map : gmap\_mda837abd167613e2f4b68c251ecd112c.map,
position : gmap\_mda837abd167613e2f4b68c251ecd112c.positions[m]
} );
}
// Redraw map to fit our new marker-based bounds
gmap\_mda837abd167613e2f4b68c251ecd112c.map.setCenter( gmap\_mda837abd167613e2f4b68c251ecd112c.positions[416] );
});