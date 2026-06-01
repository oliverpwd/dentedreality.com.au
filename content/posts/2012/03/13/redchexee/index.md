---
title: RedChexee
date: '2012-03-13T11:50:03+00:00'
format: image
service: flickr
tags:
- Austin
- chexee
- sxsw
- sxsw2012
- texas
image: http://i1.wp.com/dentedreality.com.au/wp-content/uploads/2012/03/7721697938_8d7f894a73_o.jpg?resize=607%2C813
---

[![RedChexee](http://i1.wp.com/dentedreality.com.au/wp-content/uploads/2012/03/7721697938_8d7f894a73_o.jpg?resize=607%2C813)](http://dentedreality.com.au/2012/03/13/redchexee/) 
# [RedChexee](http://dentedreality.com.au/2012/03/13/redchexee/)





* #[Austin](http://dentedreality.com.au/tags/austin/)
* #[chexee](http://dentedreality.com.au/tags/chexee/)
* #[sxsw](http://dentedreality.com.au/tags/sxsw/)
* #[sxsw2012](http://dentedreality.com.au/tags/sxsw2012/)
* #[texas](http://dentedreality.com.au/tags/texas/)

Posted on [Flickr](http://www.flickr.com/photos/borkazoid/7721697938/) [11:50 am, March 13, 2012](http://dentedreality.com.au/2012/03/13/redchexee/ "11:50 am") 
jQuery(document).ready(function(){
var gmap\_m8abfa86b365244ca4c1f45e5848bc5a8 = {
positions : {
616 : new google.maps.LatLng( '30.262833', '-97.736667' )
},
bounds : new google.maps.LatLngBounds(), // empty for now, we'll dynamically extend it later
map : new google.maps.Map(
document.getElementById( 'gmap\_m8abfa86b365244ca4c1f45e5848bc5a8' ),
{
mapTypeId: google.maps.MapTypeId.ROADMAP,
center: new google.maps.LatLng( 0, 0 ),
zoom: 16 // Seems to be a good zoom for a single point
}
),
markers : {},
}; // end of gmap
// Extend the bounds of interest based on our positions
for ( var m in gmap\_m8abfa86b365244ca4c1f45e5848bc5a8.positions ) {
gmap\_m8abfa86b365244ca4c1f45e5848bc5a8.bounds.extend( gmap\_m8abfa86b365244ca4c1f45e5848bc5a8.positions[m] );
}
// Render markers
for ( var m in gmap\_m8abfa86b365244ca4c1f45e5848bc5a8.positions ) {
gmap\_m8abfa86b365244ca4c1f45e5848bc5a8.markers[m] = new google.maps.Marker( {
clickable: true,
map : gmap\_m8abfa86b365244ca4c1f45e5848bc5a8.map,
position : gmap\_m8abfa86b365244ca4c1f45e5848bc5a8.positions[m]
} );
}
// Redraw map to fit our new marker-based bounds
gmap\_m8abfa86b365244ca4c1f45e5848bc5a8.map.setCenter( gmap\_m8abfa86b365244ca4c1f45e5848bc5a8.positions[616] );
});