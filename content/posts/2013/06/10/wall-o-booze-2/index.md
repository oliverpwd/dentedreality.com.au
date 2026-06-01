---
title: Wall o’ Booze
date: '2013-06-10T20:22:56+00:00'
format: image
service: flickr
tags:
- bar
- booze
- paddys
- Portland
- rye
- scotch
- whiskey
image: http://i0.wp.com/dentedreality.com.au/wp-content/uploads/2013/06/9439828630_636d172fc3_o.jpg?resize=607%2C452
---

[![Wall o' Booze](http://i0.wp.com/dentedreality.com.au/wp-content/uploads/2013/06/9439828630_636d172fc3_o.jpg?resize=607%2C452)](http://dentedreality.com.au/2013/06/10/wall-o-booze-2/) 
# [Wall o’ Booze](http://dentedreality.com.au/2013/06/10/wall-o-booze-2/)

At Paddy’s, Portland





* #[bar](http://dentedreality.com.au/tags/bar/)
* #[booze](http://dentedreality.com.au/tags/booze/)
* #[paddys](http://dentedreality.com.au/tags/paddys/)
* #[Portland](http://dentedreality.com.au/tags/portland/)
* #[rye](http://dentedreality.com.au/tags/rye/)
* #[scotch](http://dentedreality.com.au/tags/scotch/)
* #[whiskey](http://dentedreality.com.au/tags/whiskey/)

Posted on [Flickr](http://www.flickr.com/photos/borkazoid/9439828630/) [8:22 pm, June 10, 2013](http://dentedreality.com.au/2013/06/10/wall-o-booze-2/ "8:22 pm") 
jQuery(document).ready(function(){
var gmap\_md832c6fce8344354f971f82e9625484e = {
positions : {
224 : new google.maps.LatLng( '45.516999', '-122.674' )
},
bounds : new google.maps.LatLngBounds(), // empty for now, we'll dynamically extend it later
map : new google.maps.Map(
document.getElementById( 'gmap\_md832c6fce8344354f971f82e9625484e' ),
{
mapTypeId: google.maps.MapTypeId.ROADMAP,
center: new google.maps.LatLng( 0, 0 ),
zoom: 16 // Seems to be a good zoom for a single point
}
),
markers : {},
}; // end of gmap
// Extend the bounds of interest based on our positions
for ( var m in gmap\_md832c6fce8344354f971f82e9625484e.positions ) {
gmap\_md832c6fce8344354f971f82e9625484e.bounds.extend( gmap\_md832c6fce8344354f971f82e9625484e.positions[m] );
}
// Render markers
for ( var m in gmap\_md832c6fce8344354f971f82e9625484e.positions ) {
gmap\_md832c6fce8344354f971f82e9625484e.markers[m] = new google.maps.Marker( {
clickable: true,
map : gmap\_md832c6fce8344354f971f82e9625484e.map,
position : gmap\_md832c6fce8344354f971f82e9625484e.positions[m]
} );
}
// Redraw map to fit our new marker-based bounds
gmap\_md832c6fce8344354f971f82e9625484e.map.setCenter( gmap\_md832c6fce8344354f971f82e9625484e.positions[224] );
});