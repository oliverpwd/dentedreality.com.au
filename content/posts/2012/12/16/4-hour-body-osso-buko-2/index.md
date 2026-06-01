---
title: 4 Hour Body Osso Buko
date: '2012-12-16T13:13:54+00:00'
format: image
service: flickr
tags:
- 4HB
- cooking
- erika
- food
- ossobuko
image: http://i1.wp.com/dentedreality.com.au/wp-content/uploads/2012/12/8459274423_b4f2a699bc_o.jpg?resize=607%2C813
---

[![4 Hour Body Osso Buko](http://i1.wp.com/dentedreality.com.au/wp-content/uploads/2012/12/8459274423_b4f2a699bc_o.jpg?resize=607%2C813)](http://dentedreality.com.au/2012/12/16/4-hour-body-osso-buko-2/) 
# [4 Hour Body Osso Buko](http://dentedreality.com.au/2012/12/16/4-hour-body-osso-buko-2/)





* #[4HB](http://dentedreality.com.au/tags/4hb/)
* #[cooking](http://dentedreality.com.au/tags/cooking/)
* #[erika](http://dentedreality.com.au/tags/erika/)
* #[food](http://dentedreality.com.au/tags/food/)
* #[ossobuko](http://dentedreality.com.au/tags/ossobuko/)

Posted on [Flickr](http://www.flickr.com/photos/borkazoid/8459274423/) [1:13 pm, December 16, 2012](http://dentedreality.com.au/2012/12/16/4-hour-body-osso-buko-2/ "1:13 pm") 
jQuery(document).ready(function(){
var gmap\_mce3fb3a1fe2a9e0b1c3e8db154420180 = {
positions : {
584 : new google.maps.LatLng( '40.6695', '-73.985' )
},
bounds : new google.maps.LatLngBounds(), // empty for now, we'll dynamically extend it later
map : new google.maps.Map(
document.getElementById( 'gmap\_mce3fb3a1fe2a9e0b1c3e8db154420180' ),
{
mapTypeId: google.maps.MapTypeId.ROADMAP,
center: new google.maps.LatLng( 0, 0 ),
zoom: 16 // Seems to be a good zoom for a single point
}
),
markers : {},
}; // end of gmap
// Extend the bounds of interest based on our positions
for ( var m in gmap\_mce3fb3a1fe2a9e0b1c3e8db154420180.positions ) {
gmap\_mce3fb3a1fe2a9e0b1c3e8db154420180.bounds.extend( gmap\_mce3fb3a1fe2a9e0b1c3e8db154420180.positions[m] );
}
// Render markers
for ( var m in gmap\_mce3fb3a1fe2a9e0b1c3e8db154420180.positions ) {
gmap\_mce3fb3a1fe2a9e0b1c3e8db154420180.markers[m] = new google.maps.Marker( {
clickable: true,
map : gmap\_mce3fb3a1fe2a9e0b1c3e8db154420180.map,
position : gmap\_mce3fb3a1fe2a9e0b1c3e8db154420180.positions[m]
} );
}
// Redraw map to fit our new marker-based bounds
gmap\_mce3fb3a1fe2a9e0b1c3e8db154420180.map.setCenter( gmap\_mce3fb3a1fe2a9e0b1c3e8db154420180.positions[584] );
});