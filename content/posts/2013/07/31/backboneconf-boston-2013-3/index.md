---
title: BackboneConf Boston, 2013
date: '2013-07-31T16:51:29+00:00'
format: image
service: flickr
tags:
- automattic
- backbonejs
- Boston
- javascript
- teamsocial
image: http://i0.wp.com/dentedreality.com.au/wp-content/uploads/2013/07/9440409428_7a50d1ee14_o.jpg?resize=607%2C452
---

[![BackboneConf Boston, 2013](http://i0.wp.com/dentedreality.com.au/wp-content/uploads/2013/07/9440409428_7a50d1ee14_o.jpg?resize=607%2C452)](http://dentedreality.com.au/2013/07/31/backboneconf-boston-2013-3/) 
# [BackboneConf Boston, 2013](http://dentedreality.com.au/2013/07/31/backboneconf-boston-2013-3/)





* #[automattic](http://dentedreality.com.au/tags/automattic/)
* #[backbonejs](http://dentedreality.com.au/tags/backbonejs/)
* #[Boston](http://dentedreality.com.au/tags/boston/)
* #[javascript](http://dentedreality.com.au/tags/javascript/)
* #[teamsocial](http://dentedreality.com.au/tags/teamsocial/)

Posted on [Flickr](http://www.flickr.com/photos/borkazoid/9440409428/) [4:51 pm, July 31, 2013](http://dentedreality.com.au/2013/07/31/backboneconf-boston-2013-3/ "4:51 pm") 
jQuery(document).ready(function(){
var gmap\_m9202ca06cf63858eb02f4a4f0593061f = {
positions : {
518 : new google.maps.LatLng( '42.363333', '-71.0775' )
},
bounds : new google.maps.LatLngBounds(), // empty for now, we'll dynamically extend it later
map : new google.maps.Map(
document.getElementById( 'gmap\_m9202ca06cf63858eb02f4a4f0593061f' ),
{
mapTypeId: google.maps.MapTypeId.ROADMAP,
center: new google.maps.LatLng( 0, 0 ),
zoom: 16 // Seems to be a good zoom for a single point
}
),
markers : {},
}; // end of gmap
// Extend the bounds of interest based on our positions
for ( var m in gmap\_m9202ca06cf63858eb02f4a4f0593061f.positions ) {
gmap\_m9202ca06cf63858eb02f4a4f0593061f.bounds.extend( gmap\_m9202ca06cf63858eb02f4a4f0593061f.positions[m] );
}
// Render markers
for ( var m in gmap\_m9202ca06cf63858eb02f4a4f0593061f.positions ) {
gmap\_m9202ca06cf63858eb02f4a4f0593061f.markers[m] = new google.maps.Marker( {
clickable: true,
map : gmap\_m9202ca06cf63858eb02f4a4f0593061f.map,
position : gmap\_m9202ca06cf63858eb02f4a4f0593061f.positions[m]
} );
}
// Redraw map to fit our new marker-based bounds
gmap\_m9202ca06cf63858eb02f4a4f0593061f.map.setCenter( gmap\_m9202ca06cf63858eb02f4a4f0593061f.positions[518] );
});