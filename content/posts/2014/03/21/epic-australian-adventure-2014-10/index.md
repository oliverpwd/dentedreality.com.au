---
title: Epic Australian Adventure, 2014
date: '2014-03-21T04:54:22+00:00'
format: image
service: flickr
tags:
- mooloolaba
image: http://i2.wp.com/dentedreality.com.au/wp-content/uploads/2014/03/13928295574_100ff6d262_o.jpg?resize=607%2C809
---

[![Epic Australian Adventure, 2014](http://i2.wp.com/dentedreality.com.au/wp-content/uploads/2014/03/13928295574_100ff6d262_o.jpg?resize=607%2C809)](http://dentedreality.com.au/2014/03/21/epic-australian-adventure-2014-10/) 
# [Epic Australian Adventure, 2014](http://dentedreality.com.au/2014/03/21/epic-australian-adventure-2014-10/)

Perth, Mooloolaba and Melbourne





* #[mooloolaba](http://dentedreality.com.au/tags/mooloolaba/)

Posted on [Flickr](http://www.flickr.com/photos/borkazoid/13928295574/) [4:54 am, March 21, 2014](http://dentedreality.com.au/2014/03/21/epic-australian-adventure-2014-10/ "4:54 am") 
jQuery(document).ready(function(){
var gmap\_m425d671b563a161a284670cdb556b21b = {
positions : {
376 : new google.maps.LatLng( '-26.679006', '153.119063' )
},
bounds : new google.maps.LatLngBounds(), // empty for now, we'll dynamically extend it later
map : new google.maps.Map(
document.getElementById( 'gmap\_m425d671b563a161a284670cdb556b21b' ),
{
mapTypeId: google.maps.MapTypeId.ROADMAP,
center: new google.maps.LatLng( 0, 0 ),
zoom: 16 // Seems to be a good zoom for a single point
}
),
markers : {},
}; // end of gmap
// Extend the bounds of interest based on our positions
for ( var m in gmap\_m425d671b563a161a284670cdb556b21b.positions ) {
gmap\_m425d671b563a161a284670cdb556b21b.bounds.extend( gmap\_m425d671b563a161a284670cdb556b21b.positions[m] );
}
// Render markers
for ( var m in gmap\_m425d671b563a161a284670cdb556b21b.positions ) {
gmap\_m425d671b563a161a284670cdb556b21b.markers[m] = new google.maps.Marker( {
clickable: true,
map : gmap\_m425d671b563a161a284670cdb556b21b.map,
position : gmap\_m425d671b563a161a284670cdb556b21b.positions[m]
} );
}
// Redraw map to fit our new marker-based bounds
gmap\_m425d671b563a161a284670cdb556b21b.map.setCenter( gmap\_m425d671b563a161a284670cdb556b21b.positions[376] );
});