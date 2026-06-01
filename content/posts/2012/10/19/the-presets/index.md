---
title: The Presets
date: '2012-10-19T19:28:17+00:00'
format: image
service: flickr
tags:
- concert
- livemusic
- music
- thepresets
image: http://i0.wp.com/dentedreality.com.au/wp-content/uploads/2012/10/8245864518_6ea392dac3_o.jpg?resize=607%2C452
---

[![The Presets](http://i0.wp.com/dentedreality.com.au/wp-content/uploads/2012/10/8245864518_6ea392dac3_o.jpg?resize=607%2C452)](http://dentedreality.com.au/2012/10/19/the-presets/) 
# [The Presets](http://dentedreality.com.au/2012/10/19/the-presets/)





* #[concert](http://dentedreality.com.au/tags/concert/)
* #[livemusic](http://dentedreality.com.au/tags/livemusic/)
* #[music](http://dentedreality.com.au/tags/music/)
* #[thepresets](http://dentedreality.com.au/tags/thepresets/)

Posted on [Flickr](http://www.flickr.com/photos/borkazoid/8245864518/) [7:28 pm, October 19, 2012](http://dentedreality.com.au/2012/10/19/the-presets/ "7:28 pm") 
jQuery(document).ready(function(){
var gmap\_m1c8d3e0b58fb6a518ff1672b2942bf6d = {
positions : {
357 : new google.maps.LatLng( '40.7695', '-73.993' )
},
bounds : new google.maps.LatLngBounds(), // empty for now, we'll dynamically extend it later
map : new google.maps.Map(
document.getElementById( 'gmap\_m1c8d3e0b58fb6a518ff1672b2942bf6d' ),
{
mapTypeId: google.maps.MapTypeId.ROADMAP,
center: new google.maps.LatLng( 0, 0 ),
zoom: 16 // Seems to be a good zoom for a single point
}
),
markers : {},
}; // end of gmap
// Extend the bounds of interest based on our positions
for ( var m in gmap\_m1c8d3e0b58fb6a518ff1672b2942bf6d.positions ) {
gmap\_m1c8d3e0b58fb6a518ff1672b2942bf6d.bounds.extend( gmap\_m1c8d3e0b58fb6a518ff1672b2942bf6d.positions[m] );
}
// Render markers
for ( var m in gmap\_m1c8d3e0b58fb6a518ff1672b2942bf6d.positions ) {
gmap\_m1c8d3e0b58fb6a518ff1672b2942bf6d.markers[m] = new google.maps.Marker( {
clickable: true,
map : gmap\_m1c8d3e0b58fb6a518ff1672b2942bf6d.map,
position : gmap\_m1c8d3e0b58fb6a518ff1672b2942bf6d.positions[m]
} );
}
// Redraw map to fit our new marker-based bounds
gmap\_m1c8d3e0b58fb6a518ff1672b2942bf6d.map.setCenter( gmap\_m1c8d3e0b58fb6a518ff1672b2942bf6d.positions[357] );
});