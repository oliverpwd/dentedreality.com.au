---
title: Dinner at Bluewater
date: '2011-01-13T15:48:57+00:00'
format: image
service: flickr
tags:
- bluewater
- dinner
- perth
- restaurant
image: http://i2.wp.com/dentedreality.com.au/wp-content/uploads/2011/01/5434111669_38b8cf30d4_o.jpg?resize=607%2C452
---

[![Dinner at Bluewater](http://i2.wp.com/dentedreality.com.au/wp-content/uploads/2011/01/5434111669_38b8cf30d4_o.jpg?resize=607%2C452)](http://dentedreality.com.au/2011/01/13/dinner-at-bluewater-2/) 
# [Dinner at Bluewater](http://dentedreality.com.au/2011/01/13/dinner-at-bluewater-2/)





* #[bluewater](http://dentedreality.com.au/tags/bluewater/)
* #[dinner](http://dentedreality.com.au/tags/dinner/)
* #[perth](http://dentedreality.com.au/tags/perth/)
* #[restaurant](http://dentedreality.com.au/tags/restaurant/)

Posted on [Flickr](http://www.flickr.com/photos/borkazoid/5434111669/) [3:48 pm, January 13, 2011](http://dentedreality.com.au/2011/01/13/dinner-at-bluewater-2/ "3:48 pm") 
jQuery(document).ready(function(){
var gmap\_me34fc55c839adadfc6c6ac05c2eb49d8 = {
positions : {
743 : new google.maps.LatLng( '-32.003', '115.842166' )
},
bounds : new google.maps.LatLngBounds(), // empty for now, we'll dynamically extend it later
map : new google.maps.Map(
document.getElementById( 'gmap\_me34fc55c839adadfc6c6ac05c2eb49d8' ),
{
mapTypeId: google.maps.MapTypeId.ROADMAP,
center: new google.maps.LatLng( 0, 0 ),
zoom: 16 // Seems to be a good zoom for a single point
}
),
markers : {},
}; // end of gmap
// Extend the bounds of interest based on our positions
for ( var m in gmap\_me34fc55c839adadfc6c6ac05c2eb49d8.positions ) {
gmap\_me34fc55c839adadfc6c6ac05c2eb49d8.bounds.extend( gmap\_me34fc55c839adadfc6c6ac05c2eb49d8.positions[m] );
}
// Render markers
for ( var m in gmap\_me34fc55c839adadfc6c6ac05c2eb49d8.positions ) {
gmap\_me34fc55c839adadfc6c6ac05c2eb49d8.markers[m] = new google.maps.Marker( {
clickable: true,
map : gmap\_me34fc55c839adadfc6c6ac05c2eb49d8.map,
position : gmap\_me34fc55c839adadfc6c6ac05c2eb49d8.positions[m]
} );
}
// Redraw map to fit our new marker-based bounds
gmap\_me34fc55c839adadfc6c6ac05c2eb49d8.map.setCenter( gmap\_me34fc55c839adadfc6c6ac05c2eb49d8.positions[743] );
});