---
title: Auto-fucking-mattic, yo
date: '2012-01-12T09:36:00+00:00'
format: image
service: flickr
tags:
- automattic
- hawaii
- kailua
- meetup
- teamsocial
image: http://i2.wp.com/dentedreality.com.au/wp-content/uploads/2012/01/6959543245_3989289a28_o.jpg?resize=607%2C452
---

[![Auto-fucking-mattic, yo](http://i2.wp.com/dentedreality.com.au/wp-content/uploads/2012/01/6959543245_3989289a28_o.jpg?resize=607%2C452)](http://dentedreality.com.au/2012/01/12/auto-fucking-mattic-yo/) 
# [Auto-fucking-mattic, yo](http://dentedreality.com.au/2012/01/12/auto-fucking-mattic-yo/)





* #[automattic](http://dentedreality.com.au/tags/automattic/)
* #[hawaii](http://dentedreality.com.au/tags/hawaii/)
* #[kailua](http://dentedreality.com.au/tags/kailua/)
* #[meetup](http://dentedreality.com.au/tags/meetup/)
* #[teamsocial](http://dentedreality.com.au/tags/teamsocial/)

Posted on [Flickr](http://www.flickr.com/photos/borkazoid/6959543245/) [9:36 am, January 12, 2012](http://dentedreality.com.au/2012/01/12/auto-fucking-mattic-yo/ "9:36 am") 
jQuery(document).ready(function(){
var gmap\_m3d933b28ab94c526b93e68822f94b0ed = {
positions : {
249 : new google.maps.LatLng( '21.396833', '-157.731' )
},
bounds : new google.maps.LatLngBounds(), // empty for now, we'll dynamically extend it later
map : new google.maps.Map(
document.getElementById( 'gmap\_m3d933b28ab94c526b93e68822f94b0ed' ),
{
mapTypeId: google.maps.MapTypeId.ROADMAP,
center: new google.maps.LatLng( 0, 0 ),
zoom: 16 // Seems to be a good zoom for a single point
}
),
markers : {},
}; // end of gmap
// Extend the bounds of interest based on our positions
for ( var m in gmap\_m3d933b28ab94c526b93e68822f94b0ed.positions ) {
gmap\_m3d933b28ab94c526b93e68822f94b0ed.bounds.extend( gmap\_m3d933b28ab94c526b93e68822f94b0ed.positions[m] );
}
// Render markers
for ( var m in gmap\_m3d933b28ab94c526b93e68822f94b0ed.positions ) {
gmap\_m3d933b28ab94c526b93e68822f94b0ed.markers[m] = new google.maps.Marker( {
clickable: true,
map : gmap\_m3d933b28ab94c526b93e68822f94b0ed.map,
position : gmap\_m3d933b28ab94c526b93e68822f94b0ed.positions[m]
} );
}
// Redraw map to fit our new marker-based bounds
gmap\_m3d933b28ab94c526b93e68822f94b0ed.map.setCenter( gmap\_m3d933b28ab94c526b93e68822f94b0ed.positions[249] );
});