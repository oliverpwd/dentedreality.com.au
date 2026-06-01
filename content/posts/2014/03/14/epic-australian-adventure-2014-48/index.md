---
title: Epic Australian Adventure, 2014
date: '2014-03-14T09:51:40+00:00'
format: image
service: flickr
tags:
- perth
image: http://i2.wp.com/dentedreality.com.au/wp-content/uploads/2014/03/13927878403_97e6d3b1b0_o.jpg?resize=607%2C455
---

[![Epic Australian Adventure, 2014](http://i2.wp.com/dentedreality.com.au/wp-content/uploads/2014/03/13927878403_97e6d3b1b0_o.jpg?resize=607%2C455)](http://dentedreality.com.au/2014/03/14/epic-australian-adventure-2014-48/) 
# [Epic Australian Adventure, 2014](http://dentedreality.com.au/2014/03/14/epic-australian-adventure-2014-48/)

Perth, Mooloolaba and Melbourne





* #[perth](http://dentedreality.com.au/tags/perth/)

Posted on [Flickr](http://www.flickr.com/photos/borkazoid/13927878403/) [9:51 am, March 14, 2014](http://dentedreality.com.au/2014/03/14/epic-australian-adventure-2014-48/ "9:51 am") 
jQuery(document).ready(function(){
var gmap\_m5d8c59f6a2ee6b16c22f936c9c048c5c = {
positions : {
679 : new google.maps.LatLng( '-31.945853', '115.824013' )
},
bounds : new google.maps.LatLngBounds(), // empty for now, we'll dynamically extend it later
map : new google.maps.Map(
document.getElementById( 'gmap\_m5d8c59f6a2ee6b16c22f936c9c048c5c' ),
{
mapTypeId: google.maps.MapTypeId.ROADMAP,
center: new google.maps.LatLng( 0, 0 ),
zoom: 16 // Seems to be a good zoom for a single point
}
),
markers : {},
}; // end of gmap
// Extend the bounds of interest based on our positions
for ( var m in gmap\_m5d8c59f6a2ee6b16c22f936c9c048c5c.positions ) {
gmap\_m5d8c59f6a2ee6b16c22f936c9c048c5c.bounds.extend( gmap\_m5d8c59f6a2ee6b16c22f936c9c048c5c.positions[m] );
}
// Render markers
for ( var m in gmap\_m5d8c59f6a2ee6b16c22f936c9c048c5c.positions ) {
gmap\_m5d8c59f6a2ee6b16c22f936c9c048c5c.markers[m] = new google.maps.Marker( {
clickable: true,
map : gmap\_m5d8c59f6a2ee6b16c22f936c9c048c5c.map,
position : gmap\_m5d8c59f6a2ee6b16c22f936c9c048c5c.positions[m]
} );
}
// Redraw map to fit our new marker-based bounds
gmap\_m5d8c59f6a2ee6b16c22f936c9c048c5c.map.setCenter( gmap\_m5d8c59f6a2ee6b16c22f936c9c048c5c.positions[679] );
});