---
title: SXSW 2012
date: '2012-03-13T18:09:07+00:00'
format: image
service: flickr
tags:
- Austin
- sxsw
- sxsw2012
- texas
image: http://i0.wp.com/dentedreality.com.au/wp-content/uploads/2012/03/7721699362_58e19370bb_o.jpg?resize=607%2C452
---

[![SXSW 2012](http://i0.wp.com/dentedreality.com.au/wp-content/uploads/2012/03/7721699362_58e19370bb_o.jpg?resize=607%2C452)](http://dentedreality.com.au/2012/03/13/sxsw-2012-4/) 
# [SXSW 2012](http://dentedreality.com.au/2012/03/13/sxsw-2012-4/)





* #[Austin](http://dentedreality.com.au/tags/austin/)
* #[sxsw](http://dentedreality.com.au/tags/sxsw/)
* #[sxsw2012](http://dentedreality.com.au/tags/sxsw2012/)
* #[texas](http://dentedreality.com.au/tags/texas/)

Posted on [Flickr](http://www.flickr.com/photos/borkazoid/7721699362/) [6:09 pm, March 13, 2012](http://dentedreality.com.au/2012/03/13/sxsw-2012-4/ "6:09 pm") 
jQuery(document).ready(function(){
var gmap\_mc0656fdbb5c1da83a8d85afa68bbfbd2 = {
positions : {
695 : new google.maps.LatLng( '30.268833', '-97.735834' )
},
bounds : new google.maps.LatLngBounds(), // empty for now, we'll dynamically extend it later
map : new google.maps.Map(
document.getElementById( 'gmap\_mc0656fdbb5c1da83a8d85afa68bbfbd2' ),
{
mapTypeId: google.maps.MapTypeId.ROADMAP,
center: new google.maps.LatLng( 0, 0 ),
zoom: 16 // Seems to be a good zoom for a single point
}
),
markers : {},
}; // end of gmap
// Extend the bounds of interest based on our positions
for ( var m in gmap\_mc0656fdbb5c1da83a8d85afa68bbfbd2.positions ) {
gmap\_mc0656fdbb5c1da83a8d85afa68bbfbd2.bounds.extend( gmap\_mc0656fdbb5c1da83a8d85afa68bbfbd2.positions[m] );
}
// Render markers
for ( var m in gmap\_mc0656fdbb5c1da83a8d85afa68bbfbd2.positions ) {
gmap\_mc0656fdbb5c1da83a8d85afa68bbfbd2.markers[m] = new google.maps.Marker( {
clickable: true,
map : gmap\_mc0656fdbb5c1da83a8d85afa68bbfbd2.map,
position : gmap\_mc0656fdbb5c1da83a8d85afa68bbfbd2.positions[m]
} );
}
// Redraw map to fit our new marker-based bounds
gmap\_mc0656fdbb5c1da83a8d85afa68bbfbd2.map.setCenter( gmap\_mc0656fdbb5c1da83a8d85afa68bbfbd2.positions[695] );
});