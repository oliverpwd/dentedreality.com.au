---
title: ''
date: '2016-08-09T23:20:56+00:00'
format: image
service: instagram
tags:
- colorado
- telluride
image: http://i1.wp.com/dentedreality.com.au/wp-content/uploads/2016/08/13707355_1800699906826908_1764830866_n.jpg?fit=640%2C640
---

[![Tiny Town. Telluride. From there gondola. #colorado #telluride](http://i1.wp.com/dentedreality.com.au/wp-content/uploads/2016/08/13707355_1800699906826908_1764830866_n.jpg?fit=640%2C640)](http://dentedreality.com.au/2016/08/09/tiny-town-telluride-from-there-gondola-colorado-telluride/) 

Tiny Town. Telluride. From there gondola. #colorado #telluride





* #[colorado](http://dentedreality.com.au/tags/colorado/)
* #[telluride](http://dentedreality.com.au/tags/telluride/)

Posted on [Instagram](https://www.instagram.com/p/BI6o7BygaWr/) [11:20 pm, August 9, 2016](http://dentedreality.com.au/2016/08/09/tiny-town-telluride-from-there-gondola-colorado-telluride/ "11:20 pm") 
jQuery(document).ready(function(){
var gmap\_mc64b7452dcaff394b0b76e74068c98d6 = {
positions : {
299 : new google.maps.LatLng( '37.931484449123', '-107.83290200467' )
},
bounds : new google.maps.LatLngBounds(), // empty for now, we'll dynamically extend it later
map : new google.maps.Map(
document.getElementById( 'gmap\_mc64b7452dcaff394b0b76e74068c98d6' ),
{
mapTypeId: google.maps.MapTypeId.ROADMAP,
center: new google.maps.LatLng( 0, 0 ),
zoom: 16 // Seems to be a good zoom for a single point
}
),
markers : {},
}; // end of gmap
// Extend the bounds of interest based on our positions
for ( var m in gmap\_mc64b7452dcaff394b0b76e74068c98d6.positions ) {
gmap\_mc64b7452dcaff394b0b76e74068c98d6.bounds.extend( gmap\_mc64b7452dcaff394b0b76e74068c98d6.positions[m] );
}
// Render markers
for ( var m in gmap\_mc64b7452dcaff394b0b76e74068c98d6.positions ) {
gmap\_mc64b7452dcaff394b0b76e74068c98d6.markers[m] = new google.maps.Marker( {
clickable: true,
map : gmap\_mc64b7452dcaff394b0b76e74068c98d6.map,
position : gmap\_mc64b7452dcaff394b0b76e74068c98d6.positions[m]
} );
}
// Redraw map to fit our new marker-based bounds
gmap\_mc64b7452dcaff394b0b76e74068c98d6.map.setCenter( gmap\_mc64b7452dcaff394b0b76e74068c98d6.positions[299] );
});