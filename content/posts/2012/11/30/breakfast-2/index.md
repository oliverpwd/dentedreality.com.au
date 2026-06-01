---
title: Breakfast
date: '2012-11-30T05:21:23+00:00'
format: image
service: flickr
tags:
- automattic
- breakfast
- eggs
- meetup
- neworleans
- nola
- teamsocial
image: http://i1.wp.com/dentedreality.com.au/wp-content/uploads/2012/11/8460395222_103cccc0bc_o.jpg?resize=607%2C452
---

[![Breakfast](http://i1.wp.com/dentedreality.com.au/wp-content/uploads/2012/11/8460395222_103cccc0bc_o.jpg?resize=607%2C452)](http://dentedreality.com.au/2012/11/30/breakfast-2/) 
# [Breakfast](http://dentedreality.com.au/2012/11/30/breakfast-2/)





* #[automattic](http://dentedreality.com.au/tags/automattic/)
* #[breakfast](http://dentedreality.com.au/tags/breakfast/)
* #[eggs](http://dentedreality.com.au/tags/eggs/)
* #[meetup](http://dentedreality.com.au/tags/meetup/)
* #[neworleans](http://dentedreality.com.au/tags/neworleans/)
* #[nola](http://dentedreality.com.au/tags/nola/)
* #[teamsocial](http://dentedreality.com.au/tags/teamsocial/)

Posted on [Flickr](http://www.flickr.com/photos/borkazoid/8460395222/) [5:21 am, November 30, 2012](http://dentedreality.com.au/2012/11/30/breakfast-2/ "5:21 am") 
jQuery(document).ready(function(){
var gmap\_m2cd137aed227e31f148fd21a423372f6 = {
positions : {
788 : new google.maps.LatLng( '29.932333', '-90.1025' )
},
bounds : new google.maps.LatLngBounds(), // empty for now, we'll dynamically extend it later
map : new google.maps.Map(
document.getElementById( 'gmap\_m2cd137aed227e31f148fd21a423372f6' ),
{
mapTypeId: google.maps.MapTypeId.ROADMAP,
center: new google.maps.LatLng( 0, 0 ),
zoom: 16 // Seems to be a good zoom for a single point
}
),
markers : {},
}; // end of gmap
// Extend the bounds of interest based on our positions
for ( var m in gmap\_m2cd137aed227e31f148fd21a423372f6.positions ) {
gmap\_m2cd137aed227e31f148fd21a423372f6.bounds.extend( gmap\_m2cd137aed227e31f148fd21a423372f6.positions[m] );
}
// Render markers
for ( var m in gmap\_m2cd137aed227e31f148fd21a423372f6.positions ) {
gmap\_m2cd137aed227e31f148fd21a423372f6.markers[m] = new google.maps.Marker( {
clickable: true,
map : gmap\_m2cd137aed227e31f148fd21a423372f6.map,
position : gmap\_m2cd137aed227e31f148fd21a423372f6.positions[m]
} );
}
// Redraw map to fit our new marker-based bounds
gmap\_m2cd137aed227e31f148fd21a423372f6.map.setCenter( gmap\_m2cd137aed227e31f148fd21a423372f6.positions[788] );
});