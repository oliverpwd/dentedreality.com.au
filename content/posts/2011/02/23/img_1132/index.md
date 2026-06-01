---
title: IMG_1132
date: '2011-02-23T09:25:28-07:00'
format: image
service: flickr
tags:
- newyork
- newyorkcity
- NYC
latitude: '40.708833'
longitude: '-74.001667'
image: https://dentedreality-content.s3.amazonaws.com/wp-content/uploads/2011/02/14190132/5802616758_1fe0d616d8_o.jpg
---

[![IMG_1132](https://dentedreality-content.s3.amazonaws.com/wp-content/uploads/2011/02/14190132/5802616758_1fe0d616d8_o.jpg)](https://dentedreality.com.au/2011/02/23/img_1132/) 
# [IMG\_1132](https://dentedreality.com.au/2011/02/23/img_1132/)

[![IMG_1132](https://dentedreality-content.s3.amazonaws.com/wp-content/uploads/2011/02/14190132/5802616758_1fe0d616d8_o.jpg)](http://www.flickr.com/photos/borkazoid/5802616758/)

40.708833-74.001667




* #[newyork](https://dentedreality.com.au/tags/newyork/)
* #[newyorkcity](https://dentedreality.com.au/tags/newyorkcity/)
* #[NYC](https://dentedreality.com.au/tags/nyc/)

Posted on [Flickr](http://www.flickr.com/photos/borkazoid/5802616758/) [9:25 am, February 23, 2011](https://dentedreality.com.au/2011/02/23/img_1132/ "9:25 am") 
jQuery(document).ready(function(){
var gmap\_m5437bf5bc6e4ff89eead9944d728118d = {
positions : {
780 : new google.maps.LatLng( '40.708833', '-74.001667' )
},
bounds : new google.maps.LatLngBounds(), // empty for now, we'll dynamically extend it later
map : new google.maps.Map(
document.getElementById( 'gmap\_m5437bf5bc6e4ff89eead9944d728118d' ),
{
mapTypeId: google.maps.MapTypeId.ROADMAP,
center: new google.maps.LatLng( 0, 0 ),
zoom: 16 // Seems to be a good zoom for a single point
}
),
markers : {},
}; // end of gmap
// Extend the bounds of interest based on our positions
for ( var m in gmap\_m5437bf5bc6e4ff89eead9944d728118d.positions ) {
gmap\_m5437bf5bc6e4ff89eead9944d728118d.bounds.extend( gmap\_m5437bf5bc6e4ff89eead9944d728118d.positions[m] );
}
// Render markers
for ( var m in gmap\_m5437bf5bc6e4ff89eead9944d728118d.positions ) {
gmap\_m5437bf5bc6e4ff89eead9944d728118d.markers[m] = new google.maps.Marker( {
clickable: true,
map : gmap\_m5437bf5bc6e4ff89eead9944d728118d.map,
position : gmap\_m5437bf5bc6e4ff89eead9944d728118d.positions[m]
} );
}
// Redraw map to fit our new marker-based bounds
gmap\_m5437bf5bc6e4ff89eead9944d728118d.map.setCenter( gmap\_m5437bf5bc6e4ff89eead9944d728118d.positions[780] );
});