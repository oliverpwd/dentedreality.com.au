---
title: ''
date: '2014-09-15T13:37:07+00:00'
format: image
service: instagram
tags:
- a8cmeetup
- hyperlapse
- photo
image: http://i0.wp.com/dentedreality.com.au/wp-content/uploads/2014/09/10691890_1479884972264216_464388827_n.jpg?resize=640%2C640
---

[![#hyperlapse #a8cmeetup CO:UT](http://i0.wp.com/dentedreality.com.au/wp-content/uploads/2014/09/10691890_1479884972264216_464388827_n.jpg?resize=640%2C640)](http://dentedreality.com.au/2014/09/15/hyperlapse-a8cmeetup-cout/) 

#hyperlapse #a8cmeetup CO:UT





* #[a8cmeetup](http://dentedreality.com.au/tags/a8cmeetup/)
* #[hyperlapse](http://dentedreality.com.au/tags/hyperlapse/)
* #[photo](http://dentedreality.com.au/tags/photo/)

Posted on [Instagram](http://instagram.com/p/s-mbwWCmFY/) [1:37 pm, September 15, 2014](http://dentedreality.com.au/2014/09/15/hyperlapse-a8cmeetup-cout/ "1:37 pm") 
jQuery(document).ready(function(){
var gmap\_m9408d6d517dd1ac00541a3ceaa66551f = {
positions : {
629 : new google.maps.LatLng( '39.680147753', '-106.768818051' )
},
bounds : new google.maps.LatLngBounds(), // empty for now, we'll dynamically extend it later
map : new google.maps.Map(
document.getElementById( 'gmap\_m9408d6d517dd1ac00541a3ceaa66551f' ),
{
mapTypeId: google.maps.MapTypeId.ROADMAP,
center: new google.maps.LatLng( 0, 0 ),
zoom: 16 // Seems to be a good zoom for a single point
}
),
markers : {},
}; // end of gmap
// Extend the bounds of interest based on our positions
for ( var m in gmap\_m9408d6d517dd1ac00541a3ceaa66551f.positions ) {
gmap\_m9408d6d517dd1ac00541a3ceaa66551f.bounds.extend( gmap\_m9408d6d517dd1ac00541a3ceaa66551f.positions[m] );
}
// Render markers
for ( var m in gmap\_m9408d6d517dd1ac00541a3ceaa66551f.positions ) {
gmap\_m9408d6d517dd1ac00541a3ceaa66551f.markers[m] = new google.maps.Marker( {
clickable: true,
map : gmap\_m9408d6d517dd1ac00541a3ceaa66551f.map,
position : gmap\_m9408d6d517dd1ac00541a3ceaa66551f.positions[m]
} );
}
// Redraw map to fit our new marker-based bounds
gmap\_m9408d6d517dd1ac00541a3ceaa66551f.map.setCenter( gmap\_m9408d6d517dd1ac00541a3ceaa66551f.positions[629] );
});