---
title: Republica Dominica
date: '2013-12-30T11:31:35+00:00'
format: image
service: flickr
image: http://i2.wp.com/dentedreality.com.au/wp-content/uploads/2013/12/13924315213_edf7cfc166_o.jpg?fit=1500%2C1500
---

[![Republica Dominica](http://i2.wp.com/dentedreality.com.au/wp-content/uploads/2013/12/13924315213_edf7cfc166_o.jpg?fit=1500%2C1500)](http://dentedreality.com.au/2013/12/30/republica-dominica-4/) 
# [Republica Dominica](http://dentedreality.com.au/2013/12/30/republica-dominica-4/)





Posted on [Flickr](http://www.flickr.com/photos/borkazoid/13924315213/) [11:31 am, December 30, 2013](http://dentedreality.com.au/2013/12/30/republica-dominica-4/ "11:31 am") 
jQuery(document).ready(function(){
var gmap\_m649d04a79c49f47c4bc84c09dd75e389 = {
positions : {
905 : new google.maps.LatLng( '19.09275', '-70.594367' )
},
bounds : new google.maps.LatLngBounds(), // empty for now, we'll dynamically extend it later
map : new google.maps.Map(
document.getElementById( 'gmap\_m649d04a79c49f47c4bc84c09dd75e389' ),
{
mapTypeId: google.maps.MapTypeId.ROADMAP,
center: new google.maps.LatLng( 0, 0 ),
zoom: 16 // Seems to be a good zoom for a single point
}
),
markers : {},
}; // end of gmap
// Extend the bounds of interest based on our positions
for ( var m in gmap\_m649d04a79c49f47c4bc84c09dd75e389.positions ) {
gmap\_m649d04a79c49f47c4bc84c09dd75e389.bounds.extend( gmap\_m649d04a79c49f47c4bc84c09dd75e389.positions[m] );
}
// Render markers
for ( var m in gmap\_m649d04a79c49f47c4bc84c09dd75e389.positions ) {
gmap\_m649d04a79c49f47c4bc84c09dd75e389.markers[m] = new google.maps.Marker( {
clickable: true,
map : gmap\_m649d04a79c49f47c4bc84c09dd75e389.map,
position : gmap\_m649d04a79c49f47c4bc84c09dd75e389.positions[m]
} );
}
// Redraw map to fit our new marker-based bounds
gmap\_m649d04a79c49f47c4bc84c09dd75e389.map.setCenter( gmap\_m649d04a79c49f47c4bc84c09dd75e389.positions[905] );
});