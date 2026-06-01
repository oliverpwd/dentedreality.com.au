---
title: Connect 4 With a LadyBoy
date: '2006-12-26T09:11:16+00:00'
format: image
service: flickr
tags:
- beau
- beaulebens
- connect4
- connectfour
- ladyboy
- me
- phuket
- thailand
- thailand06
image: http://i1.wp.com/dentedreality.com.au/wp-content/uploads/2006/12/348103863_e77301a313_o.jpg?resize=607%2C455
---

[![Connect 4 With a LadyBoy](http://i1.wp.com/dentedreality.com.au/wp-content/uploads/2006/12/348103863_e77301a313_o.jpg?resize=607%2C455)](http://dentedreality.com.au/2006/12/26/connect-4-with-a-ladyboy/) 
# [Connect 4 With a LadyBoy](http://dentedreality.com.au/2006/12/26/connect-4-with-a-ladyboy/)

Notice that I’m green, and I’m about to win.





* #[beau](http://dentedreality.com.au/tags/beau/)
* #[beaulebens](http://dentedreality.com.au/tags/beaulebens/)
* #[connect4](http://dentedreality.com.au/tags/connect4/)
* #[connectfour](http://dentedreality.com.au/tags/connectfour/)
* #[ladyboy](http://dentedreality.com.au/tags/ladyboy/)
* #[me](http://dentedreality.com.au/tags/me/)
* #[phuket](http://dentedreality.com.au/tags/phuket/)
* #[thailand](http://dentedreality.com.au/tags/thailand/)
* #[thailand06](http://dentedreality.com.au/tags/thailand06/)

Posted on [Flickr](http://www.flickr.com/photos/borkazoid/348103863/) [9:11 am, December 26, 2006](http://dentedreality.com.au/2006/12/26/connect-4-with-a-ladyboy/ "9:11 am") 
jQuery(document).ready(function(){
var gmap\_m1e0135a5910fcfff776c0098c44493bd = {
positions : {
312 : new google.maps.LatLng( '7.896794', '98.295879' )
},
bounds : new google.maps.LatLngBounds(), // empty for now, we'll dynamically extend it later
map : new google.maps.Map(
document.getElementById( 'gmap\_m1e0135a5910fcfff776c0098c44493bd' ),
{
mapTypeId: google.maps.MapTypeId.ROADMAP,
center: new google.maps.LatLng( 0, 0 ),
zoom: 16 // Seems to be a good zoom for a single point
}
),
markers : {},
}; // end of gmap
// Extend the bounds of interest based on our positions
for ( var m in gmap\_m1e0135a5910fcfff776c0098c44493bd.positions ) {
gmap\_m1e0135a5910fcfff776c0098c44493bd.bounds.extend( gmap\_m1e0135a5910fcfff776c0098c44493bd.positions[m] );
}
// Render markers
for ( var m in gmap\_m1e0135a5910fcfff776c0098c44493bd.positions ) {
gmap\_m1e0135a5910fcfff776c0098c44493bd.markers[m] = new google.maps.Marker( {
clickable: true,
map : gmap\_m1e0135a5910fcfff776c0098c44493bd.map,
position : gmap\_m1e0135a5910fcfff776c0098c44493bd.positions[m]
} );
}
// Redraw map to fit our new marker-based bounds
gmap\_m1e0135a5910fcfff776c0098c44493bd.map.setCenter( gmap\_m1e0135a5910fcfff776c0098c44493bd.positions[312] );
});