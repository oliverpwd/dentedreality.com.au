---
title: Epic Australian Adventure, 2014
date: '2014-03-11T14:13:49+00:00'
format: image
service: flickr
tags:
- perth
image: http://i1.wp.com/dentedreality.com.au/wp-content/uploads/2014/03/13904700871_83ebac3374_o.jpg?resize=607%2C455
---

[![Epic Australian Adventure, 2014](http://i1.wp.com/dentedreality.com.au/wp-content/uploads/2014/03/13904700871_83ebac3374_o.jpg?resize=607%2C455)](http://dentedreality.com.au/2014/03/11/epic-australian-adventure-2014-55/) 
# [Epic Australian Adventure, 2014](http://dentedreality.com.au/2014/03/11/epic-australian-adventure-2014-55/)

Perth, Mooloolaba and Melbourne





* #[perth](http://dentedreality.com.au/tags/perth/)

Posted on [Flickr](http://www.flickr.com/photos/borkazoid/13904700871/) [2:13 pm, March 11, 2014](http://dentedreality.com.au/2014/03/11/epic-australian-adventure-2014-55/ "2:13 pm") 
jQuery(document).ready(function(){
var gmap\_m101e8aae4fad55561d100693bf4ecaef = {
positions : {
85 : new google.maps.LatLng( '-32.058887', '115.742866' )
},
bounds : new google.maps.LatLngBounds(), // empty for now, we'll dynamically extend it later
map : new google.maps.Map(
document.getElementById( 'gmap\_m101e8aae4fad55561d100693bf4ecaef' ),
{
mapTypeId: google.maps.MapTypeId.ROADMAP,
center: new google.maps.LatLng( 0, 0 ),
zoom: 16 // Seems to be a good zoom for a single point
}
),
markers : {},
}; // end of gmap
// Extend the bounds of interest based on our positions
for ( var m in gmap\_m101e8aae4fad55561d100693bf4ecaef.positions ) {
gmap\_m101e8aae4fad55561d100693bf4ecaef.bounds.extend( gmap\_m101e8aae4fad55561d100693bf4ecaef.positions[m] );
}
// Render markers
for ( var m in gmap\_m101e8aae4fad55561d100693bf4ecaef.positions ) {
gmap\_m101e8aae4fad55561d100693bf4ecaef.markers[m] = new google.maps.Marker( {
clickable: true,
map : gmap\_m101e8aae4fad55561d100693bf4ecaef.map,
position : gmap\_m101e8aae4fad55561d100693bf4ecaef.positions[m]
} );
}
// Redraw map to fit our new marker-based bounds
gmap\_m101e8aae4fad55561d100693bf4ecaef.map.setCenter( gmap\_m101e8aae4fad55561d100693bf4ecaef.positions[85] );
});