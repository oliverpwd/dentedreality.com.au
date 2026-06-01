---
title: '@wpsfo WordPress Meetup'
date: '2011-01-31T14:27:45+00:00'
format: image
service: flickr
tags:
- meetup
- sanfrancisco
- wordpress
- wordpressmeetup
- wpsfo
image: http://i1.wp.com/dentedreality.com.au/wp-content/uploads/2011/01/5802052017_fb1f55a6db_o.jpg?resize=607%2C452
---

[![@wpsfo WordPress Meetup](http://i1.wp.com/dentedreality.com.au/wp-content/uploads/2011/01/5802052017_fb1f55a6db_o.jpg?resize=607%2C452)](http://dentedreality.com.au/2011/01/31/wpsfo-wordpress-meetup-2/) 
# [@wpsfo WordPress Meetup](http://dentedreality.com.au/2011/01/31/wpsfo-wordpress-meetup-2/)





* #[meetup](http://dentedreality.com.au/tags/meetup/)
* #[sanfrancisco](http://dentedreality.com.au/tags/sanfrancisco/)
* #[wordpress](http://dentedreality.com.au/tags/wordpress/)
* #[wordpressmeetup](http://dentedreality.com.au/tags/wordpressmeetup/)
* #[wpsfo](http://dentedreality.com.au/tags/wpsfo/)

Posted on [Flickr](http://www.flickr.com/photos/borkazoid/5802052017/) [2:27 pm, January 31, 2011](http://dentedreality.com.au/2011/01/31/wpsfo-wordpress-meetup-2/ "2:27 pm") 
jQuery(document).ready(function(){
var gmap\_mb1f35aff3b68f9f83e1ea4b6cdf1337a = {
positions : {
369 : new google.maps.LatLng( '37.782666', '-122.388' )
},
bounds : new google.maps.LatLngBounds(), // empty for now, we'll dynamically extend it later
map : new google.maps.Map(
document.getElementById( 'gmap\_mb1f35aff3b68f9f83e1ea4b6cdf1337a' ),
{
mapTypeId: google.maps.MapTypeId.ROADMAP,
center: new google.maps.LatLng( 0, 0 ),
zoom: 16 // Seems to be a good zoom for a single point
}
),
markers : {},
}; // end of gmap
// Extend the bounds of interest based on our positions
for ( var m in gmap\_mb1f35aff3b68f9f83e1ea4b6cdf1337a.positions ) {
gmap\_mb1f35aff3b68f9f83e1ea4b6cdf1337a.bounds.extend( gmap\_mb1f35aff3b68f9f83e1ea4b6cdf1337a.positions[m] );
}
// Render markers
for ( var m in gmap\_mb1f35aff3b68f9f83e1ea4b6cdf1337a.positions ) {
gmap\_mb1f35aff3b68f9f83e1ea4b6cdf1337a.markers[m] = new google.maps.Marker( {
clickable: true,
map : gmap\_mb1f35aff3b68f9f83e1ea4b6cdf1337a.map,
position : gmap\_mb1f35aff3b68f9f83e1ea4b6cdf1337a.positions[m]
} );
}
// Redraw map to fit our new marker-based bounds
gmap\_mb1f35aff3b68f9f83e1ea4b6cdf1337a.map.setCenter( gmap\_mb1f35aff3b68f9f83e1ea4b6cdf1337a.positions[369] );
});