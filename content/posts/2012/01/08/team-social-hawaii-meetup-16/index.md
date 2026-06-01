---
title: Team Social Hawaii Meetup
date: '2012-01-08T11:45:30+00:00'
format: image
service: flickr
tags:
- automattic
- hawaii
- kailua
- meetup
- teamsocial
image: http://i1.wp.com/dentedreality.com.au/wp-content/uploads/2012/01/6813426752_607e187f46_o.jpg?resize=607%2C452
---

[![Team Social Hawaii Meetup](http://i1.wp.com/dentedreality.com.au/wp-content/uploads/2012/01/6813426752_607e187f46_o.jpg?resize=607%2C452)](http://dentedreality.com.au/2012/01/08/team-social-hawaii-meetup-16/) 
# [Team Social Hawaii Meetup](http://dentedreality.com.au/2012/01/08/team-social-hawaii-meetup-16/)





* #[automattic](http://dentedreality.com.au/tags/automattic/)
* #[hawaii](http://dentedreality.com.au/tags/hawaii/)
* #[kailua](http://dentedreality.com.au/tags/kailua/)
* #[meetup](http://dentedreality.com.au/tags/meetup/)
* #[teamsocial](http://dentedreality.com.au/tags/teamsocial/)

Posted on [Flickr](http://www.flickr.com/photos/borkazoid/6813426752/) [11:45 am, January 8, 2012](http://dentedreality.com.au/2012/01/08/team-social-hawaii-meetup-16/ "11:45 am") 
jQuery(document).ready(function(){
var gmap\_md9071eaf2867c6e8db1a0a6f51d309c1 = {
positions : {
723 : new google.maps.LatLng( '21.410999', '-157.742334' )
},
bounds : new google.maps.LatLngBounds(), // empty for now, we'll dynamically extend it later
map : new google.maps.Map(
document.getElementById( 'gmap\_md9071eaf2867c6e8db1a0a6f51d309c1' ),
{
mapTypeId: google.maps.MapTypeId.ROADMAP,
center: new google.maps.LatLng( 0, 0 ),
zoom: 16 // Seems to be a good zoom for a single point
}
),
markers : {},
}; // end of gmap
// Extend the bounds of interest based on our positions
for ( var m in gmap\_md9071eaf2867c6e8db1a0a6f51d309c1.positions ) {
gmap\_md9071eaf2867c6e8db1a0a6f51d309c1.bounds.extend( gmap\_md9071eaf2867c6e8db1a0a6f51d309c1.positions[m] );
}
// Render markers
for ( var m in gmap\_md9071eaf2867c6e8db1a0a6f51d309c1.positions ) {
gmap\_md9071eaf2867c6e8db1a0a6f51d309c1.markers[m] = new google.maps.Marker( {
clickable: true,
map : gmap\_md9071eaf2867c6e8db1a0a6f51d309c1.map,
position : gmap\_md9071eaf2867c6e8db1a0a6f51d309c1.positions[m]
} );
}
// Redraw map to fit our new marker-based bounds
gmap\_md9071eaf2867c6e8db1a0a6f51d309c1.map.setCenter( gmap\_md9071eaf2867c6e8db1a0a6f51d309c1.positions[723] );
});