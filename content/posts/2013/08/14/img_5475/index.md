---
title: Peter Luger. Money.
date: '2013-08-14T18:52:14-06:00'
format: image
service: flickr
tags:
- chocolate
- coin
- money
- peter luger
- steakhouse
latitude: '40.71'
longitude: '-73.962334'
image: https://s3.amazonaws.com/dentedreality-content/wp-content/uploads/2013/08/14183808/9767761371_c774021134_o.jpg
---

[![IMG_5475](https://s3.amazonaws.com/dentedreality-content/wp-content/uploads/2013/08/14183808/9767761371_c774021134_o.jpg)](https://dentedreality.com.au/2013/08/14/img_5475/) 
# [Peter Luger. Money.](https://dentedreality.com.au/2013/08/14/img_5475/)

[![IMG_5475](https://s3.amazonaws.com/dentedreality-content/wp-content/uploads/2013/08/14183808/9767761371_c774021134_o.jpg)](http://www.flickr.com/photos/borkazoid/9767761371/)

40.71-73.962334




* #[chocolate](https://dentedreality.com.au/tags/chocolate/)
* #[coin](https://dentedreality.com.au/tags/coin/)
* #[money](https://dentedreality.com.au/tags/money/)
* #[peter luger](https://dentedreality.com.au/tags/peter-luger/)
* #[steakhouse](https://dentedreality.com.au/tags/steakhouse/)

Posted on [Flickr](http://www.flickr.com/photos/borkazoid/9767761371/) [6:52 pm, August 14, 2013](https://dentedreality.com.au/2013/08/14/img_5475/ "6:52 pm") 
jQuery(document).ready(function(){
var gmap\_m842d52c60aef58c00b58c3c05730405e = {
positions : {
692 : new google.maps.LatLng( '40.71', '-73.962334' )
},
bounds : new google.maps.LatLngBounds(), // empty for now, we'll dynamically extend it later
map : new google.maps.Map(
document.getElementById( 'gmap\_m842d52c60aef58c00b58c3c05730405e' ),
{
mapTypeId: google.maps.MapTypeId.ROADMAP,
center: new google.maps.LatLng( 0, 0 ),
zoom: 16 // Seems to be a good zoom for a single point
}
),
markers : {},
}; // end of gmap
// Extend the bounds of interest based on our positions
for ( var m in gmap\_m842d52c60aef58c00b58c3c05730405e.positions ) {
gmap\_m842d52c60aef58c00b58c3c05730405e.bounds.extend( gmap\_m842d52c60aef58c00b58c3c05730405e.positions[m] );
}
// Render markers
for ( var m in gmap\_m842d52c60aef58c00b58c3c05730405e.positions ) {
gmap\_m842d52c60aef58c00b58c3c05730405e.markers[m] = new google.maps.Marker( {
clickable: true,
map : gmap\_m842d52c60aef58c00b58c3c05730405e.map,
position : gmap\_m842d52c60aef58c00b58c3c05730405e.positions[m]
} );
}
// Redraw map to fit our new marker-based bounds
gmap\_m842d52c60aef58c00b58c3c05730405e.map.setCenter( gmap\_m842d52c60aef58c00b58c3c05730405e.positions[692] );
});