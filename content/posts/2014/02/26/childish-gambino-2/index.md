---
title: Childish Gambino
date: '2014-02-26T15:51:10+00:00'
format: image
service: flickr
tags:
- childishgambino
- concert
- live
- music
- oakland
image: http://i1.wp.com/dentedreality.com.au/wp-content/uploads/2014/02/13926957395_58966d15cc_o.jpg?fit=1500%2C1500
---

[![Childish Gambino](http://i1.wp.com/dentedreality.com.au/wp-content/uploads/2014/02/13926957395_58966d15cc_o.jpg?fit=1500%2C1500)](http://dentedreality.com.au/2014/02/26/childish-gambino-2/) 
# [Childish Gambino](http://dentedreality.com.au/2014/02/26/childish-gambino-2/)

Private show at the Fox, in Oakland





* #[childishgambino](http://dentedreality.com.au/tags/childishgambino/)
* #[concert](http://dentedreality.com.au/tags/concert/)
* #[live](http://dentedreality.com.au/tags/live/)
* #[music](http://dentedreality.com.au/tags/music/)
* #[oakland](http://dentedreality.com.au/tags/oakland/)

Posted on [Flickr](http://www.flickr.com/photos/borkazoid/13926957395/) [3:51 pm, February 26, 2014](http://dentedreality.com.au/2014/02/26/childish-gambino-2/ "3:51 pm") 
jQuery(document).ready(function(){
var gmap\_mf4f971563d3682e58f20b71e1a905608 = {
positions : {
296 : new google.maps.LatLng( '37.808108', '-122.270767' )
},
bounds : new google.maps.LatLngBounds(), // empty for now, we'll dynamically extend it later
map : new google.maps.Map(
document.getElementById( 'gmap\_mf4f971563d3682e58f20b71e1a905608' ),
{
mapTypeId: google.maps.MapTypeId.ROADMAP,
center: new google.maps.LatLng( 0, 0 ),
zoom: 16 // Seems to be a good zoom for a single point
}
),
markers : {},
}; // end of gmap
// Extend the bounds of interest based on our positions
for ( var m in gmap\_mf4f971563d3682e58f20b71e1a905608.positions ) {
gmap\_mf4f971563d3682e58f20b71e1a905608.bounds.extend( gmap\_mf4f971563d3682e58f20b71e1a905608.positions[m] );
}
// Render markers
for ( var m in gmap\_mf4f971563d3682e58f20b71e1a905608.positions ) {
gmap\_mf4f971563d3682e58f20b71e1a905608.markers[m] = new google.maps.Marker( {
clickable: true,
map : gmap\_mf4f971563d3682e58f20b71e1a905608.map,
position : gmap\_mf4f971563d3682e58f20b71e1a905608.positions[m]
} );
}
// Redraw map to fit our new marker-based bounds
gmap\_mf4f971563d3682e58f20b71e1a905608.map.setCenter( gmap\_mf4f971563d3682e58f20b71e1a905608.positions[296] );
});