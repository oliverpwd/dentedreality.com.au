---
title: Sponsored Beer
date: '2012-03-10T16:39:46+00:00'
format: image
service: flickr
tags:
- Austin
- sxsw
- sxsw2012
- texas
image: http://i2.wp.com/dentedreality.com.au/wp-content/uploads/2012/03/7721571944_2a1f909515_o.jpg?resize=607%2C452
---

[![Sponsored Beer](http://i2.wp.com/dentedreality.com.au/wp-content/uploads/2012/03/7721571944_2a1f909515_o.jpg?resize=607%2C452)](http://dentedreality.com.au/2012/03/10/sponsored-beer/) 
# [Sponsored Beer](http://dentedreality.com.au/2012/03/10/sponsored-beer/)





* #[Austin](http://dentedreality.com.au/tags/austin/)
* #[sxsw](http://dentedreality.com.au/tags/sxsw/)
* #[sxsw2012](http://dentedreality.com.au/tags/sxsw2012/)
* #[texas](http://dentedreality.com.au/tags/texas/)

Posted on [Flickr](http://www.flickr.com/photos/borkazoid/7721571944/) [4:39 pm, March 10, 2012](http://dentedreality.com.au/2012/03/10/sponsored-beer/ "4:39 pm") 
jQuery(document).ready(function(){
var gmap\_m60e2b499c80097af4a52d81e41ce200a = {
positions : {
217 : new google.maps.LatLng( '30.267166', '-97.739667' )
},
bounds : new google.maps.LatLngBounds(), // empty for now, we'll dynamically extend it later
map : new google.maps.Map(
document.getElementById( 'gmap\_m60e2b499c80097af4a52d81e41ce200a' ),
{
mapTypeId: google.maps.MapTypeId.ROADMAP,
center: new google.maps.LatLng( 0, 0 ),
zoom: 16 // Seems to be a good zoom for a single point
}
),
markers : {},
}; // end of gmap
// Extend the bounds of interest based on our positions
for ( var m in gmap\_m60e2b499c80097af4a52d81e41ce200a.positions ) {
gmap\_m60e2b499c80097af4a52d81e41ce200a.bounds.extend( gmap\_m60e2b499c80097af4a52d81e41ce200a.positions[m] );
}
// Render markers
for ( var m in gmap\_m60e2b499c80097af4a52d81e41ce200a.positions ) {
gmap\_m60e2b499c80097af4a52d81e41ce200a.markers[m] = new google.maps.Marker( {
clickable: true,
map : gmap\_m60e2b499c80097af4a52d81e41ce200a.map,
position : gmap\_m60e2b499c80097af4a52d81e41ce200a.positions[m]
} );
}
// Redraw map to fit our new marker-based bounds
gmap\_m60e2b499c80097af4a52d81e41ce200a.map.setCenter( gmap\_m60e2b499c80097af4a52d81e41ce200a.positions[217] );
});