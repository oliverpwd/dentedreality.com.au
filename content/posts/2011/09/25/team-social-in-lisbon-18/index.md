---
title: Team Social in Lisbon
date: '2011-09-25T10:20:48+00:00'
format: image
service: flickr
tags:
- automattic
- boat
- Lisbon
- meetup
- portugal
- teamsocial
image: http://i2.wp.com/dentedreality.com.au/wp-content/uploads/2011/09/6958222871_61fdb4baf6_o.jpg?resize=607%2C813
---

[![Team Social in Lisbon](http://i2.wp.com/dentedreality.com.au/wp-content/uploads/2011/09/6958222871_61fdb4baf6_o.jpg?resize=607%2C813)](http://dentedreality.com.au/2011/09/25/team-social-in-lisbon-18/) 
# [Team Social in Lisbon](http://dentedreality.com.au/2011/09/25/team-social-in-lisbon-18/)





* #[automattic](http://dentedreality.com.au/tags/automattic/)
* #[boat](http://dentedreality.com.au/tags/boat/)
* #[Lisbon](http://dentedreality.com.au/tags/lisbon/)
* #[meetup](http://dentedreality.com.au/tags/meetup/)
* #[portugal](http://dentedreality.com.au/tags/portugal/)
* #[teamsocial](http://dentedreality.com.au/tags/teamsocial/)

Posted on [Flickr](http://www.flickr.com/photos/borkazoid/6958222871/) [10:20 am, September 25, 2011](http://dentedreality.com.au/2011/09/25/team-social-in-lisbon-18/ "10:20 am") 
jQuery(document).ready(function(){
var gmap\_mef0972eb6eca1d225111f432ceca6813 = {
positions : {
486 : new google.maps.LatLng( '38.702666', '-9.1655' )
},
bounds : new google.maps.LatLngBounds(), // empty for now, we'll dynamically extend it later
map : new google.maps.Map(
document.getElementById( 'gmap\_mef0972eb6eca1d225111f432ceca6813' ),
{
mapTypeId: google.maps.MapTypeId.ROADMAP,
center: new google.maps.LatLng( 0, 0 ),
zoom: 16 // Seems to be a good zoom for a single point
}
),
markers : {},
}; // end of gmap
// Extend the bounds of interest based on our positions
for ( var m in gmap\_mef0972eb6eca1d225111f432ceca6813.positions ) {
gmap\_mef0972eb6eca1d225111f432ceca6813.bounds.extend( gmap\_mef0972eb6eca1d225111f432ceca6813.positions[m] );
}
// Render markers
for ( var m in gmap\_mef0972eb6eca1d225111f432ceca6813.positions ) {
gmap\_mef0972eb6eca1d225111f432ceca6813.markers[m] = new google.maps.Marker( {
clickable: true,
map : gmap\_mef0972eb6eca1d225111f432ceca6813.map,
position : gmap\_mef0972eb6eca1d225111f432ceca6813.positions[m]
} );
}
// Redraw map to fit our new marker-based bounds
gmap\_mef0972eb6eca1d225111f432ceca6813.map.setCenter( gmap\_mef0972eb6eca1d225111f432ceca6813.positions[486] );
});