---
title: IMG_1509
date: '2011-05-14T05:40:21+00:00'
format: image
service: flickr
tags:
- california
- orangecounty
- WCOC
- wordcamp
- wordcampoc
- wordpress
image: http://i0.wp.com/dentedreality.com.au/wp-content/uploads/2011/05/5802177455_a3514e9d58_o.jpg?resize=607%2C813
---

[![IMG_1509](http://i0.wp.com/dentedreality.com.au/wp-content/uploads/2011/05/5802177455_a3514e9d58_o.jpg?resize=607%2C813)](http://dentedreality.com.au/2011/05/14/img_1509/) 
# [IMG\_1509](http://dentedreality.com.au/2011/05/14/img_1509/)





* #[california](http://dentedreality.com.au/tags/california/)
* #[orangecounty](http://dentedreality.com.au/tags/orangecounty/)
* #[WCOC](http://dentedreality.com.au/tags/wcoc/)
* #[wordcamp](http://dentedreality.com.au/tags/wordcamp/)
* #[wordcampoc](http://dentedreality.com.au/tags/wordcampoc/)
* #[wordpress](http://dentedreality.com.au/tags/wordpress/)

Posted on [Flickr](http://www.flickr.com/photos/borkazoid/5802177455/) [5:40 am, May 14, 2011](http://dentedreality.com.au/2011/05/14/img_1509/ "5:40 am") 
jQuery(document).ready(function(){
var gmap\_me4ab959b4a43c95e22df2eb9aef56d2b = {
positions : {
369 : new google.maps.LatLng( '33.792833', '-117.8535' )
},
bounds : new google.maps.LatLngBounds(), // empty for now, we'll dynamically extend it later
map : new google.maps.Map(
document.getElementById( 'gmap\_me4ab959b4a43c95e22df2eb9aef56d2b' ),
{
mapTypeId: google.maps.MapTypeId.ROADMAP,
center: new google.maps.LatLng( 0, 0 ),
zoom: 16 // Seems to be a good zoom for a single point
}
),
markers : {},
}; // end of gmap
// Extend the bounds of interest based on our positions
for ( var m in gmap\_me4ab959b4a43c95e22df2eb9aef56d2b.positions ) {
gmap\_me4ab959b4a43c95e22df2eb9aef56d2b.bounds.extend( gmap\_me4ab959b4a43c95e22df2eb9aef56d2b.positions[m] );
}
// Render markers
for ( var m in gmap\_me4ab959b4a43c95e22df2eb9aef56d2b.positions ) {
gmap\_me4ab959b4a43c95e22df2eb9aef56d2b.markers[m] = new google.maps.Marker( {
clickable: true,
map : gmap\_me4ab959b4a43c95e22df2eb9aef56d2b.map,
position : gmap\_me4ab959b4a43c95e22df2eb9aef56d2b.positions[m]
} );
}
// Redraw map to fit our new marker-based bounds
gmap\_me4ab959b4a43c95e22df2eb9aef56d2b.map.setCenter( gmap\_me4ab959b4a43c95e22df2eb9aef56d2b.positions[369] );
});