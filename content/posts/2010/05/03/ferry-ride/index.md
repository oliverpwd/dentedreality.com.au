---
title: Ferry Ride
date: '2010-05-03T14:29:38+00:00'
format: image
service: flickr
tags:
- alameda
- boat
- ferry
- sanfrancisco
- treasureisland
image: http://i0.wp.com/dentedreality.com.au/wp-content/uploads/2010/05/4746454905_aae3b9368f_o.jpg?resize=607%2C455
---

[![Ferry Ride](http://i0.wp.com/dentedreality.com.au/wp-content/uploads/2010/05/4746454905_aae3b9368f_o.jpg?resize=607%2C455)](http://dentedreality.com.au/2010/05/03/ferry-ride/) 
# [Ferry Ride](http://dentedreality.com.au/2010/05/03/ferry-ride/)





* #[alameda](http://dentedreality.com.au/tags/alameda/)
* #[boat](http://dentedreality.com.au/tags/boat/)
* #[ferry](http://dentedreality.com.au/tags/ferry/)
* #[sanfrancisco](http://dentedreality.com.au/tags/sanfrancisco/)
* #[treasureisland](http://dentedreality.com.au/tags/treasureisland/)

Posted on [Flickr](http://www.flickr.com/photos/borkazoid/4746454905/) [2:29 pm, May 3, 2010](http://dentedreality.com.au/2010/05/03/ferry-ride/ "2:29 pm") 
jQuery(document).ready(function(){
var gmap\_m05301ec9a9af799dfb50daefacbc188e = {
positions : {
586 : new google.maps.LatLng( '37.797166', '-122.373667' )
},
bounds : new google.maps.LatLngBounds(), // empty for now, we'll dynamically extend it later
map : new google.maps.Map(
document.getElementById( 'gmap\_m05301ec9a9af799dfb50daefacbc188e' ),
{
mapTypeId: google.maps.MapTypeId.ROADMAP,
center: new google.maps.LatLng( 0, 0 ),
zoom: 16 // Seems to be a good zoom for a single point
}
),
markers : {},
}; // end of gmap
// Extend the bounds of interest based on our positions
for ( var m in gmap\_m05301ec9a9af799dfb50daefacbc188e.positions ) {
gmap\_m05301ec9a9af799dfb50daefacbc188e.bounds.extend( gmap\_m05301ec9a9af799dfb50daefacbc188e.positions[m] );
}
// Render markers
for ( var m in gmap\_m05301ec9a9af799dfb50daefacbc188e.positions ) {
gmap\_m05301ec9a9af799dfb50daefacbc188e.markers[m] = new google.maps.Marker( {
clickable: true,
map : gmap\_m05301ec9a9af799dfb50daefacbc188e.map,
position : gmap\_m05301ec9a9af799dfb50daefacbc188e.positions[m]
} );
}
// Redraw map to fit our new marker-based bounds
gmap\_m05301ec9a9af799dfb50daefacbc188e.map.setCenter( gmap\_m05301ec9a9af799dfb50daefacbc188e.positions[586] );
});