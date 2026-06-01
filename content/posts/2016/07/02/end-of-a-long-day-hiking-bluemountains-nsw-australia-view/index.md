---
title: ''
date: '2016-07-02T06:14:10+00:00'
format: image
service: instagram
tags:
- australia
- bluemountains
- hiking
- nsw
- view
image: http://i0.wp.com/dentedreality.com.au/wp-content/uploads/2016/07/13532084_1061165973966676_628885740_n.jpg?fit=640%2C640
---

[![End of a long day. #hiking #bluemountains #nsw #australia #view](http://i0.wp.com/dentedreality.com.au/wp-content/uploads/2016/07/13532084_1061165973966676_628885740_n.jpg?fit=640%2C640)](http://dentedreality.com.au/2016/07/02/end-of-a-long-day-hiking-bluemountains-nsw-australia-view/) 

End of a long day. #hiking #bluemountains #nsw #australia #view





* #[australia](http://dentedreality.com.au/tags/australia/)
* #[bluemountains](http://dentedreality.com.au/tags/bluemountains/)
* #[hiking](http://dentedreality.com.au/tags/hiking/)
* #[nsw](http://dentedreality.com.au/tags/nsw/)
* #[view](http://dentedreality.com.au/tags/view/)

Posted on [Instagram](https://www.instagram.com/p/BHW9Nkfgw-v/) [6:14 am, July 2, 2016](http://dentedreality.com.au/2016/07/02/end-of-a-long-day-hiking-bluemountains-nsw-australia-view/ "6:14 am") 
jQuery(document).ready(function(){
var gmap\_m581026776c00e546cc016e8a507643ae = {
positions : {
810 : new google.maps.LatLng( '-33.724994145', '150.33186776954' )
},
bounds : new google.maps.LatLngBounds(), // empty for now, we'll dynamically extend it later
map : new google.maps.Map(
document.getElementById( 'gmap\_m581026776c00e546cc016e8a507643ae' ),
{
mapTypeId: google.maps.MapTypeId.ROADMAP,
center: new google.maps.LatLng( 0, 0 ),
zoom: 16 // Seems to be a good zoom for a single point
}
),
markers : {},
}; // end of gmap
// Extend the bounds of interest based on our positions
for ( var m in gmap\_m581026776c00e546cc016e8a507643ae.positions ) {
gmap\_m581026776c00e546cc016e8a507643ae.bounds.extend( gmap\_m581026776c00e546cc016e8a507643ae.positions[m] );
}
// Render markers
for ( var m in gmap\_m581026776c00e546cc016e8a507643ae.positions ) {
gmap\_m581026776c00e546cc016e8a507643ae.markers[m] = new google.maps.Marker( {
clickable: true,
map : gmap\_m581026776c00e546cc016e8a507643ae.map,
position : gmap\_m581026776c00e546cc016e8a507643ae.positions[m]
} );
}
// Redraw map to fit our new marker-based bounds
gmap\_m581026776c00e546cc016e8a507643ae.map.setCenter( gmap\_m581026776c00e546cc016e8a507643ae.positions[810] );
});