---
title: Cock Head
date: '2012-12-27T10:37:40+00:00'
format: image
service: flickr
tags:
- art
- cock
- rooster
- statue
image: http://i2.wp.com/dentedreality.com.au/wp-content/uploads/2012/12/8460354736_05e25eddda_o.jpg?resize=607%2C813
---

[![Cock Head](http://i2.wp.com/dentedreality.com.au/wp-content/uploads/2012/12/8460354736_05e25eddda_o.jpg?resize=607%2C813)](http://dentedreality.com.au/2012/12/27/cock-head/) 
# [Cock Head](http://dentedreality.com.au/2012/12/27/cock-head/)





* #[art](http://dentedreality.com.au/tags/art/)
* #[cock](http://dentedreality.com.au/tags/cock/)
* #[rooster](http://dentedreality.com.au/tags/rooster/)
* #[statue](http://dentedreality.com.au/tags/statue/)

Posted on [Flickr](http://www.flickr.com/photos/borkazoid/8460354736/) [10:37 am, December 27, 2012](http://dentedreality.com.au/2012/12/27/cock-head/ "10:37 am") 
jQuery(document).ready(function(){
var gmap\_m84c7c08852a9257b46cea45e386822e6 = {
positions : {
925 : new google.maps.LatLng( '38.888', '-77.021667' )
},
bounds : new google.maps.LatLngBounds(), // empty for now, we'll dynamically extend it later
map : new google.maps.Map(
document.getElementById( 'gmap\_m84c7c08852a9257b46cea45e386822e6' ),
{
mapTypeId: google.maps.MapTypeId.ROADMAP,
center: new google.maps.LatLng( 0, 0 ),
zoom: 16 // Seems to be a good zoom for a single point
}
),
markers : {},
}; // end of gmap
// Extend the bounds of interest based on our positions
for ( var m in gmap\_m84c7c08852a9257b46cea45e386822e6.positions ) {
gmap\_m84c7c08852a9257b46cea45e386822e6.bounds.extend( gmap\_m84c7c08852a9257b46cea45e386822e6.positions[m] );
}
// Render markers
for ( var m in gmap\_m84c7c08852a9257b46cea45e386822e6.positions ) {
gmap\_m84c7c08852a9257b46cea45e386822e6.markers[m] = new google.maps.Marker( {
clickable: true,
map : gmap\_m84c7c08852a9257b46cea45e386822e6.map,
position : gmap\_m84c7c08852a9257b46cea45e386822e6.positions[m]
} );
}
// Redraw map to fit our new marker-based bounds
gmap\_m84c7c08852a9257b46cea45e386822e6.map.setCenter( gmap\_m84c7c08852a9257b46cea45e386822e6.positions[925] );
});