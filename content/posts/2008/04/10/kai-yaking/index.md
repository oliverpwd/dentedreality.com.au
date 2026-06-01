---
title: Kai-yaking
date: '2008-04-10T16:25:59+00:00'
format: image
service: flickr
tags:
- australia
- kai
- kayaking
- sydney
- water
image: http://i1.wp.com/dentedreality.com.au/wp-content/uploads/2008/04/2436637333_758965e5dd_o.jpg?resize=607%2C455
---

[![Kai-yaking](http://i1.wp.com/dentedreality.com.au/wp-content/uploads/2008/04/2436637333_758965e5dd_o.jpg?resize=607%2C455)](http://dentedreality.com.au/2008/04/10/kai-yaking/) 
# [Kai-yaking](http://dentedreality.com.au/2008/04/10/kai-yaking/)

We rented kayaks at Rose Bay and kayaked around the point to get a snack.





* #[australia](http://dentedreality.com.au/tags/australia/)
* #[kai](http://dentedreality.com.au/tags/kai/)
* #[kayaking](http://dentedreality.com.au/tags/kayaking/)
* #[sydney](http://dentedreality.com.au/tags/sydney/)
* #[water](http://dentedreality.com.au/tags/water/)

Posted on [Flickr](http://www.flickr.com/photos/borkazoid/2436637333/) [4:25 pm, April 10, 2008](http://dentedreality.com.au/2008/04/10/kai-yaking/ "4:25 pm") 
jQuery(document).ready(function(){
var gmap\_m349d2456c975965648c98bc6bb05b43b = {
positions : {
752 : new google.maps.LatLng( '-33.874548', '151.261997' )
},
bounds : new google.maps.LatLngBounds(), // empty for now, we'll dynamically extend it later
map : new google.maps.Map(
document.getElementById( 'gmap\_m349d2456c975965648c98bc6bb05b43b' ),
{
mapTypeId: google.maps.MapTypeId.ROADMAP,
center: new google.maps.LatLng( 0, 0 ),
zoom: 16 // Seems to be a good zoom for a single point
}
),
markers : {},
}; // end of gmap
// Extend the bounds of interest based on our positions
for ( var m in gmap\_m349d2456c975965648c98bc6bb05b43b.positions ) {
gmap\_m349d2456c975965648c98bc6bb05b43b.bounds.extend( gmap\_m349d2456c975965648c98bc6bb05b43b.positions[m] );
}
// Render markers
for ( var m in gmap\_m349d2456c975965648c98bc6bb05b43b.positions ) {
gmap\_m349d2456c975965648c98bc6bb05b43b.markers[m] = new google.maps.Marker( {
clickable: true,
map : gmap\_m349d2456c975965648c98bc6bb05b43b.map,
position : gmap\_m349d2456c975965648c98bc6bb05b43b.positions[m]
} );
}
// Redraw map to fit our new marker-based bounds
gmap\_m349d2456c975965648c98bc6bb05b43b.map.setCenter( gmap\_m349d2456c975965648c98bc6bb05b43b.positions[752] );
});