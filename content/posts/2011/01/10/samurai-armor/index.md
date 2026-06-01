---
title: Samurai Armor
date: '2011-01-10T11:38:27-07:00'
format: image
service: flickr
tags:
- armor
- samurai
latitude: '-32.0635'
longitude: '115.936'
image: https://s3.amazonaws.com/dentedreality-content/wp-content/uploads/2011/01/14185958/5434108809_120d80e3b2_o.jpg
---

[![Samurai Armor](https://s3.amazonaws.com/dentedreality-content/wp-content/uploads/2011/01/14185958/5434108809_120d80e3b2_o.jpg)](https://dentedreality.com.au/2011/01/10/samurai-armor/) 
# [Samurai Armor](https://dentedreality.com.au/2011/01/10/samurai-armor/)

[![Samurai Armor](https://s3.amazonaws.com/dentedreality-content/wp-content/uploads/2011/01/14185958/5434108809_120d80e3b2_o.jpg)](http://www.flickr.com/photos/borkazoid/5434108809/)

-32.0635115.936




* #[armor](https://dentedreality.com.au/tags/armor/)
* #[samurai](https://dentedreality.com.au/tags/samurai/)

Posted on [Flickr](http://www.flickr.com/photos/borkazoid/5434108809/) [11:38 am, January 10, 2011](https://dentedreality.com.au/2011/01/10/samurai-armor/ "11:38 am") 
jQuery(document).ready(function(){
var gmap\_mab19a3e158abcf62364e9cb0065f94f5 = {
positions : {
679 : new google.maps.LatLng( '-32.0635', '115.936' )
},
bounds : new google.maps.LatLngBounds(), // empty for now, we'll dynamically extend it later
map : new google.maps.Map(
document.getElementById( 'gmap\_mab19a3e158abcf62364e9cb0065f94f5' ),
{
mapTypeId: google.maps.MapTypeId.ROADMAP,
center: new google.maps.LatLng( 0, 0 ),
zoom: 16 // Seems to be a good zoom for a single point
}
),
markers : {},
}; // end of gmap
// Extend the bounds of interest based on our positions
for ( var m in gmap\_mab19a3e158abcf62364e9cb0065f94f5.positions ) {
gmap\_mab19a3e158abcf62364e9cb0065f94f5.bounds.extend( gmap\_mab19a3e158abcf62364e9cb0065f94f5.positions[m] );
}
// Render markers
for ( var m in gmap\_mab19a3e158abcf62364e9cb0065f94f5.positions ) {
gmap\_mab19a3e158abcf62364e9cb0065f94f5.markers[m] = new google.maps.Marker( {
clickable: true,
map : gmap\_mab19a3e158abcf62364e9cb0065f94f5.map,
position : gmap\_mab19a3e158abcf62364e9cb0065f94f5.positions[m]
} );
}
// Redraw map to fit our new marker-based bounds
gmap\_mab19a3e158abcf62364e9cb0065f94f5.map.setCenter( gmap\_mab19a3e158abcf62364e9cb0065f94f5.positions[679] );
});