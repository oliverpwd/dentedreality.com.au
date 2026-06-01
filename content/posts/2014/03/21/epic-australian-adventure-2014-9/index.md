---
title: Epic Australian Adventure, 2014
date: '2014-03-21T07:28:37+00:00'
format: image
service: flickr
tags:
- beau
- beaulebens
- me
- mooloolaba
image: http://i1.wp.com/dentedreality.com.au/wp-content/uploads/2014/03/13904732966_53bff6fe3d_o.jpg?resize=607%2C809
---

[![Epic Australian Adventure, 2014](http://i1.wp.com/dentedreality.com.au/wp-content/uploads/2014/03/13904732966_53bff6fe3d_o.jpg?resize=607%2C809)](http://dentedreality.com.au/2014/03/21/epic-australian-adventure-2014-9/) 
# [Epic Australian Adventure, 2014](http://dentedreality.com.au/2014/03/21/epic-australian-adventure-2014-9/)

Perth, Mooloolaba and Melbourne





* #[beau](http://dentedreality.com.au/tags/beau/)
* #[beaulebens](http://dentedreality.com.au/tags/beaulebens/)
* #[me](http://dentedreality.com.au/tags/me/)
* #[mooloolaba](http://dentedreality.com.au/tags/mooloolaba/)

Posted on [Flickr](http://www.flickr.com/photos/borkazoid/13904732966/) [7:28 am, March 21, 2014](http://dentedreality.com.au/2014/03/21/epic-australian-adventure-2014-9/ "7:28 am") 
jQuery(document).ready(function(){
var gmap\_m5d5a30f7fe678bf4a1e402210c308baf = {
positions : {
633 : new google.maps.LatLng( '-26.654698', '153.088577' )
},
bounds : new google.maps.LatLngBounds(), // empty for now, we'll dynamically extend it later
map : new google.maps.Map(
document.getElementById( 'gmap\_m5d5a30f7fe678bf4a1e402210c308baf' ),
{
mapTypeId: google.maps.MapTypeId.ROADMAP,
center: new google.maps.LatLng( 0, 0 ),
zoom: 16 // Seems to be a good zoom for a single point
}
),
markers : {},
}; // end of gmap
// Extend the bounds of interest based on our positions
for ( var m in gmap\_m5d5a30f7fe678bf4a1e402210c308baf.positions ) {
gmap\_m5d5a30f7fe678bf4a1e402210c308baf.bounds.extend( gmap\_m5d5a30f7fe678bf4a1e402210c308baf.positions[m] );
}
// Render markers
for ( var m in gmap\_m5d5a30f7fe678bf4a1e402210c308baf.positions ) {
gmap\_m5d5a30f7fe678bf4a1e402210c308baf.markers[m] = new google.maps.Marker( {
clickable: true,
map : gmap\_m5d5a30f7fe678bf4a1e402210c308baf.map,
position : gmap\_m5d5a30f7fe678bf4a1e402210c308baf.positions[m]
} );
}
// Redraw map to fit our new marker-based bounds
gmap\_m5d5a30f7fe678bf4a1e402210c308baf.map.setCenter( gmap\_m5d5a30f7fe678bf4a1e402210c308baf.positions[633] );
});