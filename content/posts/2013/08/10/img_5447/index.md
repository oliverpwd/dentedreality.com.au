---
title: Paintballin’
date: '2013-08-10T10:16:30+00:00'
format: image
service: flickr
tags:
- erika
- new jersey
- new york
- paintball
- paintballing
image: http://i1.wp.com/dentedreality.com.au/wp-content/uploads/2013/08/9767965005_d6ec9c8e71_o.jpg?resize=607%2C813
---

[![IMG_5447](http://i1.wp.com/dentedreality.com.au/wp-content/uploads/2013/08/9767965005_d6ec9c8e71_o.jpg?resize=607%2C813)](http://dentedreality.com.au/2013/08/10/img_5447/) 
# [Paintballin’](http://dentedreality.com.au/2013/08/10/img_5447/)





* #[erika](http://dentedreality.com.au/tags/erika/)
* #[new jersey](http://dentedreality.com.au/tags/new-jersey/)
* #[new york](http://dentedreality.com.au/tags/new-york/)
* #[paintball](http://dentedreality.com.au/tags/paintball/)
* #[paintballing](http://dentedreality.com.au/tags/paintballing/)

Posted on [Flickr](http://www.flickr.com/photos/borkazoid/9767965005/) [10:16 am, August 10, 2013](http://dentedreality.com.au/2013/08/10/img_5447/ "10:16 am") 
jQuery(document).ready(function(){
var gmap\_md4326cdcc1a2aaf8ca2e8e002f34830a = {
positions : {
695 : new google.maps.LatLng( '41.115166', '-74.383837' )
},
bounds : new google.maps.LatLngBounds(), // empty for now, we'll dynamically extend it later
map : new google.maps.Map(
document.getElementById( 'gmap\_md4326cdcc1a2aaf8ca2e8e002f34830a' ),
{
mapTypeId: google.maps.MapTypeId.ROADMAP,
center: new google.maps.LatLng( 0, 0 ),
zoom: 16 // Seems to be a good zoom for a single point
}
),
markers : {},
}; // end of gmap
// Extend the bounds of interest based on our positions
for ( var m in gmap\_md4326cdcc1a2aaf8ca2e8e002f34830a.positions ) {
gmap\_md4326cdcc1a2aaf8ca2e8e002f34830a.bounds.extend( gmap\_md4326cdcc1a2aaf8ca2e8e002f34830a.positions[m] );
}
// Render markers
for ( var m in gmap\_md4326cdcc1a2aaf8ca2e8e002f34830a.positions ) {
gmap\_md4326cdcc1a2aaf8ca2e8e002f34830a.markers[m] = new google.maps.Marker( {
clickable: true,
map : gmap\_md4326cdcc1a2aaf8ca2e8e002f34830a.map,
position : gmap\_md4326cdcc1a2aaf8ca2e8e002f34830a.positions[m]
} );
}
// Redraw map to fit our new marker-based bounds
gmap\_md4326cdcc1a2aaf8ca2e8e002f34830a.map.setCenter( gmap\_md4326cdcc1a2aaf8ca2e8e002f34830a.positions[695] );
});