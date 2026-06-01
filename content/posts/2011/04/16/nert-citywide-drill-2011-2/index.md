---
title: NERT Citywide Drill, 2011
date: '2011-04-16T08:01:11+00:00'
format: image
service: flickr
tags:
- nert
- sanfrancisco
- sffd
image: http://i1.wp.com/dentedreality.com.au/wp-content/uploads/2011/04/5802146197_2e843c9f95_o.jpg?resize=607%2C813
---

[![NERT Citywide Drill, 2011](http://i1.wp.com/dentedreality.com.au/wp-content/uploads/2011/04/5802146197_2e843c9f95_o.jpg?resize=607%2C813)](http://dentedreality.com.au/2011/04/16/nert-citywide-drill-2011-2/) 
# [NERT Citywide Drill, 2011](http://dentedreality.com.au/2011/04/16/nert-citywide-drill-2011-2/)





* #[nert](http://dentedreality.com.au/tags/nert/)
* #[sanfrancisco](http://dentedreality.com.au/tags/sanfrancisco/)
* #[sffd](http://dentedreality.com.au/tags/sffd/)

Posted on [Flickr](http://www.flickr.com/photos/borkazoid/5802146197/) [8:01 am, April 16, 2011](http://dentedreality.com.au/2011/04/16/nert-citywide-drill-2011-2/ "8:01 am") 
jQuery(document).ready(function(){
var gmap\_mf7a62ec299c50afba2208f8814601f7e = {
positions : {
247 : new google.maps.LatLng( '37.759333', '-122.413334' )
},
bounds : new google.maps.LatLngBounds(), // empty for now, we'll dynamically extend it later
map : new google.maps.Map(
document.getElementById( 'gmap\_mf7a62ec299c50afba2208f8814601f7e' ),
{
mapTypeId: google.maps.MapTypeId.ROADMAP,
center: new google.maps.LatLng( 0, 0 ),
zoom: 16 // Seems to be a good zoom for a single point
}
),
markers : {},
}; // end of gmap
// Extend the bounds of interest based on our positions
for ( var m in gmap\_mf7a62ec299c50afba2208f8814601f7e.positions ) {
gmap\_mf7a62ec299c50afba2208f8814601f7e.bounds.extend( gmap\_mf7a62ec299c50afba2208f8814601f7e.positions[m] );
}
// Render markers
for ( var m in gmap\_mf7a62ec299c50afba2208f8814601f7e.positions ) {
gmap\_mf7a62ec299c50afba2208f8814601f7e.markers[m] = new google.maps.Marker( {
clickable: true,
map : gmap\_mf7a62ec299c50afba2208f8814601f7e.map,
position : gmap\_mf7a62ec299c50afba2208f8814601f7e.positions[m]
} );
}
// Redraw map to fit our new marker-based bounds
gmap\_mf7a62ec299c50afba2208f8814601f7e.map.setCenter( gmap\_mf7a62ec299c50afba2208f8814601f7e.positions[247] );
});