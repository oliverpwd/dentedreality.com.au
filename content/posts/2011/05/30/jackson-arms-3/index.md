---
title: Jackson Arms
date: '2011-05-30T09:01:01+00:00'
format: image
service: flickr
tags:
- jacksonarms
- memorialday
- rick
- shooting
image: http://i2.wp.com/dentedreality.com.au/wp-content/uploads/2011/05/5803435486_d333a55a6e_o.jpg?resize=607%2C813
---

[![Jackson Arms](http://i2.wp.com/dentedreality.com.au/wp-content/uploads/2011/05/5803435486_d333a55a6e_o.jpg?resize=607%2C813)](http://dentedreality.com.au/2011/05/30/jackson-arms-3/) 
# [Jackson Arms](http://dentedreality.com.au/2011/05/30/jackson-arms-3/)

Memorial Day at the range





* #[jacksonarms](http://dentedreality.com.au/tags/jacksonarms/)
* #[memorialday](http://dentedreality.com.au/tags/memorialday/)
* #[rick](http://dentedreality.com.au/tags/rick/)
* #[shooting](http://dentedreality.com.au/tags/shooting/)

Posted on [Flickr](http://www.flickr.com/photos/borkazoid/5803435486/) [9:01 am, May 30, 2011](http://dentedreality.com.au/2011/05/30/jackson-arms-3/ "9:01 am") 
jQuery(document).ready(function(){
var gmap\_m8da93730808d7526048e7bf9e9e73885 = {
positions : {
424 : new google.maps.LatLng( '37.645666', '-122.401834' )
},
bounds : new google.maps.LatLngBounds(), // empty for now, we'll dynamically extend it later
map : new google.maps.Map(
document.getElementById( 'gmap\_m8da93730808d7526048e7bf9e9e73885' ),
{
mapTypeId: google.maps.MapTypeId.ROADMAP,
center: new google.maps.LatLng( 0, 0 ),
zoom: 16 // Seems to be a good zoom for a single point
}
),
markers : {},
}; // end of gmap
// Extend the bounds of interest based on our positions
for ( var m in gmap\_m8da93730808d7526048e7bf9e9e73885.positions ) {
gmap\_m8da93730808d7526048e7bf9e9e73885.bounds.extend( gmap\_m8da93730808d7526048e7bf9e9e73885.positions[m] );
}
// Render markers
for ( var m in gmap\_m8da93730808d7526048e7bf9e9e73885.positions ) {
gmap\_m8da93730808d7526048e7bf9e9e73885.markers[m] = new google.maps.Marker( {
clickable: true,
map : gmap\_m8da93730808d7526048e7bf9e9e73885.map,
position : gmap\_m8da93730808d7526048e7bf9e9e73885.positions[m]
} );
}
// Redraw map to fit our new marker-based bounds
gmap\_m8da93730808d7526048e7bf9e9e73885.map.setCenter( gmap\_m8da93730808d7526048e7bf9e9e73885.positions[424] );
});