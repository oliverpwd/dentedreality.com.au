---
title: Epic Australian Adventure, 2014
date: '2014-03-14T05:27:47+00:00'
format: image
service: flickr
tags:
- perth
image: http://i2.wp.com/dentedreality.com.au/wp-content/uploads/2014/03/13904703671_6016eb9690_o.jpg?resize=607%2C455
---

[![Epic Australian Adventure, 2014](http://i2.wp.com/dentedreality.com.au/wp-content/uploads/2014/03/13904703671_6016eb9690_o.jpg?resize=607%2C455)](http://dentedreality.com.au/2014/03/14/epic-australian-adventure-2014-53/) 
# [Epic Australian Adventure, 2014](http://dentedreality.com.au/2014/03/14/epic-australian-adventure-2014-53/)

Perth, Mooloolaba and Melbourne





* #[perth](http://dentedreality.com.au/tags/perth/)

Posted on [Flickr](http://www.flickr.com/photos/borkazoid/13904703671/) [5:27 am, March 14, 2014](http://dentedreality.com.au/2014/03/14/epic-australian-adventure-2014-53/ "5:27 am") 
jQuery(document).ready(function(){
var gmap\_mb7580657224780dac659522c1914f40a = {
positions : {
267 : new google.maps.LatLng( '-32.076184', '115.848716' )
},
bounds : new google.maps.LatLngBounds(), // empty for now, we'll dynamically extend it later
map : new google.maps.Map(
document.getElementById( 'gmap\_mb7580657224780dac659522c1914f40a' ),
{
mapTypeId: google.maps.MapTypeId.ROADMAP,
center: new google.maps.LatLng( 0, 0 ),
zoom: 16 // Seems to be a good zoom for a single point
}
),
markers : {},
}; // end of gmap
// Extend the bounds of interest based on our positions
for ( var m in gmap\_mb7580657224780dac659522c1914f40a.positions ) {
gmap\_mb7580657224780dac659522c1914f40a.bounds.extend( gmap\_mb7580657224780dac659522c1914f40a.positions[m] );
}
// Render markers
for ( var m in gmap\_mb7580657224780dac659522c1914f40a.positions ) {
gmap\_mb7580657224780dac659522c1914f40a.markers[m] = new google.maps.Marker( {
clickable: true,
map : gmap\_mb7580657224780dac659522c1914f40a.map,
position : gmap\_mb7580657224780dac659522c1914f40a.positions[m]
} );
}
// Redraw map to fit our new marker-based bounds
gmap\_mb7580657224780dac659522c1914f40a.map.setCenter( gmap\_mb7580657224780dac659522c1914f40a.positions[267] );
});