---
title: IMG_1130
date: '2011-02-23T09:24:14+00:00'
format: image
service: flickr
tags:
- newyork
- newyorkcity
- NYC
image: http://i1.wp.com/dentedreality.com.au/wp-content/uploads/2011/02/5802058945_42075581e5_o.jpg?resize=607%2C452
---

[![IMG_1130](http://i1.wp.com/dentedreality.com.au/wp-content/uploads/2011/02/5802058945_42075581e5_o.jpg?resize=607%2C452)](http://dentedreality.com.au/2011/02/23/img_1130/) 
# [IMG\_1130](http://dentedreality.com.au/2011/02/23/img_1130/)





* #[newyork](http://dentedreality.com.au/tags/newyork/)
* #[newyorkcity](http://dentedreality.com.au/tags/newyorkcity/)
* #[NYC](http://dentedreality.com.au/tags/nyc/)

Posted on [Flickr](http://www.flickr.com/photos/borkazoid/5802058945/) [9:24 am, February 23, 2011](http://dentedreality.com.au/2011/02/23/img_1130/ "9:24 am") 
jQuery(document).ready(function(){
var gmap\_mf0e4334feb9e0702610a324db259095d = {
positions : {
288 : new google.maps.LatLng( '40.708', '-73.998834' )
},
bounds : new google.maps.LatLngBounds(), // empty for now, we'll dynamically extend it later
map : new google.maps.Map(
document.getElementById( 'gmap\_mf0e4334feb9e0702610a324db259095d' ),
{
mapTypeId: google.maps.MapTypeId.ROADMAP,
center: new google.maps.LatLng( 0, 0 ),
zoom: 16 // Seems to be a good zoom for a single point
}
),
markers : {},
}; // end of gmap
// Extend the bounds of interest based on our positions
for ( var m in gmap\_mf0e4334feb9e0702610a324db259095d.positions ) {
gmap\_mf0e4334feb9e0702610a324db259095d.bounds.extend( gmap\_mf0e4334feb9e0702610a324db259095d.positions[m] );
}
// Render markers
for ( var m in gmap\_mf0e4334feb9e0702610a324db259095d.positions ) {
gmap\_mf0e4334feb9e0702610a324db259095d.markers[m] = new google.maps.Marker( {
clickable: true,
map : gmap\_mf0e4334feb9e0702610a324db259095d.map,
position : gmap\_mf0e4334feb9e0702610a324db259095d.positions[m]
} );
}
// Redraw map to fit our new marker-based bounds
gmap\_mf0e4334feb9e0702610a324db259095d.map.setCenter( gmap\_mf0e4334feb9e0702610a324db259095d.positions[288] );
});