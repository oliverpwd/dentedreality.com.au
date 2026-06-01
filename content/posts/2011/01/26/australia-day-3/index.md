---
title: Australia Day
date: '2011-01-26T17:00:09+00:00'
format: image
service: flickr
tags:
- australia
- australiaday
- australiaday2011
- sydney
image: http://i2.wp.com/dentedreality.com.au/wp-content/uploads/2011/01/5434193635_e68998086e_o.jpg?resize=607%2C452
---

[![Australia Day](http://i2.wp.com/dentedreality.com.au/wp-content/uploads/2011/01/5434193635_e68998086e_o.jpg?resize=607%2C452)](http://dentedreality.com.au/2011/01/26/australia-day-3/) 
# [Australia Day](http://dentedreality.com.au/2011/01/26/australia-day-3/)





* #[australia](http://dentedreality.com.au/tags/australia/)
* #[australiaday](http://dentedreality.com.au/tags/australiaday/)
* #[australiaday2011](http://dentedreality.com.au/tags/australiaday2011/)
* #[sydney](http://dentedreality.com.au/tags/sydney/)

Posted on [Flickr](http://www.flickr.com/photos/borkazoid/5434193635/) [5:00 pm, January 26, 2011](http://dentedreality.com.au/2011/01/26/australia-day-3/ "5:00 pm") 
jQuery(document).ready(function(){
var gmap\_me5eba5e1664a033d7ba01215a7f452bd = {
positions : {
525 : new google.maps.LatLng( '-33.864167', '151.172' )
},
bounds : new google.maps.LatLngBounds(), // empty for now, we'll dynamically extend it later
map : new google.maps.Map(
document.getElementById( 'gmap\_me5eba5e1664a033d7ba01215a7f452bd' ),
{
mapTypeId: google.maps.MapTypeId.ROADMAP,
center: new google.maps.LatLng( 0, 0 ),
zoom: 16 // Seems to be a good zoom for a single point
}
),
markers : {},
}; // end of gmap
// Extend the bounds of interest based on our positions
for ( var m in gmap\_me5eba5e1664a033d7ba01215a7f452bd.positions ) {
gmap\_me5eba5e1664a033d7ba01215a7f452bd.bounds.extend( gmap\_me5eba5e1664a033d7ba01215a7f452bd.positions[m] );
}
// Render markers
for ( var m in gmap\_me5eba5e1664a033d7ba01215a7f452bd.positions ) {
gmap\_me5eba5e1664a033d7ba01215a7f452bd.markers[m] = new google.maps.Marker( {
clickable: true,
map : gmap\_me5eba5e1664a033d7ba01215a7f452bd.map,
position : gmap\_me5eba5e1664a033d7ba01215a7f452bd.positions[m]
} );
}
// Redraw map to fit our new marker-based bounds
gmap\_me5eba5e1664a033d7ba01215a7f452bd.map.setCenter( gmap\_me5eba5e1664a033d7ba01215a7f452bd.positions[525] );
});