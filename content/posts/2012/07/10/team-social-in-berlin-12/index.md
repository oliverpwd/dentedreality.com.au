---
title: Team Social in Berlin
date: '2012-07-10T05:51:56+00:00'
format: image
service: flickr
tags:
- automattic
- Berlin
- germany
- teamsocial
image: http://i0.wp.com/dentedreality.com.au/wp-content/uploads/2012/07/7918243880_a31dacf524_o.jpg?resize=607%2C455
---

[![Team Social in Berlin](http://i0.wp.com/dentedreality.com.au/wp-content/uploads/2012/07/7918243880_a31dacf524_o.jpg?resize=607%2C455)](http://dentedreality.com.au/2012/07/10/team-social-in-berlin-12/) 
# [Team Social in Berlin](http://dentedreality.com.au/2012/07/10/team-social-in-berlin-12/)





* #[automattic](http://dentedreality.com.au/tags/automattic/)
* #[Berlin](http://dentedreality.com.au/tags/berlin/)
* #[germany](http://dentedreality.com.au/tags/germany/)
* #[teamsocial](http://dentedreality.com.au/tags/teamsocial/)

Posted on [Flickr](http://www.flickr.com/photos/borkazoid/7918243880/) [5:51 am, July 10, 2012](http://dentedreality.com.au/2012/07/10/team-social-in-berlin-12/ "5:51 am") 
jQuery(document).ready(function(){
var gmap\_mf8a36804e52f9899452c0ce8bb48632e = {
positions : {
438 : new google.maps.LatLng( '52.517913', '13.374933' )
},
bounds : new google.maps.LatLngBounds(), // empty for now, we'll dynamically extend it later
map : new google.maps.Map(
document.getElementById( 'gmap\_mf8a36804e52f9899452c0ce8bb48632e' ),
{
mapTypeId: google.maps.MapTypeId.ROADMAP,
center: new google.maps.LatLng( 0, 0 ),
zoom: 16 // Seems to be a good zoom for a single point
}
),
markers : {},
}; // end of gmap
// Extend the bounds of interest based on our positions
for ( var m in gmap\_mf8a36804e52f9899452c0ce8bb48632e.positions ) {
gmap\_mf8a36804e52f9899452c0ce8bb48632e.bounds.extend( gmap\_mf8a36804e52f9899452c0ce8bb48632e.positions[m] );
}
// Render markers
for ( var m in gmap\_mf8a36804e52f9899452c0ce8bb48632e.positions ) {
gmap\_mf8a36804e52f9899452c0ce8bb48632e.markers[m] = new google.maps.Marker( {
clickable: true,
map : gmap\_mf8a36804e52f9899452c0ce8bb48632e.map,
position : gmap\_mf8a36804e52f9899452c0ce8bb48632e.positions[m]
} );
}
// Redraw map to fit our new marker-based bounds
gmap\_mf8a36804e52f9899452c0ce8bb48632e.map.setCenter( gmap\_mf8a36804e52f9899452c0ce8bb48632e.positions[438] );
});