---
title: Two Door Cinema Club
date: '2012-09-28T17:24:45+00:00'
format: image
service: flickr
tags:
- balloons
- centralpark
- concert
- livemusic
- music
- tdcc
- twodoorcinemaclub
image: http://i1.wp.com/dentedreality.com.au/wp-content/uploads/2012/09/8245862902_d5732cffcb_o.jpg?resize=607%2C452
---

[![Two Door Cinema Club](http://i1.wp.com/dentedreality.com.au/wp-content/uploads/2012/09/8245862902_d5732cffcb_o.jpg?resize=607%2C452)](http://dentedreality.com.au/2012/09/28/two-door-cinema-club/) 
# [Two Door Cinema Club](http://dentedreality.com.au/2012/09/28/two-door-cinema-club/)

Awesome show in Central Park





* #[balloons](http://dentedreality.com.au/tags/balloons/)
* #[centralpark](http://dentedreality.com.au/tags/centralpark/)
* #[concert](http://dentedreality.com.au/tags/concert/)
* #[livemusic](http://dentedreality.com.au/tags/livemusic/)
* #[music](http://dentedreality.com.au/tags/music/)
* #[tdcc](http://dentedreality.com.au/tags/tdcc/)
* #[twodoorcinemaclub](http://dentedreality.com.au/tags/twodoorcinemaclub/)

Posted on [Flickr](http://www.flickr.com/photos/borkazoid/8245862902/) [5:24 pm, September 28, 2012](http://dentedreality.com.au/2012/09/28/two-door-cinema-club/ "5:24 pm") 
jQuery(document).ready(function(){
var gmap\_md60da95d3fd2729916aa4012ceb6128a = {
positions : {
397 : new google.maps.LatLng( '40.772333', '-73.97' )
},
bounds : new google.maps.LatLngBounds(), // empty for now, we'll dynamically extend it later
map : new google.maps.Map(
document.getElementById( 'gmap\_md60da95d3fd2729916aa4012ceb6128a' ),
{
mapTypeId: google.maps.MapTypeId.ROADMAP,
center: new google.maps.LatLng( 0, 0 ),
zoom: 16 // Seems to be a good zoom for a single point
}
),
markers : {},
}; // end of gmap
// Extend the bounds of interest based on our positions
for ( var m in gmap\_md60da95d3fd2729916aa4012ceb6128a.positions ) {
gmap\_md60da95d3fd2729916aa4012ceb6128a.bounds.extend( gmap\_md60da95d3fd2729916aa4012ceb6128a.positions[m] );
}
// Render markers
for ( var m in gmap\_md60da95d3fd2729916aa4012ceb6128a.positions ) {
gmap\_md60da95d3fd2729916aa4012ceb6128a.markers[m] = new google.maps.Marker( {
clickable: true,
map : gmap\_md60da95d3fd2729916aa4012ceb6128a.map,
position : gmap\_md60da95d3fd2729916aa4012ceb6128a.positions[m]
} );
}
// Redraw map to fit our new marker-based bounds
gmap\_md60da95d3fd2729916aa4012ceb6128a.map.setCenter( gmap\_md60da95d3fd2729916aa4012ceb6128a.positions[397] );
});