---
title: WordCampSF, 2013
date: '2013-07-26T05:05:17+00:00'
format: image
tags:
- automattic
- sanfrancisco
- wcsf
- wcsf2013
- wordcamp
- wordpress
image: http://i0.wp.com/dentedreality.com.au/wp-content/uploads/2013/07/9437616179_7937e8b363_o.jpg?resize=607%2C452
---

[![WordCampSF, 2013](http://i0.wp.com/dentedreality.com.au/wp-content/uploads/2013/07/9437616179_7937e8b363_o.jpg?resize=607%2C452)](http://dentedreality.com.au/2013/07/26/wordcampsf-2013-9/) 
# [WordCampSF, 2013](http://dentedreality.com.au/2013/07/26/wordcampsf-2013-9/)

I attended, spoke at, and organized the Contributor Day for WordCamp San Francisco 2013. This is my eigth WCSF ![:)](http://i0.wp.com/dentedreality.com.au/wp-includes/images/smilies/icon_smile.gif?w=607)





* #[automattic](http://dentedreality.com.au/tags/automattic/)
* #[sanfrancisco](http://dentedreality.com.au/tags/sanfrancisco/)
* #[wcsf](http://dentedreality.com.au/tags/wcsf/)
* #[wcsf2013](http://dentedreality.com.au/tags/wcsf2013/)
* #[wordcamp](http://dentedreality.com.au/tags/wordcamp/)
* #[wordpress](http://dentedreality.com.au/tags/wordpress/)

Posted on [Flickr](http://www.flickr.com/photos/borkazoid/9437616179/) [5:05 am, July 26, 2013](http://dentedreality.com.au/2013/07/26/wordcampsf-2013-9/ "5:05 am") 
jQuery(document).ready(function(){
var gmap\_md17766420f0dbf913ddd3df4db516f4b = {
positions : {
343 : new google.maps.LatLng( '37.768', '-122.392667' )
},
bounds : new google.maps.LatLngBounds(), // empty for now, we'll dynamically extend it later
map : new google.maps.Map(
document.getElementById( 'gmap\_md17766420f0dbf913ddd3df4db516f4b' ),
{
mapTypeId: google.maps.MapTypeId.ROADMAP,
center: new google.maps.LatLng( 0, 0 ),
zoom: 16 // Seems to be a good zoom for a single point
}
),
markers : {},
}; // end of gmap
// Extend the bounds of interest based on our positions
for ( var m in gmap\_md17766420f0dbf913ddd3df4db516f4b.positions ) {
gmap\_md17766420f0dbf913ddd3df4db516f4b.bounds.extend( gmap\_md17766420f0dbf913ddd3df4db516f4b.positions[m] );
}
// Render markers
for ( var m in gmap\_md17766420f0dbf913ddd3df4db516f4b.positions ) {
gmap\_md17766420f0dbf913ddd3df4db516f4b.markers[m] = new google.maps.Marker( {
clickable: true,
map : gmap\_md17766420f0dbf913ddd3df4db516f4b.map,
position : gmap\_md17766420f0dbf913ddd3df4db516f4b.positions[m]
} );
}
// Redraw map to fit our new marker-based bounds
gmap\_md17766420f0dbf913ddd3df4db516f4b.map.setCenter( gmap\_md17766420f0dbf913ddd3df4db516f4b.positions[343] );
});