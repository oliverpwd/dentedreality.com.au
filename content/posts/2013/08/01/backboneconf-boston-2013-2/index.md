---
title: BackboneConf Boston, 2013
date: '2013-08-01T03:56:46+00:00'
format: image
service: flickr
tags:
- automattic
- backbonejs
- Boston
- bridge
- javascript
- swing
- teamsocial
image: http://i0.wp.com/dentedreality.com.au/wp-content/uploads/2013/08/9440410018_30bf912123_o.jpg?resize=607%2C452
---

[![BackboneConf Boston, 2013](http://i0.wp.com/dentedreality.com.au/wp-content/uploads/2013/08/9440410018_30bf912123_o.jpg?resize=607%2C452)](http://dentedreality.com.au/2013/08/01/backboneconf-boston-2013-2/) 
# [BackboneConf Boston, 2013](http://dentedreality.com.au/2013/08/01/backboneconf-boston-2013-2/)

This swing was hung under a random bridge.





* #[automattic](http://dentedreality.com.au/tags/automattic/)
* #[backbonejs](http://dentedreality.com.au/tags/backbonejs/)
* #[Boston](http://dentedreality.com.au/tags/boston/)
* #[bridge](http://dentedreality.com.au/tags/bridge/)
* #[javascript](http://dentedreality.com.au/tags/javascript/)
* #[swing](http://dentedreality.com.au/tags/swing/)
* #[teamsocial](http://dentedreality.com.au/tags/teamsocial/)

Posted on [Flickr](http://www.flickr.com/photos/borkazoid/9440410018/) [3:56 am, August 1, 2013](http://dentedreality.com.au/2013/08/01/backboneconf-boston-2013-2/ "3:56 am") 
jQuery(document).ready(function(){
var gmap\_m03d761d476116911b1095ce3fb9db132 = {
positions : {
60 : new google.maps.LatLng( '42.362', '-71.0785' )
},
bounds : new google.maps.LatLngBounds(), // empty for now, we'll dynamically extend it later
map : new google.maps.Map(
document.getElementById( 'gmap\_m03d761d476116911b1095ce3fb9db132' ),
{
mapTypeId: google.maps.MapTypeId.ROADMAP,
center: new google.maps.LatLng( 0, 0 ),
zoom: 16 // Seems to be a good zoom for a single point
}
),
markers : {},
}; // end of gmap
// Extend the bounds of interest based on our positions
for ( var m in gmap\_m03d761d476116911b1095ce3fb9db132.positions ) {
gmap\_m03d761d476116911b1095ce3fb9db132.bounds.extend( gmap\_m03d761d476116911b1095ce3fb9db132.positions[m] );
}
// Render markers
for ( var m in gmap\_m03d761d476116911b1095ce3fb9db132.positions ) {
gmap\_m03d761d476116911b1095ce3fb9db132.markers[m] = new google.maps.Marker( {
clickable: true,
map : gmap\_m03d761d476116911b1095ce3fb9db132.map,
position : gmap\_m03d761d476116911b1095ce3fb9db132.positions[m]
} );
}
// Redraw map to fit our new marker-based bounds
gmap\_m03d761d476116911b1095ce3fb9db132.map.setCenter( gmap\_m03d761d476116911b1095ce3fb9db132.positions[60] );
});