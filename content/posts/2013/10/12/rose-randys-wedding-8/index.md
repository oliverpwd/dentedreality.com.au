---
title: Rose & Randy’s Wedding
date: '2013-10-12T10:42:10+00:00'
format: image
service: flickr
tags:
- randy
- rose
- simonwedding
- vision:car=0707
- vision:mountain=0619
- vision:outdoor=0716
- vision:sky=093
- vision:sunset=0521
- wedding
image: http://i1.wp.com/dentedreality.com.au/wp-content/uploads/2013/10/12291042395_55870b0be1_o.jpg?fit=1500%2C1500
---

[![Rose & Randy's Wedding](http://i1.wp.com/dentedreality.com.au/wp-content/uploads/2013/10/12291042395_55870b0be1_o.jpg?fit=1500%2C1500)](http://dentedreality.com.au/2013/10/12/rose-randys-wedding-8/) 
# [Rose & Randy’s Wedding](http://dentedreality.com.au/2013/10/12/rose-randys-wedding-8/)





* #[randy](http://dentedreality.com.au/tags/randy/)
* #[rose](http://dentedreality.com.au/tags/rose/)
* #[simonwedding](http://dentedreality.com.au/tags/simonwedding/)
* #[vision:car=0707](http://dentedreality.com.au/tags/visioncar0707/)
* #[vision:mountain=0619](http://dentedreality.com.au/tags/visionmountain0619/)
* #[vision:outdoor=0716](http://dentedreality.com.au/tags/visionoutdoor0716/)
* #[vision:sky=093](http://dentedreality.com.au/tags/visionsky093/)
* #[vision:sunset=0521](http://dentedreality.com.au/tags/visionsunset0521/)
* #[wedding](http://dentedreality.com.au/tags/wedding/)

Posted on [Flickr](http://www.flickr.com/photos/borkazoid/12291042395/) [10:42 am, October 12, 2013](http://dentedreality.com.au/2013/10/12/rose-randys-wedding-8/ "10:42 am") 
jQuery(document).ready(function(){
var gmap\_m6ea3756f745a2bee46f4d9edbf5fbaf4 = {
positions : {
170 : new google.maps.LatLng( '38.417333', '-122.547334' )
},
bounds : new google.maps.LatLngBounds(), // empty for now, we'll dynamically extend it later
map : new google.maps.Map(
document.getElementById( 'gmap\_m6ea3756f745a2bee46f4d9edbf5fbaf4' ),
{
mapTypeId: google.maps.MapTypeId.ROADMAP,
center: new google.maps.LatLng( 0, 0 ),
zoom: 16 // Seems to be a good zoom for a single point
}
),
markers : {},
}; // end of gmap
// Extend the bounds of interest based on our positions
for ( var m in gmap\_m6ea3756f745a2bee46f4d9edbf5fbaf4.positions ) {
gmap\_m6ea3756f745a2bee46f4d9edbf5fbaf4.bounds.extend( gmap\_m6ea3756f745a2bee46f4d9edbf5fbaf4.positions[m] );
}
// Render markers
for ( var m in gmap\_m6ea3756f745a2bee46f4d9edbf5fbaf4.positions ) {
gmap\_m6ea3756f745a2bee46f4d9edbf5fbaf4.markers[m] = new google.maps.Marker( {
clickable: true,
map : gmap\_m6ea3756f745a2bee46f4d9edbf5fbaf4.map,
position : gmap\_m6ea3756f745a2bee46f4d9edbf5fbaf4.positions[m]
} );
}
// Redraw map to fit our new marker-based bounds
gmap\_m6ea3756f745a2bee46f4d9edbf5fbaf4.map.setCenter( gmap\_m6ea3756f745a2bee46f4d9edbf5fbaf4.positions[170] );
});