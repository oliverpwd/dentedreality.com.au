---
title: Team Social in Lisbon
date: '2011-09-23T07:00:43-06:00'
format: image
service: flickr
tags:
- automattic
- Lisbon
- meetup
- portugal
- teamsocial
- view
latitude: '38.7155'
longitude: '-9.145'
image: https://s3.amazonaws.com/dentedreality-content/wp-content/uploads/2011/09/14190314/6812110826_b0d21987a4_o.jpg
---

[![Team Social in Lisbon](https://s3.amazonaws.com/dentedreality-content/wp-content/uploads/2011/09/14190314/6812110826_b0d21987a4_o.jpg)](https://dentedreality.com.au/2011/09/23/team-social-in-lisbon-25/) 
# [Team Social in Lisbon](https://dentedreality.com.au/2011/09/23/team-social-in-lisbon-25/)

[![Team Social in Lisbon](https://s3.amazonaws.com/dentedreality-content/wp-content/uploads/2011/09/14190314/6812110826_b0d21987a4_o.jpg)](http://www.flickr.com/photos/borkazoid/6812110826/)

38.7155-9.145




* #[automattic](https://dentedreality.com.au/tags/automattic/)
* #[Lisbon](https://dentedreality.com.au/tags/lisbon/)
* #[meetup](https://dentedreality.com.au/tags/meetup/)
* #[portugal](https://dentedreality.com.au/tags/portugal/)
* #[teamsocial](https://dentedreality.com.au/tags/teamsocial/)
* #[view](https://dentedreality.com.au/tags/view/)

Posted on [Flickr](http://www.flickr.com/photos/borkazoid/6812110826/) [7:00 am, September 23, 2011](https://dentedreality.com.au/2011/09/23/team-social-in-lisbon-25/ "7:00 am") 
jQuery(document).ready(function(){
var gmap\_m8875bc599708e273afc89dccc1b5d224 = {
positions : {
93 : new google.maps.LatLng( '38.7155', '-9.145' )
},
bounds : new google.maps.LatLngBounds(), // empty for now, we'll dynamically extend it later
map : new google.maps.Map(
document.getElementById( 'gmap\_m8875bc599708e273afc89dccc1b5d224' ),
{
mapTypeId: google.maps.MapTypeId.ROADMAP,
center: new google.maps.LatLng( 0, 0 ),
zoom: 16 // Seems to be a good zoom for a single point
}
),
markers : {},
}; // end of gmap
// Extend the bounds of interest based on our positions
for ( var m in gmap\_m8875bc599708e273afc89dccc1b5d224.positions ) {
gmap\_m8875bc599708e273afc89dccc1b5d224.bounds.extend( gmap\_m8875bc599708e273afc89dccc1b5d224.positions[m] );
}
// Render markers
for ( var m in gmap\_m8875bc599708e273afc89dccc1b5d224.positions ) {
gmap\_m8875bc599708e273afc89dccc1b5d224.markers[m] = new google.maps.Marker( {
clickable: true,
map : gmap\_m8875bc599708e273afc89dccc1b5d224.map,
position : gmap\_m8875bc599708e273afc89dccc1b5d224.positions[m]
} );
}
// Redraw map to fit our new marker-based bounds
gmap\_m8875bc599708e273afc89dccc1b5d224.map.setCenter( gmap\_m8875bc599708e273afc89dccc1b5d224.positions[93] );
});