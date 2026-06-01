---
title: Footy
date: '2014-03-27T15:11:07+00:00'
format: image
service: flickr
tags:
- afl
- carlton
- footy
- mcg
- Melbourne
- richmond
image: http://i1.wp.com/dentedreality.com.au/wp-content/uploads/2014/03/13904755286_4fa9dc4022_o.jpg?resize=607%2C290
---

[![Footy](http://i1.wp.com/dentedreality.com.au/wp-content/uploads/2014/03/13904755286_4fa9dc4022_o.jpg?resize=607%2C290)](http://dentedreality.com.au/2014/03/27/footy/) 
# [Footy](http://dentedreality.com.au/2014/03/27/footy/)

Perth, Mooloolaba and Melbourne





* #[afl](http://dentedreality.com.au/tags/afl/)
* #[carlton](http://dentedreality.com.au/tags/carlton/)
* #[footy](http://dentedreality.com.au/tags/footy/)
* #[mcg](http://dentedreality.com.au/tags/mcg/)
* #[Melbourne](http://dentedreality.com.au/tags/melbourne/)
* #[richmond](http://dentedreality.com.au/tags/richmond/)

Posted on [Flickr](http://www.flickr.com/photos/borkazoid/13904755286/) [3:11 pm, March 27, 2014](http://dentedreality.com.au/2014/03/27/footy/ "3:11 pm") 
jQuery(document).ready(function(){
var gmap\_me64f49a38f5282508dd35f1b0f9db464 = {
positions : {
190 : new google.maps.LatLng( '-37.8198', '144.982147' )
},
bounds : new google.maps.LatLngBounds(), // empty for now, we'll dynamically extend it later
map : new google.maps.Map(
document.getElementById( 'gmap\_me64f49a38f5282508dd35f1b0f9db464' ),
{
mapTypeId: google.maps.MapTypeId.ROADMAP,
center: new google.maps.LatLng( 0, 0 ),
zoom: 16 // Seems to be a good zoom for a single point
}
),
markers : {},
}; // end of gmap
// Extend the bounds of interest based on our positions
for ( var m in gmap\_me64f49a38f5282508dd35f1b0f9db464.positions ) {
gmap\_me64f49a38f5282508dd35f1b0f9db464.bounds.extend( gmap\_me64f49a38f5282508dd35f1b0f9db464.positions[m] );
}
// Render markers
for ( var m in gmap\_me64f49a38f5282508dd35f1b0f9db464.positions ) {
gmap\_me64f49a38f5282508dd35f1b0f9db464.markers[m] = new google.maps.Marker( {
clickable: true,
map : gmap\_me64f49a38f5282508dd35f1b0f9db464.map,
position : gmap\_me64f49a38f5282508dd35f1b0f9db464.positions[m]
} );
}
// Redraw map to fit our new marker-based bounds
gmap\_me64f49a38f5282508dd35f1b0f9db464.map.setCenter( gmap\_me64f49a38f5282508dd35f1b0f9db464.positions[190] );
});