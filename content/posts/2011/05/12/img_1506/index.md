---
title: IMG_1506
date: '2011-05-12T14:56:50+00:00'
format: image
service: flickr
tags:
- california
- orangecounty
- WCOC
- wordcamp
- wordcampoc
- wordpress
image: http://i2.wp.com/dentedreality.com.au/wp-content/uploads/2011/05/5802177117_89f8952a63_o.jpg?resize=607%2C452
---

[![IMG_1506](http://i2.wp.com/dentedreality.com.au/wp-content/uploads/2011/05/5802177117_89f8952a63_o.jpg?resize=607%2C452)](http://dentedreality.com.au/2011/05/12/img_1506/) 
# [IMG\_1506](http://dentedreality.com.au/2011/05/12/img_1506/)





* #[california](http://dentedreality.com.au/tags/california/)
* #[orangecounty](http://dentedreality.com.au/tags/orangecounty/)
* #[WCOC](http://dentedreality.com.au/tags/wcoc/)
* #[wordcamp](http://dentedreality.com.au/tags/wordcamp/)
* #[wordcampoc](http://dentedreality.com.au/tags/wordcampoc/)
* #[wordpress](http://dentedreality.com.au/tags/wordpress/)

Posted on [Flickr](http://www.flickr.com/photos/borkazoid/5802177117/) [2:56 pm, May 12, 2011](http://dentedreality.com.au/2011/05/12/img_1506/ "2:56 pm") 
jQuery(document).ready(function(){
var gmap\_m7fa94c545fcc987c18ac271f3d2caafa = {
positions : {
438 : new google.maps.LatLng( '37.782', '-122.401001' )
},
bounds : new google.maps.LatLngBounds(), // empty for now, we'll dynamically extend it later
map : new google.maps.Map(
document.getElementById( 'gmap\_m7fa94c545fcc987c18ac271f3d2caafa' ),
{
mapTypeId: google.maps.MapTypeId.ROADMAP,
center: new google.maps.LatLng( 0, 0 ),
zoom: 16 // Seems to be a good zoom for a single point
}
),
markers : {},
}; // end of gmap
// Extend the bounds of interest based on our positions
for ( var m in gmap\_m7fa94c545fcc987c18ac271f3d2caafa.positions ) {
gmap\_m7fa94c545fcc987c18ac271f3d2caafa.bounds.extend( gmap\_m7fa94c545fcc987c18ac271f3d2caafa.positions[m] );
}
// Render markers
for ( var m in gmap\_m7fa94c545fcc987c18ac271f3d2caafa.positions ) {
gmap\_m7fa94c545fcc987c18ac271f3d2caafa.markers[m] = new google.maps.Marker( {
clickable: true,
map : gmap\_m7fa94c545fcc987c18ac271f3d2caafa.map,
position : gmap\_m7fa94c545fcc987c18ac271f3d2caafa.positions[m]
} );
}
// Redraw map to fit our new marker-based bounds
gmap\_m7fa94c545fcc987c18ac271f3d2caafa.map.setCenter( gmap\_m7fa94c545fcc987c18ac271f3d2caafa.positions[438] );
});