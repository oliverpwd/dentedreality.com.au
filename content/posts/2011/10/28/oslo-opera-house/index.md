---
title: Oslo Opera House
date: '2011-10-28T07:39:15+00:00'
format: image
service: flickr
tags:
- norway
- operahouse
- Oslo
image: http://i1.wp.com/dentedreality.com.au/wp-content/uploads/2011/10/6812166338_3516319d9e_o.jpg?resize=607%2C452
---

[![Oslo Opera House](http://i1.wp.com/dentedreality.com.au/wp-content/uploads/2011/10/6812166338_3516319d9e_o.jpg?resize=607%2C452)](http://dentedreality.com.au/2011/10/28/oslo-opera-house/) 
# [Oslo Opera House](http://dentedreality.com.au/2011/10/28/oslo-opera-house/)

Super cool building that looked like it was a submarine or something from the future.





* #[norway](http://dentedreality.com.au/tags/norway/)
* #[operahouse](http://dentedreality.com.au/tags/operahouse/)
* #[Oslo](http://dentedreality.com.au/tags/oslo/)

Posted on [Flickr](http://www.flickr.com/photos/borkazoid/6812166338/) [7:39 am, October 28, 2011](http://dentedreality.com.au/2011/10/28/oslo-opera-house/ "7:39 am") 
jQuery(document).ready(function(){
var gmap\_mda628233555552057707802a4311c3df = {
positions : {
287 : new google.maps.LatLng( '59.911333', '10.753833' )
},
bounds : new google.maps.LatLngBounds(), // empty for now, we'll dynamically extend it later
map : new google.maps.Map(
document.getElementById( 'gmap\_mda628233555552057707802a4311c3df' ),
{
mapTypeId: google.maps.MapTypeId.ROADMAP,
center: new google.maps.LatLng( 0, 0 ),
zoom: 16 // Seems to be a good zoom for a single point
}
),
markers : {},
}; // end of gmap
// Extend the bounds of interest based on our positions
for ( var m in gmap\_mda628233555552057707802a4311c3df.positions ) {
gmap\_mda628233555552057707802a4311c3df.bounds.extend( gmap\_mda628233555552057707802a4311c3df.positions[m] );
}
// Render markers
for ( var m in gmap\_mda628233555552057707802a4311c3df.positions ) {
gmap\_mda628233555552057707802a4311c3df.markers[m] = new google.maps.Marker( {
clickable: true,
map : gmap\_mda628233555552057707802a4311c3df.map,
position : gmap\_mda628233555552057707802a4311c3df.positions[m]
} );
}
// Redraw map to fit our new marker-based bounds
gmap\_mda628233555552057707802a4311c3df.map.setCenter( gmap\_mda628233555552057707802a4311c3df.positions[287] );
});