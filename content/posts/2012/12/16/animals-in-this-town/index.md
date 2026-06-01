---
title: Animals in this Town
date: '2012-12-16T11:38:24+00:00'
format: image
service: flickr
tags:
- aisle
- christmas
- target
image: http://i0.wp.com/dentedreality.com.au/wp-content/uploads/2012/12/8459252013_e3b7760e94_o.jpg?resize=607%2C813
---

[![Animals in this Town](http://i0.wp.com/dentedreality.com.au/wp-content/uploads/2012/12/8459252013_e3b7760e94_o.jpg?resize=607%2C813)](http://dentedreality.com.au/2012/12/16/animals-in-this-town/) 
# [Animals in this Town](http://dentedreality.com.au/2012/12/16/animals-in-this-town/)

One of the aisles in Target just before Christmas





* #[aisle](http://dentedreality.com.au/tags/aisle/)
* #[christmas](http://dentedreality.com.au/tags/christmas/)
* #[target](http://dentedreality.com.au/tags/target/)

Posted on [Flickr](http://www.flickr.com/photos/borkazoid/8459252013/) [11:38 am, December 16, 2012](http://dentedreality.com.au/2012/12/16/animals-in-this-town/ "11:38 am") 
jQuery(document).ready(function(){
var gmap\_me92738c0d86dd669780cee6060a00481 = {
positions : {
653 : new google.maps.LatLng( '40.6845', '-73.976667' )
},
bounds : new google.maps.LatLngBounds(), // empty for now, we'll dynamically extend it later
map : new google.maps.Map(
document.getElementById( 'gmap\_me92738c0d86dd669780cee6060a00481' ),
{
mapTypeId: google.maps.MapTypeId.ROADMAP,
center: new google.maps.LatLng( 0, 0 ),
zoom: 16 // Seems to be a good zoom for a single point
}
),
markers : {},
}; // end of gmap
// Extend the bounds of interest based on our positions
for ( var m in gmap\_me92738c0d86dd669780cee6060a00481.positions ) {
gmap\_me92738c0d86dd669780cee6060a00481.bounds.extend( gmap\_me92738c0d86dd669780cee6060a00481.positions[m] );
}
// Render markers
for ( var m in gmap\_me92738c0d86dd669780cee6060a00481.positions ) {
gmap\_me92738c0d86dd669780cee6060a00481.markers[m] = new google.maps.Marker( {
clickable: true,
map : gmap\_me92738c0d86dd669780cee6060a00481.map,
position : gmap\_me92738c0d86dd669780cee6060a00481.positions[m]
} );
}
// Redraw map to fit our new marker-based bounds
gmap\_me92738c0d86dd669780cee6060a00481.map.setCenter( gmap\_me92738c0d86dd669780cee6060a00481.positions[653] );
});