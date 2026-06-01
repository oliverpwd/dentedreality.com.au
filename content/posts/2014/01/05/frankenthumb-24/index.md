---
title: Frankenthumb
date: '2014-01-05T08:19:19+00:00'
format: image
service: flickr
tags:
- Frankenthumb
image: http://i0.wp.com/dentedreality.com.au/wp-content/uploads/2014/01/13901671161_9833581c71_o.jpg?fit=1500%2C1500
---

[![Frankenthumb](http://i0.wp.com/dentedreality.com.au/wp-content/uploads/2014/01/13901671161_9833581c71_o.jpg?fit=1500%2C1500)](http://dentedreality.com.au/2014/01/05/frankenthumb-24/) 
# [Frankenthumb](http://dentedreality.com.au/2014/01/05/frankenthumb-24/)





* #[Frankenthumb](http://dentedreality.com.au/tags/frankenthumb/)

Posted on [Flickr](http://www.flickr.com/photos/borkazoid/13901671161/) [8:19 am, January 5, 2014](http://dentedreality.com.au/2014/01/05/frankenthumb-24/ "8:19 am") 
jQuery(document).ready(function(){
var gmap\_m96febec27d9664e42cac23b7a19d25fa = {
positions : {
214 : new google.maps.LatLng( '40.670166', '-73.985589' )
},
bounds : new google.maps.LatLngBounds(), // empty for now, we'll dynamically extend it later
map : new google.maps.Map(
document.getElementById( 'gmap\_m96febec27d9664e42cac23b7a19d25fa' ),
{
mapTypeId: google.maps.MapTypeId.ROADMAP,
center: new google.maps.LatLng( 0, 0 ),
zoom: 16 // Seems to be a good zoom for a single point
}
),
markers : {},
}; // end of gmap
// Extend the bounds of interest based on our positions
for ( var m in gmap\_m96febec27d9664e42cac23b7a19d25fa.positions ) {
gmap\_m96febec27d9664e42cac23b7a19d25fa.bounds.extend( gmap\_m96febec27d9664e42cac23b7a19d25fa.positions[m] );
}
// Render markers
for ( var m in gmap\_m96febec27d9664e42cac23b7a19d25fa.positions ) {
gmap\_m96febec27d9664e42cac23b7a19d25fa.markers[m] = new google.maps.Marker( {
clickable: true,
map : gmap\_m96febec27d9664e42cac23b7a19d25fa.map,
position : gmap\_m96febec27d9664e42cac23b7a19d25fa.positions[m]
} );
}
// Redraw map to fit our new marker-based bounds
gmap\_m96febec27d9664e42cac23b7a19d25fa.map.setCenter( gmap\_m96febec27d9664e42cac23b7a19d25fa.positions[214] );
});