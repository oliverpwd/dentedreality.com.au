---
title: Team Social in Lisbon
date: '2011-09-28T20:38:18+00:00'
format: image
service: flickr
tags:
- automattic
- Lisbon
- meetup
- portugal
- teamsocial
image: http://i1.wp.com/dentedreality.com.au/wp-content/uploads/2011/09/6812117868_7136c1eebd_o.jpg?resize=607%2C452
---

[![Team Social in Lisbon](http://i1.wp.com/dentedreality.com.au/wp-content/uploads/2011/09/6812117868_7136c1eebd_o.jpg?resize=607%2C452)](http://dentedreality.com.au/2011/09/28/team-social-in-lisbon/) 
# [Team Social in Lisbon](http://dentedreality.com.au/2011/09/28/team-social-in-lisbon/)





* #[automattic](http://dentedreality.com.au/tags/automattic/)
* #[Lisbon](http://dentedreality.com.au/tags/lisbon/)
* #[meetup](http://dentedreality.com.au/tags/meetup/)
* #[portugal](http://dentedreality.com.au/tags/portugal/)
* #[teamsocial](http://dentedreality.com.au/tags/teamsocial/)

Posted on [Flickr](http://www.flickr.com/photos/borkazoid/6812117868/) [8:38 pm, September 28, 2011](http://dentedreality.com.au/2011/09/28/team-social-in-lisbon/ "8:38 pm") 
jQuery(document).ready(function(){
var gmap\_m7dda6a817ae02d4e1972dcb3a746a070 = {
positions : {
299 : new google.maps.LatLng( '38.744333', '-9.134667' )
},
bounds : new google.maps.LatLngBounds(), // empty for now, we'll dynamically extend it later
map : new google.maps.Map(
document.getElementById( 'gmap\_m7dda6a817ae02d4e1972dcb3a746a070' ),
{
mapTypeId: google.maps.MapTypeId.ROADMAP,
center: new google.maps.LatLng( 0, 0 ),
zoom: 16 // Seems to be a good zoom for a single point
}
),
markers : {},
}; // end of gmap
// Extend the bounds of interest based on our positions
for ( var m in gmap\_m7dda6a817ae02d4e1972dcb3a746a070.positions ) {
gmap\_m7dda6a817ae02d4e1972dcb3a746a070.bounds.extend( gmap\_m7dda6a817ae02d4e1972dcb3a746a070.positions[m] );
}
// Render markers
for ( var m in gmap\_m7dda6a817ae02d4e1972dcb3a746a070.positions ) {
gmap\_m7dda6a817ae02d4e1972dcb3a746a070.markers[m] = new google.maps.Marker( {
clickable: true,
map : gmap\_m7dda6a817ae02d4e1972dcb3a746a070.map,
position : gmap\_m7dda6a817ae02d4e1972dcb3a746a070.positions[m]
} );
}
// Redraw map to fit our new marker-based bounds
gmap\_m7dda6a817ae02d4e1972dcb3a746a070.map.setCenter( gmap\_m7dda6a817ae02d4e1972dcb3a746a070.positions[299] );
});