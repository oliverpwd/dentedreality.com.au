---
title: VIP Workshop, 2012
date: '2012-03-26T15:08:44+00:00'
format: image
service: flickr
tags:
- automattic
- vip
- wordpress
- wpvip
image: http://i2.wp.com/dentedreality.com.au/wp-content/uploads/2012/03/7770424564_c11d2afb8b_o.jpg?resize=607%2C452
---

[![VIP Workshop, 2012](http://i2.wp.com/dentedreality.com.au/wp-content/uploads/2012/03/7770424564_c11d2afb8b_o.jpg?resize=607%2C452)](http://dentedreality.com.au/2012/03/26/vip-workshop-2012-4/) 
# [VIP Workshop, 2012](http://dentedreality.com.au/2012/03/26/vip-workshop-2012-4/)





* #[automattic](http://dentedreality.com.au/tags/automattic/)
* #[vip](http://dentedreality.com.au/tags/vip/)
* #[wordpress](http://dentedreality.com.au/tags/wordpress/)
* #[wpvip](http://dentedreality.com.au/tags/wpvip/)

Posted on [Flickr](http://www.flickr.com/photos/borkazoid/7770424564/) [3:08 pm, March 26, 2012](http://dentedreality.com.au/2012/03/26/vip-workshop-2012-4/ "3:08 pm") 
jQuery(document).ready(function(){
var gmap\_m269629bed71a7c895177e133c5689b51 = {
positions : {
460 : new google.maps.LatLng( '38.258166', '-122.3335' )
},
bounds : new google.maps.LatLngBounds(), // empty for now, we'll dynamically extend it later
map : new google.maps.Map(
document.getElementById( 'gmap\_m269629bed71a7c895177e133c5689b51' ),
{
mapTypeId: google.maps.MapTypeId.ROADMAP,
center: new google.maps.LatLng( 0, 0 ),
zoom: 16 // Seems to be a good zoom for a single point
}
),
markers : {},
}; // end of gmap
// Extend the bounds of interest based on our positions
for ( var m in gmap\_m269629bed71a7c895177e133c5689b51.positions ) {
gmap\_m269629bed71a7c895177e133c5689b51.bounds.extend( gmap\_m269629bed71a7c895177e133c5689b51.positions[m] );
}
// Render markers
for ( var m in gmap\_m269629bed71a7c895177e133c5689b51.positions ) {
gmap\_m269629bed71a7c895177e133c5689b51.markers[m] = new google.maps.Marker( {
clickable: true,
map : gmap\_m269629bed71a7c895177e133c5689b51.map,
position : gmap\_m269629bed71a7c895177e133c5689b51.positions[m]
} );
}
// Redraw map to fit our new marker-based bounds
gmap\_m269629bed71a7c895177e133c5689b51.map.setCenter( gmap\_m269629bed71a7c895177e133c5689b51.positions[460] );
});