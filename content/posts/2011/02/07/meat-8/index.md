---
title: Meat!
date: '2011-02-07T14:24:24+00:00'
format: image
service: flickr
tags:
- '4505'
- 4505meats
- butchery
- lamb
- meat
image: http://i0.wp.com/dentedreality.com.au/wp-content/uploads/2011/02/5802611608_afb3f6b9d4_o.jpg?resize=607%2C452
---

[![Meat!](http://i0.wp.com/dentedreality.com.au/wp-content/uploads/2011/02/5802611608_afb3f6b9d4_o.jpg?resize=607%2C452)](http://dentedreality.com.au/2011/02/07/meat-8/) 
# [Meat!](http://dentedreality.com.au/2011/02/07/meat-8/)

Butchering a lamb with 4505 Meats





* #[4505](http://dentedreality.com.au/tags/4505/)
* #[4505meats](http://dentedreality.com.au/tags/4505meats/)
* #[butchery](http://dentedreality.com.au/tags/butchery/)
* #[lamb](http://dentedreality.com.au/tags/lamb/)
* #[meat](http://dentedreality.com.au/tags/meat/)

Posted on [Flickr](http://www.flickr.com/photos/borkazoid/5802611608/) [2:24 pm, February 7, 2011](http://dentedreality.com.au/2011/02/07/meat-8/ "2:24 pm") 
jQuery(document).ready(function(){
var gmap\_m39bc415d1fc944fae18abbe0db9b9919 = {
positions : {
35 : new google.maps.LatLng( '37.778333', '-122.4255' )
},
bounds : new google.maps.LatLngBounds(), // empty for now, we'll dynamically extend it later
map : new google.maps.Map(
document.getElementById( 'gmap\_m39bc415d1fc944fae18abbe0db9b9919' ),
{
mapTypeId: google.maps.MapTypeId.ROADMAP,
center: new google.maps.LatLng( 0, 0 ),
zoom: 16 // Seems to be a good zoom for a single point
}
),
markers : {},
}; // end of gmap
// Extend the bounds of interest based on our positions
for ( var m in gmap\_m39bc415d1fc944fae18abbe0db9b9919.positions ) {
gmap\_m39bc415d1fc944fae18abbe0db9b9919.bounds.extend( gmap\_m39bc415d1fc944fae18abbe0db9b9919.positions[m] );
}
// Render markers
for ( var m in gmap\_m39bc415d1fc944fae18abbe0db9b9919.positions ) {
gmap\_m39bc415d1fc944fae18abbe0db9b9919.markers[m] = new google.maps.Marker( {
clickable: true,
map : gmap\_m39bc415d1fc944fae18abbe0db9b9919.map,
position : gmap\_m39bc415d1fc944fae18abbe0db9b9919.positions[m]
} );
}
// Redraw map to fit our new marker-based bounds
gmap\_m39bc415d1fc944fae18abbe0db9b9919.map.setCenter( gmap\_m39bc415d1fc944fae18abbe0db9b9919.positions[35] );
});