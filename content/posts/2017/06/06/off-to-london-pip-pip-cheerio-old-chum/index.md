---
title: ''
date: '2017-06-06T20:03:50+00:00'
format: image
service: instagram
image: https://i1.wp.com/dentedreality.com.au/wp-content/uploads/2017/06/18947632_346055089130827_4716711489371635712_n.jpg?fit=640%2C640&ssl=1
---

[![Off to London. Pip pip cheerio old chum!](https://i1.wp.com/dentedreality.com.au/wp-content/uploads/2017/06/18947632_346055089130827_4716711489371635712_n.jpg?fit=640%2C640&ssl=1)](https://dentedreality.com.au/2017/06/06/off-to-london-pip-pip-cheerio-old-chum/) 

Off to London. Pip pip cheerio old chum!





Posted on [Instagram](https://www.instagram.com/p/BVBVoy1Barq/) [8:03 pm, June 6, 2017](https://dentedreality.com.au/2017/06/06/off-to-london-pip-pip-cheerio-old-chum/ "8:03 pm") 
jQuery(document).ready(function(){
var gmap\_m34e3d93d4dace6906cafa3372b8fcf61 = {
positions : {
816 : new google.maps.LatLng( '41.977518173276', '-87.904465198517' )
},
bounds : new google.maps.LatLngBounds(), // empty for now, we'll dynamically extend it later
map : new google.maps.Map(
document.getElementById( 'gmap\_m34e3d93d4dace6906cafa3372b8fcf61' ),
{
mapTypeId: google.maps.MapTypeId.ROADMAP,
center: new google.maps.LatLng( 0, 0 ),
zoom: 16 // Seems to be a good zoom for a single point
}
),
markers : {},
}; // end of gmap
// Extend the bounds of interest based on our positions
for ( var m in gmap\_m34e3d93d4dace6906cafa3372b8fcf61.positions ) {
gmap\_m34e3d93d4dace6906cafa3372b8fcf61.bounds.extend( gmap\_m34e3d93d4dace6906cafa3372b8fcf61.positions[m] );
}
// Render markers
for ( var m in gmap\_m34e3d93d4dace6906cafa3372b8fcf61.positions ) {
gmap\_m34e3d93d4dace6906cafa3372b8fcf61.markers[m] = new google.maps.Marker( {
clickable: true,
map : gmap\_m34e3d93d4dace6906cafa3372b8fcf61.map,
position : gmap\_m34e3d93d4dace6906cafa3372b8fcf61.positions[m]
} );
}
// Redraw map to fit our new marker-based bounds
gmap\_m34e3d93d4dace6906cafa3372b8fcf61.map.setCenter( gmap\_m34e3d93d4dace6906cafa3372b8fcf61.positions[816] );
});