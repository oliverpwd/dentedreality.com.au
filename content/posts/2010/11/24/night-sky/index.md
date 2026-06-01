---
title: Night Sky
date: '2010-11-24T22:38:07+00:00'
format: image
service: flickr
tags:
- lights
- night
- sanfrancisco
- skyline
image: http://i2.wp.com/dentedreality.com.au/wp-content/uploads/2010/11/5434636412_1072ae7a85_o.jpg?resize=607%2C452
---

[![Night Sky](http://i2.wp.com/dentedreality.com.au/wp-content/uploads/2010/11/5434636412_1072ae7a85_o.jpg?resize=607%2C452)](http://dentedreality.com.au/2010/11/24/night-sky/) 
# [Night Sky](http://dentedreality.com.au/2010/11/24/night-sky/)





* #[lights](http://dentedreality.com.au/tags/lights/)
* #[night](http://dentedreality.com.au/tags/night/)
* #[sanfrancisco](http://dentedreality.com.au/tags/sanfrancisco/)
* #[skyline](http://dentedreality.com.au/tags/skyline/)

Posted on [Flickr](http://www.flickr.com/photos/borkazoid/5434636412/) [10:38 pm, November 24, 2010](http://dentedreality.com.au/2010/11/24/night-sky/ "10:38 pm") 
jQuery(document).ready(function(){
var gmap\_m23b7915dafdea52fa2b37bc05d5e691c = {
positions : {
922 : new google.maps.LatLng( '37.7765', '-122.394667' )
},
bounds : new google.maps.LatLngBounds(), // empty for now, we'll dynamically extend it later
map : new google.maps.Map(
document.getElementById( 'gmap\_m23b7915dafdea52fa2b37bc05d5e691c' ),
{
mapTypeId: google.maps.MapTypeId.ROADMAP,
center: new google.maps.LatLng( 0, 0 ),
zoom: 16 // Seems to be a good zoom for a single point
}
),
markers : {},
}; // end of gmap
// Extend the bounds of interest based on our positions
for ( var m in gmap\_m23b7915dafdea52fa2b37bc05d5e691c.positions ) {
gmap\_m23b7915dafdea52fa2b37bc05d5e691c.bounds.extend( gmap\_m23b7915dafdea52fa2b37bc05d5e691c.positions[m] );
}
// Render markers
for ( var m in gmap\_m23b7915dafdea52fa2b37bc05d5e691c.positions ) {
gmap\_m23b7915dafdea52fa2b37bc05d5e691c.markers[m] = new google.maps.Marker( {
clickable: true,
map : gmap\_m23b7915dafdea52fa2b37bc05d5e691c.map,
position : gmap\_m23b7915dafdea52fa2b37bc05d5e691c.positions[m]
} );
}
// Redraw map to fit our new marker-based bounds
gmap\_m23b7915dafdea52fa2b37bc05d5e691c.map.setCenter( gmap\_m23b7915dafdea52fa2b37bc05d5e691c.positions[922] );
});