---
title: IMG_1510
date: '2011-05-14T08:33:12+00:00'
format: image
service: flickr
tags:
- california
- orangecounty
- WCOC
- wordcamp
- wordcampoc
- wordpress
image: http://i2.wp.com/dentedreality.com.au/wp-content/uploads/2011/05/5802178013_bb3171ac8a_o.jpg?resize=607%2C813
---

[![IMG_1510](http://i2.wp.com/dentedreality.com.au/wp-content/uploads/2011/05/5802178013_bb3171ac8a_o.jpg?resize=607%2C813)](http://dentedreality.com.au/2011/05/14/img_1510/) 
# [IMG\_1510](http://dentedreality.com.au/2011/05/14/img_1510/)





* #[california](http://dentedreality.com.au/tags/california/)
* #[orangecounty](http://dentedreality.com.au/tags/orangecounty/)
* #[WCOC](http://dentedreality.com.au/tags/wcoc/)
* #[wordcamp](http://dentedreality.com.au/tags/wordcamp/)
* #[wordcampoc](http://dentedreality.com.au/tags/wordcampoc/)
* #[wordpress](http://dentedreality.com.au/tags/wordpress/)

Posted on [Flickr](http://www.flickr.com/photos/borkazoid/5802178013/) [8:33 am, May 14, 2011](http://dentedreality.com.au/2011/05/14/img_1510/ "8:33 am") 
jQuery(document).ready(function(){
var gmap\_m7655e0a82fcc627c28b7b81e44e01948 = {
positions : {
347 : new google.maps.LatLng( '33.792833', '-117.853667' )
},
bounds : new google.maps.LatLngBounds(), // empty for now, we'll dynamically extend it later
map : new google.maps.Map(
document.getElementById( 'gmap\_m7655e0a82fcc627c28b7b81e44e01948' ),
{
mapTypeId: google.maps.MapTypeId.ROADMAP,
center: new google.maps.LatLng( 0, 0 ),
zoom: 16 // Seems to be a good zoom for a single point
}
),
markers : {},
}; // end of gmap
// Extend the bounds of interest based on our positions
for ( var m in gmap\_m7655e0a82fcc627c28b7b81e44e01948.positions ) {
gmap\_m7655e0a82fcc627c28b7b81e44e01948.bounds.extend( gmap\_m7655e0a82fcc627c28b7b81e44e01948.positions[m] );
}
// Render markers
for ( var m in gmap\_m7655e0a82fcc627c28b7b81e44e01948.positions ) {
gmap\_m7655e0a82fcc627c28b7b81e44e01948.markers[m] = new google.maps.Marker( {
clickable: true,
map : gmap\_m7655e0a82fcc627c28b7b81e44e01948.map,
position : gmap\_m7655e0a82fcc627c28b7b81e44e01948.positions[m]
} );
}
// Redraw map to fit our new marker-based bounds
gmap\_m7655e0a82fcc627c28b7b81e44e01948.map.setCenter( gmap\_m7655e0a82fcc627c28b7b81e44e01948.positions[347] );
});