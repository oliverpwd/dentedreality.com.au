---
title: Theater
date: '2013-12-02T05:48:50+00:00'
format: image
service: flickr
tags:
- france
- paris
- theater
image: http://i1.wp.com/dentedreality.com.au/wp-content/uploads/2013/12/13900365731_9953726cb4_o.jpg?fit=1500%2C1500
---

[![Theater](http://i1.wp.com/dentedreality.com.au/wp-content/uploads/2013/12/13900365731_9953726cb4_o.jpg?fit=1500%2C1500)](http://dentedreality.com.au/2013/12/02/theater/) 
# [Theater](http://dentedreality.com.au/2013/12/02/theater/)





* #[france](http://dentedreality.com.au/tags/france/)
* #[paris](http://dentedreality.com.au/tags/paris/)
* #[theater](http://dentedreality.com.au/tags/theater/)

Posted on [Flickr](http://www.flickr.com/photos/borkazoid/13900365731/) [5:48 am, December 2, 2013](http://dentedreality.com.au/2013/12/02/theater/ "5:48 am") 
jQuery(document).ready(function(){
var gmap\_m54f4d49799f08511f53adededbec00d3 = {
positions : {
70 : new google.maps.LatLng( '48.878777', '2.330877' )
},
bounds : new google.maps.LatLngBounds(), // empty for now, we'll dynamically extend it later
map : new google.maps.Map(
document.getElementById( 'gmap\_m54f4d49799f08511f53adededbec00d3' ),
{
mapTypeId: google.maps.MapTypeId.ROADMAP,
center: new google.maps.LatLng( 0, 0 ),
zoom: 16 // Seems to be a good zoom for a single point
}
),
markers : {},
}; // end of gmap
// Extend the bounds of interest based on our positions
for ( var m in gmap\_m54f4d49799f08511f53adededbec00d3.positions ) {
gmap\_m54f4d49799f08511f53adededbec00d3.bounds.extend( gmap\_m54f4d49799f08511f53adededbec00d3.positions[m] );
}
// Render markers
for ( var m in gmap\_m54f4d49799f08511f53adededbec00d3.positions ) {
gmap\_m54f4d49799f08511f53adededbec00d3.markers[m] = new google.maps.Marker( {
clickable: true,
map : gmap\_m54f4d49799f08511f53adededbec00d3.map,
position : gmap\_m54f4d49799f08511f53adededbec00d3.positions[m]
} );
}
// Redraw map to fit our new marker-based bounds
gmap\_m54f4d49799f08511f53adededbec00d3.map.setCenter( gmap\_m54f4d49799f08511f53adededbec00d3.positions[70] );
});