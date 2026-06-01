---
title: '100_1622'
date: '2008-04-05T02:58:15-06:00'
format: image
service: flickr
tags:
- australia
- beau
- beaulebens
- foresthillwinery
- me
- renniewedding
- timswedding
- westernaustraliadenmark
latitude: '-34.983877'
longitude: '117.298278'
image: https://dentedreality-content.s3.amazonaws.com/wp-content/uploads/2008/04/14184652/2432618009_2128165a5b_o.jpg
---

[![100_1622](https://dentedreality-content.s3.amazonaws.com/wp-content/uploads/2008/04/14184652/2432618009_2128165a5b_o.jpg)](https://dentedreality.com.au/2008/04/05/100_1622/) 
# [100\_1622](https://dentedreality.com.au/2008/04/05/100_1622/)

[![100_1622](https://dentedreality-content.s3.amazonaws.com/wp-content/uploads/2008/04/14184652/2432618009_2128165a5b_o.jpg)](http://www.flickr.com/photos/borkazoid/2432618009/)

-34.983877117.298278




* #[australia](https://dentedreality.com.au/tags/australia/)
* #[beau](https://dentedreality.com.au/tags/beau/)
* #[beaulebens](https://dentedreality.com.au/tags/beaulebens/)
* #[foresthillwinery](https://dentedreality.com.au/tags/foresthillwinery/)
* #[me](https://dentedreality.com.au/tags/me/)
* #[renniewedding](https://dentedreality.com.au/tags/renniewedding/)
* #[timswedding](https://dentedreality.com.au/tags/timswedding/)
* #[westernaustraliadenmark](https://dentedreality.com.au/tags/westernaustraliadenmark/)

Posted on [Flickr](http://www.flickr.com/photos/borkazoid/2432618009/) [2:58 am, April 5, 2008](https://dentedreality.com.au/2008/04/05/100_1622/ "2:58 am") 
jQuery(document).ready(function(){
var gmap\_mdba6f063bc222c8262b3cc2192cef8ba = {
positions : {
619 : new google.maps.LatLng( '-34.983877', '117.298278' )
},
bounds : new google.maps.LatLngBounds(), // empty for now, we'll dynamically extend it later
map : new google.maps.Map(
document.getElementById( 'gmap\_mdba6f063bc222c8262b3cc2192cef8ba' ),
{
mapTypeId: google.maps.MapTypeId.ROADMAP,
center: new google.maps.LatLng( 0, 0 ),
zoom: 16 // Seems to be a good zoom for a single point
}
),
markers : {},
}; // end of gmap
// Extend the bounds of interest based on our positions
for ( var m in gmap\_mdba6f063bc222c8262b3cc2192cef8ba.positions ) {
gmap\_mdba6f063bc222c8262b3cc2192cef8ba.bounds.extend( gmap\_mdba6f063bc222c8262b3cc2192cef8ba.positions[m] );
}
// Render markers
for ( var m in gmap\_mdba6f063bc222c8262b3cc2192cef8ba.positions ) {
gmap\_mdba6f063bc222c8262b3cc2192cef8ba.markers[m] = new google.maps.Marker( {
clickable: true,
map : gmap\_mdba6f063bc222c8262b3cc2192cef8ba.map,
position : gmap\_mdba6f063bc222c8262b3cc2192cef8ba.positions[m]
} );
}
// Redraw map to fit our new marker-based bounds
gmap\_mdba6f063bc222c8262b3cc2192cef8ba.map.setCenter( gmap\_mdba6f063bc222c8262b3cc2192cef8ba.positions[619] );
});