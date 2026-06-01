---
title: Bar-top Schoolgirls
date: '2006-12-31T05:34:29+00:00'
format: image
service: flickr
tags:
- bardancing
- newyearseve2006
- nye2006
- phuket
- schoolgirls
- skirt
- thailand
- thailand06
image: http://i0.wp.com/dentedreality.com.au/wp-content/uploads/2006/12/349553848_1ea03210cd_o.jpg?resize=607%2C455
---

[![Bar-top Schoolgirls](http://i0.wp.com/dentedreality.com.au/wp-content/uploads/2006/12/349553848_1ea03210cd_o.jpg?resize=607%2C455)](http://dentedreality.com.au/2006/12/31/bar-top-schoolgirls/) 
# [Bar-top Schoolgirls](http://dentedreality.com.au/2006/12/31/bar-top-schoolgirls/)

One of the many, many bars with "girls" (?) dancing on the bar





* #[bardancing](http://dentedreality.com.au/tags/bardancing/)
* #[newyearseve2006](http://dentedreality.com.au/tags/newyearseve2006/)
* #[nye2006](http://dentedreality.com.au/tags/nye2006/)
* #[phuket](http://dentedreality.com.au/tags/phuket/)
* #[schoolgirls](http://dentedreality.com.au/tags/schoolgirls/)
* #[skirt](http://dentedreality.com.au/tags/skirt/)
* #[thailand](http://dentedreality.com.au/tags/thailand/)
* #[thailand06](http://dentedreality.com.au/tags/thailand06/)

Posted on [Flickr](http://www.flickr.com/photos/borkazoid/349553848/) [5:34 am, December 31, 2006](http://dentedreality.com.au/2006/12/31/bar-top-schoolgirls/ "5:34 am") 
jQuery(document).ready(function(){
var gmap\_m94f12c3c6b073115f2a8836c2c980123 = {
positions : {
969 : new google.maps.LatLng( '7.896794', '98.295879' )
},
bounds : new google.maps.LatLngBounds(), // empty for now, we'll dynamically extend it later
map : new google.maps.Map(
document.getElementById( 'gmap\_m94f12c3c6b073115f2a8836c2c980123' ),
{
mapTypeId: google.maps.MapTypeId.ROADMAP,
center: new google.maps.LatLng( 0, 0 ),
zoom: 16 // Seems to be a good zoom for a single point
}
),
markers : {},
}; // end of gmap
// Extend the bounds of interest based on our positions
for ( var m in gmap\_m94f12c3c6b073115f2a8836c2c980123.positions ) {
gmap\_m94f12c3c6b073115f2a8836c2c980123.bounds.extend( gmap\_m94f12c3c6b073115f2a8836c2c980123.positions[m] );
}
// Render markers
for ( var m in gmap\_m94f12c3c6b073115f2a8836c2c980123.positions ) {
gmap\_m94f12c3c6b073115f2a8836c2c980123.markers[m] = new google.maps.Marker( {
clickable: true,
map : gmap\_m94f12c3c6b073115f2a8836c2c980123.map,
position : gmap\_m94f12c3c6b073115f2a8836c2c980123.positions[m]
} );
}
// Redraw map to fit our new marker-based bounds
gmap\_m94f12c3c6b073115f2a8836c2c980123.map.setCenter( gmap\_m94f12c3c6b073115f2a8836c2c980123.positions[969] );
});