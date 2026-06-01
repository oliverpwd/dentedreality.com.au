---
title: BackboneConf Boston, 2013
date: '2013-07-31T06:11:45+00:00'
format: image
service: flickr
tags:
- automattic
- backbonejs
- Boston
- javascript
- microsoft
- nerd
- teamsocial
image: http://i0.wp.com/dentedreality.com.au/wp-content/uploads/2013/07/9440408610_0b5594ca21_o.jpg?resize=607%2C813
---

[![BackboneConf Boston, 2013](http://i0.wp.com/dentedreality.com.au/wp-content/uploads/2013/07/9440408610_0b5594ca21_o.jpg?resize=607%2C813)](http://dentedreality.com.au/2013/07/31/backboneconf-boston-2013-4/) 
# [BackboneConf Boston, 2013](http://dentedreality.com.au/2013/07/31/backboneconf-boston-2013-4/)

Equal-opportunity Bathrooms, at the Microsoft NERD center.





* #[automattic](http://dentedreality.com.au/tags/automattic/)
* #[backbonejs](http://dentedreality.com.au/tags/backbonejs/)
* #[Boston](http://dentedreality.com.au/tags/boston/)
* #[javascript](http://dentedreality.com.au/tags/javascript/)
* #[microsoft](http://dentedreality.com.au/tags/microsoft/)
* #[nerd](http://dentedreality.com.au/tags/nerd/)
* #[teamsocial](http://dentedreality.com.au/tags/teamsocial/)

Posted on [Flickr](http://www.flickr.com/photos/borkazoid/9440408610/) [6:11 am, July 31, 2013](http://dentedreality.com.au/2013/07/31/backboneconf-boston-2013-4/ "6:11 am") 
jQuery(document).ready(function(){
var gmap\_m20bbd31b3e07d7bb26becb82c37400a2 = {
positions : {
799 : new google.maps.LatLng( '42.361166', '-71.081167' )
},
bounds : new google.maps.LatLngBounds(), // empty for now, we'll dynamically extend it later
map : new google.maps.Map(
document.getElementById( 'gmap\_m20bbd31b3e07d7bb26becb82c37400a2' ),
{
mapTypeId: google.maps.MapTypeId.ROADMAP,
center: new google.maps.LatLng( 0, 0 ),
zoom: 16 // Seems to be a good zoom for a single point
}
),
markers : {},
}; // end of gmap
// Extend the bounds of interest based on our positions
for ( var m in gmap\_m20bbd31b3e07d7bb26becb82c37400a2.positions ) {
gmap\_m20bbd31b3e07d7bb26becb82c37400a2.bounds.extend( gmap\_m20bbd31b3e07d7bb26becb82c37400a2.positions[m] );
}
// Render markers
for ( var m in gmap\_m20bbd31b3e07d7bb26becb82c37400a2.positions ) {
gmap\_m20bbd31b3e07d7bb26becb82c37400a2.markers[m] = new google.maps.Marker( {
clickable: true,
map : gmap\_m20bbd31b3e07d7bb26becb82c37400a2.map,
position : gmap\_m20bbd31b3e07d7bb26becb82c37400a2.positions[m]
} );
}
// Redraw map to fit our new marker-based bounds
gmap\_m20bbd31b3e07d7bb26becb82c37400a2.map.setCenter( gmap\_m20bbd31b3e07d7bb26becb82c37400a2.positions[799] );
});