---
title: SXSW 2012
date: '2012-03-12T10:04:32+00:00'
format: image
service: flickr
tags:
- Austin
- sxsw
- sxsw2012
- texas
image: http://i1.wp.com/dentedreality.com.au/wp-content/uploads/2012/03/7721573946_f9b538cb9d_o.jpg?resize=607%2C452
---

[![SXSW 2012](http://i1.wp.com/dentedreality.com.au/wp-content/uploads/2012/03/7721573946_f9b538cb9d_o.jpg?resize=607%2C452)](http://dentedreality.com.au/2012/03/12/sxsw-2012-7/) 
# [SXSW 2012](http://dentedreality.com.au/2012/03/12/sxsw-2012-7/)





* #[Austin](http://dentedreality.com.au/tags/austin/)
* #[sxsw](http://dentedreality.com.au/tags/sxsw/)
* #[sxsw2012](http://dentedreality.com.au/tags/sxsw2012/)
* #[texas](http://dentedreality.com.au/tags/texas/)

Posted on [Flickr](http://www.flickr.com/photos/borkazoid/7721573946/) [10:04 am, March 12, 2012](http://dentedreality.com.au/2012/03/12/sxsw-2012-7/ "10:04 am") 
jQuery(document).ready(function(){
var gmap\_m5ee1bf0549e0c087706909f96ca0870b = {
positions : {
358 : new google.maps.LatLng( '30.262833', '-97.736667' )
},
bounds : new google.maps.LatLngBounds(), // empty for now, we'll dynamically extend it later
map : new google.maps.Map(
document.getElementById( 'gmap\_m5ee1bf0549e0c087706909f96ca0870b' ),
{
mapTypeId: google.maps.MapTypeId.ROADMAP,
center: new google.maps.LatLng( 0, 0 ),
zoom: 16 // Seems to be a good zoom for a single point
}
),
markers : {},
}; // end of gmap
// Extend the bounds of interest based on our positions
for ( var m in gmap\_m5ee1bf0549e0c087706909f96ca0870b.positions ) {
gmap\_m5ee1bf0549e0c087706909f96ca0870b.bounds.extend( gmap\_m5ee1bf0549e0c087706909f96ca0870b.positions[m] );
}
// Render markers
for ( var m in gmap\_m5ee1bf0549e0c087706909f96ca0870b.positions ) {
gmap\_m5ee1bf0549e0c087706909f96ca0870b.markers[m] = new google.maps.Marker( {
clickable: true,
map : gmap\_m5ee1bf0549e0c087706909f96ca0870b.map,
position : gmap\_m5ee1bf0549e0c087706909f96ca0870b.positions[m]
} );
}
// Redraw map to fit our new marker-based bounds
gmap\_m5ee1bf0549e0c087706909f96ca0870b.map.setCenter( gmap\_m5ee1bf0549e0c087706909f96ca0870b.positions[358] );
});