---
title: Team Social in Lisbon
date: '2011-09-27T12:50:34+00:00'
format: image
service: flickr
tags:
- automattic
- church
- Lisbon
- meetup
- portugal
- teamsocial
image: http://i1.wp.com/dentedreality.com.au/wp-content/uploads/2011/09/6958226163_6f807c6923_o.jpg?resize=607%2C813
---

[![Team Social in Lisbon](http://i1.wp.com/dentedreality.com.au/wp-content/uploads/2011/09/6958226163_6f807c6923_o.jpg?resize=607%2C813)](http://dentedreality.com.au/2011/09/27/team-social-in-lisbon-7/) 
# [Team Social in Lisbon](http://dentedreality.com.au/2011/09/27/team-social-in-lisbon-7/)





* #[automattic](http://dentedreality.com.au/tags/automattic/)
* #[church](http://dentedreality.com.au/tags/church/)
* #[Lisbon](http://dentedreality.com.au/tags/lisbon/)
* #[meetup](http://dentedreality.com.au/tags/meetup/)
* #[portugal](http://dentedreality.com.au/tags/portugal/)
* #[teamsocial](http://dentedreality.com.au/tags/teamsocial/)

Posted on [Flickr](http://www.flickr.com/photos/borkazoid/6958226163/) [12:50 pm, September 27, 2011](http://dentedreality.com.au/2011/09/27/team-social-in-lisbon-7/ "12:50 pm") 
jQuery(document).ready(function(){
var gmap\_mc6627ddf292d675990c32dd60692620a = {
positions : {
533 : new google.maps.LatLng( '38.695833', '-9.205834' )
},
bounds : new google.maps.LatLngBounds(), // empty for now, we'll dynamically extend it later
map : new google.maps.Map(
document.getElementById( 'gmap\_mc6627ddf292d675990c32dd60692620a' ),
{
mapTypeId: google.maps.MapTypeId.ROADMAP,
center: new google.maps.LatLng( 0, 0 ),
zoom: 16 // Seems to be a good zoom for a single point
}
),
markers : {},
}; // end of gmap
// Extend the bounds of interest based on our positions
for ( var m in gmap\_mc6627ddf292d675990c32dd60692620a.positions ) {
gmap\_mc6627ddf292d675990c32dd60692620a.bounds.extend( gmap\_mc6627ddf292d675990c32dd60692620a.positions[m] );
}
// Render markers
for ( var m in gmap\_mc6627ddf292d675990c32dd60692620a.positions ) {
gmap\_mc6627ddf292d675990c32dd60692620a.markers[m] = new google.maps.Marker( {
clickable: true,
map : gmap\_mc6627ddf292d675990c32dd60692620a.map,
position : gmap\_mc6627ddf292d675990c32dd60692620a.positions[m]
} );
}
// Redraw map to fit our new marker-based bounds
gmap\_mc6627ddf292d675990c32dd60692620a.map.setCenter( gmap\_mc6627ddf292d675990c32dd60692620a.positions[533] );
});