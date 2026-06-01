---
title: Social Dashboard
date: '2013-06-09T07:21:42+00:00'
format: image
service: flickr
tags:
- foursquare
- hotel50
- social
- twitter
image: http://i2.wp.com/dentedreality.com.au/wp-content/uploads/2013/06/9437043507_c9ace89a9c_o.jpg?resize=607%2C452
---

[![Social Dashboard](http://i2.wp.com/dentedreality.com.au/wp-content/uploads/2013/06/9437043507_c9ace89a9c_o.jpg?resize=607%2C452)](http://dentedreality.com.au/2013/06/09/social-dashboard/) 
# [Social Dashboard](http://dentedreality.com.au/2013/06/09/social-dashboard/)

They had this dashboard thing at Hotel50 which showed foursquare check-ins and tweets, so we dominated it.





* #[foursquare](http://dentedreality.com.au/tags/foursquare-2/)
* #[hotel50](http://dentedreality.com.au/tags/hotel50/)
* #[social](http://dentedreality.com.au/tags/social/)
* #[twitter](http://dentedreality.com.au/tags/twitter-2/)

Posted on [Flickr](http://www.flickr.com/photos/borkazoid/9437043507/) [7:21 am, June 9, 2013](http://dentedreality.com.au/2013/06/09/social-dashboard/ "7:21 am") 
jQuery(document).ready(function(){
var gmap\_m810129c3c8f3b75166a111d167c12af8 = {
positions : {
310 : new google.maps.LatLng( '45.5175', '-122.672834' )
},
bounds : new google.maps.LatLngBounds(), // empty for now, we'll dynamically extend it later
map : new google.maps.Map(
document.getElementById( 'gmap\_m810129c3c8f3b75166a111d167c12af8' ),
{
mapTypeId: google.maps.MapTypeId.ROADMAP,
center: new google.maps.LatLng( 0, 0 ),
zoom: 16 // Seems to be a good zoom for a single point
}
),
markers : {},
}; // end of gmap
// Extend the bounds of interest based on our positions
for ( var m in gmap\_m810129c3c8f3b75166a111d167c12af8.positions ) {
gmap\_m810129c3c8f3b75166a111d167c12af8.bounds.extend( gmap\_m810129c3c8f3b75166a111d167c12af8.positions[m] );
}
// Render markers
for ( var m in gmap\_m810129c3c8f3b75166a111d167c12af8.positions ) {
gmap\_m810129c3c8f3b75166a111d167c12af8.markers[m] = new google.maps.Marker( {
clickable: true,
map : gmap\_m810129c3c8f3b75166a111d167c12af8.map,
position : gmap\_m810129c3c8f3b75166a111d167c12af8.positions[m]
} );
}
// Redraw map to fit our new marker-based bounds
gmap\_m810129c3c8f3b75166a111d167c12af8.map.setCenter( gmap\_m810129c3c8f3b75166a111d167c12af8.positions[310] );
});