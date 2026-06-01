---
title: Team Social in Boston
date: '2012-08-12T14:46:10+00:00'
format: image
service: flickr
tags:
- automattic
- meetup
- teamsocial
image: http://i2.wp.com/dentedreality.com.au/wp-content/uploads/2012/08/7770458868_58653d3f58_o.jpg?resize=607%2C607
---

[![Team Social in Boston](http://i2.wp.com/dentedreality.com.au/wp-content/uploads/2012/08/7770458868_58653d3f58_o.jpg?resize=607%2C607)](http://dentedreality.com.au/2012/08/12/team-social-in-boston-17/) 
# [Team Social in Boston](http://dentedreality.com.au/2012/08/12/team-social-in-boston-17/)





* #[automattic](http://dentedreality.com.au/tags/automattic/)
* #[meetup](http://dentedreality.com.au/tags/meetup/)
* #[teamsocial](http://dentedreality.com.au/tags/teamsocial/)

Posted on [Flickr](http://www.flickr.com/photos/borkazoid/7770458868/) [2:46 pm, August 12, 2012](http://dentedreality.com.au/2012/08/12/team-social-in-boston-17/ "2:46 pm") 
jQuery(document).ready(function(){
var gmap\_ma82830dfe9a5859386b71e26b5d27deb = {
positions : {
242 : new google.maps.LatLng( '42.372333', '-71.119334' )
},
bounds : new google.maps.LatLngBounds(), // empty for now, we'll dynamically extend it later
map : new google.maps.Map(
document.getElementById( 'gmap\_ma82830dfe9a5859386b71e26b5d27deb' ),
{
mapTypeId: google.maps.MapTypeId.ROADMAP,
center: new google.maps.LatLng( 0, 0 ),
zoom: 16 // Seems to be a good zoom for a single point
}
),
markers : {},
}; // end of gmap
// Extend the bounds of interest based on our positions
for ( var m in gmap\_ma82830dfe9a5859386b71e26b5d27deb.positions ) {
gmap\_ma82830dfe9a5859386b71e26b5d27deb.bounds.extend( gmap\_ma82830dfe9a5859386b71e26b5d27deb.positions[m] );
}
// Render markers
for ( var m in gmap\_ma82830dfe9a5859386b71e26b5d27deb.positions ) {
gmap\_ma82830dfe9a5859386b71e26b5d27deb.markers[m] = new google.maps.Marker( {
clickable: true,
map : gmap\_ma82830dfe9a5859386b71e26b5d27deb.map,
position : gmap\_ma82830dfe9a5859386b71e26b5d27deb.positions[m]
} );
}
// Redraw map to fit our new marker-based bounds
gmap\_ma82830dfe9a5859386b71e26b5d27deb.map.setCenter( gmap\_ma82830dfe9a5859386b71e26b5d27deb.positions[242] );
});