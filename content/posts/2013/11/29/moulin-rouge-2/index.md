---
title: Moulin Rouge
date: '2013-11-29T05:36:14+00:00'
format: image
service: flickr
tags:
- france
- moulinrouge
- paris
image: http://i2.wp.com/dentedreality.com.au/wp-content/uploads/2013/11/13900346021_080b3f4a35_o.jpg?resize=607%2C455
---

[![Moulin Rouge](http://i2.wp.com/dentedreality.com.au/wp-content/uploads/2013/11/13900346021_080b3f4a35_o.jpg?resize=607%2C455)](http://dentedreality.com.au/2013/11/29/moulin-rouge-2/) 
# [Moulin Rouge](http://dentedreality.com.au/2013/11/29/moulin-rouge-2/)





* #[france](http://dentedreality.com.au/tags/france/)
* #[moulinrouge](http://dentedreality.com.au/tags/moulinrouge/)
* #[paris](http://dentedreality.com.au/tags/paris/)

Posted on [Flickr](http://www.flickr.com/photos/borkazoid/13900346021/) [5:36 am, November 29, 2013](http://dentedreality.com.au/2013/11/29/moulin-rouge-2/ "5:36 am") 
jQuery(document).ready(function(){
var gmap\_m8c8144084e2b45dddc7ff401cc3ecce7 = {
positions : {
512 : new google.maps.LatLng( '48.8837', '2.332375' )
},
bounds : new google.maps.LatLngBounds(), // empty for now, we'll dynamically extend it later
map : new google.maps.Map(
document.getElementById( 'gmap\_m8c8144084e2b45dddc7ff401cc3ecce7' ),
{
mapTypeId: google.maps.MapTypeId.ROADMAP,
center: new google.maps.LatLng( 0, 0 ),
zoom: 16 // Seems to be a good zoom for a single point
}
),
markers : {},
}; // end of gmap
// Extend the bounds of interest based on our positions
for ( var m in gmap\_m8c8144084e2b45dddc7ff401cc3ecce7.positions ) {
gmap\_m8c8144084e2b45dddc7ff401cc3ecce7.bounds.extend( gmap\_m8c8144084e2b45dddc7ff401cc3ecce7.positions[m] );
}
// Render markers
for ( var m in gmap\_m8c8144084e2b45dddc7ff401cc3ecce7.positions ) {
gmap\_m8c8144084e2b45dddc7ff401cc3ecce7.markers[m] = new google.maps.Marker( {
clickable: true,
map : gmap\_m8c8144084e2b45dddc7ff401cc3ecce7.map,
position : gmap\_m8c8144084e2b45dddc7ff401cc3ecce7.positions[m]
} );
}
// Redraw map to fit our new marker-based bounds
gmap\_m8c8144084e2b45dddc7ff401cc3ecce7.map.setCenter( gmap\_m8c8144084e2b45dddc7ff401cc3ecce7.positions[512] );
});