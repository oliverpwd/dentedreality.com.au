---
title: Software Engineering Learnup
date: '2013-05-19T17:22:14+00:00'
format: image
service: flickr
tags:
- automattic
- hawthorne
- learnup
image: http://i2.wp.com/dentedreality.com.au/wp-content/uploads/2013/05/9436931641_242909a9f6_o.jpg?resize=607%2C452
---

[![Software Engineering Learnup](http://i2.wp.com/dentedreality.com.au/wp-content/uploads/2013/05/9436931641_242909a9f6_o.jpg?resize=607%2C452)](http://dentedreality.com.au/2013/05/19/software-engineering-learnup-2/) 
# [Software Engineering Learnup](http://dentedreality.com.au/2013/05/19/software-engineering-learnup-2/)





* #[automattic](http://dentedreality.com.au/tags/automattic/)
* #[hawthorne](http://dentedreality.com.au/tags/hawthorne/)
* #[learnup](http://dentedreality.com.au/tags/learnup/)

Posted on [Flickr](http://www.flickr.com/photos/borkazoid/9436931641/) [5:22 pm, May 19, 2013](http://dentedreality.com.au/2013/05/19/software-engineering-learnup-2/ "5:22 pm") 
jQuery(document).ready(function(){
var gmap\_m7f31ff0fbd3c74157032cdddd0e65444 = {
positions : {
535 : new google.maps.LatLng( '37.784166', '-122.397334' )
},
bounds : new google.maps.LatLngBounds(), // empty for now, we'll dynamically extend it later
map : new google.maps.Map(
document.getElementById( 'gmap\_m7f31ff0fbd3c74157032cdddd0e65444' ),
{
mapTypeId: google.maps.MapTypeId.ROADMAP,
center: new google.maps.LatLng( 0, 0 ),
zoom: 16 // Seems to be a good zoom for a single point
}
),
markers : {},
}; // end of gmap
// Extend the bounds of interest based on our positions
for ( var m in gmap\_m7f31ff0fbd3c74157032cdddd0e65444.positions ) {
gmap\_m7f31ff0fbd3c74157032cdddd0e65444.bounds.extend( gmap\_m7f31ff0fbd3c74157032cdddd0e65444.positions[m] );
}
// Render markers
for ( var m in gmap\_m7f31ff0fbd3c74157032cdddd0e65444.positions ) {
gmap\_m7f31ff0fbd3c74157032cdddd0e65444.markers[m] = new google.maps.Marker( {
clickable: true,
map : gmap\_m7f31ff0fbd3c74157032cdddd0e65444.map,
position : gmap\_m7f31ff0fbd3c74157032cdddd0e65444.positions[m]
} );
}
// Redraw map to fit our new marker-based bounds
gmap\_m7f31ff0fbd3c74157032cdddd0e65444.map.setCenter( gmap\_m7f31ff0fbd3c74157032cdddd0e65444.positions[535] );
});