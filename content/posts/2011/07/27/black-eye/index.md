---
title: Black Eye
date: '2011-07-27T17:35:29+00:00'
format: image
service: flickr
tags:
- beau
- beaulebens
- blackeye
- krav
- kravmaga
- me
image: http://i2.wp.com/dentedreality.com.au/wp-content/uploads/2011/07/6322936907_9ed605ee13_o.jpg?resize=607%2C813
---

[![Black Eye](http://i2.wp.com/dentedreality.com.au/wp-content/uploads/2011/07/6322936907_9ed605ee13_o.jpg?resize=607%2C813)](http://dentedreality.com.au/2011/07/27/black-eye/) 
# [Black Eye](http://dentedreality.com.au/2011/07/27/black-eye/)

From Krav, of course





* #[beau](http://dentedreality.com.au/tags/beau/)
* #[beaulebens](http://dentedreality.com.au/tags/beaulebens/)
* #[blackeye](http://dentedreality.com.au/tags/blackeye/)
* #[krav](http://dentedreality.com.au/tags/krav/)
* #[kravmaga](http://dentedreality.com.au/tags/kravmaga/)
* #[me](http://dentedreality.com.au/tags/me/)

Posted on [Flickr](http://www.flickr.com/photos/borkazoid/6322936907/) [5:35 pm, July 27, 2011](http://dentedreality.com.au/2011/07/27/black-eye/ "5:35 pm") 
jQuery(document).ready(function(){
var gmap\_m680107f97e2e2e7c8dc55a067c2a22da = {
positions : {
587 : new google.maps.LatLng( '37.791333', '-122.417667' )
},
bounds : new google.maps.LatLngBounds(), // empty for now, we'll dynamically extend it later
map : new google.maps.Map(
document.getElementById( 'gmap\_m680107f97e2e2e7c8dc55a067c2a22da' ),
{
mapTypeId: google.maps.MapTypeId.ROADMAP,
center: new google.maps.LatLng( 0, 0 ),
zoom: 16 // Seems to be a good zoom for a single point
}
),
markers : {},
}; // end of gmap
// Extend the bounds of interest based on our positions
for ( var m in gmap\_m680107f97e2e2e7c8dc55a067c2a22da.positions ) {
gmap\_m680107f97e2e2e7c8dc55a067c2a22da.bounds.extend( gmap\_m680107f97e2e2e7c8dc55a067c2a22da.positions[m] );
}
// Render markers
for ( var m in gmap\_m680107f97e2e2e7c8dc55a067c2a22da.positions ) {
gmap\_m680107f97e2e2e7c8dc55a067c2a22da.markers[m] = new google.maps.Marker( {
clickable: true,
map : gmap\_m680107f97e2e2e7c8dc55a067c2a22da.map,
position : gmap\_m680107f97e2e2e7c8dc55a067c2a22da.positions[m]
} );
}
// Redraw map to fit our new marker-based bounds
gmap\_m680107f97e2e2e7c8dc55a067c2a22da.map.setCenter( gmap\_m680107f97e2e2e7c8dc55a067c2a22da.positions[587] );
});