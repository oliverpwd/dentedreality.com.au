---
title: Team Social Hawaii Meetup
date: '2012-01-13T08:54:00+00:00'
format: image
service: flickr
tags:
- automattic
- cocktail
- hawaii
- kailua
- maitai
- meetup
- teamsocial
image: http://i0.wp.com/dentedreality.com.au/wp-content/uploads/2012/01/6813431670_6e5fcc9383_o.jpg?resize=607%2C813
---

[![Team Social Hawaii Meetup](http://i0.wp.com/dentedreality.com.au/wp-content/uploads/2012/01/6813431670_6e5fcc9383_o.jpg?resize=607%2C813)](http://dentedreality.com.au/2012/01/13/team-social-hawaii-meetup/) 
# [Team Social Hawaii Meetup](http://dentedreality.com.au/2012/01/13/team-social-hawaii-meetup/)

Mai-tais for everyone. Holy god these were strong.





* #[automattic](http://dentedreality.com.au/tags/automattic/)
* #[cocktail](http://dentedreality.com.au/tags/cocktail/)
* #[hawaii](http://dentedreality.com.au/tags/hawaii/)
* #[kailua](http://dentedreality.com.au/tags/kailua/)
* #[maitai](http://dentedreality.com.au/tags/maitai/)
* #[meetup](http://dentedreality.com.au/tags/meetup/)
* #[teamsocial](http://dentedreality.com.au/tags/teamsocial/)

Posted on [Flickr](http://www.flickr.com/photos/borkazoid/6813431670/) [8:54 am, January 13, 2012](http://dentedreality.com.au/2012/01/13/team-social-hawaii-meetup/ "8:54 am") 
jQuery(document).ready(function(){
var gmap\_m6c703bbf8fe9097fa5bb2f89f1da960b = {
positions : {
180 : new google.maps.LatLng( '21.329666', '-157.922667' )
},
bounds : new google.maps.LatLngBounds(), // empty for now, we'll dynamically extend it later
map : new google.maps.Map(
document.getElementById( 'gmap\_m6c703bbf8fe9097fa5bb2f89f1da960b' ),
{
mapTypeId: google.maps.MapTypeId.ROADMAP,
center: new google.maps.LatLng( 0, 0 ),
zoom: 16 // Seems to be a good zoom for a single point
}
),
markers : {},
}; // end of gmap
// Extend the bounds of interest based on our positions
for ( var m in gmap\_m6c703bbf8fe9097fa5bb2f89f1da960b.positions ) {
gmap\_m6c703bbf8fe9097fa5bb2f89f1da960b.bounds.extend( gmap\_m6c703bbf8fe9097fa5bb2f89f1da960b.positions[m] );
}
// Render markers
for ( var m in gmap\_m6c703bbf8fe9097fa5bb2f89f1da960b.positions ) {
gmap\_m6c703bbf8fe9097fa5bb2f89f1da960b.markers[m] = new google.maps.Marker( {
clickable: true,
map : gmap\_m6c703bbf8fe9097fa5bb2f89f1da960b.map,
position : gmap\_m6c703bbf8fe9097fa5bb2f89f1da960b.positions[m]
} );
}
// Redraw map to fit our new marker-based bounds
gmap\_m6c703bbf8fe9097fa5bb2f89f1da960b.map.setCenter( gmap\_m6c703bbf8fe9097fa5bb2f89f1da960b.positions[180] );
});