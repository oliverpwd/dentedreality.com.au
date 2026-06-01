---
title: ''
date: '2015-12-30T15:39:32+00:00'
format: image
service: instagram
tags:
- hiking
- hotsprings
- nofilter
- outdoors
- snow
image: http://i1.wp.com/dentedreality.com.au/wp-content/uploads/2015/12/928553_837891186319918_439837513_n.jpg?fit=640%2C640
---

[![Near Radium Hot Springs. #nofilter](http://i1.wp.com/dentedreality.com.au/wp-content/uploads/2015/12/928553_837891186319918_439837513_n.jpg?fit=640%2C640)](http://dentedreality.com.au/2015/12/30/near-radium-hot-springs-nofilter/) 

Near Radium Hot Springs. #nofilter





* #[hiking](http://dentedreality.com.au/tags/hiking/)
* #[hotsprings](http://dentedreality.com.au/tags/hotsprings/)
* #[nofilter](http://dentedreality.com.au/tags/nofilter/)
* #[outdoors](http://dentedreality.com.au/tags/outdoors/)
* #[snow](http://dentedreality.com.au/tags/snow/)

Posted on [Instagram](https://www.instagram.com/p/_7tt8wimC_/) [3:39 pm, December 30, 2015](http://dentedreality.com.au/2015/12/30/near-radium-hot-springs-nofilter/ "3:39 pm") 
jQuery(document).ready(function(){
var gmap\_mf8d2f3614714f06b6c24ae85ec539989 = {
positions : {
122 : new google.maps.LatLng( '39.953158', '-106.547003' )
},
bounds : new google.maps.LatLngBounds(), // empty for now, we'll dynamically extend it later
map : new google.maps.Map(
document.getElementById( 'gmap\_mf8d2f3614714f06b6c24ae85ec539989' ),
{
mapTypeId: google.maps.MapTypeId.ROADMAP,
center: new google.maps.LatLng( 0, 0 ),
zoom: 16 // Seems to be a good zoom for a single point
}
),
markers : {},
}; // end of gmap
// Extend the bounds of interest based on our positions
for ( var m in gmap\_mf8d2f3614714f06b6c24ae85ec539989.positions ) {
gmap\_mf8d2f3614714f06b6c24ae85ec539989.bounds.extend( gmap\_mf8d2f3614714f06b6c24ae85ec539989.positions[m] );
}
// Render markers
for ( var m in gmap\_mf8d2f3614714f06b6c24ae85ec539989.positions ) {
gmap\_mf8d2f3614714f06b6c24ae85ec539989.markers[m] = new google.maps.Marker( {
clickable: true,
map : gmap\_mf8d2f3614714f06b6c24ae85ec539989.map,
position : gmap\_mf8d2f3614714f06b6c24ae85ec539989.positions[m]
} );
}
// Redraw map to fit our new marker-based bounds
gmap\_mf8d2f3614714f06b6c24ae85ec539989.map.setCenter( gmap\_mf8d2f3614714f06b6c24ae85ec539989.positions[122] );
});