---
title: Elephant Ear!
date: '2011-05-21T10:03:59+00:00'
format: image
service: flickr
tags:
- meetup
- PDX
- Portland
- teamsocial
image: http://i1.wp.com/dentedreality.com.au/wp-content/uploads/2011/05/5802180649_5146b42f9c_o.jpg?resize=607%2C813
---

[![Elephant Ear!](http://i1.wp.com/dentedreality.com.au/wp-content/uploads/2011/05/5802180649_5146b42f9c_o.jpg?resize=607%2C813)](http://dentedreality.com.au/2011/05/21/elephant-ear/) 
# [Elephant Ear!](http://dentedreality.com.au/2011/05/21/elephant-ear/)

Even better with obscene amounts of PB&J on it ![:)](http://i0.wp.com/dentedreality.com.au/wp-includes/images/smilies/icon_smile.gif?w=607)





* #[meetup](http://dentedreality.com.au/tags/meetup/)
* #[PDX](http://dentedreality.com.au/tags/pdx/)
* #[Portland](http://dentedreality.com.au/tags/portland/)
* #[teamsocial](http://dentedreality.com.au/tags/teamsocial/)

Posted on [Flickr](http://www.flickr.com/photos/borkazoid/5802180649/) [10:03 am, May 21, 2011](http://dentedreality.com.au/2011/05/21/elephant-ear/ "10:03 am") 
jQuery(document).ready(function(){
var gmap\_m540d86f55fe2c3f17324eb888155cf0f = {
positions : {
862 : new google.maps.LatLng( '45.522666', '-122.670834' )
},
bounds : new google.maps.LatLngBounds(), // empty for now, we'll dynamically extend it later
map : new google.maps.Map(
document.getElementById( 'gmap\_m540d86f55fe2c3f17324eb888155cf0f' ),
{
mapTypeId: google.maps.MapTypeId.ROADMAP,
center: new google.maps.LatLng( 0, 0 ),
zoom: 16 // Seems to be a good zoom for a single point
}
),
markers : {},
}; // end of gmap
// Extend the bounds of interest based on our positions
for ( var m in gmap\_m540d86f55fe2c3f17324eb888155cf0f.positions ) {
gmap\_m540d86f55fe2c3f17324eb888155cf0f.bounds.extend( gmap\_m540d86f55fe2c3f17324eb888155cf0f.positions[m] );
}
// Render markers
for ( var m in gmap\_m540d86f55fe2c3f17324eb888155cf0f.positions ) {
gmap\_m540d86f55fe2c3f17324eb888155cf0f.markers[m] = new google.maps.Marker( {
clickable: true,
map : gmap\_m540d86f55fe2c3f17324eb888155cf0f.map,
position : gmap\_m540d86f55fe2c3f17324eb888155cf0f.positions[m]
} );
}
// Redraw map to fit our new marker-based bounds
gmap\_m540d86f55fe2c3f17324eb888155cf0f.map.setCenter( gmap\_m540d86f55fe2c3f17324eb888155cf0f.positions[862] );
});