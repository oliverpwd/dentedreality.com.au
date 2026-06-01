---
title: Childish Gambino
date: '2014-02-26T16:35:43+00:00'
format: image
service: flickr
tags:
- childishgambino
- concert
- live
- music
- oakland
image: http://i2.wp.com/dentedreality.com.au/wp-content/uploads/2014/02/13927401654_c673e11672_o.jpg?fit=1500%2C1500
---

[![Childish Gambino](http://i2.wp.com/dentedreality.com.au/wp-content/uploads/2014/02/13927401654_c673e11672_o.jpg?fit=1500%2C1500)](http://dentedreality.com.au/2014/02/26/childish-gambino/) 
# [Childish Gambino](http://dentedreality.com.au/2014/02/26/childish-gambino/)

Private show at the Fox, in Oakland





* #[childishgambino](http://dentedreality.com.au/tags/childishgambino/)
* #[concert](http://dentedreality.com.au/tags/concert/)
* #[live](http://dentedreality.com.au/tags/live/)
* #[music](http://dentedreality.com.au/tags/music/)
* #[oakland](http://dentedreality.com.au/tags/oakland/)

Posted on [Flickr](http://www.flickr.com/photos/borkazoid/13927401654/) [4:35 pm, February 26, 2014](http://dentedreality.com.au/2014/02/26/childish-gambino/ "4:35 pm") 
jQuery(document).ready(function(){
var gmap\_m7778277b5b31aa31ed187eee0a12f8d9 = {
positions : {
524 : new google.maps.LatLng( '37.808033', '-122.270759' )
},
bounds : new google.maps.LatLngBounds(), // empty for now, we'll dynamically extend it later
map : new google.maps.Map(
document.getElementById( 'gmap\_m7778277b5b31aa31ed187eee0a12f8d9' ),
{
mapTypeId: google.maps.MapTypeId.ROADMAP,
center: new google.maps.LatLng( 0, 0 ),
zoom: 16 // Seems to be a good zoom for a single point
}
),
markers : {},
}; // end of gmap
// Extend the bounds of interest based on our positions
for ( var m in gmap\_m7778277b5b31aa31ed187eee0a12f8d9.positions ) {
gmap\_m7778277b5b31aa31ed187eee0a12f8d9.bounds.extend( gmap\_m7778277b5b31aa31ed187eee0a12f8d9.positions[m] );
}
// Render markers
for ( var m in gmap\_m7778277b5b31aa31ed187eee0a12f8d9.positions ) {
gmap\_m7778277b5b31aa31ed187eee0a12f8d9.markers[m] = new google.maps.Marker( {
clickable: true,
map : gmap\_m7778277b5b31aa31ed187eee0a12f8d9.map,
position : gmap\_m7778277b5b31aa31ed187eee0a12f8d9.positions[m]
} );
}
// Redraw map to fit our new marker-based bounds
gmap\_m7778277b5b31aa31ed187eee0a12f8d9.map.setCenter( gmap\_m7778277b5b31aa31ed187eee0a12f8d9.positions[524] );
});