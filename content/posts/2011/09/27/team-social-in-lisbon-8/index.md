---
title: Team Social in Lisbon
date: '2011-09-27T12:50:08+00:00'
format: image
service: flickr
tags:
- automattic
- Lisbon
- meetup
- portugal
- teamsocial
- tomb
image: http://i0.wp.com/dentedreality.com.au/wp-content/uploads/2011/09/6812115898_0a99975b25_o.jpg?resize=607%2C813
---

[![Team Social in Lisbon](http://i0.wp.com/dentedreality.com.au/wp-content/uploads/2011/09/6812115898_0a99975b25_o.jpg?resize=607%2C813)](http://dentedreality.com.au/2011/09/27/team-social-in-lisbon-8/) 
# [Team Social in Lisbon](http://dentedreality.com.au/2011/09/27/team-social-in-lisbon-8/)





* #[automattic](http://dentedreality.com.au/tags/automattic/)
* #[Lisbon](http://dentedreality.com.au/tags/lisbon/)
* #[meetup](http://dentedreality.com.au/tags/meetup/)
* #[portugal](http://dentedreality.com.au/tags/portugal/)
* #[teamsocial](http://dentedreality.com.au/tags/teamsocial/)
* #[tomb](http://dentedreality.com.au/tags/tomb/)

Posted on [Flickr](http://www.flickr.com/photos/borkazoid/6812115898/) [12:50 pm, September 27, 2011](http://dentedreality.com.au/2011/09/27/team-social-in-lisbon-8/ "12:50 pm") 
jQuery(document).ready(function(){
var gmap\_m534ceecbf90b3101d7012f61a90ac456 = {
positions : {
73 : new google.maps.LatLng( '38.695833', '-9.205834' )
},
bounds : new google.maps.LatLngBounds(), // empty for now, we'll dynamically extend it later
map : new google.maps.Map(
document.getElementById( 'gmap\_m534ceecbf90b3101d7012f61a90ac456' ),
{
mapTypeId: google.maps.MapTypeId.ROADMAP,
center: new google.maps.LatLng( 0, 0 ),
zoom: 16 // Seems to be a good zoom for a single point
}
),
markers : {},
}; // end of gmap
// Extend the bounds of interest based on our positions
for ( var m in gmap\_m534ceecbf90b3101d7012f61a90ac456.positions ) {
gmap\_m534ceecbf90b3101d7012f61a90ac456.bounds.extend( gmap\_m534ceecbf90b3101d7012f61a90ac456.positions[m] );
}
// Render markers
for ( var m in gmap\_m534ceecbf90b3101d7012f61a90ac456.positions ) {
gmap\_m534ceecbf90b3101d7012f61a90ac456.markers[m] = new google.maps.Marker( {
clickable: true,
map : gmap\_m534ceecbf90b3101d7012f61a90ac456.map,
position : gmap\_m534ceecbf90b3101d7012f61a90ac456.positions[m]
} );
}
// Redraw map to fit our new marker-based bounds
gmap\_m534ceecbf90b3101d7012f61a90ac456.map.setCenter( gmap\_m534ceecbf90b3101d7012f61a90ac456.positions[73] );
});