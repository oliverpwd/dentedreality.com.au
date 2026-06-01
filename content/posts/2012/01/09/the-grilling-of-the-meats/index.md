---
title: The Grilling of the Meats
date: '2012-01-09T14:40:35+00:00'
format: image
service: flickr
tags:
- automattic
- hawaii
- kailua
- meat
- meetup
- sausages
- spam
- steak
- teamsocial
image: http://i1.wp.com/dentedreality.com.au/wp-content/uploads/2012/01/6813427802_bb6822fd99_o.jpg?resize=607%2C452
---

[![The Grilling of the Meats](http://i1.wp.com/dentedreality.com.au/wp-content/uploads/2012/01/6813427802_bb6822fd99_o.jpg?resize=607%2C452)](http://dentedreality.com.au/2012/01/09/the-grilling-of-the-meats/) 
# [The Grilling of the Meats](http://dentedreality.com.au/2012/01/09/the-grilling-of-the-meats/)





* #[automattic](http://dentedreality.com.au/tags/automattic/)
* #[hawaii](http://dentedreality.com.au/tags/hawaii/)
* #[kailua](http://dentedreality.com.au/tags/kailua/)
* #[meat](http://dentedreality.com.au/tags/meat/)
* #[meetup](http://dentedreality.com.au/tags/meetup/)
* #[sausages](http://dentedreality.com.au/tags/sausages/)
* #[spam](http://dentedreality.com.au/tags/spam/)
* #[steak](http://dentedreality.com.au/tags/steak/)
* #[teamsocial](http://dentedreality.com.au/tags/teamsocial/)

Posted on [Flickr](http://www.flickr.com/photos/borkazoid/6813427802/) [2:40 pm, January 9, 2012](http://dentedreality.com.au/2012/01/09/the-grilling-of-the-meats/ "2:40 pm") 
jQuery(document).ready(function(){
var gmap\_m715a3ab4f44abddc3dd8237a99462df0 = {
positions : {
410 : new google.maps.LatLng( '21.410833', '-157.742334' )
},
bounds : new google.maps.LatLngBounds(), // empty for now, we'll dynamically extend it later
map : new google.maps.Map(
document.getElementById( 'gmap\_m715a3ab4f44abddc3dd8237a99462df0' ),
{
mapTypeId: google.maps.MapTypeId.ROADMAP,
center: new google.maps.LatLng( 0, 0 ),
zoom: 16 // Seems to be a good zoom for a single point
}
),
markers : {},
}; // end of gmap
// Extend the bounds of interest based on our positions
for ( var m in gmap\_m715a3ab4f44abddc3dd8237a99462df0.positions ) {
gmap\_m715a3ab4f44abddc3dd8237a99462df0.bounds.extend( gmap\_m715a3ab4f44abddc3dd8237a99462df0.positions[m] );
}
// Render markers
for ( var m in gmap\_m715a3ab4f44abddc3dd8237a99462df0.positions ) {
gmap\_m715a3ab4f44abddc3dd8237a99462df0.markers[m] = new google.maps.Marker( {
clickable: true,
map : gmap\_m715a3ab4f44abddc3dd8237a99462df0.map,
position : gmap\_m715a3ab4f44abddc3dd8237a99462df0.positions[m]
} );
}
// Redraw map to fit our new marker-based bounds
gmap\_m715a3ab4f44abddc3dd8237a99462df0.map.setCenter( gmap\_m715a3ab4f44abddc3dd8237a99462df0.positions[410] );
});