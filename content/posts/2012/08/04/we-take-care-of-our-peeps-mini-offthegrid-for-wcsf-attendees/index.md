---
title: ''
date: '2012-08-04T21:54:03+00:00'
format: image
service: instagram
tags:
- photo
- wcsf
image: http://i2.wp.com/dentedreality.com.au/wp-content/uploads/2012/08/6f18dc0cdea011e19cc822000a1e8867_7.jpg?resize=607%2C607
---

[![We take care of our peeps! Mini @OffTheGrid for #wcsf attendees](http://i2.wp.com/dentedreality.com.au/wp-content/uploads/2012/08/6f18dc0cdea011e19cc822000a1e8867_7.jpg?resize=607%2C607)](http://dentedreality.com.au/2012/08/04/we-take-care-of-our-peeps-mini-offthegrid-for-wcsf-attendees/) 

We take care of our peeps! Mini @OffTheGrid for #wcsf attendees





* #[photo](http://dentedreality.com.au/tags/photo/)
* #[wcsf](http://dentedreality.com.au/tags/wcsf/)

Posted on [Instagram](http://instagram.com/p/N7b5DaimHK/) [9:54 pm, August 4, 2012](http://dentedreality.com.au/2012/08/04/we-take-care-of-our-peeps-mini-offthegrid-for-wcsf-attendees/ "9:54 pm") 
jQuery(document).ready(function(){
var gmap\_m5f45e6c91d6fe360110e041c2f711c22 = {
positions : {
470 : new google.maps.LatLng( '37.766703027', '-122.402832559' )
},
bounds : new google.maps.LatLngBounds(), // empty for now, we'll dynamically extend it later
map : new google.maps.Map(
document.getElementById( 'gmap\_m5f45e6c91d6fe360110e041c2f711c22' ),
{
mapTypeId: google.maps.MapTypeId.ROADMAP,
center: new google.maps.LatLng( 0, 0 ),
zoom: 16 // Seems to be a good zoom for a single point
}
),
markers : {},
}; // end of gmap
// Extend the bounds of interest based on our positions
for ( var m in gmap\_m5f45e6c91d6fe360110e041c2f711c22.positions ) {
gmap\_m5f45e6c91d6fe360110e041c2f711c22.bounds.extend( gmap\_m5f45e6c91d6fe360110e041c2f711c22.positions[m] );
}
// Render markers
for ( var m in gmap\_m5f45e6c91d6fe360110e041c2f711c22.positions ) {
gmap\_m5f45e6c91d6fe360110e041c2f711c22.markers[m] = new google.maps.Marker( {
clickable: true,
map : gmap\_m5f45e6c91d6fe360110e041c2f711c22.map,
position : gmap\_m5f45e6c91d6fe360110e041c2f711c22.positions[m]
} );
}
// Redraw map to fit our new marker-based bounds
gmap\_m5f45e6c91d6fe360110e041c2f711c22.map.setCenter( gmap\_m5f45e6c91d6fe360110e041c2f711c22.positions[470] );
});