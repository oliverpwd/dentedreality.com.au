---
title: Veggies
date: '2013-12-22T16:03:15+00:00'
format: image
service: flickr
tags:
- roots
- vegetables
- veggies
- wallpaper
image: http://i0.wp.com/dentedreality.com.au/wp-content/uploads/2013/12/13900600232_821676bb01_o.jpg?resize=607%2C455
---

[![Veggies](http://i0.wp.com/dentedreality.com.au/wp-content/uploads/2013/12/13900600232_821676bb01_o.jpg?resize=607%2C455)](http://dentedreality.com.au/2013/12/22/veggies/) 
# [Veggies](http://dentedreality.com.au/2013/12/22/veggies/)





* #[roots](http://dentedreality.com.au/tags/roots/)
* #[vegetables](http://dentedreality.com.au/tags/vegetables/)
* #[veggies](http://dentedreality.com.au/tags/veggies/)
* #[wallpaper](http://dentedreality.com.au/tags/wallpaper/)

Posted on [Flickr](http://www.flickr.com/photos/borkazoid/13900600232/) [4:03 pm, December 22, 2013](http://dentedreality.com.au/2013/12/22/veggies/ "4:03 pm") 
jQuery(document).ready(function(){
var gmap\_m116217945f233e1c9b0c57e45bf81b78 = {
positions : {
79 : new google.maps.LatLng( '40.669225', '-73.985206' )
},
bounds : new google.maps.LatLngBounds(), // empty for now, we'll dynamically extend it later
map : new google.maps.Map(
document.getElementById( 'gmap\_m116217945f233e1c9b0c57e45bf81b78' ),
{
mapTypeId: google.maps.MapTypeId.ROADMAP,
center: new google.maps.LatLng( 0, 0 ),
zoom: 16 // Seems to be a good zoom for a single point
}
),
markers : {},
}; // end of gmap
// Extend the bounds of interest based on our positions
for ( var m in gmap\_m116217945f233e1c9b0c57e45bf81b78.positions ) {
gmap\_m116217945f233e1c9b0c57e45bf81b78.bounds.extend( gmap\_m116217945f233e1c9b0c57e45bf81b78.positions[m] );
}
// Render markers
for ( var m in gmap\_m116217945f233e1c9b0c57e45bf81b78.positions ) {
gmap\_m116217945f233e1c9b0c57e45bf81b78.markers[m] = new google.maps.Marker( {
clickable: true,
map : gmap\_m116217945f233e1c9b0c57e45bf81b78.map,
position : gmap\_m116217945f233e1c9b0c57e45bf81b78.positions[m]
} );
}
// Redraw map to fit our new marker-based bounds
gmap\_m116217945f233e1c9b0c57e45bf81b78.map.setCenter( gmap\_m116217945f233e1c9b0c57e45bf81b78.positions[79] );
});