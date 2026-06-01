---
title: Brothers
date: '2008-04-10T15:53:00+00:00'
format: image
service: flickr
tags:
- australia
- beau
- beaulebens
- brothers
- kai
- me
- sydney
image: http://i2.wp.com/dentedreality.com.au/wp-content/uploads/2008/04/2437454546_17893fb0d1_o.jpg?resize=607%2C455
---

[![Brothers](http://i2.wp.com/dentedreality.com.au/wp-content/uploads/2008/04/2437454546_17893fb0d1_o.jpg?resize=607%2C455)](http://dentedreality.com.au/2008/04/10/brothers/) 
# [Brothers](http://dentedreality.com.au/2008/04/10/brothers/)

Sitting like this I suppose we do look pretty similar, but I still don’t see it in our faces.





* #[australia](http://dentedreality.com.au/tags/australia/)
* #[beau](http://dentedreality.com.au/tags/beau/)
* #[beaulebens](http://dentedreality.com.au/tags/beaulebens/)
* #[brothers](http://dentedreality.com.au/tags/brothers/)
* #[kai](http://dentedreality.com.au/tags/kai/)
* #[me](http://dentedreality.com.au/tags/me/)
* #[sydney](http://dentedreality.com.au/tags/sydney/)

Posted on [Flickr](http://www.flickr.com/photos/borkazoid/2437454546/) [3:53 pm, April 10, 2008](http://dentedreality.com.au/2008/04/10/brothers/ "3:53 pm") 
jQuery(document).ready(function(){
var gmap\_m4c8dcbda2752d1f7a8dd5a740f1a8a4f = {
positions : {
711 : new google.maps.LatLng( '-33.874548', '151.261997' )
},
bounds : new google.maps.LatLngBounds(), // empty for now, we'll dynamically extend it later
map : new google.maps.Map(
document.getElementById( 'gmap\_m4c8dcbda2752d1f7a8dd5a740f1a8a4f' ),
{
mapTypeId: google.maps.MapTypeId.ROADMAP,
center: new google.maps.LatLng( 0, 0 ),
zoom: 16 // Seems to be a good zoom for a single point
}
),
markers : {},
}; // end of gmap
// Extend the bounds of interest based on our positions
for ( var m in gmap\_m4c8dcbda2752d1f7a8dd5a740f1a8a4f.positions ) {
gmap\_m4c8dcbda2752d1f7a8dd5a740f1a8a4f.bounds.extend( gmap\_m4c8dcbda2752d1f7a8dd5a740f1a8a4f.positions[m] );
}
// Render markers
for ( var m in gmap\_m4c8dcbda2752d1f7a8dd5a740f1a8a4f.positions ) {
gmap\_m4c8dcbda2752d1f7a8dd5a740f1a8a4f.markers[m] = new google.maps.Marker( {
clickable: true,
map : gmap\_m4c8dcbda2752d1f7a8dd5a740f1a8a4f.map,
position : gmap\_m4c8dcbda2752d1f7a8dd5a740f1a8a4f.positions[m]
} );
}
// Redraw map to fit our new marker-based bounds
gmap\_m4c8dcbda2752d1f7a8dd5a740f1a8a4f.map.setCenter( gmap\_m4c8dcbda2752d1f7a8dd5a740f1a8a4f.positions[711] );
});