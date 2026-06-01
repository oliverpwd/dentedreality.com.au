---
title: Epic Australian Adventure, 2014
date: '2014-03-14T08:25:00+00:00'
format: image
service: flickr
tags:
- perth
image: http://i0.wp.com/dentedreality.com.au/wp-content/uploads/2014/03/13904705391_45bfe30cd5_o.jpg?resize=607%2C455
---

[![Epic Australian Adventure, 2014](http://i0.wp.com/dentedreality.com.au/wp-content/uploads/2014/03/13904705391_45bfe30cd5_o.jpg?resize=607%2C455)](http://dentedreality.com.au/2014/03/14/epic-australian-adventure-2014-51/) 
# [Epic Australian Adventure, 2014](http://dentedreality.com.au/2014/03/14/epic-australian-adventure-2014-51/)

Perth, Mooloolaba and Melbourne





* #[perth](http://dentedreality.com.au/tags/perth/)

Posted on [Flickr](http://www.flickr.com/photos/borkazoid/13904705391/) [8:25 am, March 14, 2014](http://dentedreality.com.au/2014/03/14/epic-australian-adventure-2014-51/ "8:25 am") 
jQuery(document).ready(function(){
var gmap\_mf7661bfd1923a7936ecff4d62d2aff2e = {
positions : {
116 : new google.maps.LatLng( '-31.993998', '115.859077' )
},
bounds : new google.maps.LatLngBounds(), // empty for now, we'll dynamically extend it later
map : new google.maps.Map(
document.getElementById( 'gmap\_mf7661bfd1923a7936ecff4d62d2aff2e' ),
{
mapTypeId: google.maps.MapTypeId.ROADMAP,
center: new google.maps.LatLng( 0, 0 ),
zoom: 16 // Seems to be a good zoom for a single point
}
),
markers : {},
}; // end of gmap
// Extend the bounds of interest based on our positions
for ( var m in gmap\_mf7661bfd1923a7936ecff4d62d2aff2e.positions ) {
gmap\_mf7661bfd1923a7936ecff4d62d2aff2e.bounds.extend( gmap\_mf7661bfd1923a7936ecff4d62d2aff2e.positions[m] );
}
// Render markers
for ( var m in gmap\_mf7661bfd1923a7936ecff4d62d2aff2e.positions ) {
gmap\_mf7661bfd1923a7936ecff4d62d2aff2e.markers[m] = new google.maps.Marker( {
clickable: true,
map : gmap\_mf7661bfd1923a7936ecff4d62d2aff2e.map,
position : gmap\_mf7661bfd1923a7936ecff4d62d2aff2e.positions[m]
} );
}
// Redraw map to fit our new marker-based bounds
gmap\_mf7661bfd1923a7936ecff4d62d2aff2e.map.setCenter( gmap\_mf7661bfd1923a7936ecff4d62d2aff2e.positions[116] );
});