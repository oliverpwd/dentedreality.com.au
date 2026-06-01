---
title: WordCampSF, 2013
date: '2013-07-27T09:01:37+00:00'
format: image
tags:
- automattic
- sanfrancisco
- wcsf
- wcsf2013
- wordcamp
- wordpress
image: http://i1.wp.com/dentedreality.com.au/wp-content/uploads/2013/07/9437618729_4c513d9f27_o.jpg?resize=607%2C452
---

[![WordCampSF, 2013](http://i1.wp.com/dentedreality.com.au/wp-content/uploads/2013/07/9437618729_4c513d9f27_o.jpg?resize=607%2C452)](http://dentedreality.com.au/2013/07/27/wordcampsf-2013-6/) 
# [WordCampSF, 2013](http://dentedreality.com.au/2013/07/27/wordcampsf-2013-6/)

I attended, spoke at, and organized the Contributor Day for WordCamp San Francisco 2013. This is my eigth WCSF ![:)](http://i0.wp.com/dentedreality.com.au/wp-includes/images/smilies/icon_smile.gif?w=607)





* #[automattic](http://dentedreality.com.au/tags/automattic/)
* #[sanfrancisco](http://dentedreality.com.au/tags/sanfrancisco/)
* #[wcsf](http://dentedreality.com.au/tags/wcsf/)
* #[wcsf2013](http://dentedreality.com.au/tags/wcsf2013/)
* #[wordcamp](http://dentedreality.com.au/tags/wordcamp/)
* #[wordpress](http://dentedreality.com.au/tags/wordpress/)

Posted on [Flickr](http://www.flickr.com/photos/borkazoid/9437618729/) [9:01 am, July 27, 2013](http://dentedreality.com.au/2013/07/27/wordcampsf-2013-6/ "9:01 am") 
jQuery(document).ready(function(){
var gmap\_me41a2f3a295c63a9684661a166319f01 = {
positions : {
610 : new google.maps.LatLng( '37.768166', '-122.393' )
},
bounds : new google.maps.LatLngBounds(), // empty for now, we'll dynamically extend it later
map : new google.maps.Map(
document.getElementById( 'gmap\_me41a2f3a295c63a9684661a166319f01' ),
{
mapTypeId: google.maps.MapTypeId.ROADMAP,
center: new google.maps.LatLng( 0, 0 ),
zoom: 16 // Seems to be a good zoom for a single point
}
),
markers : {},
}; // end of gmap
// Extend the bounds of interest based on our positions
for ( var m in gmap\_me41a2f3a295c63a9684661a166319f01.positions ) {
gmap\_me41a2f3a295c63a9684661a166319f01.bounds.extend( gmap\_me41a2f3a295c63a9684661a166319f01.positions[m] );
}
// Render markers
for ( var m in gmap\_me41a2f3a295c63a9684661a166319f01.positions ) {
gmap\_me41a2f3a295c63a9684661a166319f01.markers[m] = new google.maps.Marker( {
clickable: true,
map : gmap\_me41a2f3a295c63a9684661a166319f01.map,
position : gmap\_me41a2f3a295c63a9684661a166319f01.positions[m]
} );
}
// Redraw map to fit our new marker-based bounds
gmap\_me41a2f3a295c63a9684661a166319f01.map.setCenter( gmap\_me41a2f3a295c63a9684661a166319f01.positions[610] );
});