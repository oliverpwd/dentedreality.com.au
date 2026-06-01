---
title: Isolated House
date: '2006-12-28T19:19:55+00:00'
format: image
service: flickr
tags:
- house
- islandhome
- isolated
- isolatedhouse
- lonely
- phuket
- thailand
- thailand06
image: http://i1.wp.com/dentedreality.com.au/wp-content/uploads/2006/12/348095048_d1ffd2def4_o.jpg?resize=607%2C455
---

[![Isolated House](http://i1.wp.com/dentedreality.com.au/wp-content/uploads/2006/12/348095048_d1ffd2def4_o.jpg?resize=607%2C455)](http://dentedreality.com.au/2006/12/28/isolated-house/) 
# [Isolated House](http://dentedreality.com.au/2006/12/28/isolated-house/)

Surely one of the most isolated houses possible – this is the only house on an island in the middle of nowhere.





* #[house](http://dentedreality.com.au/tags/house/)
* #[islandhome](http://dentedreality.com.au/tags/islandhome/)
* #[isolated](http://dentedreality.com.au/tags/isolated/)
* #[isolatedhouse](http://dentedreality.com.au/tags/isolatedhouse/)
* #[lonely](http://dentedreality.com.au/tags/lonely/)
* #[phuket](http://dentedreality.com.au/tags/phuket/)
* #[thailand](http://dentedreality.com.au/tags/thailand/)
* #[thailand06](http://dentedreality.com.au/tags/thailand06/)

Posted on [Flickr](http://www.flickr.com/photos/borkazoid/348095048/) [7:19 pm, December 28, 2006](http://dentedreality.com.au/2006/12/28/isolated-house/ "7:19 pm") 
jQuery(document).ready(function(){
var gmap\_m648952c282bfd2bf6fec92d900a93501 = {
positions : {
64 : new google.maps.LatLng( '8.095005', '98.457927' )
},
bounds : new google.maps.LatLngBounds(), // empty for now, we'll dynamically extend it later
map : new google.maps.Map(
document.getElementById( 'gmap\_m648952c282bfd2bf6fec92d900a93501' ),
{
mapTypeId: google.maps.MapTypeId.ROADMAP,
center: new google.maps.LatLng( 0, 0 ),
zoom: 16 // Seems to be a good zoom for a single point
}
),
markers : {},
}; // end of gmap
// Extend the bounds of interest based on our positions
for ( var m in gmap\_m648952c282bfd2bf6fec92d900a93501.positions ) {
gmap\_m648952c282bfd2bf6fec92d900a93501.bounds.extend( gmap\_m648952c282bfd2bf6fec92d900a93501.positions[m] );
}
// Render markers
for ( var m in gmap\_m648952c282bfd2bf6fec92d900a93501.positions ) {
gmap\_m648952c282bfd2bf6fec92d900a93501.markers[m] = new google.maps.Marker( {
clickable: true,
map : gmap\_m648952c282bfd2bf6fec92d900a93501.map,
position : gmap\_m648952c282bfd2bf6fec92d900a93501.positions[m]
} );
}
// Redraw map to fit our new marker-based bounds
gmap\_m648952c282bfd2bf6fec92d900a93501.map.setCenter( gmap\_m648952c282bfd2bf6fec92d900a93501.positions[64] );
});