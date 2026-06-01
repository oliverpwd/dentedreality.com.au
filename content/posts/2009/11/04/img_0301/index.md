---
title: IMG_0301
date: '2009-11-04T14:36:13+00:00'
format: image
service: flickr
tags:
- newyork
- wcnyc
- wordcamp
image: http://i0.wp.com/dentedreality.com.au/wp-content/uploads/2009/11/4123180511_883d11627e_o.jpg?resize=607%2C455
---

[![IMG_0301](http://i0.wp.com/dentedreality.com.au/wp-content/uploads/2009/11/4123180511_883d11627e_o.jpg?resize=607%2C455)](http://dentedreality.com.au/2009/11/04/img_0301/) 
# [IMG\_0301](http://dentedreality.com.au/2009/11/04/img_0301/)





* #[newyork](http://dentedreality.com.au/tags/newyork/)
* #[wcnyc](http://dentedreality.com.au/tags/wcnyc/)
* #[wordcamp](http://dentedreality.com.au/tags/wordcamp/)

Posted on [Flickr](http://www.flickr.com/photos/borkazoid/4123180511/) [2:36 pm, November 4, 2009](http://dentedreality.com.au/2009/11/04/img_0301/ "2:36 pm") 
jQuery(document).ready(function(){
var gmap\_m0acd0fe5fbd3b769b72d078cad3966a5 = {
positions : {
757 : new google.maps.LatLng( '37.782166', '-122.388501' )
},
bounds : new google.maps.LatLngBounds(), // empty for now, we'll dynamically extend it later
map : new google.maps.Map(
document.getElementById( 'gmap\_m0acd0fe5fbd3b769b72d078cad3966a5' ),
{
mapTypeId: google.maps.MapTypeId.ROADMAP,
center: new google.maps.LatLng( 0, 0 ),
zoom: 16 // Seems to be a good zoom for a single point
}
),
markers : {},
}; // end of gmap
// Extend the bounds of interest based on our positions
for ( var m in gmap\_m0acd0fe5fbd3b769b72d078cad3966a5.positions ) {
gmap\_m0acd0fe5fbd3b769b72d078cad3966a5.bounds.extend( gmap\_m0acd0fe5fbd3b769b72d078cad3966a5.positions[m] );
}
// Render markers
for ( var m in gmap\_m0acd0fe5fbd3b769b72d078cad3966a5.positions ) {
gmap\_m0acd0fe5fbd3b769b72d078cad3966a5.markers[m] = new google.maps.Marker( {
clickable: true,
map : gmap\_m0acd0fe5fbd3b769b72d078cad3966a5.map,
position : gmap\_m0acd0fe5fbd3b769b72d078cad3966a5.positions[m]
} );
}
// Redraw map to fit our new marker-based bounds
gmap\_m0acd0fe5fbd3b769b72d078cad3966a5.map.setCenter( gmap\_m0acd0fe5fbd3b769b72d078cad3966a5.positions[757] );
});