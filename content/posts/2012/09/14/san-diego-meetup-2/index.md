---
title: San Diego Meetup
date: '2012-09-14T16:04:28+00:00'
format: image
service: flickr
tags:
- automattic
- chexee
- grandmeetup
- hanni
- meetup
- sandiego
- sandiego2012
- work
image: http://i0.wp.com/dentedreality.com.au/wp-content/uploads/2012/09/8460266352_16e8251f4d_o.jpg?resize=607%2C455
---

[![San Diego Meetup](http://i0.wp.com/dentedreality.com.au/wp-content/uploads/2012/09/8460266352_16e8251f4d_o.jpg?resize=607%2C455)](http://dentedreality.com.au/2012/09/14/san-diego-meetup-2/) 
# [San Diego Meetup](http://dentedreality.com.au/2012/09/14/san-diego-meetup-2/)





* #[automattic](http://dentedreality.com.au/tags/automattic/)
* #[chexee](http://dentedreality.com.au/tags/chexee/)
* #[grandmeetup](http://dentedreality.com.au/tags/grandmeetup/)
* #[hanni](http://dentedreality.com.au/tags/hanni/)
* #[meetup](http://dentedreality.com.au/tags/meetup/)
* #[sandiego](http://dentedreality.com.au/tags/sandiego/)
* #[sandiego2012](http://dentedreality.com.au/tags/sandiego2012/)
* #[work](http://dentedreality.com.au/tags/work/)

Posted on [Flickr](http://www.flickr.com/photos/borkazoid/8460266352/) [4:04 pm, September 14, 2012](http://dentedreality.com.au/2012/09/14/san-diego-meetup-2/ "4:04 pm") 
jQuery(document).ready(function(){
var gmap\_m9d1d39b3d88b59a3c5d7cc8e2f4ad407 = {
positions : {
967 : new google.maps.LatLng( '32.747483', '-117.132078' )
},
bounds : new google.maps.LatLngBounds(), // empty for now, we'll dynamically extend it later
map : new google.maps.Map(
document.getElementById( 'gmap\_m9d1d39b3d88b59a3c5d7cc8e2f4ad407' ),
{
mapTypeId: google.maps.MapTypeId.ROADMAP,
center: new google.maps.LatLng( 0, 0 ),
zoom: 16 // Seems to be a good zoom for a single point
}
),
markers : {},
}; // end of gmap
// Extend the bounds of interest based on our positions
for ( var m in gmap\_m9d1d39b3d88b59a3c5d7cc8e2f4ad407.positions ) {
gmap\_m9d1d39b3d88b59a3c5d7cc8e2f4ad407.bounds.extend( gmap\_m9d1d39b3d88b59a3c5d7cc8e2f4ad407.positions[m] );
}
// Render markers
for ( var m in gmap\_m9d1d39b3d88b59a3c5d7cc8e2f4ad407.positions ) {
gmap\_m9d1d39b3d88b59a3c5d7cc8e2f4ad407.markers[m] = new google.maps.Marker( {
clickable: true,
map : gmap\_m9d1d39b3d88b59a3c5d7cc8e2f4ad407.map,
position : gmap\_m9d1d39b3d88b59a3c5d7cc8e2f4ad407.positions[m]
} );
}
// Redraw map to fit our new marker-based bounds
gmap\_m9d1d39b3d88b59a3c5d7cc8e2f4ad407.map.setCenter( gmap\_m9d1d39b3d88b59a3c5d7cc8e2f4ad407.positions[967] );
});