---
title: BackboneConf Boston, 2013
date: '2013-07-31T04:06:10+00:00'
format: image
service: flickr
tags:
- automattic
- backbonejs
- Boston
- javascript
- teamsocial
image: http://i0.wp.com/dentedreality.com.au/wp-content/uploads/2013/07/9437624291_8e420a15d2_o.jpg?resize=607%2C452
---

[![BackboneConf Boston, 2013](http://i0.wp.com/dentedreality.com.au/wp-content/uploads/2013/07/9437624291_8e420a15d2_o.jpg?resize=607%2C452)](http://dentedreality.com.au/2013/07/31/backboneconf-boston-2013-5/) 
# [BackboneConf Boston, 2013](http://dentedreality.com.au/2013/07/31/backboneconf-boston-2013-5/)





* #[automattic](http://dentedreality.com.au/tags/automattic/)
* #[backbonejs](http://dentedreality.com.au/tags/backbonejs/)
* #[Boston](http://dentedreality.com.au/tags/boston/)
* #[javascript](http://dentedreality.com.au/tags/javascript/)
* #[teamsocial](http://dentedreality.com.au/tags/teamsocial/)

Posted on [Flickr](http://www.flickr.com/photos/borkazoid/9437624291/) [4:06 am, July 31, 2013](http://dentedreality.com.au/2013/07/31/backboneconf-boston-2013-5/ "4:06 am") 
jQuery(document).ready(function(){
var gmap\_m6e508821ed7cdaca18f1b80f81754550 = {
positions : {
889 : new google.maps.LatLng( '42.361166', '-71.0805' )
},
bounds : new google.maps.LatLngBounds(), // empty for now, we'll dynamically extend it later
map : new google.maps.Map(
document.getElementById( 'gmap\_m6e508821ed7cdaca18f1b80f81754550' ),
{
mapTypeId: google.maps.MapTypeId.ROADMAP,
center: new google.maps.LatLng( 0, 0 ),
zoom: 16 // Seems to be a good zoom for a single point
}
),
markers : {},
}; // end of gmap
// Extend the bounds of interest based on our positions
for ( var m in gmap\_m6e508821ed7cdaca18f1b80f81754550.positions ) {
gmap\_m6e508821ed7cdaca18f1b80f81754550.bounds.extend( gmap\_m6e508821ed7cdaca18f1b80f81754550.positions[m] );
}
// Render markers
for ( var m in gmap\_m6e508821ed7cdaca18f1b80f81754550.positions ) {
gmap\_m6e508821ed7cdaca18f1b80f81754550.markers[m] = new google.maps.Marker( {
clickable: true,
map : gmap\_m6e508821ed7cdaca18f1b80f81754550.map,
position : gmap\_m6e508821ed7cdaca18f1b80f81754550.positions[m]
} );
}
// Redraw map to fit our new marker-based bounds
gmap\_m6e508821ed7cdaca18f1b80f81754550.map.setCenter( gmap\_m6e508821ed7cdaca18f1b80f81754550.positions[889] );
});