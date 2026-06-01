---
title: Skyline
date: '2012-10-17T14:14:21+00:00'
format: image
service: flickr
tags:
- dusk
- newyork
- skyline
image: http://i0.wp.com/dentedreality.com.au/wp-content/uploads/2012/10/8245864100_69e6c52126_o.jpg?resize=607%2C452
---

[![Skyline](http://i0.wp.com/dentedreality.com.au/wp-content/uploads/2012/10/8245864100_69e6c52126_o.jpg?resize=607%2C452)](http://dentedreality.com.au/2012/10/17/skyline/) 
# [Skyline](http://dentedreality.com.au/2012/10/17/skyline/)





* #[dusk](http://dentedreality.com.au/tags/dusk/)
* #[newyork](http://dentedreality.com.au/tags/newyork/)
* #[skyline](http://dentedreality.com.au/tags/skyline/)

Posted on [Flickr](http://www.flickr.com/photos/borkazoid/8245864100/) [2:14 pm, October 17, 2012](http://dentedreality.com.au/2012/10/17/skyline/ "2:14 pm") 
jQuery(document).ready(function(){
var gmap\_m686bcb97549f6373f3b09b794e418f4f = {
positions : {
42 : new google.maps.LatLng( '40.723833', '-74.009' )
},
bounds : new google.maps.LatLngBounds(), // empty for now, we'll dynamically extend it later
map : new google.maps.Map(
document.getElementById( 'gmap\_m686bcb97549f6373f3b09b794e418f4f' ),
{
mapTypeId: google.maps.MapTypeId.ROADMAP,
center: new google.maps.LatLng( 0, 0 ),
zoom: 16 // Seems to be a good zoom for a single point
}
),
markers : {},
}; // end of gmap
// Extend the bounds of interest based on our positions
for ( var m in gmap\_m686bcb97549f6373f3b09b794e418f4f.positions ) {
gmap\_m686bcb97549f6373f3b09b794e418f4f.bounds.extend( gmap\_m686bcb97549f6373f3b09b794e418f4f.positions[m] );
}
// Render markers
for ( var m in gmap\_m686bcb97549f6373f3b09b794e418f4f.positions ) {
gmap\_m686bcb97549f6373f3b09b794e418f4f.markers[m] = new google.maps.Marker( {
clickable: true,
map : gmap\_m686bcb97549f6373f3b09b794e418f4f.map,
position : gmap\_m686bcb97549f6373f3b09b794e418f4f.positions[m]
} );
}
// Redraw map to fit our new marker-based bounds
gmap\_m686bcb97549f6373f3b09b794e418f4f.map.setCenter( gmap\_m686bcb97549f6373f3b09b794e418f4f.positions[42] );
});