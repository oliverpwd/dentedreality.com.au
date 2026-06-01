---
title: Frankenthumb
date: '2014-02-17T08:12:22+00:00'
format: image
service: flickr
tags:
- Frankenthumb
image: http://i1.wp.com/dentedreality.com.au/wp-content/uploads/2014/02/13901700706_27eba3e8e7_o.jpg?fit=1500%2C1500
---

[![Frankenthumb](http://i1.wp.com/dentedreality.com.au/wp-content/uploads/2014/02/13901700706_27eba3e8e7_o.jpg?fit=1500%2C1500)](http://dentedreality.com.au/2014/02/17/frankenthumb/) 
# [Frankenthumb](http://dentedreality.com.au/2014/02/17/frankenthumb/)





* #[Frankenthumb](http://dentedreality.com.au/tags/frankenthumb/)

Posted on [Flickr](http://www.flickr.com/photos/borkazoid/13901700706/) [8:12 am, February 17, 2014](http://dentedreality.com.au/2014/02/17/frankenthumb/ "8:12 am") 
jQuery(document).ready(function(){
var gmap\_m27c020fe1e90d42e9e13b40029eac185 = {
positions : {
754 : new google.maps.LatLng( '40.669444', '-73.98497' )
},
bounds : new google.maps.LatLngBounds(), // empty for now, we'll dynamically extend it later
map : new google.maps.Map(
document.getElementById( 'gmap\_m27c020fe1e90d42e9e13b40029eac185' ),
{
mapTypeId: google.maps.MapTypeId.ROADMAP,
center: new google.maps.LatLng( 0, 0 ),
zoom: 16 // Seems to be a good zoom for a single point
}
),
markers : {},
}; // end of gmap
// Extend the bounds of interest based on our positions
for ( var m in gmap\_m27c020fe1e90d42e9e13b40029eac185.positions ) {
gmap\_m27c020fe1e90d42e9e13b40029eac185.bounds.extend( gmap\_m27c020fe1e90d42e9e13b40029eac185.positions[m] );
}
// Render markers
for ( var m in gmap\_m27c020fe1e90d42e9e13b40029eac185.positions ) {
gmap\_m27c020fe1e90d42e9e13b40029eac185.markers[m] = new google.maps.Marker( {
clickable: true,
map : gmap\_m27c020fe1e90d42e9e13b40029eac185.map,
position : gmap\_m27c020fe1e90d42e9e13b40029eac185.positions[m]
} );
}
// Redraw map to fit our new marker-based bounds
gmap\_m27c020fe1e90d42e9e13b40029eac185.map.setCenter( gmap\_m27c020fe1e90d42e9e13b40029eac185.positions[754] );
});