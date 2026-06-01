---
title: Snow in Prospect Park
date: '2014-01-04T09:51:51+00:00'
format: image
service: flickr
tags:
- brooklyn
- newyork
- prospectpark
- snow
image: http://i0.wp.com/dentedreality.com.au/wp-content/uploads/2014/01/13901646892_4d70fc2238_o.jpg?resize=607%2C455
---

[![Snow in Prospect Park](http://i0.wp.com/dentedreality.com.au/wp-content/uploads/2014/01/13901646892_4d70fc2238_o.jpg?resize=607%2C455)](http://dentedreality.com.au/2014/01/04/snow-in-prospect-park/) 
# [Snow in Prospect Park](http://dentedreality.com.au/2014/01/04/snow-in-prospect-park/)





* #[brooklyn](http://dentedreality.com.au/tags/brooklyn/)
* #[newyork](http://dentedreality.com.au/tags/newyork/)
* #[prospectpark](http://dentedreality.com.au/tags/prospectpark/)
* #[snow](http://dentedreality.com.au/tags/snow/)

Posted on [Flickr](http://www.flickr.com/photos/borkazoid/13901646892/) [9:51 am, January 4, 2014](http://dentedreality.com.au/2014/01/04/snow-in-prospect-park/ "9:51 am") 
jQuery(document).ready(function(){
var gmap\_m17990de4243e9a640ef3eb998df2e9bb = {
positions : {
392 : new google.maps.LatLng( '40.669752', '-73.969987' )
},
bounds : new google.maps.LatLngBounds(), // empty for now, we'll dynamically extend it later
map : new google.maps.Map(
document.getElementById( 'gmap\_m17990de4243e9a640ef3eb998df2e9bb' ),
{
mapTypeId: google.maps.MapTypeId.ROADMAP,
center: new google.maps.LatLng( 0, 0 ),
zoom: 16 // Seems to be a good zoom for a single point
}
),
markers : {},
}; // end of gmap
// Extend the bounds of interest based on our positions
for ( var m in gmap\_m17990de4243e9a640ef3eb998df2e9bb.positions ) {
gmap\_m17990de4243e9a640ef3eb998df2e9bb.bounds.extend( gmap\_m17990de4243e9a640ef3eb998df2e9bb.positions[m] );
}
// Render markers
for ( var m in gmap\_m17990de4243e9a640ef3eb998df2e9bb.positions ) {
gmap\_m17990de4243e9a640ef3eb998df2e9bb.markers[m] = new google.maps.Marker( {
clickable: true,
map : gmap\_m17990de4243e9a640ef3eb998df2e9bb.map,
position : gmap\_m17990de4243e9a640ef3eb998df2e9bb.positions[m]
} );
}
// Redraw map to fit our new marker-based bounds
gmap\_m17990de4243e9a640ef3eb998df2e9bb.map.setCenter( gmap\_m17990de4243e9a640ef3eb998df2e9bb.positions[392] );
});