---
title: Loaded, Ready To Head Home
date: '2006-11-26T08:32:58+00:00'
format: image
service: flickr
tags:
- backpack
- beau
- beaulebens
- bigsur
- bottchersgap
- california
- hiking
- lospadresnationalpark
- me
- pack
image: http://i1.wp.com/dentedreality.com.au/wp-content/uploads/2006/11/308097084_2f31e4ca6c_o.jpg?resize=607%2C809
---

[![Loaded, Ready To Head Home](http://i1.wp.com/dentedreality.com.au/wp-content/uploads/2006/11/308097084_2f31e4ca6c_o.jpg?resize=607%2C809)](http://dentedreality.com.au/2006/11/26/loaded-ready-to-head-home/) 
# [Loaded, Ready To Head Home](http://dentedreality.com.au/2006/11/26/loaded-ready-to-head-home/)

This was me, packed up and getting ready to make the hike back down to Bottcher’s Gap and then head home.





* #[backpack](http://dentedreality.com.au/tags/backpack/)
* #[beau](http://dentedreality.com.au/tags/beau/)
* #[beaulebens](http://dentedreality.com.au/tags/beaulebens/)
* #[bigsur](http://dentedreality.com.au/tags/bigsur/)
* #[bottchersgap](http://dentedreality.com.au/tags/bottchersgap/)
* #[california](http://dentedreality.com.au/tags/california/)
* #[hiking](http://dentedreality.com.au/tags/hiking/)
* #[lospadresnationalpark](http://dentedreality.com.au/tags/lospadresnationalpark/)
* #[me](http://dentedreality.com.au/tags/me/)
* #[pack](http://dentedreality.com.au/tags/pack/)

Posted on [Flickr](http://www.flickr.com/photos/borkazoid/308097084/) [8:32 am, November 26, 2006](http://dentedreality.com.au/2006/11/26/loaded-ready-to-head-home/ "8:32 am") 
jQuery(document).ready(function(){
var gmap\_mdb989690c0c7703328b572de3634f9f7 = {
positions : {
179 : new google.maps.LatLng( '36.34389', '-121.776409' )
},
bounds : new google.maps.LatLngBounds(), // empty for now, we'll dynamically extend it later
map : new google.maps.Map(
document.getElementById( 'gmap\_mdb989690c0c7703328b572de3634f9f7' ),
{
mapTypeId: google.maps.MapTypeId.ROADMAP,
center: new google.maps.LatLng( 0, 0 ),
zoom: 16 // Seems to be a good zoom for a single point
}
),
markers : {},
}; // end of gmap
// Extend the bounds of interest based on our positions
for ( var m in gmap\_mdb989690c0c7703328b572de3634f9f7.positions ) {
gmap\_mdb989690c0c7703328b572de3634f9f7.bounds.extend( gmap\_mdb989690c0c7703328b572de3634f9f7.positions[m] );
}
// Render markers
for ( var m in gmap\_mdb989690c0c7703328b572de3634f9f7.positions ) {
gmap\_mdb989690c0c7703328b572de3634f9f7.markers[m] = new google.maps.Marker( {
clickable: true,
map : gmap\_mdb989690c0c7703328b572de3634f9f7.map,
position : gmap\_mdb989690c0c7703328b572de3634f9f7.positions[m]
} );
}
// Redraw map to fit our new marker-based bounds
gmap\_mdb989690c0c7703328b572de3634f9f7.map.setCenter( gmap\_mdb989690c0c7703328b572de3634f9f7.positions[179] );
});