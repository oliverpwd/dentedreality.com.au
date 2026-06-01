---
title: SF Cityscape
date: '2012-08-05T15:53:24+00:00'
format: image
service: flickr
tags:
- cityscape
- sanfrancisco
- sf
- skyline
- view
- wcsf
- wcsf2012
- wordcamp
- wordpress
image: http://i2.wp.com/dentedreality.com.au/wp-content/uploads/2012/08/8244723711_92e7e155cd_o.jpg?resize=607%2C455
---

[![SF Cityscape](http://i2.wp.com/dentedreality.com.au/wp-content/uploads/2012/08/8244723711_92e7e155cd_o.jpg?resize=607%2C455)](http://dentedreality.com.au/2012/08/05/sf-cityscape/) 
# [SF Cityscape](http://dentedreality.com.au/2012/08/05/sf-cityscape/)





* #[cityscape](http://dentedreality.com.au/tags/cityscape/)
* #[sanfrancisco](http://dentedreality.com.au/tags/sanfrancisco/)
* #[sf](http://dentedreality.com.au/tags/sf/)
* #[skyline](http://dentedreality.com.au/tags/skyline/)
* #[view](http://dentedreality.com.au/tags/view/)
* #[wcsf](http://dentedreality.com.au/tags/wcsf/)
* #[wcsf2012](http://dentedreality.com.au/tags/wcsf2012/)
* #[wordcamp](http://dentedreality.com.au/tags/wordcamp/)
* #[wordpress](http://dentedreality.com.au/tags/wordpress/)

Posted on [Flickr](http://www.flickr.com/photos/borkazoid/8244723711/) [3:53 pm, August 5, 2012](http://dentedreality.com.au/2012/08/05/sf-cityscape/ "3:53 pm") 
jQuery(document).ready(function(){
var gmap\_ma8801db6b5bdd304e2daac6e402eefe8 = {
positions : {
375 : new google.maps.LatLng( '37.755313', '-122.418664' )
},
bounds : new google.maps.LatLngBounds(), // empty for now, we'll dynamically extend it later
map : new google.maps.Map(
document.getElementById( 'gmap\_ma8801db6b5bdd304e2daac6e402eefe8' ),
{
mapTypeId: google.maps.MapTypeId.ROADMAP,
center: new google.maps.LatLng( 0, 0 ),
zoom: 16 // Seems to be a good zoom for a single point
}
),
markers : {},
}; // end of gmap
// Extend the bounds of interest based on our positions
for ( var m in gmap\_ma8801db6b5bdd304e2daac6e402eefe8.positions ) {
gmap\_ma8801db6b5bdd304e2daac6e402eefe8.bounds.extend( gmap\_ma8801db6b5bdd304e2daac6e402eefe8.positions[m] );
}
// Render markers
for ( var m in gmap\_ma8801db6b5bdd304e2daac6e402eefe8.positions ) {
gmap\_ma8801db6b5bdd304e2daac6e402eefe8.markers[m] = new google.maps.Marker( {
clickable: true,
map : gmap\_ma8801db6b5bdd304e2daac6e402eefe8.map,
position : gmap\_ma8801db6b5bdd304e2daac6e402eefe8.positions[m]
} );
}
// Redraw map to fit our new marker-based bounds
gmap\_ma8801db6b5bdd304e2daac6e402eefe8.map.setCenter( gmap\_ma8801db6b5bdd304e2daac6e402eefe8.positions[375] );
});