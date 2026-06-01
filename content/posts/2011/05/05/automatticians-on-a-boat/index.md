---
title: Automatticians on a Boat
date: '2011-05-05T13:11:32+00:00'
format: image
service: flickr
tags:
- boat
- francisco
- sailing
- SAN
- sanfranciscobay
image: http://i1.wp.com/dentedreality.com.au/wp-content/uploads/2011/05/5802707554_2b25dd1252_o.jpg?resize=607%2C452
---

[![Automatticians on a Boat](http://i1.wp.com/dentedreality.com.au/wp-content/uploads/2011/05/5802707554_2b25dd1252_o.jpg?resize=607%2C452)](http://dentedreality.com.au/2011/05/05/automatticians-on-a-boat/) 
# [Automatticians on a Boat](http://dentedreality.com.au/2011/05/05/automatticians-on-a-boat/)

Pete took us out sailing on the Bay. It was most awesome.





* #[boat](http://dentedreality.com.au/tags/boat/)
* #[francisco](http://dentedreality.com.au/tags/francisco/)
* #[sailing](http://dentedreality.com.au/tags/sailing/)
* #[SAN](http://dentedreality.com.au/tags/san/)
* #[sanfranciscobay](http://dentedreality.com.au/tags/sanfranciscobay/)

Posted on [Flickr](http://www.flickr.com/photos/borkazoid/5802707554/) [1:11 pm, May 5, 2011](http://dentedreality.com.au/2011/05/05/automatticians-on-a-boat/ "1:11 pm") 
jQuery(document).ready(function(){
var gmap\_m9f84128c7208c9b5233a6fc153f7b0e7 = {
positions : {
231 : new google.maps.LatLng( '37.847166', '-122.4175' )
},
bounds : new google.maps.LatLngBounds(), // empty for now, we'll dynamically extend it later
map : new google.maps.Map(
document.getElementById( 'gmap\_m9f84128c7208c9b5233a6fc153f7b0e7' ),
{
mapTypeId: google.maps.MapTypeId.ROADMAP,
center: new google.maps.LatLng( 0, 0 ),
zoom: 16 // Seems to be a good zoom for a single point
}
),
markers : {},
}; // end of gmap
// Extend the bounds of interest based on our positions
for ( var m in gmap\_m9f84128c7208c9b5233a6fc153f7b0e7.positions ) {
gmap\_m9f84128c7208c9b5233a6fc153f7b0e7.bounds.extend( gmap\_m9f84128c7208c9b5233a6fc153f7b0e7.positions[m] );
}
// Render markers
for ( var m in gmap\_m9f84128c7208c9b5233a6fc153f7b0e7.positions ) {
gmap\_m9f84128c7208c9b5233a6fc153f7b0e7.markers[m] = new google.maps.Marker( {
clickable: true,
map : gmap\_m9f84128c7208c9b5233a6fc153f7b0e7.map,
position : gmap\_m9f84128c7208c9b5233a6fc153f7b0e7.positions[m]
} );
}
// Redraw map to fit our new marker-based bounds
gmap\_m9f84128c7208c9b5233a6fc153f7b0e7.map.setCenter( gmap\_m9f84128c7208c9b5233a6fc153f7b0e7.positions[231] );
});