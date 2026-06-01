---
title: Frontsight Handgun Training
date: '2013-01-21T07:20:21+00:00'
format: image
service: flickr
tags:
- frontsight
- gun
- gunrange
- handgun
- pistol
- shooting
- training
image: http://i2.wp.com/dentedreality.com.au/wp-content/uploads/2013/01/8460187514_fb3be6a092_o.jpg?resize=607%2C452
---

[![Frontsight Handgun Training](http://i2.wp.com/dentedreality.com.au/wp-content/uploads/2013/01/8460187514_fb3be6a092_o.jpg?resize=607%2C452)](http://dentedreality.com.au/2013/01/21/frontsight-handgun-training-3/) 
# [Frontsight Handgun Training](http://dentedreality.com.au/2013/01/21/frontsight-handgun-training-3/)





* #[frontsight](http://dentedreality.com.au/tags/frontsight/)
* #[gun](http://dentedreality.com.au/tags/gun/)
* #[gunrange](http://dentedreality.com.au/tags/gunrange/)
* #[handgun](http://dentedreality.com.au/tags/handgun/)
* #[pistol](http://dentedreality.com.au/tags/pistol/)
* #[shooting](http://dentedreality.com.au/tags/shooting/)
* #[training](http://dentedreality.com.au/tags/training/)

Posted on [Flickr](http://www.flickr.com/photos/borkazoid/8460187514/) [7:20 am, January 21, 2013](http://dentedreality.com.au/2013/01/21/frontsight-handgun-training-3/ "7:20 am") 
jQuery(document).ready(function(){
var gmap\_m63f2259db1ad333e3b82aab261182686 = {
positions : {
149 : new google.maps.LatLng( '36.0355', '-115.890167' )
},
bounds : new google.maps.LatLngBounds(), // empty for now, we'll dynamically extend it later
map : new google.maps.Map(
document.getElementById( 'gmap\_m63f2259db1ad333e3b82aab261182686' ),
{
mapTypeId: google.maps.MapTypeId.ROADMAP,
center: new google.maps.LatLng( 0, 0 ),
zoom: 16 // Seems to be a good zoom for a single point
}
),
markers : {},
}; // end of gmap
// Extend the bounds of interest based on our positions
for ( var m in gmap\_m63f2259db1ad333e3b82aab261182686.positions ) {
gmap\_m63f2259db1ad333e3b82aab261182686.bounds.extend( gmap\_m63f2259db1ad333e3b82aab261182686.positions[m] );
}
// Render markers
for ( var m in gmap\_m63f2259db1ad333e3b82aab261182686.positions ) {
gmap\_m63f2259db1ad333e3b82aab261182686.markers[m] = new google.maps.Marker( {
clickable: true,
map : gmap\_m63f2259db1ad333e3b82aab261182686.map,
position : gmap\_m63f2259db1ad333e3b82aab261182686.positions[m]
} );
}
// Redraw map to fit our new marker-based bounds
gmap\_m63f2259db1ad333e3b82aab261182686.map.setCenter( gmap\_m63f2259db1ad333e3b82aab261182686.positions[149] );
});