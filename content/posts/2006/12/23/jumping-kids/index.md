---
title: Jumping Kids
date: '2006-12-23T17:45:19+00:00'
format: image
service: flickr
tags:
- jumping
- kids
- publicart
- sculpture
- thailand06
image: http://i2.wp.com/dentedreality.com.au/wp-content/uploads/2006/12/348115938_4f559a9de5_o.jpg?resize=607%2C809
---

[![Jumping Kids](http://i2.wp.com/dentedreality.com.au/wp-content/uploads/2006/12/348115938_4f559a9de5_o.jpg?resize=607%2C809)](http://dentedreality.com.au/2006/12/23/jumping-kids/) 
# [Jumping Kids](http://dentedreality.com.au/2006/12/23/jumping-kids/)





* #[jumping](http://dentedreality.com.au/tags/jumping/)
* #[kids](http://dentedreality.com.au/tags/kids/)
* #[publicart](http://dentedreality.com.au/tags/publicart/)
* #[sculpture](http://dentedreality.com.au/tags/sculpture/)
* #[thailand06](http://dentedreality.com.au/tags/thailand06/)

Posted on [Flickr](http://www.flickr.com/photos/borkazoid/348115938/) [5:45 pm, December 23, 2006](http://dentedreality.com.au/2006/12/23/jumping-kids/ "5:45 pm") 
jQuery(document).ready(function(){
var gmap\_ma62525971d6c960bd5cc46804e05b53f = {
positions : {
858 : new google.maps.LatLng( '1.300394', '103.873157' )
},
bounds : new google.maps.LatLngBounds(), // empty for now, we'll dynamically extend it later
map : new google.maps.Map(
document.getElementById( 'gmap\_ma62525971d6c960bd5cc46804e05b53f' ),
{
mapTypeId: google.maps.MapTypeId.ROADMAP,
center: new google.maps.LatLng( 0, 0 ),
zoom: 16 // Seems to be a good zoom for a single point
}
),
markers : {},
}; // end of gmap
// Extend the bounds of interest based on our positions
for ( var m in gmap\_ma62525971d6c960bd5cc46804e05b53f.positions ) {
gmap\_ma62525971d6c960bd5cc46804e05b53f.bounds.extend( gmap\_ma62525971d6c960bd5cc46804e05b53f.positions[m] );
}
// Render markers
for ( var m in gmap\_ma62525971d6c960bd5cc46804e05b53f.positions ) {
gmap\_ma62525971d6c960bd5cc46804e05b53f.markers[m] = new google.maps.Marker( {
clickable: true,
map : gmap\_ma62525971d6c960bd5cc46804e05b53f.map,
position : gmap\_ma62525971d6c960bd5cc46804e05b53f.positions[m]
} );
}
// Redraw map to fit our new marker-based bounds
gmap\_ma62525971d6c960bd5cc46804e05b53f.map.setCenter( gmap\_ma62525971d6c960bd5cc46804e05b53f.positions[858] );
});