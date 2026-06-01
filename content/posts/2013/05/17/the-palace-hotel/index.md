---
title: The Palace Hotel
date: '2013-05-17T07:01:08+00:00'
format: image
service: flickr
tags:
- automattic
- hotel
- palacehotel
- restaurant
- sanfrancisco
image: http://i1.wp.com/dentedreality.com.au/wp-content/uploads/2013/05/9439712090_7cf4ae34ef_o.jpg?resize=607%2C452
---

[![The Palace Hotel](http://i1.wp.com/dentedreality.com.au/wp-content/uploads/2013/05/9439712090_7cf4ae34ef_o.jpg?resize=607%2C452)](http://dentedreality.com.au/2013/05/17/the-palace-hotel/) 
# [The Palace Hotel](http://dentedreality.com.au/2013/05/17/the-palace-hotel/)

Dining room





* #[automattic](http://dentedreality.com.au/tags/automattic/)
* #[hotel](http://dentedreality.com.au/tags/hotel/)
* #[palacehotel](http://dentedreality.com.au/tags/palacehotel/)
* #[restaurant](http://dentedreality.com.au/tags/restaurant/)
* #[sanfrancisco](http://dentedreality.com.au/tags/sanfrancisco/)

Posted on [Flickr](http://www.flickr.com/photos/borkazoid/9439712090/) [7:01 am, May 17, 2013](http://dentedreality.com.au/2013/05/17/the-palace-hotel/ "7:01 am") 
jQuery(document).ready(function(){
var gmap\_m064178d5ccdee4cd27e049f2b74647c6 = {
positions : {
347 : new google.maps.LatLng( '37.788166', '-122.401667' )
},
bounds : new google.maps.LatLngBounds(), // empty for now, we'll dynamically extend it later
map : new google.maps.Map(
document.getElementById( 'gmap\_m064178d5ccdee4cd27e049f2b74647c6' ),
{
mapTypeId: google.maps.MapTypeId.ROADMAP,
center: new google.maps.LatLng( 0, 0 ),
zoom: 16 // Seems to be a good zoom for a single point
}
),
markers : {},
}; // end of gmap
// Extend the bounds of interest based on our positions
for ( var m in gmap\_m064178d5ccdee4cd27e049f2b74647c6.positions ) {
gmap\_m064178d5ccdee4cd27e049f2b74647c6.bounds.extend( gmap\_m064178d5ccdee4cd27e049f2b74647c6.positions[m] );
}
// Render markers
for ( var m in gmap\_m064178d5ccdee4cd27e049f2b74647c6.positions ) {
gmap\_m064178d5ccdee4cd27e049f2b74647c6.markers[m] = new google.maps.Marker( {
clickable: true,
map : gmap\_m064178d5ccdee4cd27e049f2b74647c6.map,
position : gmap\_m064178d5ccdee4cd27e049f2b74647c6.positions[m]
} );
}
// Redraw map to fit our new marker-based bounds
gmap\_m064178d5ccdee4cd27e049f2b74647c6.map.setCenter( gmap\_m064178d5ccdee4cd27e049f2b74647c6.positions[347] );
});