---
title: Athens, Greece
date: '2010-11-09T09:44:50-06:00'
format: image
service: flickr
tags:
- Athens
- automattic
- greece
- teamsocial
latitude: '37.9745'
longitude: '23.724999'
image: https://s3.amazonaws.com/dentedreality-content/wp-content/uploads/2010/11/14185852/5183191909_3dbc61a70f_o.jpg
---

[![Athens, Greece](https://s3.amazonaws.com/dentedreality-content/wp-content/uploads/2010/11/14185852/5183191909_3dbc61a70f_o.jpg)](https://dentedreality.com.au/2010/11/09/athens-greece/) 
# [Athens, Greece](https://dentedreality.com.au/2010/11/09/athens-greece/)

[![Athens, Greece](https://s3.amazonaws.com/dentedreality-content/wp-content/uploads/2010/11/14185852/5183191909_3dbc61a70f_o.jpg)](http://www.flickr.com/photos/borkazoid/5183191909/)

37.974523.724999




* #[Athens](https://dentedreality.com.au/tags/athens/)
* #[automattic](https://dentedreality.com.au/tags/automattic/)
* #[greece](https://dentedreality.com.au/tags/greece/)
* #[teamsocial](https://dentedreality.com.au/tags/teamsocial/)

Posted on [Flickr](http://www.flickr.com/photos/borkazoid/5183191909/) [9:44 am, November 9, 2010](https://dentedreality.com.au/2010/11/09/athens-greece/ "9:44 am") 
jQuery(document).ready(function(){
var gmap\_m6b70a7eece982cc92e658548c62882a0 = {
positions : {
487 : new google.maps.LatLng( '37.9745', '23.724999' )
},
bounds : new google.maps.LatLngBounds(), // empty for now, we'll dynamically extend it later
map : new google.maps.Map(
document.getElementById( 'gmap\_m6b70a7eece982cc92e658548c62882a0' ),
{
mapTypeId: google.maps.MapTypeId.ROADMAP,
center: new google.maps.LatLng( 0, 0 ),
zoom: 16 // Seems to be a good zoom for a single point
}
),
markers : {},
}; // end of gmap
// Extend the bounds of interest based on our positions
for ( var m in gmap\_m6b70a7eece982cc92e658548c62882a0.positions ) {
gmap\_m6b70a7eece982cc92e658548c62882a0.bounds.extend( gmap\_m6b70a7eece982cc92e658548c62882a0.positions[m] );
}
// Render markers
for ( var m in gmap\_m6b70a7eece982cc92e658548c62882a0.positions ) {
gmap\_m6b70a7eece982cc92e658548c62882a0.markers[m] = new google.maps.Marker( {
clickable: true,
map : gmap\_m6b70a7eece982cc92e658548c62882a0.map,
position : gmap\_m6b70a7eece982cc92e658548c62882a0.positions[m]
} );
}
// Redraw map to fit our new marker-based bounds
gmap\_m6b70a7eece982cc92e658548c62882a0.map.setCenter( gmap\_m6b70a7eece982cc92e658548c62882a0.positions[487] );
});