---
title: GGB on a nice day
date: '2011-02-06T10:08:38-07:00'
format: image
service: flickr
tags:
- california
- ggb
- goldengatebridge
- sanfrancisco
latitude: '37.809166'
longitude: '-122.4695'
image: https://dentedreality-content.s3.amazonaws.com/wp-content/uploads/2011/02/14190124/5802053165_0813a8f536_o.jpg
---

[![GGB on a nice day](https://dentedreality-content.s3.amazonaws.com/wp-content/uploads/2011/02/14190124/5802053165_0813a8f536_o.jpg)](https://dentedreality.com.au/2011/02/06/ggb-on-a-nice-day/) 
# [GGB on a nice day](https://dentedreality.com.au/2011/02/06/ggb-on-a-nice-day/)

[![GGB on a nice day](https://dentedreality-content.s3.amazonaws.com/wp-content/uploads/2011/02/14190124/5802053165_0813a8f536_o.jpg)](http://www.flickr.com/photos/borkazoid/5802053165/)

37.809166-122.4695




* #[california](https://dentedreality.com.au/tags/california/)
* #[ggb](https://dentedreality.com.au/tags/ggb/)
* #[goldengatebridge](https://dentedreality.com.au/tags/goldengatebridge/)
* #[sanfrancisco](https://dentedreality.com.au/tags/sanfrancisco/)

Posted on [Flickr](http://www.flickr.com/photos/borkazoid/5802053165/) [10:08 am, February 6, 2011](https://dentedreality.com.au/2011/02/06/ggb-on-a-nice-day/ "10:08 am") 
jQuery(document).ready(function(){
var gmap\_m320303df4d52770aa51f4c43a0ff43b0 = {
positions : {
628 : new google.maps.LatLng( '37.809166', '-122.4695' )
},
bounds : new google.maps.LatLngBounds(), // empty for now, we'll dynamically extend it later
map : new google.maps.Map(
document.getElementById( 'gmap\_m320303df4d52770aa51f4c43a0ff43b0' ),
{
mapTypeId: google.maps.MapTypeId.ROADMAP,
center: new google.maps.LatLng( 0, 0 ),
zoom: 16 // Seems to be a good zoom for a single point
}
),
markers : {},
}; // end of gmap
// Extend the bounds of interest based on our positions
for ( var m in gmap\_m320303df4d52770aa51f4c43a0ff43b0.positions ) {
gmap\_m320303df4d52770aa51f4c43a0ff43b0.bounds.extend( gmap\_m320303df4d52770aa51f4c43a0ff43b0.positions[m] );
}
// Render markers
for ( var m in gmap\_m320303df4d52770aa51f4c43a0ff43b0.positions ) {
gmap\_m320303df4d52770aa51f4c43a0ff43b0.markers[m] = new google.maps.Marker( {
clickable: true,
map : gmap\_m320303df4d52770aa51f4c43a0ff43b0.map,
position : gmap\_m320303df4d52770aa51f4c43a0ff43b0.positions[m]
} );
}
// Redraw map to fit our new marker-based bounds
gmap\_m320303df4d52770aa51f4c43a0ff43b0.map.setCenter( gmap\_m320303df4d52770aa51f4c43a0ff43b0.positions[628] );
});