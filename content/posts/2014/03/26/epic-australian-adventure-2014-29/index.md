---
title: Epic Australian Adventure, 2014
date: '2014-03-26T04:50:08+00:00'
format: image
service: flickr
tags:
- Melbourne
image: http://i0.wp.com/dentedreality.com.au/wp-content/uploads/2014/03/13904752176_99f44323c0_o.jpg?resize=607%2C455
---

[![Epic Australian Adventure, 2014](http://i0.wp.com/dentedreality.com.au/wp-content/uploads/2014/03/13904752176_99f44323c0_o.jpg?resize=607%2C455)](http://dentedreality.com.au/2014/03/26/epic-australian-adventure-2014-29/) 
# [Epic Australian Adventure, 2014](http://dentedreality.com.au/2014/03/26/epic-australian-adventure-2014-29/)

Perth, Mooloolaba and Melbourne





* #[Melbourne](http://dentedreality.com.au/tags/melbourne/)

Posted on [Flickr](http://www.flickr.com/photos/borkazoid/13904752176/) [4:50 am, March 26, 2014](http://dentedreality.com.au/2014/03/26/epic-australian-adventure-2014-29/ "4:50 am") 
jQuery(document).ready(function(){
var gmap\_mca47525cb9e4106ad5356360bbbd1b34 = {
positions : {
769 : new google.maps.LatLng( '-37.825987', '144.956572' )
},
bounds : new google.maps.LatLngBounds(), // empty for now, we'll dynamically extend it later
map : new google.maps.Map(
document.getElementById( 'gmap\_mca47525cb9e4106ad5356360bbbd1b34' ),
{
mapTypeId: google.maps.MapTypeId.ROADMAP,
center: new google.maps.LatLng( 0, 0 ),
zoom: 16 // Seems to be a good zoom for a single point
}
),
markers : {},
}; // end of gmap
// Extend the bounds of interest based on our positions
for ( var m in gmap\_mca47525cb9e4106ad5356360bbbd1b34.positions ) {
gmap\_mca47525cb9e4106ad5356360bbbd1b34.bounds.extend( gmap\_mca47525cb9e4106ad5356360bbbd1b34.positions[m] );
}
// Render markers
for ( var m in gmap\_mca47525cb9e4106ad5356360bbbd1b34.positions ) {
gmap\_mca47525cb9e4106ad5356360bbbd1b34.markers[m] = new google.maps.Marker( {
clickable: true,
map : gmap\_mca47525cb9e4106ad5356360bbbd1b34.map,
position : gmap\_mca47525cb9e4106ad5356360bbbd1b34.positions[m]
} );
}
// Redraw map to fit our new marker-based bounds
gmap\_mca47525cb9e4106ad5356360bbbd1b34.map.setCenter( gmap\_mca47525cb9e4106ad5356360bbbd1b34.positions[769] );
});