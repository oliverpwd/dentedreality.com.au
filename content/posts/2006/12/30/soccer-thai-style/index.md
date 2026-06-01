---
title: Soccer, Thai Style
date: '2006-12-30T00:40:50+00:00'
format: image
service: flickr
tags:
- dirt
- football
- phuket
- soccer
- thailand
- thailand06
image: http://i2.wp.com/dentedreality.com.au/wp-content/uploads/2006/12/349562675_086c43bf5c_o.jpg?resize=607%2C455
---

[![Soccer, Thai Style](http://i2.wp.com/dentedreality.com.au/wp-content/uploads/2006/12/349562675_086c43bf5c_o.jpg?resize=607%2C455)](http://dentedreality.com.au/2006/12/30/soccer-thai-style/) 
# [Soccer, Thai Style](http://dentedreality.com.au/2006/12/30/soccer-thai-style/)

On compacted dirt… ouch





* #[dirt](http://dentedreality.com.au/tags/dirt/)
* #[football](http://dentedreality.com.au/tags/football/)
* #[phuket](http://dentedreality.com.au/tags/phuket/)
* #[soccer](http://dentedreality.com.au/tags/soccer/)
* #[thailand](http://dentedreality.com.au/tags/thailand/)
* #[thailand06](http://dentedreality.com.au/tags/thailand06/)

Posted on [Flickr](http://www.flickr.com/photos/borkazoid/349562675/) [12:40 am, December 30, 2006](http://dentedreality.com.au/2006/12/30/soccer-thai-style/ "12:40 am") 
jQuery(document).ready(function(){
var gmap\_m1cd33b78faf60a838890f5dd686bd73d = {
positions : {
15 : new google.maps.LatLng( '7.896794', '98.295879' )
},
bounds : new google.maps.LatLngBounds(), // empty for now, we'll dynamically extend it later
map : new google.maps.Map(
document.getElementById( 'gmap\_m1cd33b78faf60a838890f5dd686bd73d' ),
{
mapTypeId: google.maps.MapTypeId.ROADMAP,
center: new google.maps.LatLng( 0, 0 ),
zoom: 16 // Seems to be a good zoom for a single point
}
),
markers : {},
}; // end of gmap
// Extend the bounds of interest based on our positions
for ( var m in gmap\_m1cd33b78faf60a838890f5dd686bd73d.positions ) {
gmap\_m1cd33b78faf60a838890f5dd686bd73d.bounds.extend( gmap\_m1cd33b78faf60a838890f5dd686bd73d.positions[m] );
}
// Render markers
for ( var m in gmap\_m1cd33b78faf60a838890f5dd686bd73d.positions ) {
gmap\_m1cd33b78faf60a838890f5dd686bd73d.markers[m] = new google.maps.Marker( {
clickable: true,
map : gmap\_m1cd33b78faf60a838890f5dd686bd73d.map,
position : gmap\_m1cd33b78faf60a838890f5dd686bd73d.positions[m]
} );
}
// Redraw map to fit our new marker-based bounds
gmap\_m1cd33b78faf60a838890f5dd686bd73d.map.setCenter( gmap\_m1cd33b78faf60a838890f5dd686bd73d.positions[15] );
});