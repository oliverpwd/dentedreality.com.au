---
title: Matt’s Interview
date: '2011-03-11T11:19:34+00:00'
format: image
service: flickr
tags:
- Austin
- sxsw
- sxsw2011
- texas
image: http://i1.wp.com/dentedreality.com.au/wp-content/uploads/2011/03/5802652338_1eb6cb81b1_o.jpg?resize=607%2C452
---

[![Matt's Interview](http://i1.wp.com/dentedreality.com.au/wp-content/uploads/2011/03/5802652338_1eb6cb81b1_o.jpg?resize=607%2C452)](http://dentedreality.com.au/2011/03/11/matts-interview-2/) 
# [Matt’s Interview](http://dentedreality.com.au/2011/03/11/matts-interview-2/)





* #[Austin](http://dentedreality.com.au/tags/austin/)
* #[sxsw](http://dentedreality.com.au/tags/sxsw/)
* #[sxsw2011](http://dentedreality.com.au/tags/sxsw2011/)
* #[texas](http://dentedreality.com.au/tags/texas/)

Posted on [Flickr](http://www.flickr.com/photos/borkazoid/5802652338/) [11:19 am, March 11, 2011](http://dentedreality.com.au/2011/03/11/matts-interview-2/ "11:19 am") 
jQuery(document).ready(function(){
var gmap\_m4cd4fb7cc4be820f2898912333c7b2b8 = {
positions : {
608 : new google.maps.LatLng( '30.2625', '-97.739667' )
},
bounds : new google.maps.LatLngBounds(), // empty for now, we'll dynamically extend it later
map : new google.maps.Map(
document.getElementById( 'gmap\_m4cd4fb7cc4be820f2898912333c7b2b8' ),
{
mapTypeId: google.maps.MapTypeId.ROADMAP,
center: new google.maps.LatLng( 0, 0 ),
zoom: 16 // Seems to be a good zoom for a single point
}
),
markers : {},
}; // end of gmap
// Extend the bounds of interest based on our positions
for ( var m in gmap\_m4cd4fb7cc4be820f2898912333c7b2b8.positions ) {
gmap\_m4cd4fb7cc4be820f2898912333c7b2b8.bounds.extend( gmap\_m4cd4fb7cc4be820f2898912333c7b2b8.positions[m] );
}
// Render markers
for ( var m in gmap\_m4cd4fb7cc4be820f2898912333c7b2b8.positions ) {
gmap\_m4cd4fb7cc4be820f2898912333c7b2b8.markers[m] = new google.maps.Marker( {
clickable: true,
map : gmap\_m4cd4fb7cc4be820f2898912333c7b2b8.map,
position : gmap\_m4cd4fb7cc4be820f2898912333c7b2b8.positions[m]
} );
}
// Redraw map to fit our new marker-based bounds
gmap\_m4cd4fb7cc4be820f2898912333c7b2b8.map.setCenter( gmap\_m4cd4fb7cc4be820f2898912333c7b2b8.positions[608] );
});