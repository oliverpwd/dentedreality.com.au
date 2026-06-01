---
title: ''
date: '2016-07-30T10:12:50-06:00'
format: image
service: instagram
tags:
- bwca
latitude: '48.15911'
longitude: '-90.86799'
image: http://i2.wp.com/dentedreality.com.au/wp-content/uploads/2016/07/13649309_595033054004862_2008995412_n.jpg?fit=640%2C640
---

[![Success. 3 nights in #bwca. Such an amazing place. Grabbed a hat as a memento.](http://i2.wp.com/dentedreality.com.au/wp-content/uploads/2016/07/13649309_595033054004862_2008995412_n.jpg?fit=640%2C640)](https://dentedreality.com.au/2016/07/30/success-3-nights-in-bwca-such-an-amazing-place-grabbed-a-hat-as-a-memento/) 

[![Success. 3 nights in #bwca. Such an amazing place. Grabbed a hat as a memento.](http://i2.wp.com/dentedreality.com.au/wp-content/uploads/2016/07/13649309_595033054004862_2008995412_n.jpg?fit=640%2C640)](https://www.instagram.com/p/BIfeyAPA5BQ/)

Success. 3 nights in #bwca. Such an amazing place. Grabbed a hat as a memento.

48.15911-90.86799




* #[bwca](https://dentedreality.com.au/tags/bwca/)

Posted on [Instagram](https://www.instagram.com/p/BIfeyAPA5BQ/) [10:12 am, July 30, 2016](https://dentedreality.com.au/2016/07/30/success-3-nights-in-bwca-such-an-amazing-place-grabbed-a-hat-as-a-memento/ "10:12 am") 
jQuery(document).ready(function(){
var gmap\_me6b97a55d16ebe94b6dcba5fba9645a1 = {
positions : {
258 : new google.maps.LatLng( '48.15911', '-90.86799' )
},
bounds : new google.maps.LatLngBounds(), // empty for now, we'll dynamically extend it later
map : new google.maps.Map(
document.getElementById( 'gmap\_me6b97a55d16ebe94b6dcba5fba9645a1' ),
{
mapTypeId: google.maps.MapTypeId.ROADMAP,
center: new google.maps.LatLng( 0, 0 ),
zoom: 16 // Seems to be a good zoom for a single point
}
),
markers : {},
}; // end of gmap
// Extend the bounds of interest based on our positions
for ( var m in gmap\_me6b97a55d16ebe94b6dcba5fba9645a1.positions ) {
gmap\_me6b97a55d16ebe94b6dcba5fba9645a1.bounds.extend( gmap\_me6b97a55d16ebe94b6dcba5fba9645a1.positions[m] );
}
// Render markers
for ( var m in gmap\_me6b97a55d16ebe94b6dcba5fba9645a1.positions ) {
gmap\_me6b97a55d16ebe94b6dcba5fba9645a1.markers[m] = new google.maps.Marker( {
clickable: true,
map : gmap\_me6b97a55d16ebe94b6dcba5fba9645a1.map,
position : gmap\_me6b97a55d16ebe94b6dcba5fba9645a1.positions[m]
} );
}
// Redraw map to fit our new marker-based bounds
gmap\_me6b97a55d16ebe94b6dcba5fba9645a1.map.setCenter( gmap\_me6b97a55d16ebe94b6dcba5fba9645a1.positions[258] );
});