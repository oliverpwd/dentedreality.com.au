---
title: Automattic VIP Training
date: '2013-05-15T16:11:07+00:00'
format: image
service: flickr
tags:
- automattic
- vip
- wordpress
image: http://i2.wp.com/dentedreality.com.au/wp-content/uploads/2013/05/9439710954_930ed39ec2_o.jpg?resize=607%2C452
---

[![Automattic VIP Training](http://i2.wp.com/dentedreality.com.au/wp-content/uploads/2013/05/9439710954_930ed39ec2_o.jpg?resize=607%2C452)](http://dentedreality.com.au/2013/05/15/automattic-vip-training/) 
# [Automattic VIP Training](http://dentedreality.com.au/2013/05/15/automattic-vip-training/)

Annual VIP training workshop, held in Napa, CA





* #[automattic](http://dentedreality.com.au/tags/automattic/)
* #[vip](http://dentedreality.com.au/tags/vip/)
* #[wordpress](http://dentedreality.com.au/tags/wordpress/)

Posted on [Flickr](http://www.flickr.com/photos/borkazoid/9439710954/) [4:11 pm, May 15, 2013](http://dentedreality.com.au/2013/05/15/automattic-vip-training/ "4:11 pm") 
jQuery(document).ready(function(){
var gmap\_m6dc0adc965e2a3049d64ba2d8c137c1d = {
positions : {
82 : new google.maps.LatLng( '38.294166', '-122.458667' )
},
bounds : new google.maps.LatLngBounds(), // empty for now, we'll dynamically extend it later
map : new google.maps.Map(
document.getElementById( 'gmap\_m6dc0adc965e2a3049d64ba2d8c137c1d' ),
{
mapTypeId: google.maps.MapTypeId.ROADMAP,
center: new google.maps.LatLng( 0, 0 ),
zoom: 16 // Seems to be a good zoom for a single point
}
),
markers : {},
}; // end of gmap
// Extend the bounds of interest based on our positions
for ( var m in gmap\_m6dc0adc965e2a3049d64ba2d8c137c1d.positions ) {
gmap\_m6dc0adc965e2a3049d64ba2d8c137c1d.bounds.extend( gmap\_m6dc0adc965e2a3049d64ba2d8c137c1d.positions[m] );
}
// Render markers
for ( var m in gmap\_m6dc0adc965e2a3049d64ba2d8c137c1d.positions ) {
gmap\_m6dc0adc965e2a3049d64ba2d8c137c1d.markers[m] = new google.maps.Marker( {
clickable: true,
map : gmap\_m6dc0adc965e2a3049d64ba2d8c137c1d.map,
position : gmap\_m6dc0adc965e2a3049d64ba2d8c137c1d.positions[m]
} );
}
// Redraw map to fit our new marker-based bounds
gmap\_m6dc0adc965e2a3049d64ba2d8c137c1d.map.setCenter( gmap\_m6dc0adc965e2a3049d64ba2d8c137c1d.positions[82] );
});