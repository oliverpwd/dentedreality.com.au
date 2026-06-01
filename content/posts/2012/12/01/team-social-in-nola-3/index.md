---
title: Team Social in NOLA
date: '2012-12-01T08:10:55+00:00'
format: image
service: flickr
tags:
- automattic
- meetup
- neworleans
- nola
- teamsocial
image: http://i1.wp.com/dentedreality.com.au/wp-content/uploads/2012/12/8460396118_52252b56c5_o.jpg?resize=607%2C455
---

[![Team Social in NOLA](http://i1.wp.com/dentedreality.com.au/wp-content/uploads/2012/12/8460396118_52252b56c5_o.jpg?resize=607%2C455)](http://dentedreality.com.au/2012/12/01/team-social-in-nola-3/) 
# [Team Social in NOLA](http://dentedreality.com.au/2012/12/01/team-social-in-nola-3/)





* #[automattic](http://dentedreality.com.au/tags/automattic/)
* #[meetup](http://dentedreality.com.au/tags/meetup/)
* #[neworleans](http://dentedreality.com.au/tags/neworleans/)
* #[nola](http://dentedreality.com.au/tags/nola/)
* #[teamsocial](http://dentedreality.com.au/tags/teamsocial/)

Posted on [Flickr](http://www.flickr.com/photos/borkazoid/8460396118/) [8:10 am, December 1, 2012](http://dentedreality.com.au/2012/12/01/team-social-in-nola-3/ "8:10 am") 
jQuery(document).ready(function(){
var gmap\_m618f792f2f2719339e35eb57c92d1dad = {
positions : {
897 : new google.maps.LatLng( '30.136355', '-90.135373' )
},
bounds : new google.maps.LatLngBounds(), // empty for now, we'll dynamically extend it later
map : new google.maps.Map(
document.getElementById( 'gmap\_m618f792f2f2719339e35eb57c92d1dad' ),
{
mapTypeId: google.maps.MapTypeId.ROADMAP,
center: new google.maps.LatLng( 0, 0 ),
zoom: 16 // Seems to be a good zoom for a single point
}
),
markers : {},
}; // end of gmap
// Extend the bounds of interest based on our positions
for ( var m in gmap\_m618f792f2f2719339e35eb57c92d1dad.positions ) {
gmap\_m618f792f2f2719339e35eb57c92d1dad.bounds.extend( gmap\_m618f792f2f2719339e35eb57c92d1dad.positions[m] );
}
// Render markers
for ( var m in gmap\_m618f792f2f2719339e35eb57c92d1dad.positions ) {
gmap\_m618f792f2f2719339e35eb57c92d1dad.markers[m] = new google.maps.Marker( {
clickable: true,
map : gmap\_m618f792f2f2719339e35eb57c92d1dad.map,
position : gmap\_m618f792f2f2719339e35eb57c92d1dad.positions[m]
} );
}
// Redraw map to fit our new marker-based bounds
gmap\_m618f792f2f2719339e35eb57c92d1dad.map.setCenter( gmap\_m618f792f2f2719339e35eb57c92d1dad.positions[897] );
});