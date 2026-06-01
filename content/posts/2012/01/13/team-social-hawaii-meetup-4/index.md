---
title: Team Social Hawaii Meetup
date: '2012-01-13T03:23:21+00:00'
format: image
service: flickr
tags:
- automattic
- beach
- hawaii
- kailua
- meetup
- sun
- sunrise
- teamsocial
image: http://i0.wp.com/dentedreality.com.au/wp-content/uploads/2012/01/6959543405_4199c7a638_o.jpg?resize=607%2C452
---

[![Team Social Hawaii Meetup](http://i0.wp.com/dentedreality.com.au/wp-content/uploads/2012/01/6959543405_4199c7a638_o.jpg?resize=607%2C452)](http://dentedreality.com.au/2012/01/13/team-social-hawaii-meetup-4/) 
# [Team Social Hawaii Meetup](http://dentedreality.com.au/2012/01/13/team-social-hawaii-meetup-4/)

Sun"rise"





* #[automattic](http://dentedreality.com.au/tags/automattic/)
* #[beach](http://dentedreality.com.au/tags/beach/)
* #[hawaii](http://dentedreality.com.au/tags/hawaii/)
* #[kailua](http://dentedreality.com.au/tags/kailua/)
* #[meetup](http://dentedreality.com.au/tags/meetup/)
* #[sun](http://dentedreality.com.au/tags/sun/)
* #[sunrise](http://dentedreality.com.au/tags/sunrise/)
* #[teamsocial](http://dentedreality.com.au/tags/teamsocial/)

Posted on [Flickr](http://www.flickr.com/photos/borkazoid/6959543405/) [3:23 am, January 13, 2012](http://dentedreality.com.au/2012/01/13/team-social-hawaii-meetup-4/ "3:23 am") 
jQuery(document).ready(function(){
var gmap\_mef04e5138b7a6e10df0d26dbe29daa30 = {
positions : {
729 : new google.maps.LatLng( '21.410999', '-157.742334' )
},
bounds : new google.maps.LatLngBounds(), // empty for now, we'll dynamically extend it later
map : new google.maps.Map(
document.getElementById( 'gmap\_mef04e5138b7a6e10df0d26dbe29daa30' ),
{
mapTypeId: google.maps.MapTypeId.ROADMAP,
center: new google.maps.LatLng( 0, 0 ),
zoom: 16 // Seems to be a good zoom for a single point
}
),
markers : {},
}; // end of gmap
// Extend the bounds of interest based on our positions
for ( var m in gmap\_mef04e5138b7a6e10df0d26dbe29daa30.positions ) {
gmap\_mef04e5138b7a6e10df0d26dbe29daa30.bounds.extend( gmap\_mef04e5138b7a6e10df0d26dbe29daa30.positions[m] );
}
// Render markers
for ( var m in gmap\_mef04e5138b7a6e10df0d26dbe29daa30.positions ) {
gmap\_mef04e5138b7a6e10df0d26dbe29daa30.markers[m] = new google.maps.Marker( {
clickable: true,
map : gmap\_mef04e5138b7a6e10df0d26dbe29daa30.map,
position : gmap\_mef04e5138b7a6e10df0d26dbe29daa30.positions[m]
} );
}
// Redraw map to fit our new marker-based bounds
gmap\_mef04e5138b7a6e10df0d26dbe29daa30.map.setCenter( gmap\_mef04e5138b7a6e10df0d26dbe29daa30.positions[729] );
});