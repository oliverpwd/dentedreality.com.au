---
title: Coffee Grinder
date: '2010-02-14T06:09:58+00:00'
format: image
service: flickr
tags:
- coffee
- coffeegrinder
- grinder
image: http://i2.wp.com/dentedreality.com.au/wp-content/uploads/2010/02/4515770283_bc8afc24f9_o.jpg?resize=607%2C809
---

[![Coffee Grinder](http://i2.wp.com/dentedreality.com.au/wp-content/uploads/2010/02/4515770283_bc8afc24f9_o.jpg?resize=607%2C809)](http://dentedreality.com.au/2010/02/14/coffee-grinder/) 
# [Coffee Grinder](http://dentedreality.com.au/2010/02/14/coffee-grinder/)

Robin’s cousin Ben got us this awesome coffee grinder for Christmas





* #[coffee](http://dentedreality.com.au/tags/coffee/)
* #[coffeegrinder](http://dentedreality.com.au/tags/coffeegrinder/)
* #[grinder](http://dentedreality.com.au/tags/grinder/)

Posted on [Flickr](http://www.flickr.com/photos/borkazoid/4515770283/) [6:09 am, February 14, 2010](http://dentedreality.com.au/2010/02/14/coffee-grinder/ "6:09 am") 
jQuery(document).ready(function(){
var gmap\_me4171ef1e744da2f843f7a80cae1ed44 = {
positions : {
604 : new google.maps.LatLng( '37.791333', '-122.4175' )
},
bounds : new google.maps.LatLngBounds(), // empty for now, we'll dynamically extend it later
map : new google.maps.Map(
document.getElementById( 'gmap\_me4171ef1e744da2f843f7a80cae1ed44' ),
{
mapTypeId: google.maps.MapTypeId.ROADMAP,
center: new google.maps.LatLng( 0, 0 ),
zoom: 16 // Seems to be a good zoom for a single point
}
),
markers : {},
}; // end of gmap
// Extend the bounds of interest based on our positions
for ( var m in gmap\_me4171ef1e744da2f843f7a80cae1ed44.positions ) {
gmap\_me4171ef1e744da2f843f7a80cae1ed44.bounds.extend( gmap\_me4171ef1e744da2f843f7a80cae1ed44.positions[m] );
}
// Render markers
for ( var m in gmap\_me4171ef1e744da2f843f7a80cae1ed44.positions ) {
gmap\_me4171ef1e744da2f843f7a80cae1ed44.markers[m] = new google.maps.Marker( {
clickable: true,
map : gmap\_me4171ef1e744da2f843f7a80cae1ed44.map,
position : gmap\_me4171ef1e744da2f843f7a80cae1ed44.positions[m]
} );
}
// Redraw map to fit our new marker-based bounds
gmap\_me4171ef1e744da2f843f7a80cae1ed44.map.setCenter( gmap\_me4171ef1e744da2f843f7a80cae1ed44.positions[604] );
});