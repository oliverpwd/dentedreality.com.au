---
title: Team Social in NOLA
date: '2012-11-26T15:34:29+00:00'
format: image
service: flickr
tags:
- automattic
- meetup
- neworleans
- nola
- teamsocial
image: http://i1.wp.com/dentedreality.com.au/wp-content/uploads/2012/11/8459288979_eb404f569f_o.jpg?resize=607%2C452
---

[![Team Social in NOLA](http://i1.wp.com/dentedreality.com.au/wp-content/uploads/2012/11/8459288979_eb404f569f_o.jpg?resize=607%2C452)](http://dentedreality.com.au/2012/11/26/team-social-in-nola-10/) 
# [Team Social in NOLA](http://dentedreality.com.au/2012/11/26/team-social-in-nola-10/)





* #[automattic](http://dentedreality.com.au/tags/automattic/)
* #[meetup](http://dentedreality.com.au/tags/meetup/)
* #[neworleans](http://dentedreality.com.au/tags/neworleans/)
* #[nola](http://dentedreality.com.au/tags/nola/)
* #[teamsocial](http://dentedreality.com.au/tags/teamsocial/)

Posted on [Flickr](http://www.flickr.com/photos/borkazoid/8459288979/) [3:34 pm, November 26, 2012](http://dentedreality.com.au/2012/11/26/team-social-in-nola-10/ "3:34 pm") 
jQuery(document).ready(function(){
var gmap\_m958e982d92de6f9c00294ba4075bb679 = {
positions : {
844 : new google.maps.LatLng( '29.935', '-90.105667' )
},
bounds : new google.maps.LatLngBounds(), // empty for now, we'll dynamically extend it later
map : new google.maps.Map(
document.getElementById( 'gmap\_m958e982d92de6f9c00294ba4075bb679' ),
{
mapTypeId: google.maps.MapTypeId.ROADMAP,
center: new google.maps.LatLng( 0, 0 ),
zoom: 16 // Seems to be a good zoom for a single point
}
),
markers : {},
}; // end of gmap
// Extend the bounds of interest based on our positions
for ( var m in gmap\_m958e982d92de6f9c00294ba4075bb679.positions ) {
gmap\_m958e982d92de6f9c00294ba4075bb679.bounds.extend( gmap\_m958e982d92de6f9c00294ba4075bb679.positions[m] );
}
// Render markers
for ( var m in gmap\_m958e982d92de6f9c00294ba4075bb679.positions ) {
gmap\_m958e982d92de6f9c00294ba4075bb679.markers[m] = new google.maps.Marker( {
clickable: true,
map : gmap\_m958e982d92de6f9c00294ba4075bb679.map,
position : gmap\_m958e982d92de6f9c00294ba4075bb679.positions[m]
} );
}
// Redraw map to fit our new marker-based bounds
gmap\_m958e982d92de6f9c00294ba4075bb679.map.setCenter( gmap\_m958e982d92de6f9c00294ba4075bb679.positions[844] );
});