---
title: SXSW 2012
date: '2012-03-14T12:27:33+00:00'
format: image
service: flickr
tags:
- Austin
- sxsw
- sxsw2012
- texas
image: http://i2.wp.com/dentedreality.com.au/wp-content/uploads/2012/03/7721700672_9b8d6900ea_o.jpg?resize=607%2C452
---

[![SXSW 2012](http://i2.wp.com/dentedreality.com.au/wp-content/uploads/2012/03/7721700672_9b8d6900ea_o.jpg?resize=607%2C452)](http://dentedreality.com.au/2012/03/14/sxsw-2012-2/) 
# [SXSW 2012](http://dentedreality.com.au/2012/03/14/sxsw-2012-2/)





* #[Austin](http://dentedreality.com.au/tags/austin/)
* #[sxsw](http://dentedreality.com.au/tags/sxsw/)
* #[sxsw2012](http://dentedreality.com.au/tags/sxsw2012/)
* #[texas](http://dentedreality.com.au/tags/texas/)

Posted on [Flickr](http://www.flickr.com/photos/borkazoid/7721700672/) [12:27 pm, March 14, 2012](http://dentedreality.com.au/2012/03/14/sxsw-2012-2/ "12:27 pm") 
jQuery(document).ready(function(){
var gmap\_mf0df1af8025f6957f30aa8af67832203 = {
positions : {
45 : new google.maps.LatLng( '30.265333', '-97.74' )
},
bounds : new google.maps.LatLngBounds(), // empty for now, we'll dynamically extend it later
map : new google.maps.Map(
document.getElementById( 'gmap\_mf0df1af8025f6957f30aa8af67832203' ),
{
mapTypeId: google.maps.MapTypeId.ROADMAP,
center: new google.maps.LatLng( 0, 0 ),
zoom: 16 // Seems to be a good zoom for a single point
}
),
markers : {},
}; // end of gmap
// Extend the bounds of interest based on our positions
for ( var m in gmap\_mf0df1af8025f6957f30aa8af67832203.positions ) {
gmap\_mf0df1af8025f6957f30aa8af67832203.bounds.extend( gmap\_mf0df1af8025f6957f30aa8af67832203.positions[m] );
}
// Render markers
for ( var m in gmap\_mf0df1af8025f6957f30aa8af67832203.positions ) {
gmap\_mf0df1af8025f6957f30aa8af67832203.markers[m] = new google.maps.Marker( {
clickable: true,
map : gmap\_mf0df1af8025f6957f30aa8af67832203.map,
position : gmap\_mf0df1af8025f6957f30aa8af67832203.positions[m]
} );
}
// Redraw map to fit our new marker-based bounds
gmap\_mf0df1af8025f6957f30aa8af67832203.map.setCenter( gmap\_mf0df1af8025f6957f30aa8af67832203.positions[45] );
});