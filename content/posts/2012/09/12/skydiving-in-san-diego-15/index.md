---
title: Skydiving in San Diego
date: '2012-09-12T12:54:52+00:00'
format: image
service: flickr
tags:
- automattic
- beau
- beaulebens
- me
- skydiving
- wordpress
image: http://i0.wp.com/dentedreality.com.au/wp-content/uploads/2012/09/8245862430_e59297a60c_o.jpg?resize=607%2C813
---

[![Skydiving in San Diego](http://i0.wp.com/dentedreality.com.au/wp-content/uploads/2012/09/8245862430_e59297a60c_o.jpg?resize=607%2C813)](http://dentedreality.com.au/2012/09/12/skydiving-in-san-diego-15/) 
# [Skydiving in San Diego](http://dentedreality.com.au/2012/09/12/skydiving-in-san-diego-15/)

At the Automattic Grand Meetup, 2012





* #[automattic](http://dentedreality.com.au/tags/automattic/)
* #[beau](http://dentedreality.com.au/tags/beau/)
* #[beaulebens](http://dentedreality.com.au/tags/beaulebens/)
* #[me](http://dentedreality.com.au/tags/me/)
* #[skydiving](http://dentedreality.com.au/tags/skydiving/)
* #[wordpress](http://dentedreality.com.au/tags/wordpress/)

Posted on [Flickr](http://www.flickr.com/photos/borkazoid/8245862430/) [12:54 pm, September 12, 2012](http://dentedreality.com.au/2012/09/12/skydiving-in-san-diego-15/ "12:54 pm") 
jQuery(document).ready(function(){
var gmap\_m4355ddf046b9c21c2c74d5c0750d684f = {
positions : {
656 : new google.maps.LatLng( '32.569333', '-117.059334' )
},
bounds : new google.maps.LatLngBounds(), // empty for now, we'll dynamically extend it later
map : new google.maps.Map(
document.getElementById( 'gmap\_m4355ddf046b9c21c2c74d5c0750d684f' ),
{
mapTypeId: google.maps.MapTypeId.ROADMAP,
center: new google.maps.LatLng( 0, 0 ),
zoom: 16 // Seems to be a good zoom for a single point
}
),
markers : {},
}; // end of gmap
// Extend the bounds of interest based on our positions
for ( var m in gmap\_m4355ddf046b9c21c2c74d5c0750d684f.positions ) {
gmap\_m4355ddf046b9c21c2c74d5c0750d684f.bounds.extend( gmap\_m4355ddf046b9c21c2c74d5c0750d684f.positions[m] );
}
// Render markers
for ( var m in gmap\_m4355ddf046b9c21c2c74d5c0750d684f.positions ) {
gmap\_m4355ddf046b9c21c2c74d5c0750d684f.markers[m] = new google.maps.Marker( {
clickable: true,
map : gmap\_m4355ddf046b9c21c2c74d5c0750d684f.map,
position : gmap\_m4355ddf046b9c21c2c74d5c0750d684f.positions[m]
} );
}
// Redraw map to fit our new marker-based bounds
gmap\_m4355ddf046b9c21c2c74d5c0750d684f.map.setCenter( gmap\_m4355ddf046b9c21c2c74d5c0750d684f.positions[656] );
});