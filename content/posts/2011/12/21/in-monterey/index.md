---
title: In Monterey
date: '2011-12-21T16:53:03+00:00'
format: image
service: flickr
tags:
- beau
- beaulebens
- erika
- fire
- me
- monterey
image: http://i0.wp.com/dentedreality.com.au/wp-content/uploads/2011/12/6959403743_38ca59c142_o.jpg?resize=607%2C452
---

[![In Monterey](http://i0.wp.com/dentedreality.com.au/wp-content/uploads/2011/12/6959403743_38ca59c142_o.jpg?resize=607%2C452)](http://dentedreality.com.au/2011/12/21/in-monterey/) 
# [In Monterey](http://dentedreality.com.au/2011/12/21/in-monterey/)





* #[beau](http://dentedreality.com.au/tags/beau/)
* #[beaulebens](http://dentedreality.com.au/tags/beaulebens/)
* #[erika](http://dentedreality.com.au/tags/erika/)
* #[fire](http://dentedreality.com.au/tags/fire/)
* #[me](http://dentedreality.com.au/tags/me/)
* #[monterey](http://dentedreality.com.au/tags/monterey/)

Posted on [Flickr](http://www.flickr.com/photos/borkazoid/6959403743/) [4:53 pm, December 21, 2011](http://dentedreality.com.au/2011/12/21/in-monterey/ "4:53 pm") 
jQuery(document).ready(function(){
var gmap\_m1055a6827d870b79dae74710a5dd34df = {
positions : {
348 : new google.maps.LatLng( '36.595166', '-121.8935' )
},
bounds : new google.maps.LatLngBounds(), // empty for now, we'll dynamically extend it later
map : new google.maps.Map(
document.getElementById( 'gmap\_m1055a6827d870b79dae74710a5dd34df' ),
{
mapTypeId: google.maps.MapTypeId.ROADMAP,
center: new google.maps.LatLng( 0, 0 ),
zoom: 16 // Seems to be a good zoom for a single point
}
),
markers : {},
}; // end of gmap
// Extend the bounds of interest based on our positions
for ( var m in gmap\_m1055a6827d870b79dae74710a5dd34df.positions ) {
gmap\_m1055a6827d870b79dae74710a5dd34df.bounds.extend( gmap\_m1055a6827d870b79dae74710a5dd34df.positions[m] );
}
// Render markers
for ( var m in gmap\_m1055a6827d870b79dae74710a5dd34df.positions ) {
gmap\_m1055a6827d870b79dae74710a5dd34df.markers[m] = new google.maps.Marker( {
clickable: true,
map : gmap\_m1055a6827d870b79dae74710a5dd34df.map,
position : gmap\_m1055a6827d870b79dae74710a5dd34df.positions[m]
} );
}
// Redraw map to fit our new marker-based bounds
gmap\_m1055a6827d870b79dae74710a5dd34df.map.setCenter( gmap\_m1055a6827d870b79dae74710a5dd34df.positions[348] );
});