---
title: Childish Gambino
date: '2014-02-26T15:25:45+00:00'
format: image
service: flickr
tags:
- childishgambino
- concert
- live
- music
- oakland
image: http://i1.wp.com/dentedreality.com.au/wp-content/uploads/2014/02/13903839092_c65d03c0f2_o.jpg?fit=1500%2C1500
---

[![Childish Gambino](http://i1.wp.com/dentedreality.com.au/wp-content/uploads/2014/02/13903839092_c65d03c0f2_o.jpg?fit=1500%2C1500)](http://dentedreality.com.au/2014/02/26/childish-gambino-5/) 
# [Childish Gambino](http://dentedreality.com.au/2014/02/26/childish-gambino-5/)

Private show at the Fox, in Oakland





* #[childishgambino](http://dentedreality.com.au/tags/childishgambino/)
* #[concert](http://dentedreality.com.au/tags/concert/)
* #[live](http://dentedreality.com.au/tags/live/)
* #[music](http://dentedreality.com.au/tags/music/)
* #[oakland](http://dentedreality.com.au/tags/oakland/)

Posted on [Flickr](http://www.flickr.com/photos/borkazoid/13903839092/) [3:25 pm, February 26, 2014](http://dentedreality.com.au/2014/02/26/childish-gambino-5/ "3:25 pm") 
jQuery(document).ready(function(){
var gmap\_m672f13db990106a221a9bdd6ba51c7af = {
positions : {
233 : new google.maps.LatLng( '37.808052', '-122.270753' )
},
bounds : new google.maps.LatLngBounds(), // empty for now, we'll dynamically extend it later
map : new google.maps.Map(
document.getElementById( 'gmap\_m672f13db990106a221a9bdd6ba51c7af' ),
{
mapTypeId: google.maps.MapTypeId.ROADMAP,
center: new google.maps.LatLng( 0, 0 ),
zoom: 16 // Seems to be a good zoom for a single point
}
),
markers : {},
}; // end of gmap
// Extend the bounds of interest based on our positions
for ( var m in gmap\_m672f13db990106a221a9bdd6ba51c7af.positions ) {
gmap\_m672f13db990106a221a9bdd6ba51c7af.bounds.extend( gmap\_m672f13db990106a221a9bdd6ba51c7af.positions[m] );
}
// Render markers
for ( var m in gmap\_m672f13db990106a221a9bdd6ba51c7af.positions ) {
gmap\_m672f13db990106a221a9bdd6ba51c7af.markers[m] = new google.maps.Marker( {
clickable: true,
map : gmap\_m672f13db990106a221a9bdd6ba51c7af.map,
position : gmap\_m672f13db990106a221a9bdd6ba51c7af.positions[m]
} );
}
// Redraw map to fit our new marker-based bounds
gmap\_m672f13db990106a221a9bdd6ba51c7af.map.setCenter( gmap\_m672f13db990106a221a9bdd6ba51c7af.positions[233] );
});