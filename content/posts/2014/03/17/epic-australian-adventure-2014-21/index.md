---
title: Epic Australian Adventure, 2014
date: '2014-03-17T11:56:20+00:00'
format: image
service: flickr
tags:
- perth
image: http://i2.wp.com/dentedreality.com.au/wp-content/uploads/2014/03/13904722732_827bc5c0d2_o.jpg?resize=607%2C455
---

[![Epic Australian Adventure, 2014](http://i2.wp.com/dentedreality.com.au/wp-content/uploads/2014/03/13904722732_827bc5c0d2_o.jpg?resize=607%2C455)](http://dentedreality.com.au/2014/03/17/epic-australian-adventure-2014-21/) 
# [Epic Australian Adventure, 2014](http://dentedreality.com.au/2014/03/17/epic-australian-adventure-2014-21/)

Perth, Mooloolaba and Melbourne





* #[perth](http://dentedreality.com.au/tags/perth/)

Posted on [Flickr](http://www.flickr.com/photos/borkazoid/13904722732/) [11:56 am, March 17, 2014](http://dentedreality.com.au/2014/03/17/epic-australian-adventure-2014-21/ "11:56 am") 
jQuery(document).ready(function(){
var gmap\_m581c5a6f24bb1567a3677452fc5eac62 = {
positions : {
672 : new google.maps.LatLng( '-31.775328', '115.968719' )
},
bounds : new google.maps.LatLngBounds(), // empty for now, we'll dynamically extend it later
map : new google.maps.Map(
document.getElementById( 'gmap\_m581c5a6f24bb1567a3677452fc5eac62' ),
{
mapTypeId: google.maps.MapTypeId.ROADMAP,
center: new google.maps.LatLng( 0, 0 ),
zoom: 16 // Seems to be a good zoom for a single point
}
),
markers : {},
}; // end of gmap
// Extend the bounds of interest based on our positions
for ( var m in gmap\_m581c5a6f24bb1567a3677452fc5eac62.positions ) {
gmap\_m581c5a6f24bb1567a3677452fc5eac62.bounds.extend( gmap\_m581c5a6f24bb1567a3677452fc5eac62.positions[m] );
}
// Render markers
for ( var m in gmap\_m581c5a6f24bb1567a3677452fc5eac62.positions ) {
gmap\_m581c5a6f24bb1567a3677452fc5eac62.markers[m] = new google.maps.Marker( {
clickable: true,
map : gmap\_m581c5a6f24bb1567a3677452fc5eac62.map,
position : gmap\_m581c5a6f24bb1567a3677452fc5eac62.positions[m]
} );
}
// Redraw map to fit our new marker-based bounds
gmap\_m581c5a6f24bb1567a3677452fc5eac62.map.setCenter( gmap\_m581c5a6f24bb1567a3677452fc5eac62.positions[672] );
});