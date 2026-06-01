---
title: Meat!
date: '2011-02-07T16:50:12-07:00'
format: image
service: flickr
tags:
- '4505'
- 4505meats
- butchery
- lamb
- meat
latitude: '37.778333'
longitude: '-122.425834'
image: https://dentedreality-content.s3.amazonaws.com/wp-content/uploads/2011/02/14190129/5802614202_3c23e83870_o.jpg
---

[![Meat!](https://dentedreality-content.s3.amazonaws.com/wp-content/uploads/2011/02/14190129/5802614202_3c23e83870_o.jpg)](https://dentedreality.com.au/2011/02/07/meat-2/) 
# [Meat!](https://dentedreality.com.au/2011/02/07/meat-2/)

[![Meat!](https://dentedreality-content.s3.amazonaws.com/wp-content/uploads/2011/02/14190129/5802614202_3c23e83870_o.jpg)](http://www.flickr.com/photos/borkazoid/5802614202/)

Butchering a lamb with 4505 Meats

37.778333-122.425834




* #[4505](https://dentedreality.com.au/tags/4505/)
* #[4505meats](https://dentedreality.com.au/tags/4505meats/)
* #[butchery](https://dentedreality.com.au/tags/butchery/)
* #[lamb](https://dentedreality.com.au/tags/lamb/)
* #[meat](https://dentedreality.com.au/tags/meat/)

Posted on [Flickr](http://www.flickr.com/photos/borkazoid/5802614202/) [4:50 pm, February 7, 2011](https://dentedreality.com.au/2011/02/07/meat-2/ "4:50 pm") 
jQuery(document).ready(function(){
var gmap\_mc7a4d1755a345d143208da2ce8b7ef92 = {
positions : {
656 : new google.maps.LatLng( '37.778333', '-122.425834' )
},
bounds : new google.maps.LatLngBounds(), // empty for now, we'll dynamically extend it later
map : new google.maps.Map(
document.getElementById( 'gmap\_mc7a4d1755a345d143208da2ce8b7ef92' ),
{
mapTypeId: google.maps.MapTypeId.ROADMAP,
center: new google.maps.LatLng( 0, 0 ),
zoom: 16 // Seems to be a good zoom for a single point
}
),
markers : {},
}; // end of gmap
// Extend the bounds of interest based on our positions
for ( var m in gmap\_mc7a4d1755a345d143208da2ce8b7ef92.positions ) {
gmap\_mc7a4d1755a345d143208da2ce8b7ef92.bounds.extend( gmap\_mc7a4d1755a345d143208da2ce8b7ef92.positions[m] );
}
// Render markers
for ( var m in gmap\_mc7a4d1755a345d143208da2ce8b7ef92.positions ) {
gmap\_mc7a4d1755a345d143208da2ce8b7ef92.markers[m] = new google.maps.Marker( {
clickable: true,
map : gmap\_mc7a4d1755a345d143208da2ce8b7ef92.map,
position : gmap\_mc7a4d1755a345d143208da2ce8b7ef92.positions[m]
} );
}
// Redraw map to fit our new marker-based bounds
gmap\_mc7a4d1755a345d143208da2ce8b7ef92.map.setCenter( gmap\_mc7a4d1755a345d143208da2ce8b7ef92.positions[656] );
});