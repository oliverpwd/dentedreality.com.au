---
title: Childish Gambino
date: '2014-02-26T15:18:46+00:00'
format: image
service: flickr
tags:
- childishgambino
- concert
- live
- music
- oakland
image: http://i0.wp.com/dentedreality.com.au/wp-content/uploads/2014/02/13927008063_0ccaebc2a1_o.jpg?fit=1500%2C1500
---

[![Childish Gambino](http://i0.wp.com/dentedreality.com.au/wp-content/uploads/2014/02/13927008063_0ccaebc2a1_o.jpg?fit=1500%2C1500)](http://dentedreality.com.au/2014/02/26/childish-gambino-6/) 
# [Childish Gambino](http://dentedreality.com.au/2014/02/26/childish-gambino-6/)

Private show at the Fox, in Oakland





* #[childishgambino](http://dentedreality.com.au/tags/childishgambino/)
* #[concert](http://dentedreality.com.au/tags/concert/)
* #[live](http://dentedreality.com.au/tags/live/)
* #[music](http://dentedreality.com.au/tags/music/)
* #[oakland](http://dentedreality.com.au/tags/oakland/)

Posted on [Flickr](http://www.flickr.com/photos/borkazoid/13927008063/) [3:18 pm, February 26, 2014](http://dentedreality.com.au/2014/02/26/childish-gambino-6/ "3:18 pm") 
jQuery(document).ready(function(){
var gmap\_m77f06edabd2e1609d65586f36c4ac869 = {
positions : {
716 : new google.maps.LatLng( '37.808227', '-122.270578' )
},
bounds : new google.maps.LatLngBounds(), // empty for now, we'll dynamically extend it later
map : new google.maps.Map(
document.getElementById( 'gmap\_m77f06edabd2e1609d65586f36c4ac869' ),
{
mapTypeId: google.maps.MapTypeId.ROADMAP,
center: new google.maps.LatLng( 0, 0 ),
zoom: 16 // Seems to be a good zoom for a single point
}
),
markers : {},
}; // end of gmap
// Extend the bounds of interest based on our positions
for ( var m in gmap\_m77f06edabd2e1609d65586f36c4ac869.positions ) {
gmap\_m77f06edabd2e1609d65586f36c4ac869.bounds.extend( gmap\_m77f06edabd2e1609d65586f36c4ac869.positions[m] );
}
// Render markers
for ( var m in gmap\_m77f06edabd2e1609d65586f36c4ac869.positions ) {
gmap\_m77f06edabd2e1609d65586f36c4ac869.markers[m] = new google.maps.Marker( {
clickable: true,
map : gmap\_m77f06edabd2e1609d65586f36c4ac869.map,
position : gmap\_m77f06edabd2e1609d65586f36c4ac869.positions[m]
} );
}
// Redraw map to fit our new marker-based bounds
gmap\_m77f06edabd2e1609d65586f36c4ac869.map.setCenter( gmap\_m77f06edabd2e1609d65586f36c4ac869.positions[716] );
});