---
title: Two Door Cinema Club
date: '2012-09-28T17:22:01+00:00'
format: image
service: flickr
tags:
- centralpark
- concert
- livemusic
- music
- tdcc
- twodoorcinemaclub
image: http://i2.wp.com/dentedreality.com.au/wp-content/uploads/2012/09/8245862738_ca2496946a_o.jpg?resize=607%2C452
---

[![Two Door Cinema Club](http://i2.wp.com/dentedreality.com.au/wp-content/uploads/2012/09/8245862738_ca2496946a_o.jpg?resize=607%2C452)](http://dentedreality.com.au/2012/09/28/two-door-cinema-club-2/) 
# [Two Door Cinema Club](http://dentedreality.com.au/2012/09/28/two-door-cinema-club-2/)





* #[centralpark](http://dentedreality.com.au/tags/centralpark/)
* #[concert](http://dentedreality.com.au/tags/concert/)
* #[livemusic](http://dentedreality.com.au/tags/livemusic/)
* #[music](http://dentedreality.com.au/tags/music/)
* #[tdcc](http://dentedreality.com.au/tags/tdcc/)
* #[twodoorcinemaclub](http://dentedreality.com.au/tags/twodoorcinemaclub/)

Posted on [Flickr](http://www.flickr.com/photos/borkazoid/8245862738/) [5:22 pm, September 28, 2012](http://dentedreality.com.au/2012/09/28/two-door-cinema-club-2/ "5:22 pm") 
jQuery(document).ready(function(){
var gmap\_m222ab84a9445562d7314c11e384f590b = {
positions : {
658 : new google.maps.LatLng( '40.772166', '-73.969834' )
},
bounds : new google.maps.LatLngBounds(), // empty for now, we'll dynamically extend it later
map : new google.maps.Map(
document.getElementById( 'gmap\_m222ab84a9445562d7314c11e384f590b' ),
{
mapTypeId: google.maps.MapTypeId.ROADMAP,
center: new google.maps.LatLng( 0, 0 ),
zoom: 16 // Seems to be a good zoom for a single point
}
),
markers : {},
}; // end of gmap
// Extend the bounds of interest based on our positions
for ( var m in gmap\_m222ab84a9445562d7314c11e384f590b.positions ) {
gmap\_m222ab84a9445562d7314c11e384f590b.bounds.extend( gmap\_m222ab84a9445562d7314c11e384f590b.positions[m] );
}
// Render markers
for ( var m in gmap\_m222ab84a9445562d7314c11e384f590b.positions ) {
gmap\_m222ab84a9445562d7314c11e384f590b.markers[m] = new google.maps.Marker( {
clickable: true,
map : gmap\_m222ab84a9445562d7314c11e384f590b.map,
position : gmap\_m222ab84a9445562d7314c11e384f590b.positions[m]
} );
}
// Redraw map to fit our new marker-based bounds
gmap\_m222ab84a9445562d7314c11e384f590b.map.setCenter( gmap\_m222ab84a9445562d7314c11e384f590b.positions[658] );
});