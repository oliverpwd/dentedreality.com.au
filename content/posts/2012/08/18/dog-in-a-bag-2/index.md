---
title: Dog in a Bag
date: '2012-08-18T10:45:34+00:00'
format: image
service: flickr
tags:
- bag
- bambi
- bicycle
- bike
- erika
image: http://i2.wp.com/dentedreality.com.au/wp-content/uploads/2012/08/8245861144_64a4ac15c1_o.jpg?resize=607%2C813
---

[![Dog in a Bag](http://i2.wp.com/dentedreality.com.au/wp-content/uploads/2012/08/8245861144_64a4ac15c1_o.jpg?resize=607%2C813)](http://dentedreality.com.au/2012/08/18/dog-in-a-bag-2/) 
# [Dog in a Bag](http://dentedreality.com.au/2012/08/18/dog-in-a-bag-2/)





* #[bag](http://dentedreality.com.au/tags/bag/)
* #[bambi](http://dentedreality.com.au/tags/bambi/)
* #[bicycle](http://dentedreality.com.au/tags/bicycle/)
* #[bike](http://dentedreality.com.au/tags/bike/)
* #[erika](http://dentedreality.com.au/tags/erika/)

Posted on [Flickr](http://www.flickr.com/photos/borkazoid/8245861144/) [10:45 am, August 18, 2012](http://dentedreality.com.au/2012/08/18/dog-in-a-bag-2/ "10:45 am") 
jQuery(document).ready(function(){
var gmap\_mcd64a8225394f1c557ddc04202b3ea37 = {
positions : {
690 : new google.maps.LatLng( '40.669333', '-73.984667' )
},
bounds : new google.maps.LatLngBounds(), // empty for now, we'll dynamically extend it later
map : new google.maps.Map(
document.getElementById( 'gmap\_mcd64a8225394f1c557ddc04202b3ea37' ),
{
mapTypeId: google.maps.MapTypeId.ROADMAP,
center: new google.maps.LatLng( 0, 0 ),
zoom: 16 // Seems to be a good zoom for a single point
}
),
markers : {},
}; // end of gmap
// Extend the bounds of interest based on our positions
for ( var m in gmap\_mcd64a8225394f1c557ddc04202b3ea37.positions ) {
gmap\_mcd64a8225394f1c557ddc04202b3ea37.bounds.extend( gmap\_mcd64a8225394f1c557ddc04202b3ea37.positions[m] );
}
// Render markers
for ( var m in gmap\_mcd64a8225394f1c557ddc04202b3ea37.positions ) {
gmap\_mcd64a8225394f1c557ddc04202b3ea37.markers[m] = new google.maps.Marker( {
clickable: true,
map : gmap\_mcd64a8225394f1c557ddc04202b3ea37.map,
position : gmap\_mcd64a8225394f1c557ddc04202b3ea37.positions[m]
} );
}
// Redraw map to fit our new marker-based bounds
gmap\_mcd64a8225394f1c557ddc04202b3ea37.map.setCenter( gmap\_mcd64a8225394f1c557ddc04202b3ea37.positions[690] );
});