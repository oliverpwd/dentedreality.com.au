---
title: Aston Martin DB9
date: '2011-01-13T11:43:24+00:00'
format: image
service: flickr
tags:
- astonmartin
- astonmartindb9
- car
- db9
image: http://i2.wp.com/dentedreality.com.au/wp-content/uploads/2011/01/5434724658_02c03484e4_o.jpg?resize=607%2C452
---

[![Aston Martin DB9](http://i2.wp.com/dentedreality.com.au/wp-content/uploads/2011/01/5434724658_02c03484e4_o.jpg?resize=607%2C452)](http://dentedreality.com.au/2011/01/13/aston-martin-db9/) 
# [Aston Martin DB9](http://dentedreality.com.au/2011/01/13/aston-martin-db9/)





* #[astonmartin](http://dentedreality.com.au/tags/astonmartin/)
* #[astonmartindb9](http://dentedreality.com.au/tags/astonmartindb9/)
* #[car](http://dentedreality.com.au/tags/car/)
* #[db9](http://dentedreality.com.au/tags/db9/)

Posted on [Flickr](http://www.flickr.com/photos/borkazoid/5434724658/) [11:43 am, January 13, 2011](http://dentedreality.com.au/2011/01/13/aston-martin-db9/ "11:43 am") 
jQuery(document).ready(function(){
var gmap\_m02a5237d9e7ee0fb5ab4fcf6085f08c2 = {
positions : {
850 : new google.maps.LatLng( '-31.803', '115.805833' )
},
bounds : new google.maps.LatLngBounds(), // empty for now, we'll dynamically extend it later
map : new google.maps.Map(
document.getElementById( 'gmap\_m02a5237d9e7ee0fb5ab4fcf6085f08c2' ),
{
mapTypeId: google.maps.MapTypeId.ROADMAP,
center: new google.maps.LatLng( 0, 0 ),
zoom: 16 // Seems to be a good zoom for a single point
}
),
markers : {},
}; // end of gmap
// Extend the bounds of interest based on our positions
for ( var m in gmap\_m02a5237d9e7ee0fb5ab4fcf6085f08c2.positions ) {
gmap\_m02a5237d9e7ee0fb5ab4fcf6085f08c2.bounds.extend( gmap\_m02a5237d9e7ee0fb5ab4fcf6085f08c2.positions[m] );
}
// Render markers
for ( var m in gmap\_m02a5237d9e7ee0fb5ab4fcf6085f08c2.positions ) {
gmap\_m02a5237d9e7ee0fb5ab4fcf6085f08c2.markers[m] = new google.maps.Marker( {
clickable: true,
map : gmap\_m02a5237d9e7ee0fb5ab4fcf6085f08c2.map,
position : gmap\_m02a5237d9e7ee0fb5ab4fcf6085f08c2.positions[m]
} );
}
// Redraw map to fit our new marker-based bounds
gmap\_m02a5237d9e7ee0fb5ab4fcf6085f08c2.map.setCenter( gmap\_m02a5237d9e7ee0fb5ab4fcf6085f08c2.positions[850] );
});