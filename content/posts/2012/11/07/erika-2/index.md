---
title: Erika
date: '2012-11-07T12:42:17+00:00'
format: image
service: flickr
tags:
- erika
- jacket
- raincoat
- yellow
image: http://i2.wp.com/dentedreality.com.au/wp-content/uploads/2012/11/8459250839_7010bb37d9_o.jpg?resize=607%2C813
---

[![Erika](http://i2.wp.com/dentedreality.com.au/wp-content/uploads/2012/11/8459250839_7010bb37d9_o.jpg?resize=607%2C813)](http://dentedreality.com.au/2012/11/07/erika-2/) 
# [Erika](http://dentedreality.com.au/2012/11/07/erika-2/)





* #[erika](http://dentedreality.com.au/tags/erika/)
* #[jacket](http://dentedreality.com.au/tags/jacket/)
* #[raincoat](http://dentedreality.com.au/tags/raincoat/)
* #[yellow](http://dentedreality.com.au/tags/yellow/)

Posted on [Flickr](http://www.flickr.com/photos/borkazoid/8459250839/) [12:42 pm, November 7, 2012](http://dentedreality.com.au/2012/11/07/erika-2/ "12:42 pm") 
jQuery(document).ready(function(){
var gmap\_m0fc8ec066c7a1e7ef479f4c846569285 = {
positions : {
875 : new google.maps.LatLng( '40.671499', '-73.985834' )
},
bounds : new google.maps.LatLngBounds(), // empty for now, we'll dynamically extend it later
map : new google.maps.Map(
document.getElementById( 'gmap\_m0fc8ec066c7a1e7ef479f4c846569285' ),
{
mapTypeId: google.maps.MapTypeId.ROADMAP,
center: new google.maps.LatLng( 0, 0 ),
zoom: 16 // Seems to be a good zoom for a single point
}
),
markers : {},
}; // end of gmap
// Extend the bounds of interest based on our positions
for ( var m in gmap\_m0fc8ec066c7a1e7ef479f4c846569285.positions ) {
gmap\_m0fc8ec066c7a1e7ef479f4c846569285.bounds.extend( gmap\_m0fc8ec066c7a1e7ef479f4c846569285.positions[m] );
}
// Render markers
for ( var m in gmap\_m0fc8ec066c7a1e7ef479f4c846569285.positions ) {
gmap\_m0fc8ec066c7a1e7ef479f4c846569285.markers[m] = new google.maps.Marker( {
clickable: true,
map : gmap\_m0fc8ec066c7a1e7ef479f4c846569285.map,
position : gmap\_m0fc8ec066c7a1e7ef479f4c846569285.positions[m]
} );
}
// Redraw map to fit our new marker-based bounds
gmap\_m0fc8ec066c7a1e7ef479f4c846569285.map.setCenter( gmap\_m0fc8ec066c7a1e7ef479f4c846569285.positions[875] );
});