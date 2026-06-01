---
title: ''
date: '2019-05-27T18:19:03-06:00'
format: image
service: instagram
tags:
- kayak
- lake
- memorialday
- river
- Seattle
latitude: '47.65161'
longitude: '-122.31441'
image: https://i1.wp.com/s3.amazonaws.com/dentedreality-content/wp-content/uploads/2019/05/27192512/60909995_885704388430030_5040881531330097752_n.jpg?fit=640%2C640&ssl=1
---

[![Solid afternoon paddle. Nice work Seattle! #kayak #lake #river #seattle #memorialday](https://i1.wp.com/s3.amazonaws.com/dentedreality-content/wp-content/uploads/2019/05/27192512/60909995_885704388430030_5040881531330097752_n.jpg?fit=640%2C640&ssl=1)](https://dentedreality.com.au/2019/05/27/solid-afternoon-paddle-nice-work-seattle-kayak-lake-river-seattle-memorialday/) 

[![Solid afternoon paddle. Nice work Seattle! #kayak #lake #river #seattle #memorialday](https://i1.wp.com/s3.amazonaws.com/dentedreality-content/wp-content/uploads/2019/05/27192512/60909995_885704388430030_5040881531330097752_n.jpg?fit=640%2C640&ssl=1)](https://www.instagram.com/p/Bx_F_UKJAIr/)

Solid afternoon paddle. Nice work Seattle! #kayak #lake #river #seattle #memorialday

47.65161-122.31441




* #[kayak](https://dentedreality.com.au/tags/kayak/)
* #[lake](https://dentedreality.com.au/tags/lake/)
* #[memorialday](https://dentedreality.com.au/tags/memorialday/)
* #[river](https://dentedreality.com.au/tags/river/)
* #[Seattle](https://dentedreality.com.au/tags/seattle/)

Posted on [Instagram](https://www.instagram.com/p/Bx_F_UKJAIr/) [6:19 pm, May 27, 2019](https://dentedreality.com.au/2019/05/27/solid-afternoon-paddle-nice-work-seattle-kayak-lake-river-seattle-memorialday/ "6:19 pm") 
jQuery(document).ready(function(){
var gmap\_m0c8aadc2c38bca5a255b36f901bd27f9 = {
positions : {
556 : new google.maps.LatLng( '47.65161', '-122.31441' )
},
bounds : new google.maps.LatLngBounds(), // empty for now, we'll dynamically extend it later
map : new google.maps.Map(
document.getElementById( 'gmap\_m0c8aadc2c38bca5a255b36f901bd27f9' ),
{
mapTypeId: google.maps.MapTypeId.ROADMAP,
center: new google.maps.LatLng( 0, 0 ),
zoom: 16 // Seems to be a good zoom for a single point
}
),
markers : {},
}; // end of gmap
// Extend the bounds of interest based on our positions
for ( var m in gmap\_m0c8aadc2c38bca5a255b36f901bd27f9.positions ) {
gmap\_m0c8aadc2c38bca5a255b36f901bd27f9.bounds.extend( gmap\_m0c8aadc2c38bca5a255b36f901bd27f9.positions[m] );
}
// Render markers
for ( var m in gmap\_m0c8aadc2c38bca5a255b36f901bd27f9.positions ) {
gmap\_m0c8aadc2c38bca5a255b36f901bd27f9.markers[m] = new google.maps.Marker( {
clickable: true,
map : gmap\_m0c8aadc2c38bca5a255b36f901bd27f9.map,
position : gmap\_m0c8aadc2c38bca5a255b36f901bd27f9.positions[m]
} );
}
// Redraw map to fit our new marker-based bounds
gmap\_m0c8aadc2c38bca5a255b36f901bd27f9.map.setCenter( gmap\_m0c8aadc2c38bca5a255b36f901bd27f9.positions[556] );
});