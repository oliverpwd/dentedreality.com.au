---
title: Automattic VIP Training
date: '2013-05-13T13:26:37+00:00'
format: image
service: flickr
tags:
- automattic
- vip
- wordpress
image: http://i0.wp.com/dentedreality.com.au/wp-content/uploads/2013/05/9439707212_09bd3a1394_o.jpg?resize=607%2C452
---

[![Automattic VIP Training](http://i0.wp.com/dentedreality.com.au/wp-content/uploads/2013/05/9439707212_09bd3a1394_o.jpg?resize=607%2C452)](http://dentedreality.com.au/2013/05/13/automattic-vip-training-8/) 
# [Automattic VIP Training](http://dentedreality.com.au/2013/05/13/automattic-vip-training-8/)

Annual VIP training workshop, held in Napa, CA





* #[automattic](http://dentedreality.com.au/tags/automattic/)
* #[vip](http://dentedreality.com.au/tags/vip/)
* #[wordpress](http://dentedreality.com.au/tags/wordpress/)

Posted on [Flickr](http://www.flickr.com/photos/borkazoid/9439707212/) [1:26 pm, May 13, 2013](http://dentedreality.com.au/2013/05/13/automattic-vip-training-8/ "1:26 pm") 
jQuery(document).ready(function(){
var gmap\_ma5be695a30c8bf6cd34901bbd7a2f615 = {
positions : {
434 : new google.maps.LatLng( '38.256333', '-122.334334' )
},
bounds : new google.maps.LatLngBounds(), // empty for now, we'll dynamically extend it later
map : new google.maps.Map(
document.getElementById( 'gmap\_ma5be695a30c8bf6cd34901bbd7a2f615' ),
{
mapTypeId: google.maps.MapTypeId.ROADMAP,
center: new google.maps.LatLng( 0, 0 ),
zoom: 16 // Seems to be a good zoom for a single point
}
),
markers : {},
}; // end of gmap
// Extend the bounds of interest based on our positions
for ( var m in gmap\_ma5be695a30c8bf6cd34901bbd7a2f615.positions ) {
gmap\_ma5be695a30c8bf6cd34901bbd7a2f615.bounds.extend( gmap\_ma5be695a30c8bf6cd34901bbd7a2f615.positions[m] );
}
// Render markers
for ( var m in gmap\_ma5be695a30c8bf6cd34901bbd7a2f615.positions ) {
gmap\_ma5be695a30c8bf6cd34901bbd7a2f615.markers[m] = new google.maps.Marker( {
clickable: true,
map : gmap\_ma5be695a30c8bf6cd34901bbd7a2f615.map,
position : gmap\_ma5be695a30c8bf6cd34901bbd7a2f615.positions[m]
} );
}
// Redraw map to fit our new marker-based bounds
gmap\_ma5be695a30c8bf6cd34901bbd7a2f615.map.setCenter( gmap\_ma5be695a30c8bf6cd34901bbd7a2f615.positions[434] );
});