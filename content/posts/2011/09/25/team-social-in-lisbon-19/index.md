---
title: Team Social in Lisbon
date: '2011-09-25T09:48:01-06:00'
format: image
service: flickr
tags:
- automattic
- Lisbon
- meetup
- portugal
- teamsocial
latitude: '38.719833'
longitude: '-9.1475'
image: https://s3.amazonaws.com/dentedreality-content/wp-content/uploads/2011/09/14190319/6812112670_2f30fc82b0_o.jpg
---

[![Team Social in Lisbon](https://s3.amazonaws.com/dentedreality-content/wp-content/uploads/2011/09/14190319/6812112670_2f30fc82b0_o.jpg)](https://dentedreality.com.au/2011/09/25/team-social-in-lisbon-19/) 
# [Team Social in Lisbon](https://dentedreality.com.au/2011/09/25/team-social-in-lisbon-19/)

[![Team Social in Lisbon](https://s3.amazonaws.com/dentedreality-content/wp-content/uploads/2011/09/14190319/6812112670_2f30fc82b0_o.jpg)](http://www.flickr.com/photos/borkazoid/6812112670/)

38.719833-9.1475




* #[automattic](https://dentedreality.com.au/tags/automattic/)
* #[Lisbon](https://dentedreality.com.au/tags/lisbon/)
* #[meetup](https://dentedreality.com.au/tags/meetup/)
* #[portugal](https://dentedreality.com.au/tags/portugal/)
* #[teamsocial](https://dentedreality.com.au/tags/teamsocial/)

Posted on [Flickr](http://www.flickr.com/photos/borkazoid/6812112670/) [9:48 am, September 25, 2011](https://dentedreality.com.au/2011/09/25/team-social-in-lisbon-19/ "9:48 am") 
jQuery(document).ready(function(){
var gmap\_m00815dedaa5c63e4ab81764ea951b6b4 = {
positions : {
254 : new google.maps.LatLng( '38.719833', '-9.1475' )
},
bounds : new google.maps.LatLngBounds(), // empty for now, we'll dynamically extend it later
map : new google.maps.Map(
document.getElementById( 'gmap\_m00815dedaa5c63e4ab81764ea951b6b4' ),
{
mapTypeId: google.maps.MapTypeId.ROADMAP,
center: new google.maps.LatLng( 0, 0 ),
zoom: 16 // Seems to be a good zoom for a single point
}
),
markers : {},
}; // end of gmap
// Extend the bounds of interest based on our positions
for ( var m in gmap\_m00815dedaa5c63e4ab81764ea951b6b4.positions ) {
gmap\_m00815dedaa5c63e4ab81764ea951b6b4.bounds.extend( gmap\_m00815dedaa5c63e4ab81764ea951b6b4.positions[m] );
}
// Render markers
for ( var m in gmap\_m00815dedaa5c63e4ab81764ea951b6b4.positions ) {
gmap\_m00815dedaa5c63e4ab81764ea951b6b4.markers[m] = new google.maps.Marker( {
clickable: true,
map : gmap\_m00815dedaa5c63e4ab81764ea951b6b4.map,
position : gmap\_m00815dedaa5c63e4ab81764ea951b6b4.positions[m]
} );
}
// Redraw map to fit our new marker-based bounds
gmap\_m00815dedaa5c63e4ab81764ea951b6b4.map.setCenter( gmap\_m00815dedaa5c63e4ab81764ea951b6b4.positions[254] );
});