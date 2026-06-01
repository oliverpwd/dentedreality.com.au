---
title: Twilight
date: '2012-06-22T13:44:56+00:00'
format: image
service: flickr
tags:
- brooklyn
- night
- twilight
- view
image: http://i1.wp.com/dentedreality.com.au/wp-content/uploads/2012/06/7911189390_4232bd3c10_o.jpg?resize=607%2C455
---

[![Twilight](http://i1.wp.com/dentedreality.com.au/wp-content/uploads/2012/06/7911189390_4232bd3c10_o.jpg?resize=607%2C455)](http://dentedreality.com.au/2012/06/22/twilight/) 
# [Twilight](http://dentedreality.com.au/2012/06/22/twilight/)





* #[brooklyn](http://dentedreality.com.au/tags/brooklyn/)
* #[night](http://dentedreality.com.au/tags/night/)
* #[twilight](http://dentedreality.com.au/tags/twilight/)
* #[view](http://dentedreality.com.au/tags/view/)

Posted on [Flickr](http://www.flickr.com/photos/borkazoid/7911189390/) [1:44 pm, June 22, 2012](http://dentedreality.com.au/2012/06/22/twilight/ "1:44 pm") 
jQuery(document).ready(function(){
var gmap\_m11ba678336bbf6598a5fa6657a4a2513 = {
positions : {
470 : new google.maps.LatLng( '40.669316', '-73.985012' )
},
bounds : new google.maps.LatLngBounds(), // empty for now, we'll dynamically extend it later
map : new google.maps.Map(
document.getElementById( 'gmap\_m11ba678336bbf6598a5fa6657a4a2513' ),
{
mapTypeId: google.maps.MapTypeId.ROADMAP,
center: new google.maps.LatLng( 0, 0 ),
zoom: 16 // Seems to be a good zoom for a single point
}
),
markers : {},
}; // end of gmap
// Extend the bounds of interest based on our positions
for ( var m in gmap\_m11ba678336bbf6598a5fa6657a4a2513.positions ) {
gmap\_m11ba678336bbf6598a5fa6657a4a2513.bounds.extend( gmap\_m11ba678336bbf6598a5fa6657a4a2513.positions[m] );
}
// Render markers
for ( var m in gmap\_m11ba678336bbf6598a5fa6657a4a2513.positions ) {
gmap\_m11ba678336bbf6598a5fa6657a4a2513.markers[m] = new google.maps.Marker( {
clickable: true,
map : gmap\_m11ba678336bbf6598a5fa6657a4a2513.map,
position : gmap\_m11ba678336bbf6598a5fa6657a4a2513.positions[m]
} );
}
// Redraw map to fit our new marker-based bounds
gmap\_m11ba678336bbf6598a5fa6657a4a2513.map.setCenter( gmap\_m11ba678336bbf6598a5fa6657a4a2513.positions[470] );
});