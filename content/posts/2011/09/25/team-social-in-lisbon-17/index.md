---
title: Team Social in Lisbon
date: '2011-09-25T11:17:21+00:00'
format: image
service: flickr
tags:
- automattic
- boat
- Lisbon
- meetup
- portugal
- sail
- teamsocial
image: http://i0.wp.com/dentedreality.com.au/wp-content/uploads/2011/09/6812113364_84fb195b57_o.jpg?resize=607%2C813
---

[![Team Social in Lisbon](http://i0.wp.com/dentedreality.com.au/wp-content/uploads/2011/09/6812113364_84fb195b57_o.jpg?resize=607%2C813)](http://dentedreality.com.au/2011/09/25/team-social-in-lisbon-17/) 
# [Team Social in Lisbon](http://dentedreality.com.au/2011/09/25/team-social-in-lisbon-17/)





* #[automattic](http://dentedreality.com.au/tags/automattic/)
* #[boat](http://dentedreality.com.au/tags/boat/)
* #[Lisbon](http://dentedreality.com.au/tags/lisbon/)
* #[meetup](http://dentedreality.com.au/tags/meetup/)
* #[portugal](http://dentedreality.com.au/tags/portugal/)
* #[sail](http://dentedreality.com.au/tags/sail/)
* #[teamsocial](http://dentedreality.com.au/tags/teamsocial/)

Posted on [Flickr](http://www.flickr.com/photos/borkazoid/6812113364/) [11:17 am, September 25, 2011](http://dentedreality.com.au/2011/09/25/team-social-in-lisbon-17/ "11:17 am") 
jQuery(document).ready(function(){
var gmap\_m66ac2c32655c3cc314e181d95cdbbb4a = {
positions : {
583 : new google.maps.LatLng( '38.768499', '-9.167834' )
},
bounds : new google.maps.LatLngBounds(), // empty for now, we'll dynamically extend it later
map : new google.maps.Map(
document.getElementById( 'gmap\_m66ac2c32655c3cc314e181d95cdbbb4a' ),
{
mapTypeId: google.maps.MapTypeId.ROADMAP,
center: new google.maps.LatLng( 0, 0 ),
zoom: 16 // Seems to be a good zoom for a single point
}
),
markers : {},
}; // end of gmap
// Extend the bounds of interest based on our positions
for ( var m in gmap\_m66ac2c32655c3cc314e181d95cdbbb4a.positions ) {
gmap\_m66ac2c32655c3cc314e181d95cdbbb4a.bounds.extend( gmap\_m66ac2c32655c3cc314e181d95cdbbb4a.positions[m] );
}
// Render markers
for ( var m in gmap\_m66ac2c32655c3cc314e181d95cdbbb4a.positions ) {
gmap\_m66ac2c32655c3cc314e181d95cdbbb4a.markers[m] = new google.maps.Marker( {
clickable: true,
map : gmap\_m66ac2c32655c3cc314e181d95cdbbb4a.map,
position : gmap\_m66ac2c32655c3cc314e181d95cdbbb4a.positions[m]
} );
}
// Redraw map to fit our new marker-based bounds
gmap\_m66ac2c32655c3cc314e181d95cdbbb4a.map.setCenter( gmap\_m66ac2c32655c3cc314e181d95cdbbb4a.positions[583] );
});