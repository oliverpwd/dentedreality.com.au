---
title: Team Social in Lisbon
date: '2011-09-27T17:07:45+00:00'
format: image
service: flickr
tags:
- automattic
- hugo
- jorge
- Lisbon
- meetup
- portugal
- teamsocial
image: http://i1.wp.com/dentedreality.com.au/wp-content/uploads/2011/09/6958227267_d2e653e6af_o.jpg?resize=607%2C452
---

[![Team Social in Lisbon](http://i1.wp.com/dentedreality.com.au/wp-content/uploads/2011/09/6958227267_d2e653e6af_o.jpg?resize=607%2C452)](http://dentedreality.com.au/2011/09/27/team-social-in-lisbon-3/) 
# [Team Social in Lisbon](http://dentedreality.com.au/2011/09/27/team-social-in-lisbon-3/)





* #[automattic](http://dentedreality.com.au/tags/automattic/)
* #[hugo](http://dentedreality.com.au/tags/hugo/)
* #[jorge](http://dentedreality.com.au/tags/jorge/)
* #[Lisbon](http://dentedreality.com.au/tags/lisbon/)
* #[meetup](http://dentedreality.com.au/tags/meetup/)
* #[portugal](http://dentedreality.com.au/tags/portugal/)
* #[teamsocial](http://dentedreality.com.au/tags/teamsocial/)

Posted on [Flickr](http://www.flickr.com/photos/borkazoid/6958227267/) [5:07 pm, September 27, 2011](http://dentedreality.com.au/2011/09/27/team-social-in-lisbon-3/ "5:07 pm") 
jQuery(document).ready(function(){
var gmap\_mb4eb8b6d318bd3b32305239bab83f641 = {
positions : {
653 : new google.maps.LatLng( '38.707', '-9.178667' )
},
bounds : new google.maps.LatLngBounds(), // empty for now, we'll dynamically extend it later
map : new google.maps.Map(
document.getElementById( 'gmap\_mb4eb8b6d318bd3b32305239bab83f641' ),
{
mapTypeId: google.maps.MapTypeId.ROADMAP,
center: new google.maps.LatLng( 0, 0 ),
zoom: 16 // Seems to be a good zoom for a single point
}
),
markers : {},
}; // end of gmap
// Extend the bounds of interest based on our positions
for ( var m in gmap\_mb4eb8b6d318bd3b32305239bab83f641.positions ) {
gmap\_mb4eb8b6d318bd3b32305239bab83f641.bounds.extend( gmap\_mb4eb8b6d318bd3b32305239bab83f641.positions[m] );
}
// Render markers
for ( var m in gmap\_mb4eb8b6d318bd3b32305239bab83f641.positions ) {
gmap\_mb4eb8b6d318bd3b32305239bab83f641.markers[m] = new google.maps.Marker( {
clickable: true,
map : gmap\_mb4eb8b6d318bd3b32305239bab83f641.map,
position : gmap\_mb4eb8b6d318bd3b32305239bab83f641.positions[m]
} );
}
// Redraw map to fit our new marker-based bounds
gmap\_mb4eb8b6d318bd3b32305239bab83f641.map.setCenter( gmap\_mb4eb8b6d318bd3b32305239bab83f641.positions[653] );
});