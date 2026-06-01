---
title: Big v Small
date: '2011-03-11T15:49:22+00:00'
format: image
service: flickr
tags:
- Austin
- sxsw
- sxsw2011
- texas
image: http://i1.wp.com/dentedreality.com.au/wp-content/uploads/2011/03/5802652778_d9139a68ec_o.jpg?resize=607%2C813
---

[![Big v Small](http://i1.wp.com/dentedreality.com.au/wp-content/uploads/2011/03/5802652778_d9139a68ec_o.jpg?resize=607%2C813)](http://dentedreality.com.au/2011/03/11/big-v-small/) 
# [Big v Small](http://dentedreality.com.au/2011/03/11/big-v-small/)





* #[Austin](http://dentedreality.com.au/tags/austin/)
* #[sxsw](http://dentedreality.com.au/tags/sxsw/)
* #[sxsw2011](http://dentedreality.com.au/tags/sxsw2011/)
* #[texas](http://dentedreality.com.au/tags/texas/)

Posted on [Flickr](http://www.flickr.com/photos/borkazoid/5802652778/) [3:49 pm, March 11, 2011](http://dentedreality.com.au/2011/03/11/big-v-small/ "3:49 pm") 
jQuery(document).ready(function(){
var gmap\_m598a1a022fd2980005b84cd459ac7007 = {
positions : {
940 : new google.maps.LatLng( '30.27', '-97.749667' )
},
bounds : new google.maps.LatLngBounds(), // empty for now, we'll dynamically extend it later
map : new google.maps.Map(
document.getElementById( 'gmap\_m598a1a022fd2980005b84cd459ac7007' ),
{
mapTypeId: google.maps.MapTypeId.ROADMAP,
center: new google.maps.LatLng( 0, 0 ),
zoom: 16 // Seems to be a good zoom for a single point
}
),
markers : {},
}; // end of gmap
// Extend the bounds of interest based on our positions
for ( var m in gmap\_m598a1a022fd2980005b84cd459ac7007.positions ) {
gmap\_m598a1a022fd2980005b84cd459ac7007.bounds.extend( gmap\_m598a1a022fd2980005b84cd459ac7007.positions[m] );
}
// Render markers
for ( var m in gmap\_m598a1a022fd2980005b84cd459ac7007.positions ) {
gmap\_m598a1a022fd2980005b84cd459ac7007.markers[m] = new google.maps.Marker( {
clickable: true,
map : gmap\_m598a1a022fd2980005b84cd459ac7007.map,
position : gmap\_m598a1a022fd2980005b84cd459ac7007.positions[m]
} );
}
// Redraw map to fit our new marker-based bounds
gmap\_m598a1a022fd2980005b84cd459ac7007.map.setCenter( gmap\_m598a1a022fd2980005b84cd459ac7007.positions[940] );
});