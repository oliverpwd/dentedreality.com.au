---
title: Patxi’s!
date: '2011-05-27T16:22:23+00:00'
format: image
service: flickr
tags:
- owenswedding
- wedding
image: http://i2.wp.com/dentedreality.com.au/wp-content/uploads/2011/05/5803430784_3ff9aaeed9_o.jpg?resize=607%2C452
---

[![Patxi's!](http://i2.wp.com/dentedreality.com.au/wp-content/uploads/2011/05/5803430784_3ff9aaeed9_o.jpg?resize=607%2C452)](http://dentedreality.com.au/2011/05/27/patxis/) 
# [Patxi’s!](http://dentedreality.com.au/2011/05/27/patxis/)





* #[owenswedding](http://dentedreality.com.au/tags/owenswedding/)
* #[wedding](http://dentedreality.com.au/tags/wedding/)

Posted on [Flickr](http://www.flickr.com/photos/borkazoid/5803430784/) [4:22 pm, May 27, 2011](http://dentedreality.com.au/2011/05/27/patxis/ "4:22 pm") 
jQuery(document).ready(function(){
var gmap\_ma0e603d884c14868e5447bbd3bcce18b = {
positions : {
166 : new google.maps.LatLng( '37.800333', '-122.436' )
},
bounds : new google.maps.LatLngBounds(), // empty for now, we'll dynamically extend it later
map : new google.maps.Map(
document.getElementById( 'gmap\_ma0e603d884c14868e5447bbd3bcce18b' ),
{
mapTypeId: google.maps.MapTypeId.ROADMAP,
center: new google.maps.LatLng( 0, 0 ),
zoom: 16 // Seems to be a good zoom for a single point
}
),
markers : {},
}; // end of gmap
// Extend the bounds of interest based on our positions
for ( var m in gmap\_ma0e603d884c14868e5447bbd3bcce18b.positions ) {
gmap\_ma0e603d884c14868e5447bbd3bcce18b.bounds.extend( gmap\_ma0e603d884c14868e5447bbd3bcce18b.positions[m] );
}
// Render markers
for ( var m in gmap\_ma0e603d884c14868e5447bbd3bcce18b.positions ) {
gmap\_ma0e603d884c14868e5447bbd3bcce18b.markers[m] = new google.maps.Marker( {
clickable: true,
map : gmap\_ma0e603d884c14868e5447bbd3bcce18b.map,
position : gmap\_ma0e603d884c14868e5447bbd3bcce18b.positions[m]
} );
}
// Redraw map to fit our new marker-based bounds
gmap\_ma0e603d884c14868e5447bbd3bcce18b.map.setCenter( gmap\_ma0e603d884c14868e5447bbd3bcce18b.positions[166] );
});