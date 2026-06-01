---
title: Team Social in Lisbon
date: '2011-09-24T17:26:23+00:00'
format: image
service: flickr
tags:
- automattic
- ceiling
- Lisbon
- meetup
- portugal
- teamsocial
image: http://i2.wp.com/dentedreality.com.au/wp-content/uploads/2011/09/6958221617_fe6ecb55f5_o.jpg?resize=607%2C452
---

[![Team Social in Lisbon](http://i2.wp.com/dentedreality.com.au/wp-content/uploads/2011/09/6958221617_fe6ecb55f5_o.jpg?resize=607%2C452)](http://dentedreality.com.au/2011/09/24/team-social-in-lisbon-21/) 
# [Team Social in Lisbon](http://dentedreality.com.au/2011/09/24/team-social-in-lisbon-21/)





* #[automattic](http://dentedreality.com.au/tags/automattic/)
* #[ceiling](http://dentedreality.com.au/tags/ceiling/)
* #[Lisbon](http://dentedreality.com.au/tags/lisbon/)
* #[meetup](http://dentedreality.com.au/tags/meetup/)
* #[portugal](http://dentedreality.com.au/tags/portugal/)
* #[teamsocial](http://dentedreality.com.au/tags/teamsocial/)

Posted on [Flickr](http://www.flickr.com/photos/borkazoid/6958221617/) [5:26 pm, September 24, 2011](http://dentedreality.com.au/2011/09/24/team-social-in-lisbon-21/ "5:26 pm") 
jQuery(document).ready(function(){
var gmap\_m617c3d59622ea4141ae9169388542cfc = {
positions : {
72 : new google.maps.LatLng( '38.7085', '-9.137167' )
},
bounds : new google.maps.LatLngBounds(), // empty for now, we'll dynamically extend it later
map : new google.maps.Map(
document.getElementById( 'gmap\_m617c3d59622ea4141ae9169388542cfc' ),
{
mapTypeId: google.maps.MapTypeId.ROADMAP,
center: new google.maps.LatLng( 0, 0 ),
zoom: 16 // Seems to be a good zoom for a single point
}
),
markers : {},
}; // end of gmap
// Extend the bounds of interest based on our positions
for ( var m in gmap\_m617c3d59622ea4141ae9169388542cfc.positions ) {
gmap\_m617c3d59622ea4141ae9169388542cfc.bounds.extend( gmap\_m617c3d59622ea4141ae9169388542cfc.positions[m] );
}
// Render markers
for ( var m in gmap\_m617c3d59622ea4141ae9169388542cfc.positions ) {
gmap\_m617c3d59622ea4141ae9169388542cfc.markers[m] = new google.maps.Marker( {
clickable: true,
map : gmap\_m617c3d59622ea4141ae9169388542cfc.map,
position : gmap\_m617c3d59622ea4141ae9169388542cfc.positions[m]
} );
}
// Redraw map to fit our new marker-based bounds
gmap\_m617c3d59622ea4141ae9169388542cfc.map.setCenter( gmap\_m617c3d59622ea4141ae9169388542cfc.positions[72] );
});