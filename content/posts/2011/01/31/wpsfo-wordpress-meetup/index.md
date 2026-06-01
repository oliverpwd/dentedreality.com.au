---
title: '@wpsfo WordPress Meetup'
date: '2011-01-31T14:37:49+00:00'
format: image
service: flickr
tags:
- meetup
- sanfrancisco
- wordpress
- wordpressmeetup
- wpsfo
image: http://i1.wp.com/dentedreality.com.au/wp-content/uploads/2011/01/5802609646_8fe067d1a6_o.jpg?resize=607%2C452
---

[![@wpsfo WordPress Meetup](http://i1.wp.com/dentedreality.com.au/wp-content/uploads/2011/01/5802609646_8fe067d1a6_o.jpg?resize=607%2C452)](http://dentedreality.com.au/2011/01/31/wpsfo-wordpress-meetup/) 
# [@wpsfo WordPress Meetup](http://dentedreality.com.au/2011/01/31/wpsfo-wordpress-meetup/)





* #[meetup](http://dentedreality.com.au/tags/meetup/)
* #[sanfrancisco](http://dentedreality.com.au/tags/sanfrancisco/)
* #[wordpress](http://dentedreality.com.au/tags/wordpress/)
* #[wordpressmeetup](http://dentedreality.com.au/tags/wordpressmeetup/)
* #[wpsfo](http://dentedreality.com.au/tags/wpsfo/)

Posted on [Flickr](http://www.flickr.com/photos/borkazoid/5802609646/) [2:37 pm, January 31, 2011](http://dentedreality.com.au/2011/01/31/wpsfo-wordpress-meetup/ "2:37 pm") 
jQuery(document).ready(function(){
var gmap\_me3aae78a78aca748d88a12686ce2e65f = {
positions : {
933 : new google.maps.LatLng( '37.7825', '-122.388' )
},
bounds : new google.maps.LatLngBounds(), // empty for now, we'll dynamically extend it later
map : new google.maps.Map(
document.getElementById( 'gmap\_me3aae78a78aca748d88a12686ce2e65f' ),
{
mapTypeId: google.maps.MapTypeId.ROADMAP,
center: new google.maps.LatLng( 0, 0 ),
zoom: 16 // Seems to be a good zoom for a single point
}
),
markers : {},
}; // end of gmap
// Extend the bounds of interest based on our positions
for ( var m in gmap\_me3aae78a78aca748d88a12686ce2e65f.positions ) {
gmap\_me3aae78a78aca748d88a12686ce2e65f.bounds.extend( gmap\_me3aae78a78aca748d88a12686ce2e65f.positions[m] );
}
// Render markers
for ( var m in gmap\_me3aae78a78aca748d88a12686ce2e65f.positions ) {
gmap\_me3aae78a78aca748d88a12686ce2e65f.markers[m] = new google.maps.Marker( {
clickable: true,
map : gmap\_me3aae78a78aca748d88a12686ce2e65f.map,
position : gmap\_me3aae78a78aca748d88a12686ce2e65f.positions[m]
} );
}
// Redraw map to fit our new marker-based bounds
gmap\_me3aae78a78aca748d88a12686ce2e65f.map.setCenter( gmap\_me3aae78a78aca748d88a12686ce2e65f.positions[933] );
});