---
title: Meat!
date: '2011-02-07T15:19:18+00:00'
format: image
service: flickr
tags:
- '4505'
- 4505meats
- butchery
- lamb
- meat
image: http://i2.wp.com/dentedreality.com.au/wp-content/uploads/2011/02/5802055601_b993903e91_o.jpg?resize=607%2C452
---

[![Meat!](http://i2.wp.com/dentedreality.com.au/wp-content/uploads/2011/02/5802055601_b993903e91_o.jpg?resize=607%2C452)](http://dentedreality.com.au/2011/02/07/meat-5/) 
# [Meat!](http://dentedreality.com.au/2011/02/07/meat-5/)

Butchering a lamb with 4505 Meats





* #[4505](http://dentedreality.com.au/tags/4505/)
* #[4505meats](http://dentedreality.com.au/tags/4505meats/)
* #[butchery](http://dentedreality.com.au/tags/butchery/)
* #[lamb](http://dentedreality.com.au/tags/lamb/)
* #[meat](http://dentedreality.com.au/tags/meat/)

Posted on [Flickr](http://www.flickr.com/photos/borkazoid/5802055601/) [3:19 pm, February 7, 2011](http://dentedreality.com.au/2011/02/07/meat-5/ "3:19 pm") 
jQuery(document).ready(function(){
var gmap\_me54c42efeba1ca387b56f3d9d4254dda = {
positions : {
135 : new google.maps.LatLng( '37.778166', '-122.426' )
},
bounds : new google.maps.LatLngBounds(), // empty for now, we'll dynamically extend it later
map : new google.maps.Map(
document.getElementById( 'gmap\_me54c42efeba1ca387b56f3d9d4254dda' ),
{
mapTypeId: google.maps.MapTypeId.ROADMAP,
center: new google.maps.LatLng( 0, 0 ),
zoom: 16 // Seems to be a good zoom for a single point
}
),
markers : {},
}; // end of gmap
// Extend the bounds of interest based on our positions
for ( var m in gmap\_me54c42efeba1ca387b56f3d9d4254dda.positions ) {
gmap\_me54c42efeba1ca387b56f3d9d4254dda.bounds.extend( gmap\_me54c42efeba1ca387b56f3d9d4254dda.positions[m] );
}
// Render markers
for ( var m in gmap\_me54c42efeba1ca387b56f3d9d4254dda.positions ) {
gmap\_me54c42efeba1ca387b56f3d9d4254dda.markers[m] = new google.maps.Marker( {
clickable: true,
map : gmap\_me54c42efeba1ca387b56f3d9d4254dda.map,
position : gmap\_me54c42efeba1ca387b56f3d9d4254dda.positions[m]
} );
}
// Redraw map to fit our new marker-based bounds
gmap\_me54c42efeba1ca387b56f3d9d4254dda.map.setCenter( gmap\_me54c42efeba1ca387b56f3d9d4254dda.positions[135] );
});