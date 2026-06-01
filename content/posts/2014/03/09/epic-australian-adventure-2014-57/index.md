---
title: Epic Australian Adventure, 2014
date: '2014-03-09T12:57:27+00:00'
format: image
service: flickr
tags:
- perth
image: http://i1.wp.com/dentedreality.com.au/wp-content/uploads/2014/03/13904704222_9354d825b0_o.jpg?resize=607%2C455
---

[![Epic Australian Adventure, 2014](http://i1.wp.com/dentedreality.com.au/wp-content/uploads/2014/03/13904704222_9354d825b0_o.jpg?resize=607%2C455)](http://dentedreality.com.au/2014/03/09/epic-australian-adventure-2014-57/) 
# [Epic Australian Adventure, 2014](http://dentedreality.com.au/2014/03/09/epic-australian-adventure-2014-57/)

Perth, Mooloolaba and Melbourne





* #[perth](http://dentedreality.com.au/tags/perth/)

Posted on [Flickr](http://www.flickr.com/photos/borkazoid/13904704222/) [12:57 pm, March 9, 2014](http://dentedreality.com.au/2014/03/09/epic-australian-adventure-2014-57/ "12:57 pm") 
jQuery(document).ready(function(){
var gmap\_mbd47ed01082a91d5a13aab25f6b8570f = {
positions : {
200 : new google.maps.LatLng( '-32.053131', '115.846313' )
},
bounds : new google.maps.LatLngBounds(), // empty for now, we'll dynamically extend it later
map : new google.maps.Map(
document.getElementById( 'gmap\_mbd47ed01082a91d5a13aab25f6b8570f' ),
{
mapTypeId: google.maps.MapTypeId.ROADMAP,
center: new google.maps.LatLng( 0, 0 ),
zoom: 16 // Seems to be a good zoom for a single point
}
),
markers : {},
}; // end of gmap
// Extend the bounds of interest based on our positions
for ( var m in gmap\_mbd47ed01082a91d5a13aab25f6b8570f.positions ) {
gmap\_mbd47ed01082a91d5a13aab25f6b8570f.bounds.extend( gmap\_mbd47ed01082a91d5a13aab25f6b8570f.positions[m] );
}
// Render markers
for ( var m in gmap\_mbd47ed01082a91d5a13aab25f6b8570f.positions ) {
gmap\_mbd47ed01082a91d5a13aab25f6b8570f.markers[m] = new google.maps.Marker( {
clickable: true,
map : gmap\_mbd47ed01082a91d5a13aab25f6b8570f.map,
position : gmap\_mbd47ed01082a91d5a13aab25f6b8570f.positions[m]
} );
}
// Redraw map to fit our new marker-based bounds
gmap\_mbd47ed01082a91d5a13aab25f6b8570f.map.setCenter( gmap\_mbd47ed01082a91d5a13aab25f6b8570f.positions[200] );
});