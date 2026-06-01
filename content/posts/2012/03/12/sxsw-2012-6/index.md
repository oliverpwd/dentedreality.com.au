---
title: SXSW 2012
date: '2012-03-12T19:42:00+00:00'
format: image
service: flickr
tags:
- Austin
- chelsea
- chexee
- helen
- sxsw
- sxsw2012
- texas
image: http://i0.wp.com/dentedreality.com.au/wp-content/uploads/2012/03/7721574366_604327ce7e_o.jpg?resize=607%2C452
---

[![SXSW 2012](http://i0.wp.com/dentedreality.com.au/wp-content/uploads/2012/03/7721574366_604327ce7e_o.jpg?resize=607%2C452)](http://dentedreality.com.au/2012/03/12/sxsw-2012-6/) 
# [SXSW 2012](http://dentedreality.com.au/2012/03/12/sxsw-2012-6/)





* #[Austin](http://dentedreality.com.au/tags/austin/)
* #[chelsea](http://dentedreality.com.au/tags/chelsea/)
* #[chexee](http://dentedreality.com.au/tags/chexee/)
* #[helen](http://dentedreality.com.au/tags/helen/)
* #[sxsw](http://dentedreality.com.au/tags/sxsw/)
* #[sxsw2012](http://dentedreality.com.au/tags/sxsw2012/)
* #[texas](http://dentedreality.com.au/tags/texas/)

Posted on [Flickr](http://www.flickr.com/photos/borkazoid/7721574366/) [7:42 pm, March 12, 2012](http://dentedreality.com.au/2012/03/12/sxsw-2012-6/ "7:42 pm") 
jQuery(document).ready(function(){
var gmap\_m71bd38e2c865654be0699e6305d3d769 = {
positions : {
19 : new google.maps.LatLng( '30.267', '-97.739' )
},
bounds : new google.maps.LatLngBounds(), // empty for now, we'll dynamically extend it later
map : new google.maps.Map(
document.getElementById( 'gmap\_m71bd38e2c865654be0699e6305d3d769' ),
{
mapTypeId: google.maps.MapTypeId.ROADMAP,
center: new google.maps.LatLng( 0, 0 ),
zoom: 16 // Seems to be a good zoom for a single point
}
),
markers : {},
}; // end of gmap
// Extend the bounds of interest based on our positions
for ( var m in gmap\_m71bd38e2c865654be0699e6305d3d769.positions ) {
gmap\_m71bd38e2c865654be0699e6305d3d769.bounds.extend( gmap\_m71bd38e2c865654be0699e6305d3d769.positions[m] );
}
// Render markers
for ( var m in gmap\_m71bd38e2c865654be0699e6305d3d769.positions ) {
gmap\_m71bd38e2c865654be0699e6305d3d769.markers[m] = new google.maps.Marker( {
clickable: true,
map : gmap\_m71bd38e2c865654be0699e6305d3d769.map,
position : gmap\_m71bd38e2c865654be0699e6305d3d769.positions[m]
} );
}
// Redraw map to fit our new marker-based bounds
gmap\_m71bd38e2c865654be0699e6305d3d769.map.setCenter( gmap\_m71bd38e2c865654be0699e6305d3d769.positions[19] );
});