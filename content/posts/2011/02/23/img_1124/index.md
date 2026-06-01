---
title: IMG_1124
date: '2011-02-23T09:06:06-07:00'
format: image
service: flickr
tags:
- newyork
- newyorkcity
- NYC
latitude: '40.7155'
longitude: '-74.003667'
image: https://dentedreality-content.s3.amazonaws.com/wp-content/uploads/2011/02/14190130/5802058255_385b7f3e04_o.jpg
---

[![IMG_1124](https://dentedreality-content.s3.amazonaws.com/wp-content/uploads/2011/02/14190130/5802058255_385b7f3e04_o.jpg)](https://dentedreality.com.au/2011/02/23/img_1124/) 
# [IMG\_1124](https://dentedreality.com.au/2011/02/23/img_1124/)

[![IMG_1124](https://dentedreality-content.s3.amazonaws.com/wp-content/uploads/2011/02/14190130/5802058255_385b7f3e04_o.jpg)](http://www.flickr.com/photos/borkazoid/5802058255/)

40.7155-74.003667




* #[newyork](https://dentedreality.com.au/tags/newyork/)
* #[newyorkcity](https://dentedreality.com.au/tags/newyorkcity/)
* #[NYC](https://dentedreality.com.au/tags/nyc/)

Posted on [Flickr](http://www.flickr.com/photos/borkazoid/5802058255/) [9:06 am, February 23, 2011](https://dentedreality.com.au/2011/02/23/img_1124/ "9:06 am") 
jQuery(document).ready(function(){
var gmap\_m8cd7ee7a7aeb637b5c723f3f3b8fffc4 = {
positions : {
735 : new google.maps.LatLng( '40.7155', '-74.003667' )
},
bounds : new google.maps.LatLngBounds(), // empty for now, we'll dynamically extend it later
map : new google.maps.Map(
document.getElementById( 'gmap\_m8cd7ee7a7aeb637b5c723f3f3b8fffc4' ),
{
mapTypeId: google.maps.MapTypeId.ROADMAP,
center: new google.maps.LatLng( 0, 0 ),
zoom: 16 // Seems to be a good zoom for a single point
}
),
markers : {},
}; // end of gmap
// Extend the bounds of interest based on our positions
for ( var m in gmap\_m8cd7ee7a7aeb637b5c723f3f3b8fffc4.positions ) {
gmap\_m8cd7ee7a7aeb637b5c723f3f3b8fffc4.bounds.extend( gmap\_m8cd7ee7a7aeb637b5c723f3f3b8fffc4.positions[m] );
}
// Render markers
for ( var m in gmap\_m8cd7ee7a7aeb637b5c723f3f3b8fffc4.positions ) {
gmap\_m8cd7ee7a7aeb637b5c723f3f3b8fffc4.markers[m] = new google.maps.Marker( {
clickable: true,
map : gmap\_m8cd7ee7a7aeb637b5c723f3f3b8fffc4.map,
position : gmap\_m8cd7ee7a7aeb637b5c723f3f3b8fffc4.positions[m]
} );
}
// Redraw map to fit our new marker-based bounds
gmap\_m8cd7ee7a7aeb637b5c723f3f3b8fffc4.map.setCenter( gmap\_m8cd7ee7a7aeb637b5c723f3f3b8fffc4.positions[735] );
});