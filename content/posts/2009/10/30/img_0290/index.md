---
title: IMG_0290
date: '2009-10-30T15:52:01+00:00'
format: image
service: flickr
tags:
- newyork
- wcnyc
- wordcamp
image: http://i2.wp.com/dentedreality.com.au/wp-content/uploads/2009/10/4123949608_5ca08cea54_o.jpg?resize=607%2C809
---

[![IMG_0290](http://i2.wp.com/dentedreality.com.au/wp-content/uploads/2009/10/4123949608_5ca08cea54_o.jpg?resize=607%2C809)](http://dentedreality.com.au/2009/10/30/img_0290/) 
# [IMG\_0290](http://dentedreality.com.au/2009/10/30/img_0290/)





* #[newyork](http://dentedreality.com.au/tags/newyork/)
* #[wcnyc](http://dentedreality.com.au/tags/wcnyc/)
* #[wordcamp](http://dentedreality.com.au/tags/wordcamp/)

Posted on [Flickr](http://www.flickr.com/photos/borkazoid/4123949608/) [3:52 pm, October 30, 2009](http://dentedreality.com.au/2009/10/30/img_0290/ "3:52 pm") 
jQuery(document).ready(function(){
var gmap\_mbe022c48cb36271118522f3118ad3eb3 = {
positions : {
271 : new google.maps.LatLng( '37.849', '-122.2375' )
},
bounds : new google.maps.LatLngBounds(), // empty for now, we'll dynamically extend it later
map : new google.maps.Map(
document.getElementById( 'gmap\_mbe022c48cb36271118522f3118ad3eb3' ),
{
mapTypeId: google.maps.MapTypeId.ROADMAP,
center: new google.maps.LatLng( 0, 0 ),
zoom: 16 // Seems to be a good zoom for a single point
}
),
markers : {},
}; // end of gmap
// Extend the bounds of interest based on our positions
for ( var m in gmap\_mbe022c48cb36271118522f3118ad3eb3.positions ) {
gmap\_mbe022c48cb36271118522f3118ad3eb3.bounds.extend( gmap\_mbe022c48cb36271118522f3118ad3eb3.positions[m] );
}
// Render markers
for ( var m in gmap\_mbe022c48cb36271118522f3118ad3eb3.positions ) {
gmap\_mbe022c48cb36271118522f3118ad3eb3.markers[m] = new google.maps.Marker( {
clickable: true,
map : gmap\_mbe022c48cb36271118522f3118ad3eb3.map,
position : gmap\_mbe022c48cb36271118522f3118ad3eb3.positions[m]
} );
}
// Redraw map to fit our new marker-based bounds
gmap\_mbe022c48cb36271118522f3118ad3eb3.map.setCenter( gmap\_mbe022c48cb36271118522f3118ad3eb3.positions[271] );
});