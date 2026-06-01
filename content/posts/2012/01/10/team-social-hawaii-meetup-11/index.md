---
title: Team Social Hawaii Meetup
date: '2012-01-10T09:04:03+00:00'
format: image
service: flickr
tags:
- automattic
- hawaii
- kailua
- meetup
- skype
- teamsocial
- teleconference
- videochat
image: http://i1.wp.com/dentedreality.com.au/wp-content/uploads/2012/01/6813428048_b107e6c2dc_o.jpg?resize=607%2C452
---

[![Team Social Hawaii Meetup](http://i1.wp.com/dentedreality.com.au/wp-content/uploads/2012/01/6813428048_b107e6c2dc_o.jpg?resize=607%2C452)](http://dentedreality.com.au/2012/01/10/team-social-hawaii-meetup-11/) 
# [Team Social Hawaii Meetup](http://dentedreality.com.au/2012/01/10/team-social-hawaii-meetup-11/)

Teleconference





* #[automattic](http://dentedreality.com.au/tags/automattic/)
* #[hawaii](http://dentedreality.com.au/tags/hawaii/)
* #[kailua](http://dentedreality.com.au/tags/kailua/)
* #[meetup](http://dentedreality.com.au/tags/meetup/)
* #[skype](http://dentedreality.com.au/tags/skype/)
* #[teamsocial](http://dentedreality.com.au/tags/teamsocial/)
* #[teleconference](http://dentedreality.com.au/tags/teleconference/)
* #[videochat](http://dentedreality.com.au/tags/videochat/)

Posted on [Flickr](http://www.flickr.com/photos/borkazoid/6813428048/) [9:04 am, January 10, 2012](http://dentedreality.com.au/2012/01/10/team-social-hawaii-meetup-11/ "9:04 am") 
jQuery(document).ready(function(){
var gmap\_m52d1ebaa8ca8631e34bc30b5a55c6a75 = {
positions : {
46 : new google.maps.LatLng( '21.410999', '-157.742334' )
},
bounds : new google.maps.LatLngBounds(), // empty for now, we'll dynamically extend it later
map : new google.maps.Map(
document.getElementById( 'gmap\_m52d1ebaa8ca8631e34bc30b5a55c6a75' ),
{
mapTypeId: google.maps.MapTypeId.ROADMAP,
center: new google.maps.LatLng( 0, 0 ),
zoom: 16 // Seems to be a good zoom for a single point
}
),
markers : {},
}; // end of gmap
// Extend the bounds of interest based on our positions
for ( var m in gmap\_m52d1ebaa8ca8631e34bc30b5a55c6a75.positions ) {
gmap\_m52d1ebaa8ca8631e34bc30b5a55c6a75.bounds.extend( gmap\_m52d1ebaa8ca8631e34bc30b5a55c6a75.positions[m] );
}
// Render markers
for ( var m in gmap\_m52d1ebaa8ca8631e34bc30b5a55c6a75.positions ) {
gmap\_m52d1ebaa8ca8631e34bc30b5a55c6a75.markers[m] = new google.maps.Marker( {
clickable: true,
map : gmap\_m52d1ebaa8ca8631e34bc30b5a55c6a75.map,
position : gmap\_m52d1ebaa8ca8631e34bc30b5a55c6a75.positions[m]
} );
}
// Redraw map to fit our new marker-based bounds
gmap\_m52d1ebaa8ca8631e34bc30b5a55c6a75.map.setCenter( gmap\_m52d1ebaa8ca8631e34bc30b5a55c6a75.positions[46] );
});