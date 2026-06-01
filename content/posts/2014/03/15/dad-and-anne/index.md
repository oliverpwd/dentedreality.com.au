---
title: Dad and Anne
date: '2014-03-15T17:09:34+00:00'
format: image
service: flickr
tags:
- anne
- craig
- dad
- perth
image: http://i0.wp.com/dentedreality.com.au/wp-content/uploads/2014/03/13904721542_22fc93a83d_o.jpg?resize=607%2C455
---

[![Dad and Anne](http://i0.wp.com/dentedreality.com.au/wp-content/uploads/2014/03/13904721542_22fc93a83d_o.jpg?resize=607%2C455)](http://dentedreality.com.au/2014/03/15/dad-and-anne/) 
# [Dad and Anne](http://dentedreality.com.au/2014/03/15/dad-and-anne/)

Perth, Mooloolaba and Melbourne





* #[anne](http://dentedreality.com.au/tags/anne/)
* #[craig](http://dentedreality.com.au/tags/craig/)
* #[dad](http://dentedreality.com.au/tags/dad/)
* #[perth](http://dentedreality.com.au/tags/perth/)

Posted on [Flickr](http://www.flickr.com/photos/borkazoid/13904721542/) [5:09 pm, March 15, 2014](http://dentedreality.com.au/2014/03/15/dad-and-anne/ "5:09 pm") 
jQuery(document).ready(function(){
var gmap\_m15acf9789bb0da01856c70b2a09735a5 = {
positions : {
598 : new google.maps.LatLng( '-32.053106', '115.846375' )
},
bounds : new google.maps.LatLngBounds(), // empty for now, we'll dynamically extend it later
map : new google.maps.Map(
document.getElementById( 'gmap\_m15acf9789bb0da01856c70b2a09735a5' ),
{
mapTypeId: google.maps.MapTypeId.ROADMAP,
center: new google.maps.LatLng( 0, 0 ),
zoom: 16 // Seems to be a good zoom for a single point
}
),
markers : {},
}; // end of gmap
// Extend the bounds of interest based on our positions
for ( var m in gmap\_m15acf9789bb0da01856c70b2a09735a5.positions ) {
gmap\_m15acf9789bb0da01856c70b2a09735a5.bounds.extend( gmap\_m15acf9789bb0da01856c70b2a09735a5.positions[m] );
}
// Render markers
for ( var m in gmap\_m15acf9789bb0da01856c70b2a09735a5.positions ) {
gmap\_m15acf9789bb0da01856c70b2a09735a5.markers[m] = new google.maps.Marker( {
clickable: true,
map : gmap\_m15acf9789bb0da01856c70b2a09735a5.map,
position : gmap\_m15acf9789bb0da01856c70b2a09735a5.positions[m]
} );
}
// Redraw map to fit our new marker-based bounds
gmap\_m15acf9789bb0da01856c70b2a09735a5.map.setCenter( gmap\_m15acf9789bb0da01856c70b2a09735a5.positions[598] );
});