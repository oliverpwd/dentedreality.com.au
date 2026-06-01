---
title: Crazy Icelandic Booze
date: '2012-02-23T18:02:55-06:00'
format: image
service: flickr
tags:
- alcohol
- iceland
latitude: '37.766666'
longitude: '-122.433'
image: https://i0.wp.com/s3.amazonaws.com/dentedreality-content/wp-content/uploads/2012/02/14190516/6813461694_19d76080ff_o-764x1024.jpg?resize=607%2C813&ssl=1
---

[![Crazy Icelandic Booze](https://i0.wp.com/s3.amazonaws.com/dentedreality-content/wp-content/uploads/2012/02/14190516/6813461694_19d76080ff_o-764x1024.jpg?resize=607%2C813&ssl=1)](https://dentedreality.com.au/2012/02/23/crazy-icelandic-booze/) 
# [Crazy Icelandic Booze](https://dentedreality.com.au/2012/02/23/crazy-icelandic-booze/)

[![Crazy Icelandic Booze](https://i0.wp.com/s3.amazonaws.com/dentedreality-content/wp-content/uploads/2012/02/14190516/6813461694_19d76080ff_o-764x1024.jpg?resize=607%2C813&ssl=1)](http://www.flickr.com/photos/borkazoid/6813461694/)

37.766666-122.433




* #[alcohol](https://dentedreality.com.au/tags/alcohol/)
* #[iceland](https://dentedreality.com.au/tags/iceland/)

Posted on [Flickr](http://www.flickr.com/photos/borkazoid/6813461694/) [6:02 pm, February 23, 2012](https://dentedreality.com.au/2012/02/23/crazy-icelandic-booze/ "6:02 pm") 
jQuery(document).ready(function(){
var gmap\_m03a13640e2d627e991c95c9937c49ba2 = {
positions : {
961 : new google.maps.LatLng( '37.766666', '-122.433' )
},
bounds : new google.maps.LatLngBounds(), // empty for now, we'll dynamically extend it later
map : new google.maps.Map(
document.getElementById( 'gmap\_m03a13640e2d627e991c95c9937c49ba2' ),
{
mapTypeId: google.maps.MapTypeId.ROADMAP,
center: new google.maps.LatLng( 0, 0 ),
zoom: 16 // Seems to be a good zoom for a single point
}
),
markers : {},
}; // end of gmap
// Extend the bounds of interest based on our positions
for ( var m in gmap\_m03a13640e2d627e991c95c9937c49ba2.positions ) {
gmap\_m03a13640e2d627e991c95c9937c49ba2.bounds.extend( gmap\_m03a13640e2d627e991c95c9937c49ba2.positions[m] );
}
// Render markers
for ( var m in gmap\_m03a13640e2d627e991c95c9937c49ba2.positions ) {
gmap\_m03a13640e2d627e991c95c9937c49ba2.markers[m] = new google.maps.Marker( {
clickable: true,
map : gmap\_m03a13640e2d627e991c95c9937c49ba2.map,
position : gmap\_m03a13640e2d627e991c95c9937c49ba2.positions[m]
} );
}
// Redraw map to fit our new marker-based bounds
gmap\_m03a13640e2d627e991c95c9937c49ba2.map.setCenter( gmap\_m03a13640e2d627e991c95c9937c49ba2.positions[961] );
});