---
title: More Roos Near Karma Chalets
date: '2008-04-06T13:34:06+00:00'
format: image
service: flickr
tags:
- australia
- kangaroos
- renniewedding
- roos
- timswedding
- westernaustraliadenmark
image: http://i2.wp.com/dentedreality.com.au/wp-content/uploads/2008/04/2433441828_c30f63786e_o.jpg?resize=607%2C455
---

[![More Roos Near Karma Chalets](http://i2.wp.com/dentedreality.com.au/wp-content/uploads/2008/04/2433441828_c30f63786e_o.jpg?resize=607%2C455)](http://dentedreality.com.au/2008/04/06/more-roos-near-karma-chalets/) 
# [More Roos Near Karma Chalets](http://dentedreality.com.au/2008/04/06/more-roos-near-karma-chalets/)





* #[australia](http://dentedreality.com.au/tags/australia/)
* #[kangaroos](http://dentedreality.com.au/tags/kangaroos/)
* #[renniewedding](http://dentedreality.com.au/tags/renniewedding/)
* #[roos](http://dentedreality.com.au/tags/roos/)
* #[timswedding](http://dentedreality.com.au/tags/timswedding/)
* #[westernaustraliadenmark](http://dentedreality.com.au/tags/westernaustraliadenmark/)

Posted on [Flickr](http://www.flickr.com/photos/borkazoid/2433441828/) [1:34 pm, April 6, 2008](http://dentedreality.com.au/2008/04/06/more-roos-near-karma-chalets/ "1:34 pm") 
jQuery(document).ready(function(){
var gmap\_m974fcb8f514174d25a044f92dd333c66 = {
positions : {
439 : new google.maps.LatLng( '-34.983877', '117.298278' )
},
bounds : new google.maps.LatLngBounds(), // empty for now, we'll dynamically extend it later
map : new google.maps.Map(
document.getElementById( 'gmap\_m974fcb8f514174d25a044f92dd333c66' ),
{
mapTypeId: google.maps.MapTypeId.ROADMAP,
center: new google.maps.LatLng( 0, 0 ),
zoom: 16 // Seems to be a good zoom for a single point
}
),
markers : {},
}; // end of gmap
// Extend the bounds of interest based on our positions
for ( var m in gmap\_m974fcb8f514174d25a044f92dd333c66.positions ) {
gmap\_m974fcb8f514174d25a044f92dd333c66.bounds.extend( gmap\_m974fcb8f514174d25a044f92dd333c66.positions[m] );
}
// Render markers
for ( var m in gmap\_m974fcb8f514174d25a044f92dd333c66.positions ) {
gmap\_m974fcb8f514174d25a044f92dd333c66.markers[m] = new google.maps.Marker( {
clickable: true,
map : gmap\_m974fcb8f514174d25a044f92dd333c66.map,
position : gmap\_m974fcb8f514174d25a044f92dd333c66.positions[m]
} );
}
// Redraw map to fit our new marker-based bounds
gmap\_m974fcb8f514174d25a044f92dd333c66.map.setCenter( gmap\_m974fcb8f514174d25a044f92dd333c66.positions[439] );
});