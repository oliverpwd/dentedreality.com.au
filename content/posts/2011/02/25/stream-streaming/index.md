---
title: Stream-streaming
date: '2011-02-25T10:15:25+00:00'
format: image
service: flickr
tags:
- newyork
- newyorkcity
- NYC
- stream
- video
image: http://i1.wp.com/dentedreality.com.au/wp-content/uploads/2011/02/5802060957_de25a30eb2_o.jpg?resize=607%2C452
---

[![Stream-streaming](http://i1.wp.com/dentedreality.com.au/wp-content/uploads/2011/02/5802060957_de25a30eb2_o.jpg?resize=607%2C452)](http://dentedreality.com.au/2011/02/25/stream-streaming/) 
# [Stream-streaming](http://dentedreality.com.au/2011/02/25/stream-streaming/)

Streaming a video from Youtube into our monthly townhall video stream/meeting so everyone in the company could watch it ![:)](http://i0.wp.com/dentedreality.com.au/wp-includes/images/smilies/icon_smile.gif?w=607)





* #[newyork](http://dentedreality.com.au/tags/newyork/)
* #[newyorkcity](http://dentedreality.com.au/tags/newyorkcity/)
* #[NYC](http://dentedreality.com.au/tags/nyc/)
* #[stream](http://dentedreality.com.au/tags/stream/)
* #[video](http://dentedreality.com.au/tags/video/)

Posted on [Flickr](http://www.flickr.com/photos/borkazoid/5802060957/) [10:15 am, February 25, 2011](http://dentedreality.com.au/2011/02/25/stream-streaming/ "10:15 am") 
jQuery(document).ready(function(){
var gmap\_mb4b79868e7714fad7bda29d7b7866203 = {
positions : {
288 : new google.maps.LatLng( '40.725333', '-73.995' )
},
bounds : new google.maps.LatLngBounds(), // empty for now, we'll dynamically extend it later
map : new google.maps.Map(
document.getElementById( 'gmap\_mb4b79868e7714fad7bda29d7b7866203' ),
{
mapTypeId: google.maps.MapTypeId.ROADMAP,
center: new google.maps.LatLng( 0, 0 ),
zoom: 16 // Seems to be a good zoom for a single point
}
),
markers : {},
}; // end of gmap
// Extend the bounds of interest based on our positions
for ( var m in gmap\_mb4b79868e7714fad7bda29d7b7866203.positions ) {
gmap\_mb4b79868e7714fad7bda29d7b7866203.bounds.extend( gmap\_mb4b79868e7714fad7bda29d7b7866203.positions[m] );
}
// Render markers
for ( var m in gmap\_mb4b79868e7714fad7bda29d7b7866203.positions ) {
gmap\_mb4b79868e7714fad7bda29d7b7866203.markers[m] = new google.maps.Marker( {
clickable: true,
map : gmap\_mb4b79868e7714fad7bda29d7b7866203.map,
position : gmap\_mb4b79868e7714fad7bda29d7b7866203.positions[m]
} );
}
// Redraw map to fit our new marker-based bounds
gmap\_mb4b79868e7714fad7bda29d7b7866203.map.setCenter( gmap\_mb4b79868e7714fad7bda29d7b7866203.positions[288] );
});