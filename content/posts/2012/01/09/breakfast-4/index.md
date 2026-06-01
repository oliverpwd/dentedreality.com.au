---
title: Breakfast
date: '2012-01-09T05:28:54+00:00'
format: image
service: flickr
tags:
- automattic
- eggs
- hawaii
- kailua
- meetup
- teamsocial
image: http://i1.wp.com/dentedreality.com.au/wp-content/uploads/2012/01/6959540089_5877f03ee1_o.jpg?resize=607%2C452
---

[![Breakfast](http://i1.wp.com/dentedreality.com.au/wp-content/uploads/2012/01/6959540089_5877f03ee1_o.jpg?resize=607%2C452)](http://dentedreality.com.au/2012/01/09/breakfast-4/) 
# [Breakfast](http://dentedreality.com.au/2012/01/09/breakfast-4/)





* #[automattic](http://dentedreality.com.au/tags/automattic/)
* #[eggs](http://dentedreality.com.au/tags/eggs/)
* #[hawaii](http://dentedreality.com.au/tags/hawaii/)
* #[kailua](http://dentedreality.com.au/tags/kailua/)
* #[meetup](http://dentedreality.com.au/tags/meetup/)
* #[teamsocial](http://dentedreality.com.au/tags/teamsocial/)

Posted on [Flickr](http://www.flickr.com/photos/borkazoid/6959540089/) [5:28 am, January 9, 2012](http://dentedreality.com.au/2012/01/09/breakfast-4/ "5:28 am") 
jQuery(document).ready(function(){
var gmap\_m66c762b4c14f8ad33566871ef110a171 = {
positions : {
459 : new google.maps.LatLng( '21.410999', '-157.7425' )
},
bounds : new google.maps.LatLngBounds(), // empty for now, we'll dynamically extend it later
map : new google.maps.Map(
document.getElementById( 'gmap\_m66c762b4c14f8ad33566871ef110a171' ),
{
mapTypeId: google.maps.MapTypeId.ROADMAP,
center: new google.maps.LatLng( 0, 0 ),
zoom: 16 // Seems to be a good zoom for a single point
}
),
markers : {},
}; // end of gmap
// Extend the bounds of interest based on our positions
for ( var m in gmap\_m66c762b4c14f8ad33566871ef110a171.positions ) {
gmap\_m66c762b4c14f8ad33566871ef110a171.bounds.extend( gmap\_m66c762b4c14f8ad33566871ef110a171.positions[m] );
}
// Render markers
for ( var m in gmap\_m66c762b4c14f8ad33566871ef110a171.positions ) {
gmap\_m66c762b4c14f8ad33566871ef110a171.markers[m] = new google.maps.Marker( {
clickable: true,
map : gmap\_m66c762b4c14f8ad33566871ef110a171.map,
position : gmap\_m66c762b4c14f8ad33566871ef110a171.positions[m]
} );
}
// Redraw map to fit our new marker-based bounds
gmap\_m66c762b4c14f8ad33566871ef110a171.map.setCenter( gmap\_m66c762b4c14f8ad33566871ef110a171.positions[459] );
});