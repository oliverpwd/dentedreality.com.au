---
title: WordPress in Buenos Aires
date: '2009-12-26T09:52:23-07:00'
format: image
service: flickr
tags:
- argentina
- buenosaires
- cazuela
- logo
- wordpress
latitude: '-34.602167'
longitude: '-58.386667'
image: https://dentedreality-content.s3.amazonaws.com/wp-content/uploads/2009/12/14185430/4222680272_59106a71d8_o.jpg
---

[![WordPress in Buenos Aires](https://dentedreality-content.s3.amazonaws.com/wp-content/uploads/2009/12/14185430/4222680272_59106a71d8_o.jpg)](https://dentedreality.com.au/2009/12/26/wordpress-in-buenos-aires/) 
# [WordPress in Buenos Aires](https://dentedreality.com.au/2009/12/26/wordpress-in-buenos-aires/)

[![WordPress in Buenos Aires](https://dentedreality-content.s3.amazonaws.com/wp-content/uploads/2009/12/14185430/4222680272_59106a71d8_o.jpg)](http://www.flickr.com/photos/borkazoid/4222680272/)

They provided the crayons, so I did what I could. It ended up looking like a bit of a fauxgo (short version of the (W) logo), but I never claimed to be an artist…

-34.602167-58.386667




* #[argentina](https://dentedreality.com.au/tags/argentina/)
* #[buenosaires](https://dentedreality.com.au/tags/buenosaires/)
* #[cazuela](https://dentedreality.com.au/tags/cazuela/)
* #[logo](https://dentedreality.com.au/tags/logo/)
* #[wordpress](https://dentedreality.com.au/tags/wordpress/)

Posted on [Flickr](http://www.flickr.com/photos/borkazoid/4222680272/) [9:52 am, December 26, 2009](https://dentedreality.com.au/2009/12/26/wordpress-in-buenos-aires/ "9:52 am") 
jQuery(document).ready(function(){
var gmap\_m72b2f490b9cb39d42437b9ee2ebac700 = {
positions : {
590 : new google.maps.LatLng( '-34.602167', '-58.386667' )
},
bounds : new google.maps.LatLngBounds(), // empty for now, we'll dynamically extend it later
map : new google.maps.Map(
document.getElementById( 'gmap\_m72b2f490b9cb39d42437b9ee2ebac700' ),
{
mapTypeId: google.maps.MapTypeId.ROADMAP,
center: new google.maps.LatLng( 0, 0 ),
zoom: 16 // Seems to be a good zoom for a single point
}
),
markers : {},
}; // end of gmap
// Extend the bounds of interest based on our positions
for ( var m in gmap\_m72b2f490b9cb39d42437b9ee2ebac700.positions ) {
gmap\_m72b2f490b9cb39d42437b9ee2ebac700.bounds.extend( gmap\_m72b2f490b9cb39d42437b9ee2ebac700.positions[m] );
}
// Render markers
for ( var m in gmap\_m72b2f490b9cb39d42437b9ee2ebac700.positions ) {
gmap\_m72b2f490b9cb39d42437b9ee2ebac700.markers[m] = new google.maps.Marker( {
clickable: true,
map : gmap\_m72b2f490b9cb39d42437b9ee2ebac700.map,
position : gmap\_m72b2f490b9cb39d42437b9ee2ebac700.positions[m]
} );
}
// Redraw map to fit our new marker-based bounds
gmap\_m72b2f490b9cb39d42437b9ee2ebac700.map.setCenter( gmap\_m72b2f490b9cb39d42437b9ee2ebac700.positions[590] );
});