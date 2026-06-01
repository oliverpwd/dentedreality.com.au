---
title: Rose & Randy’s Wedding
date: '2013-10-12T15:21:06+00:00'
format: image
service: flickr
tags:
- randy
- rose
- simonwedding
- wedding
image: http://i2.wp.com/dentedreality.com.au/wp-content/uploads/2013/10/12291594846_2a2907152c_o.jpg?fit=1500%2C1500
---

[![Rose & Randy's Wedding](http://i2.wp.com/dentedreality.com.au/wp-content/uploads/2013/10/12291594846_2a2907152c_o.jpg?fit=1500%2C1500)](http://dentedreality.com.au/2013/10/12/rose-randys-wedding-3/) 
# [Rose & Randy’s Wedding](http://dentedreality.com.au/2013/10/12/rose-randys-wedding-3/)





* #[randy](http://dentedreality.com.au/tags/randy/)
* #[rose](http://dentedreality.com.au/tags/rose/)
* #[simonwedding](http://dentedreality.com.au/tags/simonwedding/)
* #[wedding](http://dentedreality.com.au/tags/wedding/)

Posted on [Flickr](http://www.flickr.com/photos/borkazoid/12291594846/) [3:21 pm, October 12, 2013](http://dentedreality.com.au/2013/10/12/rose-randys-wedding-3/ "3:21 pm") 
jQuery(document).ready(function(){
var gmap\_mf7c59e0e428f2dd9dee04db6ee3178f4 = {
positions : {
810 : new google.maps.LatLng( '38.413166', '-122.552' )
},
bounds : new google.maps.LatLngBounds(), // empty for now, we'll dynamically extend it later
map : new google.maps.Map(
document.getElementById( 'gmap\_mf7c59e0e428f2dd9dee04db6ee3178f4' ),
{
mapTypeId: google.maps.MapTypeId.ROADMAP,
center: new google.maps.LatLng( 0, 0 ),
zoom: 16 // Seems to be a good zoom for a single point
}
),
markers : {},
}; // end of gmap
// Extend the bounds of interest based on our positions
for ( var m in gmap\_mf7c59e0e428f2dd9dee04db6ee3178f4.positions ) {
gmap\_mf7c59e0e428f2dd9dee04db6ee3178f4.bounds.extend( gmap\_mf7c59e0e428f2dd9dee04db6ee3178f4.positions[m] );
}
// Render markers
for ( var m in gmap\_mf7c59e0e428f2dd9dee04db6ee3178f4.positions ) {
gmap\_mf7c59e0e428f2dd9dee04db6ee3178f4.markers[m] = new google.maps.Marker( {
clickable: true,
map : gmap\_mf7c59e0e428f2dd9dee04db6ee3178f4.map,
position : gmap\_mf7c59e0e428f2dd9dee04db6ee3178f4.positions[m]
} );
}
// Redraw map to fit our new marker-based bounds
gmap\_mf7c59e0e428f2dd9dee04db6ee3178f4.map.setCenter( gmap\_mf7c59e0e428f2dd9dee04db6ee3178f4.positions[810] );
});