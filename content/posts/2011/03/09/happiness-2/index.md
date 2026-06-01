---
title: Happiness
date: '2011-03-09T10:09:17-07:00'
format: image
service: flickr
tags:
- banner
- billboard
- happiness
latitude: '37.789333'
longitude: '-122.418667'
image: https://dentedreality-content.s3.amazonaws.com/wp-content/uploads/2011/03/14190136/5802619870_7aa3def184_o.jpg
---

[![Happiness](https://dentedreality-content.s3.amazonaws.com/wp-content/uploads/2011/03/14190136/5802619870_7aa3def184_o.jpg)](https://dentedreality.com.au/2011/03/09/happiness-2/) 
# [Happiness](https://dentedreality.com.au/2011/03/09/happiness-2/)

[![Happiness](https://dentedreality-content.s3.amazonaws.com/wp-content/uploads/2011/03/14190136/5802619870_7aa3def184_o.jpg)](http://www.flickr.com/photos/borkazoid/5802619870/)

37.789333-122.418667




* #[banner](https://dentedreality.com.au/tags/banner/)
* #[billboard](https://dentedreality.com.au/tags/billboard/)
* #[happiness](https://dentedreality.com.au/tags/happiness/)

Posted on [Flickr](http://www.flickr.com/photos/borkazoid/5802619870/) [10:09 am, March 9, 2011](https://dentedreality.com.au/2011/03/09/happiness-2/ "10:09 am") 
jQuery(document).ready(function(){
var gmap\_md5cf244ef95eab57ca74da4cacf9ccd3 = {
positions : {
386 : new google.maps.LatLng( '37.789333', '-122.418667' )
},
bounds : new google.maps.LatLngBounds(), // empty for now, we'll dynamically extend it later
map : new google.maps.Map(
document.getElementById( 'gmap\_md5cf244ef95eab57ca74da4cacf9ccd3' ),
{
mapTypeId: google.maps.MapTypeId.ROADMAP,
center: new google.maps.LatLng( 0, 0 ),
zoom: 16 // Seems to be a good zoom for a single point
}
),
markers : {},
}; // end of gmap
// Extend the bounds of interest based on our positions
for ( var m in gmap\_md5cf244ef95eab57ca74da4cacf9ccd3.positions ) {
gmap\_md5cf244ef95eab57ca74da4cacf9ccd3.bounds.extend( gmap\_md5cf244ef95eab57ca74da4cacf9ccd3.positions[m] );
}
// Render markers
for ( var m in gmap\_md5cf244ef95eab57ca74da4cacf9ccd3.positions ) {
gmap\_md5cf244ef95eab57ca74da4cacf9ccd3.markers[m] = new google.maps.Marker( {
clickable: true,
map : gmap\_md5cf244ef95eab57ca74da4cacf9ccd3.map,
position : gmap\_md5cf244ef95eab57ca74da4cacf9ccd3.positions[m]
} );
}
// Redraw map to fit our new marker-based bounds
gmap\_md5cf244ef95eab57ca74da4cacf9ccd3.map.setCenter( gmap\_md5cf244ef95eab57ca74da4cacf9ccd3.positions[386] );
});