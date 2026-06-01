---
title: What happened here?
date: '2011-05-20T14:59:59+00:00'
format: image
service: flickr
tags:
- meetup
- PDX
- pooltable
- Portland
- teamsocial
image: http://i2.wp.com/dentedreality.com.au/wp-content/uploads/2011/05/5802735436_66fc51d990_o.jpg?resize=607%2C813
---

[![What happened here?](http://i2.wp.com/dentedreality.com.au/wp-content/uploads/2011/05/5802735436_66fc51d990_o.jpg?resize=607%2C813)](http://dentedreality.com.au/2011/05/20/what-happened-here-2/) 
# [What happened here?](http://dentedreality.com.au/2011/05/20/what-happened-here-2/)





* #[meetup](http://dentedreality.com.au/tags/meetup/)
* #[PDX](http://dentedreality.com.au/tags/pdx/)
* #[pooltable](http://dentedreality.com.au/tags/pooltable/)
* #[Portland](http://dentedreality.com.au/tags/portland/)
* #[teamsocial](http://dentedreality.com.au/tags/teamsocial/)

Posted on [Flickr](http://www.flickr.com/photos/borkazoid/5802735436/) [2:59 pm, May 20, 2011](http://dentedreality.com.au/2011/05/20/what-happened-here-2/ "2:59 pm") 
jQuery(document).ready(function(){
var gmap\_m30d5fcd39c85b90a5de0fe1571cb039b = {
positions : {
411 : new google.maps.LatLng( '45.521', '-122.673334' )
},
bounds : new google.maps.LatLngBounds(), // empty for now, we'll dynamically extend it later
map : new google.maps.Map(
document.getElementById( 'gmap\_m30d5fcd39c85b90a5de0fe1571cb039b' ),
{
mapTypeId: google.maps.MapTypeId.ROADMAP,
center: new google.maps.LatLng( 0, 0 ),
zoom: 16 // Seems to be a good zoom for a single point
}
),
markers : {},
}; // end of gmap
// Extend the bounds of interest based on our positions
for ( var m in gmap\_m30d5fcd39c85b90a5de0fe1571cb039b.positions ) {
gmap\_m30d5fcd39c85b90a5de0fe1571cb039b.bounds.extend( gmap\_m30d5fcd39c85b90a5de0fe1571cb039b.positions[m] );
}
// Render markers
for ( var m in gmap\_m30d5fcd39c85b90a5de0fe1571cb039b.positions ) {
gmap\_m30d5fcd39c85b90a5de0fe1571cb039b.markers[m] = new google.maps.Marker( {
clickable: true,
map : gmap\_m30d5fcd39c85b90a5de0fe1571cb039b.map,
position : gmap\_m30d5fcd39c85b90a5de0fe1571cb039b.positions[m]
} );
}
// Redraw map to fit our new marker-based bounds
gmap\_m30d5fcd39c85b90a5de0fe1571cb039b.map.setCenter( gmap\_m30d5fcd39c85b90a5de0fe1571cb039b.positions[411] );
});