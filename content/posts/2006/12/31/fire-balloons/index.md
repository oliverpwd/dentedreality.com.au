---
title: Fire Balloons
date: '2006-12-31T07:13:40+00:00'
format: image
service: flickr
tags:
- fireworks
- newyearseve2006
- nye2006
- phuket
- pyrotechnics
- thailand
- thailand06
image: http://i1.wp.com/dentedreality.com.au/wp-content/uploads/2006/12/349546232_5eb4917f8b_o.jpg?resize=607%2C455
---

[![Fire Balloons](http://i1.wp.com/dentedreality.com.au/wp-content/uploads/2006/12/349546232_5eb4917f8b_o.jpg?resize=607%2C455)](http://dentedreality.com.au/2006/12/31/fire-balloons/) 
# [Fire Balloons](http://dentedreality.com.au/2006/12/31/fire-balloons/)

These were the really cool "fire balloons" that everyone was letting off. They were like a one-time hot air balloon that was made of tissue-paper.





* #[fireworks](http://dentedreality.com.au/tags/fireworks/)
* #[newyearseve2006](http://dentedreality.com.au/tags/newyearseve2006/)
* #[nye2006](http://dentedreality.com.au/tags/nye2006/)
* #[phuket](http://dentedreality.com.au/tags/phuket/)
* #[pyrotechnics](http://dentedreality.com.au/tags/pyrotechnics/)
* #[thailand](http://dentedreality.com.au/tags/thailand/)
* #[thailand06](http://dentedreality.com.au/tags/thailand06/)

Posted on [Flickr](http://www.flickr.com/photos/borkazoid/349546232/) [7:13 am, December 31, 2006](http://dentedreality.com.au/2006/12/31/fire-balloons/ "7:13 am") 
jQuery(document).ready(function(){
var gmap\_m049e2f3db0b1a5e628003f6fa18370e2 = {
positions : {
677 : new google.maps.LatLng( '7.896794', '98.295879' )
},
bounds : new google.maps.LatLngBounds(), // empty for now, we'll dynamically extend it later
map : new google.maps.Map(
document.getElementById( 'gmap\_m049e2f3db0b1a5e628003f6fa18370e2' ),
{
mapTypeId: google.maps.MapTypeId.ROADMAP,
center: new google.maps.LatLng( 0, 0 ),
zoom: 16 // Seems to be a good zoom for a single point
}
),
markers : {},
}; // end of gmap
// Extend the bounds of interest based on our positions
for ( var m in gmap\_m049e2f3db0b1a5e628003f6fa18370e2.positions ) {
gmap\_m049e2f3db0b1a5e628003f6fa18370e2.bounds.extend( gmap\_m049e2f3db0b1a5e628003f6fa18370e2.positions[m] );
}
// Render markers
for ( var m in gmap\_m049e2f3db0b1a5e628003f6fa18370e2.positions ) {
gmap\_m049e2f3db0b1a5e628003f6fa18370e2.markers[m] = new google.maps.Marker( {
clickable: true,
map : gmap\_m049e2f3db0b1a5e628003f6fa18370e2.map,
position : gmap\_m049e2f3db0b1a5e628003f6fa18370e2.positions[m]
} );
}
// Redraw map to fit our new marker-based bounds
gmap\_m049e2f3db0b1a5e628003f6fa18370e2.map.setCenter( gmap\_m049e2f3db0b1a5e628003f6fa18370e2.positions[677] );
});