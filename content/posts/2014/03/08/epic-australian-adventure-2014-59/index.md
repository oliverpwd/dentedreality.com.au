---
title: Epic Australian Adventure, 2014
date: '2014-03-08T09:02:15+00:00'
format: image
service: flickr
image: http://i2.wp.com/dentedreality.com.au/wp-content/uploads/2014/03/13904696481_b5659ec2f7_o.jpg?resize=607%2C455
---

[![Epic Australian Adventure, 2014](http://i2.wp.com/dentedreality.com.au/wp-content/uploads/2014/03/13904696481_b5659ec2f7_o.jpg?resize=607%2C455)](http://dentedreality.com.au/2014/03/08/epic-australian-adventure-2014-59/) 
# [Epic Australian Adventure, 2014](http://dentedreality.com.au/2014/03/08/epic-australian-adventure-2014-59/)

Perth, Mooloolaba and Melbourne





Posted on [Flickr](http://www.flickr.com/photos/borkazoid/13904696481/) [9:02 am, March 8, 2014](http://dentedreality.com.au/2014/03/08/epic-australian-adventure-2014-59/ "9:02 am") 
jQuery(document).ready(function(){
var gmap\_m181b9f81a7fa14c08413add9645a9062 = {
positions : {
506 : new google.maps.LatLng( '-33.93142', '151.168258' )
},
bounds : new google.maps.LatLngBounds(), // empty for now, we'll dynamically extend it later
map : new google.maps.Map(
document.getElementById( 'gmap\_m181b9f81a7fa14c08413add9645a9062' ),
{
mapTypeId: google.maps.MapTypeId.ROADMAP,
center: new google.maps.LatLng( 0, 0 ),
zoom: 16 // Seems to be a good zoom for a single point
}
),
markers : {},
}; // end of gmap
// Extend the bounds of interest based on our positions
for ( var m in gmap\_m181b9f81a7fa14c08413add9645a9062.positions ) {
gmap\_m181b9f81a7fa14c08413add9645a9062.bounds.extend( gmap\_m181b9f81a7fa14c08413add9645a9062.positions[m] );
}
// Render markers
for ( var m in gmap\_m181b9f81a7fa14c08413add9645a9062.positions ) {
gmap\_m181b9f81a7fa14c08413add9645a9062.markers[m] = new google.maps.Marker( {
clickable: true,
map : gmap\_m181b9f81a7fa14c08413add9645a9062.map,
position : gmap\_m181b9f81a7fa14c08413add9645a9062.positions[m]
} );
}
// Redraw map to fit our new marker-based bounds
gmap\_m181b9f81a7fa14c08413add9645a9062.map.setCenter( gmap\_m181b9f81a7fa14c08413add9645a9062.positions[506] );
});