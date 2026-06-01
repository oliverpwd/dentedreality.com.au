---
title: Automattic VIP Training
date: '2013-05-14T13:40:52+00:00'
format: image
service: flickr
tags:
- automattic
- vip
- wordpress
image: http://i0.wp.com/dentedreality.com.au/wp-content/uploads/2013/05/9439709412_6675f4336e_o.jpg?resize=607%2C452
---

[![Automattic VIP Training](http://i0.wp.com/dentedreality.com.au/wp-content/uploads/2013/05/9439709412_6675f4336e_o.jpg?resize=607%2C452)](http://dentedreality.com.au/2013/05/14/automattic-vip-training-4/) 
# [Automattic VIP Training](http://dentedreality.com.au/2013/05/14/automattic-vip-training-4/)

Annual VIP training workshop, held in Napa, CA





* #[automattic](http://dentedreality.com.au/tags/automattic/)
* #[vip](http://dentedreality.com.au/tags/vip/)
* #[wordpress](http://dentedreality.com.au/tags/wordpress/)

Posted on [Flickr](http://www.flickr.com/photos/borkazoid/9439709412/) [1:40 pm, May 14, 2013](http://dentedreality.com.au/2013/05/14/automattic-vip-training-4/ "1:40 pm") 
jQuery(document).ready(function(){
var gmap\_maffd9a713da95e3cf99447e51668364e = {
positions : {
800 : new google.maps.LatLng( '38.256', '-122.331167' )
},
bounds : new google.maps.LatLngBounds(), // empty for now, we'll dynamically extend it later
map : new google.maps.Map(
document.getElementById( 'gmap\_maffd9a713da95e3cf99447e51668364e' ),
{
mapTypeId: google.maps.MapTypeId.ROADMAP,
center: new google.maps.LatLng( 0, 0 ),
zoom: 16 // Seems to be a good zoom for a single point
}
),
markers : {},
}; // end of gmap
// Extend the bounds of interest based on our positions
for ( var m in gmap\_maffd9a713da95e3cf99447e51668364e.positions ) {
gmap\_maffd9a713da95e3cf99447e51668364e.bounds.extend( gmap\_maffd9a713da95e3cf99447e51668364e.positions[m] );
}
// Render markers
for ( var m in gmap\_maffd9a713da95e3cf99447e51668364e.positions ) {
gmap\_maffd9a713da95e3cf99447e51668364e.markers[m] = new google.maps.Marker( {
clickable: true,
map : gmap\_maffd9a713da95e3cf99447e51668364e.map,
position : gmap\_maffd9a713da95e3cf99447e51668364e.positions[m]
} );
}
// Redraw map to fit our new marker-based bounds
gmap\_maffd9a713da95e3cf99447e51668364e.map.setCenter( gmap\_maffd9a713da95e3cf99447e51668364e.positions[800] );
});