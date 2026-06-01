---
title: View
date: '2010-04-29T13:59:21+00:00'
format: image
service: flickr
tags:
- bridge
- city
- sanfrancisco
- view
image: http://i1.wp.com/dentedreality.com.au/wp-content/uploads/2010/04/4747050068_105e34e6ba_o.jpg?resize=607%2C455
---

[![View](http://i1.wp.com/dentedreality.com.au/wp-content/uploads/2010/04/4747050068_105e34e6ba_o.jpg?resize=607%2C455)](http://dentedreality.com.au/2010/04/29/view-3/) 
# [View](http://dentedreality.com.au/2010/04/29/view-3/)





* #[bridge](http://dentedreality.com.au/tags/bridge/)
* #[city](http://dentedreality.com.au/tags/city/)
* #[sanfrancisco](http://dentedreality.com.au/tags/sanfrancisco/)
* #[view](http://dentedreality.com.au/tags/view/)

Posted on [Flickr](http://www.flickr.com/photos/borkazoid/4747050068/) [1:59 pm, April 29, 2010](http://dentedreality.com.au/2010/04/29/view-3/ "1:59 pm") 
jQuery(document).ready(function(){
var gmap\_m7dc22f6c127427e4e861576fce1f65f9 = {
positions : {
130 : new google.maps.LatLng( '37.785833', '-122.392334' )
},
bounds : new google.maps.LatLngBounds(), // empty for now, we'll dynamically extend it later
map : new google.maps.Map(
document.getElementById( 'gmap\_m7dc22f6c127427e4e861576fce1f65f9' ),
{
mapTypeId: google.maps.MapTypeId.ROADMAP,
center: new google.maps.LatLng( 0, 0 ),
zoom: 16 // Seems to be a good zoom for a single point
}
),
markers : {},
}; // end of gmap
// Extend the bounds of interest based on our positions
for ( var m in gmap\_m7dc22f6c127427e4e861576fce1f65f9.positions ) {
gmap\_m7dc22f6c127427e4e861576fce1f65f9.bounds.extend( gmap\_m7dc22f6c127427e4e861576fce1f65f9.positions[m] );
}
// Render markers
for ( var m in gmap\_m7dc22f6c127427e4e861576fce1f65f9.positions ) {
gmap\_m7dc22f6c127427e4e861576fce1f65f9.markers[m] = new google.maps.Marker( {
clickable: true,
map : gmap\_m7dc22f6c127427e4e861576fce1f65f9.map,
position : gmap\_m7dc22f6c127427e4e861576fce1f65f9.positions[m]
} );
}
// Redraw map to fit our new marker-based bounds
gmap\_m7dc22f6c127427e4e861576fce1f65f9.map.setCenter( gmap\_m7dc22f6c127427e4e861576fce1f65f9.positions[130] );
});