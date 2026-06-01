---
title: The Campsite
date: '2011-11-26T03:49:18+00:00'
format: image
service: flickr
tags:
- angelisland
- california
- camping
- outdoors
- sanfrancisco
image: http://i2.wp.com/dentedreality.com.au/wp-content/uploads/2011/11/6958319043_a16f66ee0c_o.jpg?resize=607%2C452
---

[![The Campsite](http://i2.wp.com/dentedreality.com.au/wp-content/uploads/2011/11/6958319043_a16f66ee0c_o.jpg?resize=607%2C452)](http://dentedreality.com.au/2011/11/26/the-campsite/) 
# [The Campsite](http://dentedreality.com.au/2011/11/26/the-campsite/)





* #[angelisland](http://dentedreality.com.au/tags/angelisland/)
* #[california](http://dentedreality.com.au/tags/california/)
* #[camping](http://dentedreality.com.au/tags/camping/)
* #[outdoors](http://dentedreality.com.au/tags/outdoors/)
* #[sanfrancisco](http://dentedreality.com.au/tags/sanfrancisco/)

Posted on [Flickr](http://www.flickr.com/photos/borkazoid/6958319043/) [3:49 am, November 26, 2011](http://dentedreality.com.au/2011/11/26/the-campsite/ "3:49 am") 
jQuery(document).ready(function(){
var gmap\_ma6d61572891433f678edee7b672abe1c = {
positions : {
528 : new google.maps.LatLng( '37.8325', '-122.313167' )
},
bounds : new google.maps.LatLngBounds(), // empty for now, we'll dynamically extend it later
map : new google.maps.Map(
document.getElementById( 'gmap\_ma6d61572891433f678edee7b672abe1c' ),
{
mapTypeId: google.maps.MapTypeId.ROADMAP,
center: new google.maps.LatLng( 0, 0 ),
zoom: 16 // Seems to be a good zoom for a single point
}
),
markers : {},
}; // end of gmap
// Extend the bounds of interest based on our positions
for ( var m in gmap\_ma6d61572891433f678edee7b672abe1c.positions ) {
gmap\_ma6d61572891433f678edee7b672abe1c.bounds.extend( gmap\_ma6d61572891433f678edee7b672abe1c.positions[m] );
}
// Render markers
for ( var m in gmap\_ma6d61572891433f678edee7b672abe1c.positions ) {
gmap\_ma6d61572891433f678edee7b672abe1c.markers[m] = new google.maps.Marker( {
clickable: true,
map : gmap\_ma6d61572891433f678edee7b672abe1c.map,
position : gmap\_ma6d61572891433f678edee7b672abe1c.positions[m]
} );
}
// Redraw map to fit our new marker-based bounds
gmap\_ma6d61572891433f678edee7b672abe1c.map.setCenter( gmap\_ma6d61572891433f678edee7b672abe1c.positions[528] );
});