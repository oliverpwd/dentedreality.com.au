---
title: Erika’s View
date: '2011-12-07T03:42:32+00:00'
format: image
service: flickr
tags:
- cityscape
- glenpark
- sanfrancisco
- skyline
- view
- wallpaper
image: http://i1.wp.com/dentedreality.com.au/wp-content/uploads/2011/12/6862687888_e6d4415c87_o.jpg?resize=607%2C452
---

[![Erika's View](http://i1.wp.com/dentedreality.com.au/wp-content/uploads/2011/12/6862687888_e6d4415c87_o.jpg?resize=607%2C452)](http://dentedreality.com.au/2011/12/07/erikas-view/) 
# [Erika’s View](http://dentedreality.com.au/2011/12/07/erikas-view/)

View from Glen Park





* #[cityscape](http://dentedreality.com.au/tags/cityscape/)
* #[glenpark](http://dentedreality.com.au/tags/glenpark/)
* #[sanfrancisco](http://dentedreality.com.au/tags/sanfrancisco/)
* #[skyline](http://dentedreality.com.au/tags/skyline/)
* #[view](http://dentedreality.com.au/tags/view/)
* #[wallpaper](http://dentedreality.com.au/tags/wallpaper/)

Posted on [Flickr](http://www.flickr.com/photos/borkazoid/6862687888/) [3:42 am, December 7, 2011](http://dentedreality.com.au/2011/12/07/erikas-view/ "3:42 am") 
jQuery(document).ready(function(){
var gmap\_mde338980e9bff3028db667bfa1184cca = {
positions : {
923 : new google.maps.LatLng( '37.735833', '-122.433501' )
},
bounds : new google.maps.LatLngBounds(), // empty for now, we'll dynamically extend it later
map : new google.maps.Map(
document.getElementById( 'gmap\_mde338980e9bff3028db667bfa1184cca' ),
{
mapTypeId: google.maps.MapTypeId.ROADMAP,
center: new google.maps.LatLng( 0, 0 ),
zoom: 16 // Seems to be a good zoom for a single point
}
),
markers : {},
}; // end of gmap
// Extend the bounds of interest based on our positions
for ( var m in gmap\_mde338980e9bff3028db667bfa1184cca.positions ) {
gmap\_mde338980e9bff3028db667bfa1184cca.bounds.extend( gmap\_mde338980e9bff3028db667bfa1184cca.positions[m] );
}
// Render markers
for ( var m in gmap\_mde338980e9bff3028db667bfa1184cca.positions ) {
gmap\_mde338980e9bff3028db667bfa1184cca.markers[m] = new google.maps.Marker( {
clickable: true,
map : gmap\_mde338980e9bff3028db667bfa1184cca.map,
position : gmap\_mde338980e9bff3028db667bfa1184cca.positions[m]
} );
}
// Redraw map to fit our new marker-based bounds
gmap\_mde338980e9bff3028db667bfa1184cca.map.setCenter( gmap\_mde338980e9bff3028db667bfa1184cca.positions[923] );
});