---
title: Capitalism is Over
date: '2011-09-09T18:38:04+00:00'
format: image
service: flickr
tags:
- art
- capitalism
- mission
image: http://i1.wp.com/dentedreality.com.au/wp-content/uploads/2011/09/6323523864_cdaf14c942_o.jpg?resize=607%2C813
---

[![Capitalism is Over](http://i1.wp.com/dentedreality.com.au/wp-content/uploads/2011/09/6323523864_cdaf14c942_o.jpg?resize=607%2C813)](http://dentedreality.com.au/2011/09/09/capitalism-is-over/) 
# [Capitalism is Over](http://dentedreality.com.au/2011/09/09/capitalism-is-over/)





* #[art](http://dentedreality.com.au/tags/art/)
* #[capitalism](http://dentedreality.com.au/tags/capitalism/)
* #[mission](http://dentedreality.com.au/tags/mission/)

Posted on [Flickr](http://www.flickr.com/photos/borkazoid/6323523864/) [6:38 pm, September 9, 2011](http://dentedreality.com.au/2011/09/09/capitalism-is-over/ "6:38 pm") 
jQuery(document).ready(function(){
var gmap\_m577c985bd36f14a0c0609a931b589aef = {
positions : {
882 : new google.maps.LatLng( '37.757', '-122.421' )
},
bounds : new google.maps.LatLngBounds(), // empty for now, we'll dynamically extend it later
map : new google.maps.Map(
document.getElementById( 'gmap\_m577c985bd36f14a0c0609a931b589aef' ),
{
mapTypeId: google.maps.MapTypeId.ROADMAP,
center: new google.maps.LatLng( 0, 0 ),
zoom: 16 // Seems to be a good zoom for a single point
}
),
markers : {},
}; // end of gmap
// Extend the bounds of interest based on our positions
for ( var m in gmap\_m577c985bd36f14a0c0609a931b589aef.positions ) {
gmap\_m577c985bd36f14a0c0609a931b589aef.bounds.extend( gmap\_m577c985bd36f14a0c0609a931b589aef.positions[m] );
}
// Render markers
for ( var m in gmap\_m577c985bd36f14a0c0609a931b589aef.positions ) {
gmap\_m577c985bd36f14a0c0609a931b589aef.markers[m] = new google.maps.Marker( {
clickable: true,
map : gmap\_m577c985bd36f14a0c0609a931b589aef.map,
position : gmap\_m577c985bd36f14a0c0609a931b589aef.positions[m]
} );
}
// Redraw map to fit our new marker-based bounds
gmap\_m577c985bd36f14a0c0609a931b589aef.map.setCenter( gmap\_m577c985bd36f14a0c0609a931b589aef.positions[882] );
});