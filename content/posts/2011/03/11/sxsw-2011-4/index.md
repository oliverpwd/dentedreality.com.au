---
title: SXSW 2011
date: '2011-03-11T16:00:28+00:00'
format: image
service: flickr
tags:
- Austin
- sxsw
- sxsw2011
- texas
image: http://i2.wp.com/dentedreality.com.au/wp-content/uploads/2011/03/5802095989_1cc2b34abb_o.jpg?resize=607%2C452
---

[![SXSW 2011](http://i2.wp.com/dentedreality.com.au/wp-content/uploads/2011/03/5802095989_1cc2b34abb_o.jpg?resize=607%2C452)](http://dentedreality.com.au/2011/03/11/sxsw-2011-4/) 
# [SXSW 2011](http://dentedreality.com.au/2011/03/11/sxsw-2011-4/)





* #[Austin](http://dentedreality.com.au/tags/austin/)
* #[sxsw](http://dentedreality.com.au/tags/sxsw/)
* #[sxsw2011](http://dentedreality.com.au/tags/sxsw2011/)
* #[texas](http://dentedreality.com.au/tags/texas/)

Posted on [Flickr](http://www.flickr.com/photos/borkazoid/5802095989/) [4:00 pm, March 11, 2011](http://dentedreality.com.au/2011/03/11/sxsw-2011-4/ "4:00 pm") 
jQuery(document).ready(function(){
var gmap\_m2a45248a73902848275489543e44744a = {
positions : {
962 : new google.maps.LatLng( '30.269666', '-97.749167' )
},
bounds : new google.maps.LatLngBounds(), // empty for now, we'll dynamically extend it later
map : new google.maps.Map(
document.getElementById( 'gmap\_m2a45248a73902848275489543e44744a' ),
{
mapTypeId: google.maps.MapTypeId.ROADMAP,
center: new google.maps.LatLng( 0, 0 ),
zoom: 16 // Seems to be a good zoom for a single point
}
),
markers : {},
}; // end of gmap
// Extend the bounds of interest based on our positions
for ( var m in gmap\_m2a45248a73902848275489543e44744a.positions ) {
gmap\_m2a45248a73902848275489543e44744a.bounds.extend( gmap\_m2a45248a73902848275489543e44744a.positions[m] );
}
// Render markers
for ( var m in gmap\_m2a45248a73902848275489543e44744a.positions ) {
gmap\_m2a45248a73902848275489543e44744a.markers[m] = new google.maps.Marker( {
clickable: true,
map : gmap\_m2a45248a73902848275489543e44744a.map,
position : gmap\_m2a45248a73902848275489543e44744a.positions[m]
} );
}
// Redraw map to fit our new marker-based bounds
gmap\_m2a45248a73902848275489543e44744a.map.setCenter( gmap\_m2a45248a73902848275489543e44744a.positions[962] );
});