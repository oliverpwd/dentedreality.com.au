---
title: Home Made Ramen
date: '2013-08-16T04:56:09+00:00'
format: image
tags:
- egg
- noodles
- ramen
image: http://i1.wp.com/dentedreality.com.au/wp-content/uploads/2013/08/9767768432_0ff3b304fc_o.jpg?resize=607%2C452
---

[![Home Made Ramen](http://i1.wp.com/dentedreality.com.au/wp-content/uploads/2013/08/9767768432_0ff3b304fc_o.jpg?resize=607%2C452)](http://dentedreality.com.au/2013/08/16/home-made-ramen/) 
# [Home Made Ramen](http://dentedreality.com.au/2013/08/16/home-made-ramen/)

By Erika’s Mom.





* #[egg](http://dentedreality.com.au/tags/egg/)
* #[noodles](http://dentedreality.com.au/tags/noodles/)
* #[ramen](http://dentedreality.com.au/tags/ramen/)

Posted on [Flickr](http://www.flickr.com/photos/borkazoid/9767768432/) [4:56 am, August 16, 2013](http://dentedreality.com.au/2013/08/16/home-made-ramen/ "4:56 am") 
jQuery(document).ready(function(){
var gmap\_m6ad9e85fd052ceb341ac173aba7295af = {
positions : {
739 : new google.maps.LatLng( '40.669333', '-73.985' )
},
bounds : new google.maps.LatLngBounds(), // empty for now, we'll dynamically extend it later
map : new google.maps.Map(
document.getElementById( 'gmap\_m6ad9e85fd052ceb341ac173aba7295af' ),
{
mapTypeId: google.maps.MapTypeId.ROADMAP,
center: new google.maps.LatLng( 0, 0 ),
zoom: 16 // Seems to be a good zoom for a single point
}
),
markers : {},
}; // end of gmap
// Extend the bounds of interest based on our positions
for ( var m in gmap\_m6ad9e85fd052ceb341ac173aba7295af.positions ) {
gmap\_m6ad9e85fd052ceb341ac173aba7295af.bounds.extend( gmap\_m6ad9e85fd052ceb341ac173aba7295af.positions[m] );
}
// Render markers
for ( var m in gmap\_m6ad9e85fd052ceb341ac173aba7295af.positions ) {
gmap\_m6ad9e85fd052ceb341ac173aba7295af.markers[m] = new google.maps.Marker( {
clickable: true,
map : gmap\_m6ad9e85fd052ceb341ac173aba7295af.map,
position : gmap\_m6ad9e85fd052ceb341ac173aba7295af.positions[m]
} );
}
// Redraw map to fit our new marker-based bounds
gmap\_m6ad9e85fd052ceb341ac173aba7295af.map.setCenter( gmap\_m6ad9e85fd052ceb341ac173aba7295af.positions[739] );
});