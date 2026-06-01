---
title: Hiking at The Pinnacles, CA
date: '2012-02-25T10:25:19+00:00'
format: image
service: flickr
tags:
- california
- hike
- hiking
- pinnacles
image: http://i1.wp.com/dentedreality.com.au/wp-content/uploads/2012/02/6959577927_35faa01f2b_o.jpg?resize=607%2C452
---

[![Hiking at The Pinnacles, CA](http://i1.wp.com/dentedreality.com.au/wp-content/uploads/2012/02/6959577927_35faa01f2b_o.jpg?resize=607%2C452)](http://dentedreality.com.au/2012/02/25/hiking-at-the-pinnacles-ca-3/) 
# [Hiking at The Pinnacles, CA](http://dentedreality.com.au/2012/02/25/hiking-at-the-pinnacles-ca-3/)





* #[california](http://dentedreality.com.au/tags/california/)
* #[hike](http://dentedreality.com.au/tags/hike/)
* #[hiking](http://dentedreality.com.au/tags/hiking/)
* #[pinnacles](http://dentedreality.com.au/tags/pinnacles/)

Posted on [Flickr](http://www.flickr.com/photos/borkazoid/6959577927/) [10:25 am, February 25, 2012](http://dentedreality.com.au/2012/02/25/hiking-at-the-pinnacles-ca-3/ "10:25 am") 
jQuery(document).ready(function(){
var gmap\_m0fb6f6c5e47ff8b538ad18d3719b1d5b = {
positions : {
613 : new google.maps.LatLng( '37.163', '-121.7685' )
},
bounds : new google.maps.LatLngBounds(), // empty for now, we'll dynamically extend it later
map : new google.maps.Map(
document.getElementById( 'gmap\_m0fb6f6c5e47ff8b538ad18d3719b1d5b' ),
{
mapTypeId: google.maps.MapTypeId.ROADMAP,
center: new google.maps.LatLng( 0, 0 ),
zoom: 16 // Seems to be a good zoom for a single point
}
),
markers : {},
}; // end of gmap
// Extend the bounds of interest based on our positions
for ( var m in gmap\_m0fb6f6c5e47ff8b538ad18d3719b1d5b.positions ) {
gmap\_m0fb6f6c5e47ff8b538ad18d3719b1d5b.bounds.extend( gmap\_m0fb6f6c5e47ff8b538ad18d3719b1d5b.positions[m] );
}
// Render markers
for ( var m in gmap\_m0fb6f6c5e47ff8b538ad18d3719b1d5b.positions ) {
gmap\_m0fb6f6c5e47ff8b538ad18d3719b1d5b.markers[m] = new google.maps.Marker( {
clickable: true,
map : gmap\_m0fb6f6c5e47ff8b538ad18d3719b1d5b.map,
position : gmap\_m0fb6f6c5e47ff8b538ad18d3719b1d5b.positions[m]
} );
}
// Redraw map to fit our new marker-based bounds
gmap\_m0fb6f6c5e47ff8b538ad18d3719b1d5b.map.setCenter( gmap\_m0fb6f6c5e47ff8b538ad18d3719b1d5b.positions[613] );
});