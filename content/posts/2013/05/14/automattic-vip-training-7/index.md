---
title: Automattic VIP Training
date: '2013-05-14T09:25:48+00:00'
format: image
service: flickr
tags:
- automattic
- vip
- wordpress
image: http://i0.wp.com/dentedreality.com.au/wp-content/uploads/2013/05/9439707830_892d2fb740_o.jpg?resize=607%2C452
---

[![Automattic VIP Training](http://i0.wp.com/dentedreality.com.au/wp-content/uploads/2013/05/9439707830_892d2fb740_o.jpg?resize=607%2C452)](http://dentedreality.com.au/2013/05/14/automattic-vip-training-7/) 
# [Automattic VIP Training](http://dentedreality.com.au/2013/05/14/automattic-vip-training-7/)

Annual VIP training workshop, held in Napa, CA





* #[automattic](http://dentedreality.com.au/tags/automattic/)
* #[vip](http://dentedreality.com.au/tags/vip/)
* #[wordpress](http://dentedreality.com.au/tags/wordpress/)

Posted on [Flickr](http://www.flickr.com/photos/borkazoid/9439707830/) [9:25 am, May 14, 2013](http://dentedreality.com.au/2013/05/14/automattic-vip-training-7/ "9:25 am") 
jQuery(document).ready(function(){
var gmap\_m5200143dfb3304bcd365281554915fbf = {
positions : {
968 : new google.maps.LatLng( '38.255166', '-122.334834' )
},
bounds : new google.maps.LatLngBounds(), // empty for now, we'll dynamically extend it later
map : new google.maps.Map(
document.getElementById( 'gmap\_m5200143dfb3304bcd365281554915fbf' ),
{
mapTypeId: google.maps.MapTypeId.ROADMAP,
center: new google.maps.LatLng( 0, 0 ),
zoom: 16 // Seems to be a good zoom for a single point
}
),
markers : {},
}; // end of gmap
// Extend the bounds of interest based on our positions
for ( var m in gmap\_m5200143dfb3304bcd365281554915fbf.positions ) {
gmap\_m5200143dfb3304bcd365281554915fbf.bounds.extend( gmap\_m5200143dfb3304bcd365281554915fbf.positions[m] );
}
// Render markers
for ( var m in gmap\_m5200143dfb3304bcd365281554915fbf.positions ) {
gmap\_m5200143dfb3304bcd365281554915fbf.markers[m] = new google.maps.Marker( {
clickable: true,
map : gmap\_m5200143dfb3304bcd365281554915fbf.map,
position : gmap\_m5200143dfb3304bcd365281554915fbf.positions[m]
} );
}
// Redraw map to fit our new marker-based bounds
gmap\_m5200143dfb3304bcd365281554915fbf.map.setCenter( gmap\_m5200143dfb3304bcd365281554915fbf.positions[968] );
});