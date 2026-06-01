---
title: View
date: '2011-05-29T09:05:42+00:00'
format: image
service: flickr
tags:
- owenswedding
- wedding
image: http://i0.wp.com/dentedreality.com.au/wp-content/uploads/2011/05/5803431574_986fd445bc_o.jpg?resize=607%2C452
---

[![View](http://i0.wp.com/dentedreality.com.au/wp-content/uploads/2011/05/5803431574_986fd445bc_o.jpg?resize=607%2C452)](http://dentedreality.com.au/2011/05/29/view-2/) 
# [View](http://dentedreality.com.au/2011/05/29/view-2/)





* #[owenswedding](http://dentedreality.com.au/tags/owenswedding/)
* #[wedding](http://dentedreality.com.au/tags/wedding/)

Posted on [Flickr](http://www.flickr.com/photos/borkazoid/5803431574/) [9:05 am, May 29, 2011](http://dentedreality.com.au/2011/05/29/view-2/ "9:05 am") 
jQuery(document).ready(function(){
var gmap\_m1837cd41e6a48b6a66c2f9917bd869af = {
positions : {
897 : new google.maps.LatLng( '37.806166', '-122.448001' )
},
bounds : new google.maps.LatLngBounds(), // empty for now, we'll dynamically extend it later
map : new google.maps.Map(
document.getElementById( 'gmap\_m1837cd41e6a48b6a66c2f9917bd869af' ),
{
mapTypeId: google.maps.MapTypeId.ROADMAP,
center: new google.maps.LatLng( 0, 0 ),
zoom: 16 // Seems to be a good zoom for a single point
}
),
markers : {},
}; // end of gmap
// Extend the bounds of interest based on our positions
for ( var m in gmap\_m1837cd41e6a48b6a66c2f9917bd869af.positions ) {
gmap\_m1837cd41e6a48b6a66c2f9917bd869af.bounds.extend( gmap\_m1837cd41e6a48b6a66c2f9917bd869af.positions[m] );
}
// Render markers
for ( var m in gmap\_m1837cd41e6a48b6a66c2f9917bd869af.positions ) {
gmap\_m1837cd41e6a48b6a66c2f9917bd869af.markers[m] = new google.maps.Marker( {
clickable: true,
map : gmap\_m1837cd41e6a48b6a66c2f9917bd869af.map,
position : gmap\_m1837cd41e6a48b6a66c2f9917bd869af.positions[m]
} );
}
// Redraw map to fit our new marker-based bounds
gmap\_m1837cd41e6a48b6a66c2f9917bd869af.map.setCenter( gmap\_m1837cd41e6a48b6a66c2f9917bd869af.positions[897] );
});