---
title: My Business Card
date: '2010-08-10T12:22:08+00:00'
format: image
service: flickr
tags:
- beau
- beaulebens
- businesscard
image: http://i1.wp.com/dentedreality.com.au/wp-content/uploads/2010/08/4880203859_5b76dbcd88_o.jpg?resize=607%2C455
---

[![My Business Card](http://i1.wp.com/dentedreality.com.au/wp-content/uploads/2010/08/4880203859_5b76dbcd88_o.jpg?resize=607%2C455)](http://dentedreality.com.au/2010/08/10/my-business-card/) 
# [My Business Card](http://dentedreality.com.au/2010/08/10/my-business-card/)

I squeezed as much as I could in there ![;)](http://i2.wp.com/dentedreality.com.au/wp-includes/images/smilies/icon_wink.gif?w=607)





* #[beau](http://dentedreality.com.au/tags/beau/)
* #[beaulebens](http://dentedreality.com.au/tags/beaulebens/)
* #[businesscard](http://dentedreality.com.au/tags/businesscard/)

Posted on [Flickr](http://www.flickr.com/photos/borkazoid/4880203859/) [12:22 pm, August 10, 2010](http://dentedreality.com.au/2010/08/10/my-business-card/ "12:22 pm") 
jQuery(document).ready(function(){
var gmap\_maef59bf5c706ee283df9900749a0ec46 = {
positions : {
688 : new google.maps.LatLng( '37.7825', '-122.387834' )
},
bounds : new google.maps.LatLngBounds(), // empty for now, we'll dynamically extend it later
map : new google.maps.Map(
document.getElementById( 'gmap\_maef59bf5c706ee283df9900749a0ec46' ),
{
mapTypeId: google.maps.MapTypeId.ROADMAP,
center: new google.maps.LatLng( 0, 0 ),
zoom: 16 // Seems to be a good zoom for a single point
}
),
markers : {},
}; // end of gmap
// Extend the bounds of interest based on our positions
for ( var m in gmap\_maef59bf5c706ee283df9900749a0ec46.positions ) {
gmap\_maef59bf5c706ee283df9900749a0ec46.bounds.extend( gmap\_maef59bf5c706ee283df9900749a0ec46.positions[m] );
}
// Render markers
for ( var m in gmap\_maef59bf5c706ee283df9900749a0ec46.positions ) {
gmap\_maef59bf5c706ee283df9900749a0ec46.markers[m] = new google.maps.Marker( {
clickable: true,
map : gmap\_maef59bf5c706ee283df9900749a0ec46.map,
position : gmap\_maef59bf5c706ee283df9900749a0ec46.positions[m]
} );
}
// Redraw map to fit our new marker-based bounds
gmap\_maef59bf5c706ee283df9900749a0ec46.map.setCenter( gmap\_maef59bf5c706ee283df9900749a0ec46.positions[688] );
});