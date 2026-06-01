---
title: The Naked and Famous
date: '2011-12-19T18:41:21+00:00'
format: image
service: flickr
tags:
- band
- livemusic
- music
- theindependent
- thenakedandfamous
- tnaf
image: http://i1.wp.com/dentedreality.com.au/wp-content/uploads/2011/12/6813291748_8dcf14dfca_o.jpg?resize=607%2C452
---

[![The Naked and Famous](http://i1.wp.com/dentedreality.com.au/wp-content/uploads/2011/12/6813291748_8dcf14dfca_o.jpg?resize=607%2C452)](http://dentedreality.com.au/2011/12/19/the-naked-and-famous/) 
# [The Naked and Famous](http://dentedreality.com.au/2011/12/19/the-naked-and-famous/)





* #[band](http://dentedreality.com.au/tags/band/)
* #[livemusic](http://dentedreality.com.au/tags/livemusic/)
* #[music](http://dentedreality.com.au/tags/music/)
* #[theindependent](http://dentedreality.com.au/tags/theindependent/)
* #[thenakedandfamous](http://dentedreality.com.au/tags/thenakedandfamous/)
* #[tnaf](http://dentedreality.com.au/tags/tnaf/)

Posted on [Flickr](http://www.flickr.com/photos/borkazoid/6813291748/) [6:41 pm, December 19, 2011](http://dentedreality.com.au/2011/12/19/the-naked-and-famous/ "6:41 pm") 
jQuery(document).ready(function(){
var gmap\_mf8728de785b22c1146b511b80313bb34 = {
positions : {
364 : new google.maps.LatLng( '37.7755', '-122.437667' )
},
bounds : new google.maps.LatLngBounds(), // empty for now, we'll dynamically extend it later
map : new google.maps.Map(
document.getElementById( 'gmap\_mf8728de785b22c1146b511b80313bb34' ),
{
mapTypeId: google.maps.MapTypeId.ROADMAP,
center: new google.maps.LatLng( 0, 0 ),
zoom: 16 // Seems to be a good zoom for a single point
}
),
markers : {},
}; // end of gmap
// Extend the bounds of interest based on our positions
for ( var m in gmap\_mf8728de785b22c1146b511b80313bb34.positions ) {
gmap\_mf8728de785b22c1146b511b80313bb34.bounds.extend( gmap\_mf8728de785b22c1146b511b80313bb34.positions[m] );
}
// Render markers
for ( var m in gmap\_mf8728de785b22c1146b511b80313bb34.positions ) {
gmap\_mf8728de785b22c1146b511b80313bb34.markers[m] = new google.maps.Marker( {
clickable: true,
map : gmap\_mf8728de785b22c1146b511b80313bb34.map,
position : gmap\_mf8728de785b22c1146b511b80313bb34.positions[m]
} );
}
// Redraw map to fit our new marker-based bounds
gmap\_mf8728de785b22c1146b511b80313bb34.map.setCenter( gmap\_mf8728de785b22c1146b511b80313bb34.positions[364] );
});