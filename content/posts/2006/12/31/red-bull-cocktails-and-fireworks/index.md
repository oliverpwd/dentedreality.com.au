---
title: Red Bull, Cocktails and Fireworks
date: '2006-12-31T03:59:48+00:00'
format: image
service: flickr
tags:
- fireworks
- newyearseve2006
- nye2006
- phuket
- redbull
- thailand
- thailand06
- vodkaorange
image: http://i0.wp.com/dentedreality.com.au/wp-content/uploads/2006/12/349554509_eba56b1d84_o.jpg?resize=607%2C455
---

[![Red Bull, Cocktails and Fireworks](http://i0.wp.com/dentedreality.com.au/wp-content/uploads/2006/12/349554509_eba56b1d84_o.jpg?resize=607%2C455)](http://dentedreality.com.au/2006/12/31/red-bull-cocktails-and-fireworks/) 
# [Red Bull, Cocktails and Fireworks](http://dentedreality.com.au/2006/12/31/red-bull-cocktails-and-fireworks/)

The cube-looking one had 16 separate bits that shot into the air and exploded, the tall one was just one big one. Best $7 ever spent!





* #[fireworks](http://dentedreality.com.au/tags/fireworks/)
* #[newyearseve2006](http://dentedreality.com.au/tags/newyearseve2006/)
* #[nye2006](http://dentedreality.com.au/tags/nye2006/)
* #[phuket](http://dentedreality.com.au/tags/phuket/)
* #[redbull](http://dentedreality.com.au/tags/redbull/)
* #[thailand](http://dentedreality.com.au/tags/thailand/)
* #[thailand06](http://dentedreality.com.au/tags/thailand06/)
* #[vodkaorange](http://dentedreality.com.au/tags/vodkaorange/)

Posted on [Flickr](http://www.flickr.com/photos/borkazoid/349554509/) [3:59 am, December 31, 2006](http://dentedreality.com.au/2006/12/31/red-bull-cocktails-and-fireworks/ "3:59 am") 
jQuery(document).ready(function(){
var gmap\_mde07f59123d5278f96dd5c92e8c3e1f9 = {
positions : {
901 : new google.maps.LatLng( '7.896794', '98.295879' )
},
bounds : new google.maps.LatLngBounds(), // empty for now, we'll dynamically extend it later
map : new google.maps.Map(
document.getElementById( 'gmap\_mde07f59123d5278f96dd5c92e8c3e1f9' ),
{
mapTypeId: google.maps.MapTypeId.ROADMAP,
center: new google.maps.LatLng( 0, 0 ),
zoom: 16 // Seems to be a good zoom for a single point
}
),
markers : {},
}; // end of gmap
// Extend the bounds of interest based on our positions
for ( var m in gmap\_mde07f59123d5278f96dd5c92e8c3e1f9.positions ) {
gmap\_mde07f59123d5278f96dd5c92e8c3e1f9.bounds.extend( gmap\_mde07f59123d5278f96dd5c92e8c3e1f9.positions[m] );
}
// Render markers
for ( var m in gmap\_mde07f59123d5278f96dd5c92e8c3e1f9.positions ) {
gmap\_mde07f59123d5278f96dd5c92e8c3e1f9.markers[m] = new google.maps.Marker( {
clickable: true,
map : gmap\_mde07f59123d5278f96dd5c92e8c3e1f9.map,
position : gmap\_mde07f59123d5278f96dd5c92e8c3e1f9.positions[m]
} );
}
// Redraw map to fit our new marker-based bounds
gmap\_mde07f59123d5278f96dd5c92e8c3e1f9.map.setCenter( gmap\_mde07f59123d5278f96dd5c92e8c3e1f9.positions[901] );
});