---
title: Bats
date: '2008-04-09T16:38:36+00:00'
format: image
service: flickr
tags:
- australia
- bats
- botanicalgardens
- sydney
image: http://i0.wp.com/dentedreality.com.au/wp-content/uploads/2008/04/2436623601_f1312c8a06_o.jpg?resize=607%2C808
---

[![Bats](http://i0.wp.com/dentedreality.com.au/wp-content/uploads/2008/04/2436623601_f1312c8a06_o.jpg?resize=607%2C808)](http://dentedreality.com.au/2008/04/09/bats-2/) 
# [Bats](http://dentedreality.com.au/2008/04/09/bats-2/)

What’s with all the bats in the Botanical Gardens?





* #[australia](http://dentedreality.com.au/tags/australia/)
* #[bats](http://dentedreality.com.au/tags/bats/)
* #[botanicalgardens](http://dentedreality.com.au/tags/botanicalgardens/)
* #[sydney](http://dentedreality.com.au/tags/sydney/)

Posted on [Flickr](http://www.flickr.com/photos/borkazoid/2436623601/) [4:38 pm, April 9, 2008](http://dentedreality.com.au/2008/04/09/bats-2/ "4:38 pm") 
jQuery(document).ready(function(){
var gmap\_m7f0915a135c99e808956482ee713dd20 = {
positions : {
763 : new google.maps.LatLng( '-33.871555', '151.226291' )
},
bounds : new google.maps.LatLngBounds(), // empty for now, we'll dynamically extend it later
map : new google.maps.Map(
document.getElementById( 'gmap\_m7f0915a135c99e808956482ee713dd20' ),
{
mapTypeId: google.maps.MapTypeId.ROADMAP,
center: new google.maps.LatLng( 0, 0 ),
zoom: 16 // Seems to be a good zoom for a single point
}
),
markers : {},
}; // end of gmap
// Extend the bounds of interest based on our positions
for ( var m in gmap\_m7f0915a135c99e808956482ee713dd20.positions ) {
gmap\_m7f0915a135c99e808956482ee713dd20.bounds.extend( gmap\_m7f0915a135c99e808956482ee713dd20.positions[m] );
}
// Render markers
for ( var m in gmap\_m7f0915a135c99e808956482ee713dd20.positions ) {
gmap\_m7f0915a135c99e808956482ee713dd20.markers[m] = new google.maps.Marker( {
clickable: true,
map : gmap\_m7f0915a135c99e808956482ee713dd20.map,
position : gmap\_m7f0915a135c99e808956482ee713dd20.positions[m]
} );
}
// Redraw map to fit our new marker-based bounds
gmap\_m7f0915a135c99e808956482ee713dd20.map.setCenter( gmap\_m7f0915a135c99e808956482ee713dd20.positions[763] );
});