---
title: Thanksgiving 2012
date: '2012-11-22T12:00:12+00:00'
format: image
service: flickr
tags:
- beau
- beaulebens
- food
- me
- thanksgiving
- tray
image: http://i1.wp.com/dentedreality.com.au/wp-content/uploads/2012/11/8460375592_619fea00a4_o.jpg?resize=607%2C813
---

[![Thanksgiving 2012](http://i1.wp.com/dentedreality.com.au/wp-content/uploads/2012/11/8460375592_619fea00a4_o.jpg?resize=607%2C813)](http://dentedreality.com.au/2012/11/22/thanksgiving-2012/) 
# [Thanksgiving 2012](http://dentedreality.com.au/2012/11/22/thanksgiving-2012/)





* #[beau](http://dentedreality.com.au/tags/beau/)
* #[beaulebens](http://dentedreality.com.au/tags/beaulebens/)
* #[food](http://dentedreality.com.au/tags/food/)
* #[me](http://dentedreality.com.au/tags/me/)
* #[thanksgiving](http://dentedreality.com.au/tags/thanksgiving/)
* #[tray](http://dentedreality.com.au/tags/tray/)

Posted on [Flickr](http://www.flickr.com/photos/borkazoid/8460375592/) [12:00 pm, November 22, 2012](http://dentedreality.com.au/2012/11/22/thanksgiving-2012/ "12:00 pm") 
jQuery(document).ready(function(){
var gmap\_m83e7925da6da286e55676a9feb48becd = {
positions : {
763 : new google.maps.LatLng( '39.080666', '-77.472667' )
},
bounds : new google.maps.LatLngBounds(), // empty for now, we'll dynamically extend it later
map : new google.maps.Map(
document.getElementById( 'gmap\_m83e7925da6da286e55676a9feb48becd' ),
{
mapTypeId: google.maps.MapTypeId.ROADMAP,
center: new google.maps.LatLng( 0, 0 ),
zoom: 16 // Seems to be a good zoom for a single point
}
),
markers : {},
}; // end of gmap
// Extend the bounds of interest based on our positions
for ( var m in gmap\_m83e7925da6da286e55676a9feb48becd.positions ) {
gmap\_m83e7925da6da286e55676a9feb48becd.bounds.extend( gmap\_m83e7925da6da286e55676a9feb48becd.positions[m] );
}
// Render markers
for ( var m in gmap\_m83e7925da6da286e55676a9feb48becd.positions ) {
gmap\_m83e7925da6da286e55676a9feb48becd.markers[m] = new google.maps.Marker( {
clickable: true,
map : gmap\_m83e7925da6da286e55676a9feb48becd.map,
position : gmap\_m83e7925da6da286e55676a9feb48becd.positions[m]
} );
}
// Redraw map to fit our new marker-based bounds
gmap\_m83e7925da6da286e55676a9feb48becd.map.setCenter( gmap\_m83e7925da6da286e55676a9feb48becd.positions[763] );
});