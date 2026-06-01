---
title: Tiger Snake
date: '2008-04-07T15:38:32-06:00'
format: image
service: flickr
tags:
- australia
- snake
- tigersnake
- westernaustraliabremerbay
latitude: '-34.36859'
longitude: '119.322681'
image: https://dentedreality-content.s3.amazonaws.com/wp-content/uploads/2008/04/14184656/2433446920_32a58c8570_o.jpg
---

[![Tiger Snake](https://dentedreality-content.s3.amazonaws.com/wp-content/uploads/2008/04/14184656/2433446920_32a58c8570_o.jpg)](https://dentedreality.com.au/2008/04/07/tiger-snake/) 
# [Tiger Snake](https://dentedreality.com.au/2008/04/07/tiger-snake/)

[![Tiger Snake](https://dentedreality-content.s3.amazonaws.com/wp-content/uploads/2008/04/14184656/2433446920_32a58c8570_o.jpg)](http://www.flickr.com/photos/borkazoid/2433446920/)

Driving around near Bremer is like being on a safari, you just pull over to see the wildlife. This was a pretty big one – a couple meters long.

-34.36859119.322681




* #[australia](https://dentedreality.com.au/tags/australia/)
* #[snake](https://dentedreality.com.au/tags/snake/)
* #[tigersnake](https://dentedreality.com.au/tags/tigersnake/)
* #[westernaustraliabremerbay](https://dentedreality.com.au/tags/westernaustraliabremerbay/)

Posted on [Flickr](http://www.flickr.com/photos/borkazoid/2433446920/) [3:38 pm, April 7, 2008](https://dentedreality.com.au/2008/04/07/tiger-snake/ "3:38 pm") 
jQuery(document).ready(function(){
var gmap\_m8d19de24119ba50e89566e83682ac162 = {
positions : {
122 : new google.maps.LatLng( '-34.36859', '119.322681' )
},
bounds : new google.maps.LatLngBounds(), // empty for now, we'll dynamically extend it later
map : new google.maps.Map(
document.getElementById( 'gmap\_m8d19de24119ba50e89566e83682ac162' ),
{
mapTypeId: google.maps.MapTypeId.ROADMAP,
center: new google.maps.LatLng( 0, 0 ),
zoom: 16 // Seems to be a good zoom for a single point
}
),
markers : {},
}; // end of gmap
// Extend the bounds of interest based on our positions
for ( var m in gmap\_m8d19de24119ba50e89566e83682ac162.positions ) {
gmap\_m8d19de24119ba50e89566e83682ac162.bounds.extend( gmap\_m8d19de24119ba50e89566e83682ac162.positions[m] );
}
// Render markers
for ( var m in gmap\_m8d19de24119ba50e89566e83682ac162.positions ) {
gmap\_m8d19de24119ba50e89566e83682ac162.markers[m] = new google.maps.Marker( {
clickable: true,
map : gmap\_m8d19de24119ba50e89566e83682ac162.map,
position : gmap\_m8d19de24119ba50e89566e83682ac162.positions[m]
} );
}
// Redraw map to fit our new marker-based bounds
gmap\_m8d19de24119ba50e89566e83682ac162.map.setCenter( gmap\_m8d19de24119ba50e89566e83682ac162.positions[122] );
});