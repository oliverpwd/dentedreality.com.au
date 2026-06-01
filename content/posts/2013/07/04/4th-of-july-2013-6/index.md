---
title: 4th of July, 2013
date: '2013-07-04T16:29:02+00:00'
format: image
service: flickr
tags:
- '20130704'
- 4thofjuly
- erika
- mattmoser
image: http://i2.wp.com/dentedreality.com.au/wp-content/uploads/2013/07/9437056007_f1f0c18bea_o.jpg?resize=607%2C452
---

[![4th of July, 2013](http://i2.wp.com/dentedreality.com.au/wp-content/uploads/2013/07/9437056007_f1f0c18bea_o.jpg?resize=607%2C452)](http://dentedreality.com.au/2013/07/04/4th-of-july-2013-6/) 
# [4th of July, 2013](http://dentedreality.com.au/2013/07/04/4th-of-july-2013-6/)





* #[20130704](http://dentedreality.com.au/tags/20130704/)
* #[4thofjuly](http://dentedreality.com.au/tags/4thofjuly/)
* #[erika](http://dentedreality.com.au/tags/erika/)
* #[mattmoser](http://dentedreality.com.au/tags/mattmoser/)

Posted on [Flickr](http://www.flickr.com/photos/borkazoid/9437056007/) [4:29 pm, July 4, 2013](http://dentedreality.com.au/2013/07/04/4th-of-july-2013-6/ "4:29 pm") 
jQuery(document).ready(function(){
var gmap\_mcabc54e104a744ee351b76e273a4f5dd = {
positions : {
958 : new google.maps.LatLng( '40.717', '-73.945667' )
},
bounds : new google.maps.LatLngBounds(), // empty for now, we'll dynamically extend it later
map : new google.maps.Map(
document.getElementById( 'gmap\_mcabc54e104a744ee351b76e273a4f5dd' ),
{
mapTypeId: google.maps.MapTypeId.ROADMAP,
center: new google.maps.LatLng( 0, 0 ),
zoom: 16 // Seems to be a good zoom for a single point
}
),
markers : {},
}; // end of gmap
// Extend the bounds of interest based on our positions
for ( var m in gmap\_mcabc54e104a744ee351b76e273a4f5dd.positions ) {
gmap\_mcabc54e104a744ee351b76e273a4f5dd.bounds.extend( gmap\_mcabc54e104a744ee351b76e273a4f5dd.positions[m] );
}
// Render markers
for ( var m in gmap\_mcabc54e104a744ee351b76e273a4f5dd.positions ) {
gmap\_mcabc54e104a744ee351b76e273a4f5dd.markers[m] = new google.maps.Marker( {
clickable: true,
map : gmap\_mcabc54e104a744ee351b76e273a4f5dd.map,
position : gmap\_mcabc54e104a744ee351b76e273a4f5dd.positions[m]
} );
}
// Redraw map to fit our new marker-based bounds
gmap\_mcabc54e104a744ee351b76e273a4f5dd.map.setCenter( gmap\_mcabc54e104a744ee351b76e273a4f5dd.positions[958] );
});