---
title: 4 Hour Body Osso Buko
date: '2012-12-16T15:22:57+00:00'
format: image
service: flickr
tags:
- 4HB
- cooking
- food
- ossobuko
image: http://i0.wp.com/dentedreality.com.au/wp-content/uploads/2012/12/8460376824_ef519661f1_o.jpg?resize=607%2C452
---

[![4 Hour Body Osso Buko](http://i0.wp.com/dentedreality.com.au/wp-content/uploads/2012/12/8460376824_ef519661f1_o.jpg?resize=607%2C452)](http://dentedreality.com.au/2012/12/16/4-hour-body-osso-buko/) 
# [4 Hour Body Osso Buko](http://dentedreality.com.au/2012/12/16/4-hour-body-osso-buko/)





* #[4HB](http://dentedreality.com.au/tags/4hb/)
* #[cooking](http://dentedreality.com.au/tags/cooking/)
* #[food](http://dentedreality.com.au/tags/food/)
* #[ossobuko](http://dentedreality.com.au/tags/ossobuko/)

Posted on [Flickr](http://www.flickr.com/photos/borkazoid/8460376824/) [3:22 pm, December 16, 2012](http://dentedreality.com.au/2012/12/16/4-hour-body-osso-buko/ "3:22 pm") 
jQuery(document).ready(function(){
var gmap\_m881ac8525f0d340d745057ca05cba52e = {
positions : {
584 : new google.maps.LatLng( '40.6695', '-73.985' )
},
bounds : new google.maps.LatLngBounds(), // empty for now, we'll dynamically extend it later
map : new google.maps.Map(
document.getElementById( 'gmap\_m881ac8525f0d340d745057ca05cba52e' ),
{
mapTypeId: google.maps.MapTypeId.ROADMAP,
center: new google.maps.LatLng( 0, 0 ),
zoom: 16 // Seems to be a good zoom for a single point
}
),
markers : {},
}; // end of gmap
// Extend the bounds of interest based on our positions
for ( var m in gmap\_m881ac8525f0d340d745057ca05cba52e.positions ) {
gmap\_m881ac8525f0d340d745057ca05cba52e.bounds.extend( gmap\_m881ac8525f0d340d745057ca05cba52e.positions[m] );
}
// Render markers
for ( var m in gmap\_m881ac8525f0d340d745057ca05cba52e.positions ) {
gmap\_m881ac8525f0d340d745057ca05cba52e.markers[m] = new google.maps.Marker( {
clickable: true,
map : gmap\_m881ac8525f0d340d745057ca05cba52e.map,
position : gmap\_m881ac8525f0d340d745057ca05cba52e.positions[m]
} );
}
// Redraw map to fit our new marker-based bounds
gmap\_m881ac8525f0d340d745057ca05cba52e.map.setCenter( gmap\_m881ac8525f0d340d745057ca05cba52e.positions[584] );
});