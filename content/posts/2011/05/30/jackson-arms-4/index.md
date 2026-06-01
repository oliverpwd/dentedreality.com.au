---
title: Jackson Arms
date: '2011-05-30T09:00:49+00:00'
format: image
service: flickr
tags:
- jacksonarms
- jenn
- memorialday
- shooting
image: http://i0.wp.com/dentedreality.com.au/wp-content/uploads/2011/05/5802878485_5c96c7b123_o.jpg?resize=607%2C813
---

[![Jackson Arms](http://i0.wp.com/dentedreality.com.au/wp-content/uploads/2011/05/5802878485_5c96c7b123_o.jpg?resize=607%2C813)](http://dentedreality.com.au/2011/05/30/jackson-arms-4/) 
# [Jackson Arms](http://dentedreality.com.au/2011/05/30/jackson-arms-4/)

Memorial Day at the range





* #[jacksonarms](http://dentedreality.com.au/tags/jacksonarms/)
* #[jenn](http://dentedreality.com.au/tags/jenn/)
* #[memorialday](http://dentedreality.com.au/tags/memorialday/)
* #[shooting](http://dentedreality.com.au/tags/shooting/)

Posted on [Flickr](http://www.flickr.com/photos/borkazoid/5802878485/) [9:00 am, May 30, 2011](http://dentedreality.com.au/2011/05/30/jackson-arms-4/ "9:00 am") 
jQuery(document).ready(function(){
var gmap\_mcfd52295e07e3425e993bb4ef2e07017 = {
positions : {
596 : new google.maps.LatLng( '37.645166', '-122.402334' )
},
bounds : new google.maps.LatLngBounds(), // empty for now, we'll dynamically extend it later
map : new google.maps.Map(
document.getElementById( 'gmap\_mcfd52295e07e3425e993bb4ef2e07017' ),
{
mapTypeId: google.maps.MapTypeId.ROADMAP,
center: new google.maps.LatLng( 0, 0 ),
zoom: 16 // Seems to be a good zoom for a single point
}
),
markers : {},
}; // end of gmap
// Extend the bounds of interest based on our positions
for ( var m in gmap\_mcfd52295e07e3425e993bb4ef2e07017.positions ) {
gmap\_mcfd52295e07e3425e993bb4ef2e07017.bounds.extend( gmap\_mcfd52295e07e3425e993bb4ef2e07017.positions[m] );
}
// Render markers
for ( var m in gmap\_mcfd52295e07e3425e993bb4ef2e07017.positions ) {
gmap\_mcfd52295e07e3425e993bb4ef2e07017.markers[m] = new google.maps.Marker( {
clickable: true,
map : gmap\_mcfd52295e07e3425e993bb4ef2e07017.map,
position : gmap\_mcfd52295e07e3425e993bb4ef2e07017.positions[m]
} );
}
// Redraw map to fit our new marker-based bounds
gmap\_mcfd52295e07e3425e993bb4ef2e07017.map.setCenter( gmap\_mcfd52295e07e3425e993bb4ef2e07017.positions[596] );
});