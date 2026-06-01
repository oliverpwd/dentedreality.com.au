---
title: VIP Workshop, 2012
date: '2012-03-28T19:11:41+00:00'
format: image
service: flickr
tags:
- automattic
- vip
- wordpress
- wpvip
image: http://i2.wp.com/dentedreality.com.au/wp-content/uploads/2012/03/7770426078_db98107a49_o.jpg?resize=607%2C452
---

[![VIP Workshop, 2012](http://i2.wp.com/dentedreality.com.au/wp-content/uploads/2012/03/7770426078_db98107a49_o.jpg?resize=607%2C452)](http://dentedreality.com.au/2012/03/28/vip-workshop-2012/) 
# [VIP Workshop, 2012](http://dentedreality.com.au/2012/03/28/vip-workshop-2012/)





* #[automattic](http://dentedreality.com.au/tags/automattic/)
* #[vip](http://dentedreality.com.au/tags/vip/)
* #[wordpress](http://dentedreality.com.au/tags/wordpress/)
* #[wpvip](http://dentedreality.com.au/tags/wpvip/)

Posted on [Flickr](http://www.flickr.com/photos/borkazoid/7770426078/) [7:11 pm, March 28, 2012](http://dentedreality.com.au/2012/03/28/vip-workshop-2012/ "7:11 pm") 
jQuery(document).ready(function(){
var gmap\_m15c2e4009c44381d4b28751364fe11b2 = {
positions : {
87 : new google.maps.LatLng( '38.255333', '-122.3355' )
},
bounds : new google.maps.LatLngBounds(), // empty for now, we'll dynamically extend it later
map : new google.maps.Map(
document.getElementById( 'gmap\_m15c2e4009c44381d4b28751364fe11b2' ),
{
mapTypeId: google.maps.MapTypeId.ROADMAP,
center: new google.maps.LatLng( 0, 0 ),
zoom: 16 // Seems to be a good zoom for a single point
}
),
markers : {},
}; // end of gmap
// Extend the bounds of interest based on our positions
for ( var m in gmap\_m15c2e4009c44381d4b28751364fe11b2.positions ) {
gmap\_m15c2e4009c44381d4b28751364fe11b2.bounds.extend( gmap\_m15c2e4009c44381d4b28751364fe11b2.positions[m] );
}
// Render markers
for ( var m in gmap\_m15c2e4009c44381d4b28751364fe11b2.positions ) {
gmap\_m15c2e4009c44381d4b28751364fe11b2.markers[m] = new google.maps.Marker( {
clickable: true,
map : gmap\_m15c2e4009c44381d4b28751364fe11b2.map,
position : gmap\_m15c2e4009c44381d4b28751364fe11b2.positions[m]
} );
}
// Redraw map to fit our new marker-based bounds
gmap\_m15c2e4009c44381d4b28751364fe11b2.map.setCenter( gmap\_m15c2e4009c44381d4b28751364fe11b2.positions[87] );
});