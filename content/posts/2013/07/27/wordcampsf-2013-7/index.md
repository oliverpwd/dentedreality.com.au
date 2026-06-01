---
title: WordCampSF, 2013
date: '2013-07-27T08:22:32+00:00'
format: image
tags:
- automattic
- sanfrancisco
- wcsf
- wcsf2013
- wordcamp
- wordpress
image: http://i2.wp.com/dentedreality.com.au/wp-content/uploads/2013/07/9437618031_ff33837902_o.jpg?resize=607%2C813
---

[![WordCampSF, 2013](http://i2.wp.com/dentedreality.com.au/wp-content/uploads/2013/07/9437618031_ff33837902_o.jpg?resize=607%2C813)](http://dentedreality.com.au/2013/07/27/wordcampsf-2013-7/) 
# [WordCampSF, 2013](http://dentedreality.com.au/2013/07/27/wordcampsf-2013-7/)

I attended, spoke at, and organized the Contributor Day for WordCamp San Francisco 2013. This is my eigth WCSF ![:)](http://i0.wp.com/dentedreality.com.au/wp-includes/images/smilies/icon_smile.gif?w=607)





* #[automattic](http://dentedreality.com.au/tags/automattic/)
* #[sanfrancisco](http://dentedreality.com.au/tags/sanfrancisco/)
* #[wcsf](http://dentedreality.com.au/tags/wcsf/)
* #[wcsf2013](http://dentedreality.com.au/tags/wcsf2013/)
* #[wordcamp](http://dentedreality.com.au/tags/wordcamp/)
* #[wordpress](http://dentedreality.com.au/tags/wordpress/)

Posted on [Flickr](http://www.flickr.com/photos/borkazoid/9437618031/) [8:22 am, July 27, 2013](http://dentedreality.com.au/2013/07/27/wordcampsf-2013-7/ "8:22 am") 
jQuery(document).ready(function(){
var gmap\_m984c686f4c906780c6aa942dd85495e7 = {
positions : {
272 : new google.maps.LatLng( '37.768', '-122.392501' )
},
bounds : new google.maps.LatLngBounds(), // empty for now, we'll dynamically extend it later
map : new google.maps.Map(
document.getElementById( 'gmap\_m984c686f4c906780c6aa942dd85495e7' ),
{
mapTypeId: google.maps.MapTypeId.ROADMAP,
center: new google.maps.LatLng( 0, 0 ),
zoom: 16 // Seems to be a good zoom for a single point
}
),
markers : {},
}; // end of gmap
// Extend the bounds of interest based on our positions
for ( var m in gmap\_m984c686f4c906780c6aa942dd85495e7.positions ) {
gmap\_m984c686f4c906780c6aa942dd85495e7.bounds.extend( gmap\_m984c686f4c906780c6aa942dd85495e7.positions[m] );
}
// Render markers
for ( var m in gmap\_m984c686f4c906780c6aa942dd85495e7.positions ) {
gmap\_m984c686f4c906780c6aa942dd85495e7.markers[m] = new google.maps.Marker( {
clickable: true,
map : gmap\_m984c686f4c906780c6aa942dd85495e7.map,
position : gmap\_m984c686f4c906780c6aa942dd85495e7.positions[m]
} );
}
// Redraw map to fit our new marker-based bounds
gmap\_m984c686f4c906780c6aa942dd85495e7.map.setCenter( gmap\_m984c686f4c906780c6aa942dd85495e7.positions[272] );
});