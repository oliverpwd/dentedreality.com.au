---
title: Chairs
date: '2013-12-04T08:49:32+00:00'
format: image
service: flickr
tags:
- chairs
- france
- paris
- tables
image: http://i0.wp.com/dentedreality.com.au/wp-content/uploads/2013/12/13900380236_68a9fcd797_o.jpg?fit=1500%2C1500
---

[![Chairs](http://i0.wp.com/dentedreality.com.au/wp-content/uploads/2013/12/13900380236_68a9fcd797_o.jpg?fit=1500%2C1500)](http://dentedreality.com.au/2013/12/04/chairs/) 
# [Chairs](http://dentedreality.com.au/2013/12/04/chairs/)





* #[chairs](http://dentedreality.com.au/tags/chairs/)
* #[france](http://dentedreality.com.au/tags/france/)
* #[paris](http://dentedreality.com.au/tags/paris/)
* #[tables](http://dentedreality.com.au/tags/tables/)

Posted on [Flickr](http://www.flickr.com/photos/borkazoid/13900380236/) [8:49 am, December 4, 2013](http://dentedreality.com.au/2013/12/04/chairs/ "8:49 am") 
jQuery(document).ready(function(){
var gmap\_mb80d44f2a719ab16382393750733b7f4 = {
positions : {
821 : new google.maps.LatLng( '48.852977', '2.368205' )
},
bounds : new google.maps.LatLngBounds(), // empty for now, we'll dynamically extend it later
map : new google.maps.Map(
document.getElementById( 'gmap\_mb80d44f2a719ab16382393750733b7f4' ),
{
mapTypeId: google.maps.MapTypeId.ROADMAP,
center: new google.maps.LatLng( 0, 0 ),
zoom: 16 // Seems to be a good zoom for a single point
}
),
markers : {},
}; // end of gmap
// Extend the bounds of interest based on our positions
for ( var m in gmap\_mb80d44f2a719ab16382393750733b7f4.positions ) {
gmap\_mb80d44f2a719ab16382393750733b7f4.bounds.extend( gmap\_mb80d44f2a719ab16382393750733b7f4.positions[m] );
}
// Render markers
for ( var m in gmap\_mb80d44f2a719ab16382393750733b7f4.positions ) {
gmap\_mb80d44f2a719ab16382393750733b7f4.markers[m] = new google.maps.Marker( {
clickable: true,
map : gmap\_mb80d44f2a719ab16382393750733b7f4.map,
position : gmap\_mb80d44f2a719ab16382393750733b7f4.positions[m]
} );
}
// Redraw map to fit our new marker-based bounds
gmap\_mb80d44f2a719ab16382393750733b7f4.map.setCenter( gmap\_mb80d44f2a719ab16382393750733b7f4.positions[821] );
});