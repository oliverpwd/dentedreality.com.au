---
title: New Chair
date: '2012-02-01T04:47:15+00:00'
format: image
service: flickr
tags:
- chair
- desk
- ergonomics
- workspace
image: http://i1.wp.com/dentedreality.com.au/wp-content/uploads/2012/02/6959569351_a6597bc02a_o.jpg?resize=607%2C452
---

[![New Chair](http://i1.wp.com/dentedreality.com.au/wp-content/uploads/2012/02/6959569351_a6597bc02a_o.jpg?resize=607%2C452)](http://dentedreality.com.au/2012/02/01/new-chair/) 
# [New Chair](http://dentedreality.com.au/2012/02/01/new-chair/)

It’s ergonomic, yo.





* #[chair](http://dentedreality.com.au/tags/chair/)
* #[desk](http://dentedreality.com.au/tags/desk/)
* #[ergonomics](http://dentedreality.com.au/tags/ergonomics/)
* #[workspace](http://dentedreality.com.au/tags/workspace/)

Posted on [Flickr](http://www.flickr.com/photos/borkazoid/6959569351/) [4:47 am, February 1, 2012](http://dentedreality.com.au/2012/02/01/new-chair/ "4:47 am") 
jQuery(document).ready(function(){
var gmap\_mb54503eb948b933a7e7e38fac536d33e = {
positions : {
330 : new google.maps.LatLng( '37.791333', '-122.417834' )
},
bounds : new google.maps.LatLngBounds(), // empty for now, we'll dynamically extend it later
map : new google.maps.Map(
document.getElementById( 'gmap\_mb54503eb948b933a7e7e38fac536d33e' ),
{
mapTypeId: google.maps.MapTypeId.ROADMAP,
center: new google.maps.LatLng( 0, 0 ),
zoom: 16 // Seems to be a good zoom for a single point
}
),
markers : {},
}; // end of gmap
// Extend the bounds of interest based on our positions
for ( var m in gmap\_mb54503eb948b933a7e7e38fac536d33e.positions ) {
gmap\_mb54503eb948b933a7e7e38fac536d33e.bounds.extend( gmap\_mb54503eb948b933a7e7e38fac536d33e.positions[m] );
}
// Render markers
for ( var m in gmap\_mb54503eb948b933a7e7e38fac536d33e.positions ) {
gmap\_mb54503eb948b933a7e7e38fac536d33e.markers[m] = new google.maps.Marker( {
clickable: true,
map : gmap\_mb54503eb948b933a7e7e38fac536d33e.map,
position : gmap\_mb54503eb948b933a7e7e38fac536d33e.positions[m]
} );
}
// Redraw map to fit our new marker-based bounds
gmap\_mb54503eb948b933a7e7e38fac536d33e.map.setCenter( gmap\_mb54503eb948b933a7e7e38fac536d33e.positions[330] );
});