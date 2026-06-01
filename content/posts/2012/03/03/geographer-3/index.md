---
title: Geographer
date: '2012-03-03T20:01:45+00:00'
format: image
service: flickr
tags:
- band
- geographer
- livemusic
- music
- theindependent
image: http://i2.wp.com/dentedreality.com.au/wp-content/uploads/2012/03/6959579361_103f8155e2_o.jpg?resize=607%2C452
---

[![Geographer](http://i2.wp.com/dentedreality.com.au/wp-content/uploads/2012/03/6959579361_103f8155e2_o.jpg?resize=607%2C452)](http://dentedreality.com.au/2012/03/03/geographer-3/) 
# [Geographer](http://dentedreality.com.au/2012/03/03/geographer-3/)

At The Independent





* #[band](http://dentedreality.com.au/tags/band/)
* #[geographer](http://dentedreality.com.au/tags/geographer/)
* #[livemusic](http://dentedreality.com.au/tags/livemusic/)
* #[music](http://dentedreality.com.au/tags/music/)
* #[theindependent](http://dentedreality.com.au/tags/theindependent/)

Posted on [Flickr](http://www.flickr.com/photos/borkazoid/6959579361/) [8:01 pm, March 3, 2012](http://dentedreality.com.au/2012/03/03/geographer-3/ "8:01 pm") 
jQuery(document).ready(function(){
var gmap\_m6a54877af1a1b2ef86e67bd9bb015bd1 = {
positions : {
311 : new google.maps.LatLng( '37.7755', '-122.437667' )
},
bounds : new google.maps.LatLngBounds(), // empty for now, we'll dynamically extend it later
map : new google.maps.Map(
document.getElementById( 'gmap\_m6a54877af1a1b2ef86e67bd9bb015bd1' ),
{
mapTypeId: google.maps.MapTypeId.ROADMAP,
center: new google.maps.LatLng( 0, 0 ),
zoom: 16 // Seems to be a good zoom for a single point
}
),
markers : {},
}; // end of gmap
// Extend the bounds of interest based on our positions
for ( var m in gmap\_m6a54877af1a1b2ef86e67bd9bb015bd1.positions ) {
gmap\_m6a54877af1a1b2ef86e67bd9bb015bd1.bounds.extend( gmap\_m6a54877af1a1b2ef86e67bd9bb015bd1.positions[m] );
}
// Render markers
for ( var m in gmap\_m6a54877af1a1b2ef86e67bd9bb015bd1.positions ) {
gmap\_m6a54877af1a1b2ef86e67bd9bb015bd1.markers[m] = new google.maps.Marker( {
clickable: true,
map : gmap\_m6a54877af1a1b2ef86e67bd9bb015bd1.map,
position : gmap\_m6a54877af1a1b2ef86e67bd9bb015bd1.positions[m]
} );
}
// Redraw map to fit our new marker-based bounds
gmap\_m6a54877af1a1b2ef86e67bd9bb015bd1.map.setCenter( gmap\_m6a54877af1a1b2ef86e67bd9bb015bd1.positions[311] );
});