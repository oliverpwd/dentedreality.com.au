---
title: BackboneConf Boston, 2013
date: '2013-08-01T18:06:45+00:00'
format: image
service: flickr
tags:
- accidentallimo
- automattic
- backbonejs
- Boston
- javascript
- teamsocial
image: http://i0.wp.com/dentedreality.com.au/wp-content/uploads/2013/08/9440410632_15c6c1d806_o.jpg?resize=607%2C452
---

[![BackboneConf Boston, 2013](http://i0.wp.com/dentedreality.com.au/wp-content/uploads/2013/08/9440410632_15c6c1d806_o.jpg?resize=607%2C452)](http://dentedreality.com.au/2013/08/01/backboneconf-boston-2013/) 
# [BackboneConf Boston, 2013](http://dentedreality.com.au/2013/08/01/backboneconf-boston-2013/)





* #[accidentallimo](http://dentedreality.com.au/tags/accidentallimo/)
* #[automattic](http://dentedreality.com.au/tags/automattic/)
* #[backbonejs](http://dentedreality.com.au/tags/backbonejs/)
* #[Boston](http://dentedreality.com.au/tags/boston/)
* #[javascript](http://dentedreality.com.au/tags/javascript/)
* #[teamsocial](http://dentedreality.com.au/tags/teamsocial/)

Posted on [Flickr](http://www.flickr.com/photos/borkazoid/9440410632/) [6:06 pm, August 1, 2013](http://dentedreality.com.au/2013/08/01/backboneconf-boston-2013/ "6:06 pm") 
jQuery(document).ready(function(){
var gmap\_ma3393a48999f521b33710c8b1d5c8e9f = {
positions : {
51 : new google.maps.LatLng( '42.3505', '-71.072334' )
},
bounds : new google.maps.LatLngBounds(), // empty for now, we'll dynamically extend it later
map : new google.maps.Map(
document.getElementById( 'gmap\_ma3393a48999f521b33710c8b1d5c8e9f' ),
{
mapTypeId: google.maps.MapTypeId.ROADMAP,
center: new google.maps.LatLng( 0, 0 ),
zoom: 16 // Seems to be a good zoom for a single point
}
),
markers : {},
}; // end of gmap
// Extend the bounds of interest based on our positions
for ( var m in gmap\_ma3393a48999f521b33710c8b1d5c8e9f.positions ) {
gmap\_ma3393a48999f521b33710c8b1d5c8e9f.bounds.extend( gmap\_ma3393a48999f521b33710c8b1d5c8e9f.positions[m] );
}
// Render markers
for ( var m in gmap\_ma3393a48999f521b33710c8b1d5c8e9f.positions ) {
gmap\_ma3393a48999f521b33710c8b1d5c8e9f.markers[m] = new google.maps.Marker( {
clickable: true,
map : gmap\_ma3393a48999f521b33710c8b1d5c8e9f.map,
position : gmap\_ma3393a48999f521b33710c8b1d5c8e9f.positions[m]
} );
}
// Redraw map to fit our new marker-based bounds
gmap\_ma3393a48999f521b33710c8b1d5c8e9f.map.setCenter( gmap\_ma3393a48999f521b33710c8b1d5c8e9f.positions[51] );
});