---
title: San Diego View
date: '2012-10-26T08:52:02+00:00'
format: image
service: flickr
tags:
- beach
- california
- sandiego
- view
image: http://i2.wp.com/dentedreality.com.au/wp-content/uploads/2012/10/8244798137_0277f80385_o.jpg?resize=607%2C813
---

[![San Diego View](http://i2.wp.com/dentedreality.com.au/wp-content/uploads/2012/10/8244798137_0277f80385_o.jpg?resize=607%2C813)](http://dentedreality.com.au/2012/10/26/san-diego-view/) 
# [San Diego View](http://dentedreality.com.au/2012/10/26/san-diego-view/)

From my window





* #[beach](http://dentedreality.com.au/tags/beach/)
* #[california](http://dentedreality.com.au/tags/california/)
* #[sandiego](http://dentedreality.com.au/tags/sandiego/)
* #[view](http://dentedreality.com.au/tags/view/)

Posted on [Flickr](http://www.flickr.com/photos/borkazoid/8244798137/) [8:52 am, October 26, 2012](http://dentedreality.com.au/2012/10/26/san-diego-view/ "8:52 am") 
jQuery(document).ready(function(){
var gmap\_me75771d48c4e0af24e83bdf58b36f805 = {
positions : {
325 : new google.maps.LatLng( '32.788833', '-117.251667' )
},
bounds : new google.maps.LatLngBounds(), // empty for now, we'll dynamically extend it later
map : new google.maps.Map(
document.getElementById( 'gmap\_me75771d48c4e0af24e83bdf58b36f805' ),
{
mapTypeId: google.maps.MapTypeId.ROADMAP,
center: new google.maps.LatLng( 0, 0 ),
zoom: 16 // Seems to be a good zoom for a single point
}
),
markers : {},
}; // end of gmap
// Extend the bounds of interest based on our positions
for ( var m in gmap\_me75771d48c4e0af24e83bdf58b36f805.positions ) {
gmap\_me75771d48c4e0af24e83bdf58b36f805.bounds.extend( gmap\_me75771d48c4e0af24e83bdf58b36f805.positions[m] );
}
// Render markers
for ( var m in gmap\_me75771d48c4e0af24e83bdf58b36f805.positions ) {
gmap\_me75771d48c4e0af24e83bdf58b36f805.markers[m] = new google.maps.Marker( {
clickable: true,
map : gmap\_me75771d48c4e0af24e83bdf58b36f805.map,
position : gmap\_me75771d48c4e0af24e83bdf58b36f805.positions[m]
} );
}
// Redraw map to fit our new marker-based bounds
gmap\_me75771d48c4e0af24e83bdf58b36f805.map.setCenter( gmap\_me75771d48c4e0af24e83bdf58b36f805.positions[325] );
});