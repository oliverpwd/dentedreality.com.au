---
title: Automattic VIP Training
date: '2013-05-14T10:31:20+00:00'
format: image
service: flickr
tags:
- automattic
- vip
- wordpress
image: http://i2.wp.com/dentedreality.com.au/wp-content/uploads/2013/05/9436926495_90a0fcb4f1_o.jpg?resize=607%2C452
---

[![Automattic VIP Training](http://i2.wp.com/dentedreality.com.au/wp-content/uploads/2013/05/9436926495_90a0fcb4f1_o.jpg?resize=607%2C452)](http://dentedreality.com.au/2013/05/14/automattic-vip-training-6/) 
# [Automattic VIP Training](http://dentedreality.com.au/2013/05/14/automattic-vip-training-6/)

Annual VIP training workshop, held in Napa, CA





* #[automattic](http://dentedreality.com.au/tags/automattic/)
* #[vip](http://dentedreality.com.au/tags/vip/)
* #[wordpress](http://dentedreality.com.au/tags/wordpress/)

Posted on [Flickr](http://www.flickr.com/photos/borkazoid/9436926495/) [10:31 am, May 14, 2013](http://dentedreality.com.au/2013/05/14/automattic-vip-training-6/ "10:31 am") 
jQuery(document).ready(function(){
var gmap\_m0c743084c63bbf6e4c0eef9ec2a3950c = {
positions : {
25 : new google.maps.LatLng( '38.256333', '-122.334334' )
},
bounds : new google.maps.LatLngBounds(), // empty for now, we'll dynamically extend it later
map : new google.maps.Map(
document.getElementById( 'gmap\_m0c743084c63bbf6e4c0eef9ec2a3950c' ),
{
mapTypeId: google.maps.MapTypeId.ROADMAP,
center: new google.maps.LatLng( 0, 0 ),
zoom: 16 // Seems to be a good zoom for a single point
}
),
markers : {},
}; // end of gmap
// Extend the bounds of interest based on our positions
for ( var m in gmap\_m0c743084c63bbf6e4c0eef9ec2a3950c.positions ) {
gmap\_m0c743084c63bbf6e4c0eef9ec2a3950c.bounds.extend( gmap\_m0c743084c63bbf6e4c0eef9ec2a3950c.positions[m] );
}
// Render markers
for ( var m in gmap\_m0c743084c63bbf6e4c0eef9ec2a3950c.positions ) {
gmap\_m0c743084c63bbf6e4c0eef9ec2a3950c.markers[m] = new google.maps.Marker( {
clickable: true,
map : gmap\_m0c743084c63bbf6e4c0eef9ec2a3950c.map,
position : gmap\_m0c743084c63bbf6e4c0eef9ec2a3950c.positions[m]
} );
}
// Redraw map to fit our new marker-based bounds
gmap\_m0c743084c63bbf6e4c0eef9ec2a3950c.map.setCenter( gmap\_m0c743084c63bbf6e4c0eef9ec2a3950c.positions[25] );
});