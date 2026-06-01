---
title: '100_1617'
date: '2008-04-05T02:55:00-06:00'
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
image: https://dentedreality-content.s3.amazonaws.com/wp-content/uploads/2008/04/14184652/2433433098_9a9e7f614f_o.jpg
---

[![100_1617](https://dentedreality-content.s3.amazonaws.com/wp-content/uploads/2008/04/14184652/2433433098_9a9e7f614f_o.jpg)](https://dentedreality.com.au/2008/04/05/100_1617/) 
# [100\_1617](https://dentedreality.com.au/2008/04/05/100_1617/)

[![100_1617](https://dentedreality-content.s3.amazonaws.com/wp-content/uploads/2008/04/14184652/2433433098_9a9e7f614f_o.jpg)](http://www.flickr.com/photos/borkazoid/2433433098/)

-34.983877117.298278




* #[australia](https://dentedreality.com.au/tags/australia/)
* #[beau](https://dentedreality.com.au/tags/beau/)
* #[beaulebens](https://dentedreality.com.au/tags/beaulebens/)
* #[foresthillwinery](https://dentedreality.com.au/tags/foresthillwinery/)
* #[me](https://dentedreality.com.au/tags/me/)
* #[renniewedding](https://dentedreality.com.au/tags/renniewedding/)
* #[timswedding](https://dentedreality.com.au/tags/timswedding/)
* #[westernaustraliadenmark](https://dentedreality.com.au/tags/westernaustraliadenmark/)

Posted on [Flickr](http://www.flickr.com/photos/borkazoid/2433433098/) [2:55 am, April 5, 2008](https://dentedreality.com.au/2008/04/05/100_1617/ "2:55 am") 
jQuery(document).ready(function(){
var gmap\_m0326f132902c2a1f689fb7b24371f2e3 = {
positions : {
526 : new google.maps.LatLng( '-34.983877', '117.298278' )
},
bounds : new google.maps.LatLngBounds(), // empty for now, we'll dynamically extend it later
map : new google.maps.Map(
document.getElementById( 'gmap\_m0326f132902c2a1f689fb7b24371f2e3' ),
{
mapTypeId: google.maps.MapTypeId.ROADMAP,
center: new google.maps.LatLng( 0, 0 ),
zoom: 16 // Seems to be a good zoom for a single point
}
),
markers : {},
}; // end of gmap
// Extend the bounds of interest based on our positions
for ( var m in gmap\_m0326f132902c2a1f689fb7b24371f2e3.positions ) {
gmap\_m0326f132902c2a1f689fb7b24371f2e3.bounds.extend( gmap\_m0326f132902c2a1f689fb7b24371f2e3.positions[m] );
}
// Render markers
for ( var m in gmap\_m0326f132902c2a1f689fb7b24371f2e3.positions ) {
gmap\_m0326f132902c2a1f689fb7b24371f2e3.markers[m] = new google.maps.Marker( {
clickable: true,
map : gmap\_m0326f132902c2a1f689fb7b24371f2e3.map,
position : gmap\_m0326f132902c2a1f689fb7b24371f2e3.positions[m]
} );
}
// Redraw map to fit our new marker-based bounds
gmap\_m0326f132902c2a1f689fb7b24371f2e3.map.setCenter( gmap\_m0326f132902c2a1f689fb7b24371f2e3.positions[526] );
});