---
title: Sunset at the Beach
date: '2006-12-27T01:11:32+00:00'
format: image
service: flickr
tags:
- beach
- dusk
- phuket
- sunset
- thailand
- thailand06
image: http://i0.wp.com/dentedreality.com.au/wp-content/uploads/2006/12/348100674_00b54e9d13_o.jpg?resize=607%2C809
---

[![Sunset at the Beach](http://i0.wp.com/dentedreality.com.au/wp-content/uploads/2006/12/348100674_00b54e9d13_o.jpg?resize=607%2C809)](http://dentedreality.com.au/2006/12/27/sunset-at-the-beach/) 
# [Sunset at the Beach](http://dentedreality.com.au/2006/12/27/sunset-at-the-beach/)





* #[beach](http://dentedreality.com.au/tags/beach/)
* #[dusk](http://dentedreality.com.au/tags/dusk/)
* #[phuket](http://dentedreality.com.au/tags/phuket/)
* #[sunset](http://dentedreality.com.au/tags/sunset/)
* #[thailand](http://dentedreality.com.au/tags/thailand/)
* #[thailand06](http://dentedreality.com.au/tags/thailand06/)

Posted on [Flickr](http://www.flickr.com/photos/borkazoid/348100674/) [1:11 am, December 27, 2006](http://dentedreality.com.au/2006/12/27/sunset-at-the-beach/ "1:11 am") 
jQuery(document).ready(function(){
var gmap\_me8be42e323378439140985e745330e6d = {
positions : {
852 : new google.maps.LatLng( '7.955282', '98.282489' )
},
bounds : new google.maps.LatLngBounds(), // empty for now, we'll dynamically extend it later
map : new google.maps.Map(
document.getElementById( 'gmap\_me8be42e323378439140985e745330e6d' ),
{
mapTypeId: google.maps.MapTypeId.ROADMAP,
center: new google.maps.LatLng( 0, 0 ),
zoom: 16 // Seems to be a good zoom for a single point
}
),
markers : {},
}; // end of gmap
// Extend the bounds of interest based on our positions
for ( var m in gmap\_me8be42e323378439140985e745330e6d.positions ) {
gmap\_me8be42e323378439140985e745330e6d.bounds.extend( gmap\_me8be42e323378439140985e745330e6d.positions[m] );
}
// Render markers
for ( var m in gmap\_me8be42e323378439140985e745330e6d.positions ) {
gmap\_me8be42e323378439140985e745330e6d.markers[m] = new google.maps.Marker( {
clickable: true,
map : gmap\_me8be42e323378439140985e745330e6d.map,
position : gmap\_me8be42e323378439140985e745330e6d.positions[m]
} );
}
// Redraw map to fit our new marker-based bounds
gmap\_me8be42e323378439140985e745330e6d.map.setCenter( gmap\_me8be42e323378439140985e745330e6d.positions[852] );
});