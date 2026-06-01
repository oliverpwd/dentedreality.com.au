---
title: Team Social in NOLA
date: '2012-11-26T15:33:11+00:00'
format: image
service: flickr
tags:
- automattic
- meetup
- neworleans
- nola
- teamsocial
image: http://i2.wp.com/dentedreality.com.au/wp-content/uploads/2012/11/8459288825_3a23821deb_o.jpg?resize=607%2C813
---

[![Team Social in NOLA](http://i2.wp.com/dentedreality.com.au/wp-content/uploads/2012/11/8459288825_3a23821deb_o.jpg?resize=607%2C813)](http://dentedreality.com.au/2012/11/26/team-social-in-nola-11/) 
# [Team Social in NOLA](http://dentedreality.com.au/2012/11/26/team-social-in-nola-11/)





* #[automattic](http://dentedreality.com.au/tags/automattic/)
* #[meetup](http://dentedreality.com.au/tags/meetup/)
* #[neworleans](http://dentedreality.com.au/tags/neworleans/)
* #[nola](http://dentedreality.com.au/tags/nola/)
* #[teamsocial](http://dentedreality.com.au/tags/teamsocial/)

Posted on [Flickr](http://www.flickr.com/photos/borkazoid/8459288825/) [3:33 pm, November 26, 2012](http://dentedreality.com.au/2012/11/26/team-social-in-nola-11/ "3:33 pm") 
jQuery(document).ready(function(){
var gmap\_mb178dab0e3044e05b644e50d492080f1 = {
positions : {
812 : new google.maps.LatLng( '29.935', '-90.105667' )
},
bounds : new google.maps.LatLngBounds(), // empty for now, we'll dynamically extend it later
map : new google.maps.Map(
document.getElementById( 'gmap\_mb178dab0e3044e05b644e50d492080f1' ),
{
mapTypeId: google.maps.MapTypeId.ROADMAP,
center: new google.maps.LatLng( 0, 0 ),
zoom: 16 // Seems to be a good zoom for a single point
}
),
markers : {},
}; // end of gmap
// Extend the bounds of interest based on our positions
for ( var m in gmap\_mb178dab0e3044e05b644e50d492080f1.positions ) {
gmap\_mb178dab0e3044e05b644e50d492080f1.bounds.extend( gmap\_mb178dab0e3044e05b644e50d492080f1.positions[m] );
}
// Render markers
for ( var m in gmap\_mb178dab0e3044e05b644e50d492080f1.positions ) {
gmap\_mb178dab0e3044e05b644e50d492080f1.markers[m] = new google.maps.Marker( {
clickable: true,
map : gmap\_mb178dab0e3044e05b644e50d492080f1.map,
position : gmap\_mb178dab0e3044e05b644e50d492080f1.positions[m]
} );
}
// Redraw map to fit our new marker-based bounds
gmap\_mb178dab0e3044e05b644e50d492080f1.map.setCenter( gmap\_mb178dab0e3044e05b644e50d492080f1.positions[812] );
});