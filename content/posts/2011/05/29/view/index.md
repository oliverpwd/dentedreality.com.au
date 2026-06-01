---
title: View
date: '2011-05-29T11:11:22+00:00'
format: image
service: flickr
tags:
- owenswedding
- wedding
image: http://i2.wp.com/dentedreality.com.au/wp-content/uploads/2011/05/5802875067_9ca1dfc2a3_o.jpg?resize=607%2C452
---

[![View](http://i2.wp.com/dentedreality.com.au/wp-content/uploads/2011/05/5802875067_9ca1dfc2a3_o.jpg?resize=607%2C452)](http://dentedreality.com.au/2011/05/29/view/) 
# [View](http://dentedreality.com.au/2011/05/29/view/)





* #[owenswedding](http://dentedreality.com.au/tags/owenswedding/)
* #[wedding](http://dentedreality.com.au/tags/wedding/)

Posted on [Flickr](http://www.flickr.com/photos/borkazoid/5802875067/) [11:11 am, May 29, 2011](http://dentedreality.com.au/2011/05/29/view/ "11:11 am") 
jQuery(document).ready(function(){
var gmap\_mcbdd83aa8c58280494fafc517e4632b4 = {
positions : {
176 : new google.maps.LatLng( '37.776333', '-122.393667' )
},
bounds : new google.maps.LatLngBounds(), // empty for now, we'll dynamically extend it later
map : new google.maps.Map(
document.getElementById( 'gmap\_mcbdd83aa8c58280494fafc517e4632b4' ),
{
mapTypeId: google.maps.MapTypeId.ROADMAP,
center: new google.maps.LatLng( 0, 0 ),
zoom: 16 // Seems to be a good zoom for a single point
}
),
markers : {},
}; // end of gmap
// Extend the bounds of interest based on our positions
for ( var m in gmap\_mcbdd83aa8c58280494fafc517e4632b4.positions ) {
gmap\_mcbdd83aa8c58280494fafc517e4632b4.bounds.extend( gmap\_mcbdd83aa8c58280494fafc517e4632b4.positions[m] );
}
// Render markers
for ( var m in gmap\_mcbdd83aa8c58280494fafc517e4632b4.positions ) {
gmap\_mcbdd83aa8c58280494fafc517e4632b4.markers[m] = new google.maps.Marker( {
clickable: true,
map : gmap\_mcbdd83aa8c58280494fafc517e4632b4.map,
position : gmap\_mcbdd83aa8c58280494fafc517e4632b4.positions[m]
} );
}
// Redraw map to fit our new marker-based bounds
gmap\_mcbdd83aa8c58280494fafc517e4632b4.map.setCenter( gmap\_mcbdd83aa8c58280494fafc517e4632b4.positions[176] );
});