---
title: Team Social Hawaii Meetup
date: '2012-01-13T07:12:42+00:00'
format: image
service: flickr
tags:
- automattic
- bacon
- baconfat
- fat
- hawaii
- kailua
- meetup
- teamsocial
image: http://i0.wp.com/dentedreality.com.au/wp-content/uploads/2012/01/6959543967_09a2f2c028_o.jpg?resize=607%2C452
---

[![Team Social Hawaii Meetup](http://i0.wp.com/dentedreality.com.au/wp-content/uploads/2012/01/6959543967_09a2f2c028_o.jpg?resize=607%2C452)](http://dentedreality.com.au/2012/01/13/team-social-hawaii-meetup-2/) 
# [Team Social Hawaii Meetup](http://dentedreality.com.au/2012/01/13/team-social-hawaii-meetup-2/)

That is one week’s worth of bacon fat. Mmmmm





* #[automattic](http://dentedreality.com.au/tags/automattic/)
* #[bacon](http://dentedreality.com.au/tags/bacon/)
* #[baconfat](http://dentedreality.com.au/tags/baconfat/)
* #[fat](http://dentedreality.com.au/tags/fat/)
* #[hawaii](http://dentedreality.com.au/tags/hawaii/)
* #[kailua](http://dentedreality.com.au/tags/kailua/)
* #[meetup](http://dentedreality.com.au/tags/meetup/)
* #[teamsocial](http://dentedreality.com.au/tags/teamsocial/)

Posted on [Flickr](http://www.flickr.com/photos/borkazoid/6959543967/) [7:12 am, January 13, 2012](http://dentedreality.com.au/2012/01/13/team-social-hawaii-meetup-2/ "7:12 am") 
jQuery(document).ready(function(){
var gmap\_m8d819bc12644ef49add88868da7c8b3e = {
positions : {
87 : new google.maps.LatLng( '21.410999', '-157.742334' )
},
bounds : new google.maps.LatLngBounds(), // empty for now, we'll dynamically extend it later
map : new google.maps.Map(
document.getElementById( 'gmap\_m8d819bc12644ef49add88868da7c8b3e' ),
{
mapTypeId: google.maps.MapTypeId.ROADMAP,
center: new google.maps.LatLng( 0, 0 ),
zoom: 16 // Seems to be a good zoom for a single point
}
),
markers : {},
}; // end of gmap
// Extend the bounds of interest based on our positions
for ( var m in gmap\_m8d819bc12644ef49add88868da7c8b3e.positions ) {
gmap\_m8d819bc12644ef49add88868da7c8b3e.bounds.extend( gmap\_m8d819bc12644ef49add88868da7c8b3e.positions[m] );
}
// Render markers
for ( var m in gmap\_m8d819bc12644ef49add88868da7c8b3e.positions ) {
gmap\_m8d819bc12644ef49add88868da7c8b3e.markers[m] = new google.maps.Marker( {
clickable: true,
map : gmap\_m8d819bc12644ef49add88868da7c8b3e.map,
position : gmap\_m8d819bc12644ef49add88868da7c8b3e.positions[m]
} );
}
// Redraw map to fit our new marker-based bounds
gmap\_m8d819bc12644ef49add88868da7c8b3e.map.setCenter( gmap\_m8d819bc12644ef49add88868da7c8b3e.positions[87] );
});