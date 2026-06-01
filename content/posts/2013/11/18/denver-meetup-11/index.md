---
title: Denver Meetup
date: '2013-11-18T08:55:49+00:00'
format: image
service: flickr
tags:
- automattic
- colorado
- Denver
- meetup
- mercury
- vision:clouds=0709
- vision:mountain=0673
- vision:outdoor=099
- vision:sky=0973
image: http://i1.wp.com/dentedreality.com.au/wp-content/uploads/2013/11/12291694926_126ddaaa13_o.jpg?resize=607%2C455
---

[![Denver Meetup](http://i1.wp.com/dentedreality.com.au/wp-content/uploads/2013/11/12291694926_126ddaaa13_o.jpg?resize=607%2C455)](http://dentedreality.com.au/2013/11/18/denver-meetup-11/) 
# [Denver Meetup](http://dentedreality.com.au/2013/11/18/denver-meetup-11/)

Team Mercury meetup (and a few days after) in Denver, Colorado.





* #[automattic](http://dentedreality.com.au/tags/automattic/)
* #[colorado](http://dentedreality.com.au/tags/colorado/)
* #[Denver](http://dentedreality.com.au/tags/denver/)
* #[meetup](http://dentedreality.com.au/tags/meetup/)
* #[mercury](http://dentedreality.com.au/tags/mercury/)
* #[vision:clouds=0709](http://dentedreality.com.au/tags/visionclouds0709/)
* #[vision:mountain=0673](http://dentedreality.com.au/tags/visionmountain0673/)
* #[vision:outdoor=099](http://dentedreality.com.au/tags/visionoutdoor099/)
* #[vision:sky=0973](http://dentedreality.com.au/tags/visionsky0973/)

Posted on [Flickr](http://www.flickr.com/photos/borkazoid/12291694926/) [8:55 am, November 18, 2013](http://dentedreality.com.au/2013/11/18/denver-meetup-11/ "8:55 am") 
jQuery(document).ready(function(){
var gmap\_md7e837f6c6775b6ba5d1527fb53d5384 = {
positions : {
768 : new google.maps.LatLng( '39.661483', '-105.204698' )
},
bounds : new google.maps.LatLngBounds(), // empty for now, we'll dynamically extend it later
map : new google.maps.Map(
document.getElementById( 'gmap\_md7e837f6c6775b6ba5d1527fb53d5384' ),
{
mapTypeId: google.maps.MapTypeId.ROADMAP,
center: new google.maps.LatLng( 0, 0 ),
zoom: 16 // Seems to be a good zoom for a single point
}
),
markers : {},
}; // end of gmap
// Extend the bounds of interest based on our positions
for ( var m in gmap\_md7e837f6c6775b6ba5d1527fb53d5384.positions ) {
gmap\_md7e837f6c6775b6ba5d1527fb53d5384.bounds.extend( gmap\_md7e837f6c6775b6ba5d1527fb53d5384.positions[m] );
}
// Render markers
for ( var m in gmap\_md7e837f6c6775b6ba5d1527fb53d5384.positions ) {
gmap\_md7e837f6c6775b6ba5d1527fb53d5384.markers[m] = new google.maps.Marker( {
clickable: true,
map : gmap\_md7e837f6c6775b6ba5d1527fb53d5384.map,
position : gmap\_md7e837f6c6775b6ba5d1527fb53d5384.positions[m]
} );
}
// Redraw map to fit our new marker-based bounds
gmap\_md7e837f6c6775b6ba5d1527fb53d5384.map.setCenter( gmap\_md7e837f6c6775b6ba5d1527fb53d5384.positions[768] );
});