---
title: Denver Meetup
date: '2013-11-21T05:43:45+00:00'
format: image
service: flickr
tags:
- automattic
- colorado
- Denver
- meetup
- mercury
- vision:outdoor=0754
image: http://i0.wp.com/dentedreality.com.au/wp-content/uploads/2013/11/12291553784_f73222f44e_o.jpg?resize=607%2C455
---

[![Denver Meetup](http://i0.wp.com/dentedreality.com.au/wp-content/uploads/2013/11/12291553784_f73222f44e_o.jpg?resize=607%2C455)](http://dentedreality.com.au/2013/11/21/denver-meetup-5/) 
# [Denver Meetup](http://dentedreality.com.au/2013/11/21/denver-meetup-5/)

Team Mercury meetup (and a few days after) in Denver, Colorado.





* #[automattic](http://dentedreality.com.au/tags/automattic/)
* #[colorado](http://dentedreality.com.au/tags/colorado/)
* #[Denver](http://dentedreality.com.au/tags/denver/)
* #[meetup](http://dentedreality.com.au/tags/meetup/)
* #[mercury](http://dentedreality.com.au/tags/mercury/)
* #[vision:outdoor=0754](http://dentedreality.com.au/tags/visionoutdoor0754/)

Posted on [Flickr](http://www.flickr.com/photos/borkazoid/12291553784/) [5:43 am, November 21, 2013](http://dentedreality.com.au/2013/11/21/denver-meetup-5/ "5:43 am") 
jQuery(document).ready(function(){
var gmap\_m7dbac03ba58994873f397019e9243eb8 = {
positions : {
718 : new google.maps.LatLng( '39.736813', '-104.979859' )
},
bounds : new google.maps.LatLngBounds(), // empty for now, we'll dynamically extend it later
map : new google.maps.Map(
document.getElementById( 'gmap\_m7dbac03ba58994873f397019e9243eb8' ),
{
mapTypeId: google.maps.MapTypeId.ROADMAP,
center: new google.maps.LatLng( 0, 0 ),
zoom: 16 // Seems to be a good zoom for a single point
}
),
markers : {},
}; // end of gmap
// Extend the bounds of interest based on our positions
for ( var m in gmap\_m7dbac03ba58994873f397019e9243eb8.positions ) {
gmap\_m7dbac03ba58994873f397019e9243eb8.bounds.extend( gmap\_m7dbac03ba58994873f397019e9243eb8.positions[m] );
}
// Render markers
for ( var m in gmap\_m7dbac03ba58994873f397019e9243eb8.positions ) {
gmap\_m7dbac03ba58994873f397019e9243eb8.markers[m] = new google.maps.Marker( {
clickable: true,
map : gmap\_m7dbac03ba58994873f397019e9243eb8.map,
position : gmap\_m7dbac03ba58994873f397019e9243eb8.positions[m]
} );
}
// Redraw map to fit our new marker-based bounds
gmap\_m7dbac03ba58994873f397019e9243eb8.map.setCenter( gmap\_m7dbac03ba58994873f397019e9243eb8.positions[718] );
});