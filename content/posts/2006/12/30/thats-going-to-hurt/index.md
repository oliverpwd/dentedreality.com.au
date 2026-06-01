---
title: That’s Going to Hurt
date: '2006-12-30T04:22:04+00:00'
format: image
service: flickr
tags:
- boxing
- fight
- muaythai
- phuket
- thaiboxing
- thailand
- thailand06
image: http://i0.wp.com/dentedreality.com.au/wp-content/uploads/2006/12/349558524_bf09c6344d_o.jpg?resize=607%2C455
---

[![That's Going to Hurt](http://i0.wp.com/dentedreality.com.au/wp-content/uploads/2006/12/349558524_bf09c6344d_o.jpg?resize=607%2C455)](http://dentedreality.com.au/2006/12/30/thats-going-to-hurt/) 
# [That’s Going to Hurt](http://dentedreality.com.au/2006/12/30/thats-going-to-hurt/)





* #[boxing](http://dentedreality.com.au/tags/boxing/)
* #[fight](http://dentedreality.com.au/tags/fight/)
* #[muaythai](http://dentedreality.com.au/tags/muaythai/)
* #[phuket](http://dentedreality.com.au/tags/phuket/)
* #[thaiboxing](http://dentedreality.com.au/tags/thaiboxing/)
* #[thailand](http://dentedreality.com.au/tags/thailand/)
* #[thailand06](http://dentedreality.com.au/tags/thailand06/)

Posted on [Flickr](http://www.flickr.com/photos/borkazoid/349558524/) [4:22 am, December 30, 2006](http://dentedreality.com.au/2006/12/30/thats-going-to-hurt/ "4:22 am") 
jQuery(document).ready(function(){
var gmap\_m09c1803458783e86a46955ef5f667cdd = {
positions : {
531 : new google.maps.LatLng( '7.896794', '98.295879' )
},
bounds : new google.maps.LatLngBounds(), // empty for now, we'll dynamically extend it later
map : new google.maps.Map(
document.getElementById( 'gmap\_m09c1803458783e86a46955ef5f667cdd' ),
{
mapTypeId: google.maps.MapTypeId.ROADMAP,
center: new google.maps.LatLng( 0, 0 ),
zoom: 16 // Seems to be a good zoom for a single point
}
),
markers : {},
}; // end of gmap
// Extend the bounds of interest based on our positions
for ( var m in gmap\_m09c1803458783e86a46955ef5f667cdd.positions ) {
gmap\_m09c1803458783e86a46955ef5f667cdd.bounds.extend( gmap\_m09c1803458783e86a46955ef5f667cdd.positions[m] );
}
// Render markers
for ( var m in gmap\_m09c1803458783e86a46955ef5f667cdd.positions ) {
gmap\_m09c1803458783e86a46955ef5f667cdd.markers[m] = new google.maps.Marker( {
clickable: true,
map : gmap\_m09c1803458783e86a46955ef5f667cdd.map,
position : gmap\_m09c1803458783e86a46955ef5f667cdd.positions[m]
} );
}
// Redraw map to fit our new marker-based bounds
gmap\_m09c1803458783e86a46955ef5f667cdd.map.setCenter( gmap\_m09c1803458783e86a46955ef5f667cdd.positions[531] );
});