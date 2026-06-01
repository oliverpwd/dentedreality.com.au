---
title: Automatticians on a Boat
date: '2011-05-05T12:30:56+00:00'
format: image
service: flickr
tags:
- boat
- francisco
- lori
- sailing
- SAN
- sanfranciscobay
image: http://i2.wp.com/dentedreality.com.au/wp-content/uploads/2011/05/5802706422_82f83d1544_o.jpg?resize=607%2C813
---

[![Automatticians on a Boat](http://i2.wp.com/dentedreality.com.au/wp-content/uploads/2011/05/5802706422_82f83d1544_o.jpg?resize=607%2C813)](http://dentedreality.com.au/2011/05/05/automatticians-on-a-boat-4/) 
# [Automatticians on a Boat](http://dentedreality.com.au/2011/05/05/automatticians-on-a-boat-4/)

Pete took us out sailing on the Bay. It was most awesome.





* #[boat](http://dentedreality.com.au/tags/boat/)
* #[francisco](http://dentedreality.com.au/tags/francisco/)
* #[lori](http://dentedreality.com.au/tags/lori/)
* #[sailing](http://dentedreality.com.au/tags/sailing/)
* #[SAN](http://dentedreality.com.au/tags/san/)
* #[sanfranciscobay](http://dentedreality.com.au/tags/sanfranciscobay/)

Posted on [Flickr](http://www.flickr.com/photos/borkazoid/5802706422/) [12:30 pm, May 5, 2011](http://dentedreality.com.au/2011/05/05/automatticians-on-a-boat-4/ "12:30 pm") 
jQuery(document).ready(function(){
var gmap\_m70d9ea885bbdc1a3e373fb1212084935 = {
positions : {
762 : new google.maps.LatLng( '37.856', '-122.473' )
},
bounds : new google.maps.LatLngBounds(), // empty for now, we'll dynamically extend it later
map : new google.maps.Map(
document.getElementById( 'gmap\_m70d9ea885bbdc1a3e373fb1212084935' ),
{
mapTypeId: google.maps.MapTypeId.ROADMAP,
center: new google.maps.LatLng( 0, 0 ),
zoom: 16 // Seems to be a good zoom for a single point
}
),
markers : {},
}; // end of gmap
// Extend the bounds of interest based on our positions
for ( var m in gmap\_m70d9ea885bbdc1a3e373fb1212084935.positions ) {
gmap\_m70d9ea885bbdc1a3e373fb1212084935.bounds.extend( gmap\_m70d9ea885bbdc1a3e373fb1212084935.positions[m] );
}
// Render markers
for ( var m in gmap\_m70d9ea885bbdc1a3e373fb1212084935.positions ) {
gmap\_m70d9ea885bbdc1a3e373fb1212084935.markers[m] = new google.maps.Marker( {
clickable: true,
map : gmap\_m70d9ea885bbdc1a3e373fb1212084935.map,
position : gmap\_m70d9ea885bbdc1a3e373fb1212084935.positions[m]
} );
}
// Redraw map to fit our new marker-based bounds
gmap\_m70d9ea885bbdc1a3e373fb1212084935.map.setCenter( gmap\_m70d9ea885bbdc1a3e373fb1212084935.positions[762] );
});