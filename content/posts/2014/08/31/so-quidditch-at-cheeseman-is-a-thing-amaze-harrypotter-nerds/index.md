---
title: ''
date: '2014-08-31T19:46:55+00:00'
format: image
service: instagram
tags:
- harrypotter
- nerds
- photo
image: http://i0.wp.com/dentedreality.com.au/wp-content/uploads/2014/08/10598513_808325449199492_95769308_n.jpg?resize=640%2C640
---

[![So, Quidditch at Cheeseman is a thing. Amaze. #harrypotter #nerds](http://i0.wp.com/dentedreality.com.au/wp-content/uploads/2014/08/10598513_808325449199492_95769308_n.jpg?resize=640%2C640)](http://dentedreality.com.au/2014/08/31/so-quidditch-at-cheeseman-is-a-thing-amaze-harrypotter-nerds/) 

So, Quidditch at Cheeseman is a thing. Amaze. #harrypotter #nerds





* #[harrypotter](http://dentedreality.com.au/tags/harrypotter/)
* #[nerds](http://dentedreality.com.au/tags/nerds/)
* #[photo](http://dentedreality.com.au/tags/photo/)

Posted on [Instagram](http://instagram.com/p/sYo1JUimCY/) [7:46 pm, August 31, 2014](http://dentedreality.com.au/2014/08/31/so-quidditch-at-cheeseman-is-a-thing-amaze-harrypotter-nerds/ "7:46 pm") 
jQuery(document).ready(function(){
var gmap\_m1a66d5d5cdde106f34806b24fd0b3b30 = {
positions : {
16 : new google.maps.LatLng( '39.732777778', '-104.965833333' )
},
bounds : new google.maps.LatLngBounds(), // empty for now, we'll dynamically extend it later
map : new google.maps.Map(
document.getElementById( 'gmap\_m1a66d5d5cdde106f34806b24fd0b3b30' ),
{
mapTypeId: google.maps.MapTypeId.ROADMAP,
center: new google.maps.LatLng( 0, 0 ),
zoom: 16 // Seems to be a good zoom for a single point
}
),
markers : {},
}; // end of gmap
// Extend the bounds of interest based on our positions
for ( var m in gmap\_m1a66d5d5cdde106f34806b24fd0b3b30.positions ) {
gmap\_m1a66d5d5cdde106f34806b24fd0b3b30.bounds.extend( gmap\_m1a66d5d5cdde106f34806b24fd0b3b30.positions[m] );
}
// Render markers
for ( var m in gmap\_m1a66d5d5cdde106f34806b24fd0b3b30.positions ) {
gmap\_m1a66d5d5cdde106f34806b24fd0b3b30.markers[m] = new google.maps.Marker( {
clickable: true,
map : gmap\_m1a66d5d5cdde106f34806b24fd0b3b30.map,
position : gmap\_m1a66d5d5cdde106f34806b24fd0b3b30.positions[m]
} );
}
// Redraw map to fit our new marker-based bounds
gmap\_m1a66d5d5cdde106f34806b24fd0b3b30.map.setCenter( gmap\_m1a66d5d5cdde106f34806b24fd0b3b30.positions[16] );
});