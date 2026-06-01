---
title: ''
date: '2015-08-29T16:41:34+00:00'
format: image
service: instagram
image: http://i2.wp.com/dentedreality.com.au/wp-content/uploads/2015/08/11821190_851274578254408_339467755_n.jpg?resize=640%2C640
---

[![Almighty Cheesus.](http://i2.wp.com/dentedreality.com.au/wp-content/uploads/2015/08/11821190_851274578254408_339467755_n.jpg?resize=640%2C640)](http://dentedreality.com.au/2015/08/29/almighty-cheesus/) 

Almighty Cheesus.





Posted on [Instagram](https://instagram.com/p/6_ALLDCmCh/) [4:41 pm, August 29, 2015](http://dentedreality.com.au/2015/08/29/almighty-cheesus/ "4:41 pm") 
jQuery(document).ready(function(){
var gmap\_m0360e5777624d15dd427b364949fa0df = {
positions : {
861 : new google.maps.LatLng( '43.667932333', '-70.280268848' )
},
bounds : new google.maps.LatLngBounds(), // empty for now, we'll dynamically extend it later
map : new google.maps.Map(
document.getElementById( 'gmap\_m0360e5777624d15dd427b364949fa0df' ),
{
mapTypeId: google.maps.MapTypeId.ROADMAP,
center: new google.maps.LatLng( 0, 0 ),
zoom: 16 // Seems to be a good zoom for a single point
}
),
markers : {},
}; // end of gmap
// Extend the bounds of interest based on our positions
for ( var m in gmap\_m0360e5777624d15dd427b364949fa0df.positions ) {
gmap\_m0360e5777624d15dd427b364949fa0df.bounds.extend( gmap\_m0360e5777624d15dd427b364949fa0df.positions[m] );
}
// Render markers
for ( var m in gmap\_m0360e5777624d15dd427b364949fa0df.positions ) {
gmap\_m0360e5777624d15dd427b364949fa0df.markers[m] = new google.maps.Marker( {
clickable: true,
map : gmap\_m0360e5777624d15dd427b364949fa0df.map,
position : gmap\_m0360e5777624d15dd427b364949fa0df.positions[m]
} );
}
// Redraw map to fit our new marker-based bounds
gmap\_m0360e5777624d15dd427b364949fa0df.map.setCenter( gmap\_m0360e5777624d15dd427b364949fa0df.positions[861] );
});