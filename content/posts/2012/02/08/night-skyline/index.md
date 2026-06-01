---
title: Night Skyline
date: '2012-02-08T14:17:01+00:00'
format: image
service: flickr
tags:
- night
- sanfrancisco
- skyline
image: http://i2.wp.com/dentedreality.com.au/wp-content/uploads/2012/02/6813458730_66c6a966ae_o.jpg?resize=607%2C452
---

[![Night Skyline](http://i2.wp.com/dentedreality.com.au/wp-content/uploads/2012/02/6813458730_66c6a966ae_o.jpg?resize=607%2C452)](http://dentedreality.com.au/2012/02/08/night-skyline/) 
# [Night Skyline](http://dentedreality.com.au/2012/02/08/night-skyline/)





* #[night](http://dentedreality.com.au/tags/night/)
* #[sanfrancisco](http://dentedreality.com.au/tags/sanfrancisco/)
* #[skyline](http://dentedreality.com.au/tags/skyline/)

Posted on [Flickr](http://www.flickr.com/photos/borkazoid/6813458730/) [2:17 pm, February 8, 2012](http://dentedreality.com.au/2012/02/08/night-skyline/ "2:17 pm") 
jQuery(document).ready(function(){
var gmap\_m8506ba59095706a191bef4f0610c25a8 = {
positions : {
725 : new google.maps.LatLng( '37.786166', '-122.397501' )
},
bounds : new google.maps.LatLngBounds(), // empty for now, we'll dynamically extend it later
map : new google.maps.Map(
document.getElementById( 'gmap\_m8506ba59095706a191bef4f0610c25a8' ),
{
mapTypeId: google.maps.MapTypeId.ROADMAP,
center: new google.maps.LatLng( 0, 0 ),
zoom: 16 // Seems to be a good zoom for a single point
}
),
markers : {},
}; // end of gmap
// Extend the bounds of interest based on our positions
for ( var m in gmap\_m8506ba59095706a191bef4f0610c25a8.positions ) {
gmap\_m8506ba59095706a191bef4f0610c25a8.bounds.extend( gmap\_m8506ba59095706a191bef4f0610c25a8.positions[m] );
}
// Render markers
for ( var m in gmap\_m8506ba59095706a191bef4f0610c25a8.positions ) {
gmap\_m8506ba59095706a191bef4f0610c25a8.markers[m] = new google.maps.Marker( {
clickable: true,
map : gmap\_m8506ba59095706a191bef4f0610c25a8.map,
position : gmap\_m8506ba59095706a191bef4f0610c25a8.positions[m]
} );
}
// Redraw map to fit our new marker-based bounds
gmap\_m8506ba59095706a191bef4f0610c25a8.map.setCenter( gmap\_m8506ba59095706a191bef4f0610c25a8.positions[725] );
});