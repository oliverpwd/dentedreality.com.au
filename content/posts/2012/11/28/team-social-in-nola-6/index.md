---
title: Team Social in NOLA
date: '2012-11-28T16:29:59+00:00'
format: image
service: flickr
tags:
- automattic
- meetup
- neworleans
- nola
- teamsocial
image: http://i0.wp.com/dentedreality.com.au/wp-content/uploads/2012/11/8460392296_16ba7b37cc_o.jpg?resize=607%2C813
---

[![Team Social in NOLA](http://i0.wp.com/dentedreality.com.au/wp-content/uploads/2012/11/8460392296_16ba7b37cc_o.jpg?resize=607%2C813)](http://dentedreality.com.au/2012/11/28/team-social-in-nola-6/) 
# [Team Social in NOLA](http://dentedreality.com.au/2012/11/28/team-social-in-nola-6/)





* #[automattic](http://dentedreality.com.au/tags/automattic/)
* #[meetup](http://dentedreality.com.au/tags/meetup/)
* #[neworleans](http://dentedreality.com.au/tags/neworleans/)
* #[nola](http://dentedreality.com.au/tags/nola/)
* #[teamsocial](http://dentedreality.com.au/tags/teamsocial/)

Posted on [Flickr](http://www.flickr.com/photos/borkazoid/8460392296/) [4:29 pm, November 28, 2012](http://dentedreality.com.au/2012/11/28/team-social-in-nola-6/ "4:29 pm") 
jQuery(document).ready(function(){
var gmap\_m9c3f6fdf0825cf4abaf0ac9eb5e65759 = {
positions : {
912 : new google.maps.LatLng( '29.971833', '-90.0915' )
},
bounds : new google.maps.LatLngBounds(), // empty for now, we'll dynamically extend it later
map : new google.maps.Map(
document.getElementById( 'gmap\_m9c3f6fdf0825cf4abaf0ac9eb5e65759' ),
{
mapTypeId: google.maps.MapTypeId.ROADMAP,
center: new google.maps.LatLng( 0, 0 ),
zoom: 16 // Seems to be a good zoom for a single point
}
),
markers : {},
}; // end of gmap
// Extend the bounds of interest based on our positions
for ( var m in gmap\_m9c3f6fdf0825cf4abaf0ac9eb5e65759.positions ) {
gmap\_m9c3f6fdf0825cf4abaf0ac9eb5e65759.bounds.extend( gmap\_m9c3f6fdf0825cf4abaf0ac9eb5e65759.positions[m] );
}
// Render markers
for ( var m in gmap\_m9c3f6fdf0825cf4abaf0ac9eb5e65759.positions ) {
gmap\_m9c3f6fdf0825cf4abaf0ac9eb5e65759.markers[m] = new google.maps.Marker( {
clickable: true,
map : gmap\_m9c3f6fdf0825cf4abaf0ac9eb5e65759.map,
position : gmap\_m9c3f6fdf0825cf4abaf0ac9eb5e65759.positions[m]
} );
}
// Redraw map to fit our new marker-based bounds
gmap\_m9c3f6fdf0825cf4abaf0ac9eb5e65759.map.setCenter( gmap\_m9c3f6fdf0825cf4abaf0ac9eb5e65759.positions[912] );
});