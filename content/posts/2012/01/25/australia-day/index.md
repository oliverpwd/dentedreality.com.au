---
title: Australia Day
date: '2012-01-25T17:18:44+00:00'
format: image
service: flickr
tags:
- australiaday
- australiaday2012
image: http://i2.wp.com/dentedreality.com.au/wp-content/uploads/2012/01/6813456430_5c4beae79c_o.jpg?resize=607%2C813
---

[![Australia Day](http://i2.wp.com/dentedreality.com.au/wp-content/uploads/2012/01/6813456430_5c4beae79c_o.jpg?resize=607%2C813)](http://dentedreality.com.au/2012/01/25/australia-day/) 
# [Australia Day](http://dentedreality.com.au/2012/01/25/australia-day/)

BOOM





* #[australiaday](http://dentedreality.com.au/tags/australiaday/)
* #[australiaday2012](http://dentedreality.com.au/tags/australiaday2012/)

Posted on [Flickr](http://www.flickr.com/photos/borkazoid/6813456430/) [5:18 pm, January 25, 2012](http://dentedreality.com.au/2012/01/25/australia-day/ "5:18 pm") 
jQuery(document).ready(function(){
var gmap\_m8c43da30ba430aea573c6bada9d6b3cc = {
positions : {
403 : new google.maps.LatLng( '37.736333', '-122.433334' )
},
bounds : new google.maps.LatLngBounds(), // empty for now, we'll dynamically extend it later
map : new google.maps.Map(
document.getElementById( 'gmap\_m8c43da30ba430aea573c6bada9d6b3cc' ),
{
mapTypeId: google.maps.MapTypeId.ROADMAP,
center: new google.maps.LatLng( 0, 0 ),
zoom: 16 // Seems to be a good zoom for a single point
}
),
markers : {},
}; // end of gmap
// Extend the bounds of interest based on our positions
for ( var m in gmap\_m8c43da30ba430aea573c6bada9d6b3cc.positions ) {
gmap\_m8c43da30ba430aea573c6bada9d6b3cc.bounds.extend( gmap\_m8c43da30ba430aea573c6bada9d6b3cc.positions[m] );
}
// Render markers
for ( var m in gmap\_m8c43da30ba430aea573c6bada9d6b3cc.positions ) {
gmap\_m8c43da30ba430aea573c6bada9d6b3cc.markers[m] = new google.maps.Marker( {
clickable: true,
map : gmap\_m8c43da30ba430aea573c6bada9d6b3cc.map,
position : gmap\_m8c43da30ba430aea573c6bada9d6b3cc.positions[m]
} );
}
// Redraw map to fit our new marker-based bounds
gmap\_m8c43da30ba430aea573c6bada9d6b3cc.map.setCenter( gmap\_m8c43da30ba430aea573c6bada9d6b3cc.positions[403] );
});