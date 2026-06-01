---
title: Precarious Parking
date: '2010-11-09T09:02:41-06:00'
format: image
service: flickr
tags:
- Athens
- automattic
- greece
- teamsocial
latitude: '37.9735'
longitude: '23.729166'
image: https://s3.amazonaws.com/dentedreality-content/wp-content/uploads/2010/11/14185851/5183789972_3e467ba3cb_o.jpg
---

[![Precarious Parking](https://s3.amazonaws.com/dentedreality-content/wp-content/uploads/2010/11/14185851/5183789972_3e467ba3cb_o.jpg)](https://dentedreality.com.au/2010/11/09/precarious-parking/) 
# [Precarious Parking](https://dentedreality.com.au/2010/11/09/precarious-parking/)

[![Precarious Parking](https://s3.amazonaws.com/dentedreality-content/wp-content/uploads/2010/11/14185851/5183789972_3e467ba3cb_o.jpg)](http://www.flickr.com/photos/borkazoid/5183789972/)

37.973523.729166




* #[Athens](https://dentedreality.com.au/tags/athens/)
* #[automattic](https://dentedreality.com.au/tags/automattic/)
* #[greece](https://dentedreality.com.au/tags/greece/)
* #[teamsocial](https://dentedreality.com.au/tags/teamsocial/)

Posted on [Flickr](http://www.flickr.com/photos/borkazoid/5183789972/) [9:02 am, November 9, 2010](https://dentedreality.com.au/2010/11/09/precarious-parking/ "9:02 am") 
jQuery(document).ready(function(){
var gmap\_m1d4b0e8edf518fa8d0b99c23fbb7029a = {
positions : {
959 : new google.maps.LatLng( '37.9735', '23.729166' )
},
bounds : new google.maps.LatLngBounds(), // empty for now, we'll dynamically extend it later
map : new google.maps.Map(
document.getElementById( 'gmap\_m1d4b0e8edf518fa8d0b99c23fbb7029a' ),
{
mapTypeId: google.maps.MapTypeId.ROADMAP,
center: new google.maps.LatLng( 0, 0 ),
zoom: 16 // Seems to be a good zoom for a single point
}
),
markers : {},
}; // end of gmap
// Extend the bounds of interest based on our positions
for ( var m in gmap\_m1d4b0e8edf518fa8d0b99c23fbb7029a.positions ) {
gmap\_m1d4b0e8edf518fa8d0b99c23fbb7029a.bounds.extend( gmap\_m1d4b0e8edf518fa8d0b99c23fbb7029a.positions[m] );
}
// Render markers
for ( var m in gmap\_m1d4b0e8edf518fa8d0b99c23fbb7029a.positions ) {
gmap\_m1d4b0e8edf518fa8d0b99c23fbb7029a.markers[m] = new google.maps.Marker( {
clickable: true,
map : gmap\_m1d4b0e8edf518fa8d0b99c23fbb7029a.map,
position : gmap\_m1d4b0e8edf518fa8d0b99c23fbb7029a.positions[m]
} );
}
// Redraw map to fit our new marker-based bounds
gmap\_m1d4b0e8edf518fa8d0b99c23fbb7029a.map.setCenter( gmap\_m1d4b0e8edf518fa8d0b99c23fbb7029a.positions[959] );
});