---
title: Busy Bangla Road
date: '2006-12-26T06:11:55+00:00'
format: image
service: flickr
tags:
- bangla
- banglaroad
- bars
- busy
- people
- phuket
- thailand
- thailand06
image: http://i1.wp.com/dentedreality.com.au/wp-content/uploads/2006/12/348104245_0b51c7eb4a_o.jpg?resize=607%2C455
---

[![Busy Bangla Road](http://i1.wp.com/dentedreality.com.au/wp-content/uploads/2006/12/348104245_0b51c7eb4a_o.jpg?resize=607%2C455)](http://dentedreality.com.au/2006/12/26/busy-bangla-road/) 
# [Busy Bangla Road](http://dentedreality.com.au/2006/12/26/busy-bangla-road/)

This is in one of the many bar-buildings. They are these weird buildings which contain around 20 different bars, each of which is operated independently and is only big enough for about 20-ish people to sit at a bar.





* #[bangla](http://dentedreality.com.au/tags/bangla/)
* #[banglaroad](http://dentedreality.com.au/tags/banglaroad/)
* #[bars](http://dentedreality.com.au/tags/bars/)
* #[busy](http://dentedreality.com.au/tags/busy/)
* #[people](http://dentedreality.com.au/tags/people/)
* #[phuket](http://dentedreality.com.au/tags/phuket/)
* #[thailand](http://dentedreality.com.au/tags/thailand/)
* #[thailand06](http://dentedreality.com.au/tags/thailand06/)

Posted on [Flickr](http://www.flickr.com/photos/borkazoid/348104245/) [6:11 am, December 26, 2006](http://dentedreality.com.au/2006/12/26/busy-bangla-road/ "6:11 am") 
jQuery(document).ready(function(){
var gmap\_mc7f2658d813f511019d1f940d96b6c33 = {
positions : {
124 : new google.maps.LatLng( '7.896794', '98.295879' )
},
bounds : new google.maps.LatLngBounds(), // empty for now, we'll dynamically extend it later
map : new google.maps.Map(
document.getElementById( 'gmap\_mc7f2658d813f511019d1f940d96b6c33' ),
{
mapTypeId: google.maps.MapTypeId.ROADMAP,
center: new google.maps.LatLng( 0, 0 ),
zoom: 16 // Seems to be a good zoom for a single point
}
),
markers : {},
}; // end of gmap
// Extend the bounds of interest based on our positions
for ( var m in gmap\_mc7f2658d813f511019d1f940d96b6c33.positions ) {
gmap\_mc7f2658d813f511019d1f940d96b6c33.bounds.extend( gmap\_mc7f2658d813f511019d1f940d96b6c33.positions[m] );
}
// Render markers
for ( var m in gmap\_mc7f2658d813f511019d1f940d96b6c33.positions ) {
gmap\_mc7f2658d813f511019d1f940d96b6c33.markers[m] = new google.maps.Marker( {
clickable: true,
map : gmap\_mc7f2658d813f511019d1f940d96b6c33.map,
position : gmap\_mc7f2658d813f511019d1f940d96b6c33.positions[m]
} );
}
// Redraw map to fit our new marker-based bounds
gmap\_mc7f2658d813f511019d1f940d96b6c33.map.setCenter( gmap\_mc7f2658d813f511019d1f940d96b6c33.positions[124] );
});