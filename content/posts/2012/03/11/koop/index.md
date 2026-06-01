---
title: KOOP
date: '2012-03-11T18:24:29+00:00'
format: image
service: flickr
tags:
- Austin
- sxsw
- sxsw2012
- texas
image: http://i1.wp.com/dentedreality.com.au/wp-content/uploads/2012/03/7721573544_4874305bc1_o.jpg?resize=607%2C452
---

[![KOOP](http://i1.wp.com/dentedreality.com.au/wp-content/uploads/2012/03/7721573544_4874305bc1_o.jpg?resize=607%2C452)](http://dentedreality.com.au/2012/03/11/koop/) 
# [KOOP](http://dentedreality.com.au/2012/03/11/koop/)





* #[Austin](http://dentedreality.com.au/tags/austin/)
* #[sxsw](http://dentedreality.com.au/tags/sxsw/)
* #[sxsw2012](http://dentedreality.com.au/tags/sxsw2012/)
* #[texas](http://dentedreality.com.au/tags/texas/)

Posted on [Flickr](http://www.flickr.com/photos/borkazoid/7721573544/) [6:24 pm, March 11, 2012](http://dentedreality.com.au/2012/03/11/koop/ "6:24 pm") 
jQuery(document).ready(function(){
var gmap\_m8aa6f8ace4371fab312f47bcc57b7fb6 = {
positions : {
593 : new google.maps.LatLng( '30.27', '-97.749' )
},
bounds : new google.maps.LatLngBounds(), // empty for now, we'll dynamically extend it later
map : new google.maps.Map(
document.getElementById( 'gmap\_m8aa6f8ace4371fab312f47bcc57b7fb6' ),
{
mapTypeId: google.maps.MapTypeId.ROADMAP,
center: new google.maps.LatLng( 0, 0 ),
zoom: 16 // Seems to be a good zoom for a single point
}
),
markers : {},
}; // end of gmap
// Extend the bounds of interest based on our positions
for ( var m in gmap\_m8aa6f8ace4371fab312f47bcc57b7fb6.positions ) {
gmap\_m8aa6f8ace4371fab312f47bcc57b7fb6.bounds.extend( gmap\_m8aa6f8ace4371fab312f47bcc57b7fb6.positions[m] );
}
// Render markers
for ( var m in gmap\_m8aa6f8ace4371fab312f47bcc57b7fb6.positions ) {
gmap\_m8aa6f8ace4371fab312f47bcc57b7fb6.markers[m] = new google.maps.Marker( {
clickable: true,
map : gmap\_m8aa6f8ace4371fab312f47bcc57b7fb6.map,
position : gmap\_m8aa6f8ace4371fab312f47bcc57b7fb6.positions[m]
} );
}
// Redraw map to fit our new marker-based bounds
gmap\_m8aa6f8ace4371fab312f47bcc57b7fb6.map.setCenter( gmap\_m8aa6f8ace4371fab312f47bcc57b7fb6.positions[593] );
});