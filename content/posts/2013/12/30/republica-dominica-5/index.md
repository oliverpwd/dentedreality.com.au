---
title: Republica Dominica
date: '2013-12-30T11:14:20+00:00'
format: image
service: flickr
tags:
- beau
- beaulebens
- dominicanrepublic
- erika
- me
image: http://i1.wp.com/dentedreality.com.au/wp-content/uploads/2013/12/13901153692_f17d3e2369_o.jpg?fit=1500%2C1500
---

[![Republica Dominica](http://i1.wp.com/dentedreality.com.au/wp-content/uploads/2013/12/13901153692_f17d3e2369_o.jpg?fit=1500%2C1500)](http://dentedreality.com.au/2013/12/30/republica-dominica-5/) 
# [Republica Dominica](http://dentedreality.com.au/2013/12/30/republica-dominica-5/)





* #[beau](http://dentedreality.com.au/tags/beau/)
* #[beaulebens](http://dentedreality.com.au/tags/beaulebens/)
* #[dominicanrepublic](http://dentedreality.com.au/tags/dominicanrepublic/)
* #[erika](http://dentedreality.com.au/tags/erika/)
* #[me](http://dentedreality.com.au/tags/me/)

Posted on [Flickr](http://www.flickr.com/photos/borkazoid/13901153692/) [11:14 am, December 30, 2013](http://dentedreality.com.au/2013/12/30/republica-dominica-5/ "11:14 am") 
jQuery(document).ready(function(){
var gmap\_me9a14d14ff9fd85041b15546c76e8401 = {
positions : {
623 : new google.maps.LatLng( '19.093644', '-70.594248' )
},
bounds : new google.maps.LatLngBounds(), // empty for now, we'll dynamically extend it later
map : new google.maps.Map(
document.getElementById( 'gmap\_me9a14d14ff9fd85041b15546c76e8401' ),
{
mapTypeId: google.maps.MapTypeId.ROADMAP,
center: new google.maps.LatLng( 0, 0 ),
zoom: 16 // Seems to be a good zoom for a single point
}
),
markers : {},
}; // end of gmap
// Extend the bounds of interest based on our positions
for ( var m in gmap\_me9a14d14ff9fd85041b15546c76e8401.positions ) {
gmap\_me9a14d14ff9fd85041b15546c76e8401.bounds.extend( gmap\_me9a14d14ff9fd85041b15546c76e8401.positions[m] );
}
// Render markers
for ( var m in gmap\_me9a14d14ff9fd85041b15546c76e8401.positions ) {
gmap\_me9a14d14ff9fd85041b15546c76e8401.markers[m] = new google.maps.Marker( {
clickable: true,
map : gmap\_me9a14d14ff9fd85041b15546c76e8401.map,
position : gmap\_me9a14d14ff9fd85041b15546c76e8401.positions[m]
} );
}
// Redraw map to fit our new marker-based bounds
gmap\_me9a14d14ff9fd85041b15546c76e8401.map.setCenter( gmap\_me9a14d14ff9fd85041b15546c76e8401.positions[623] );
});