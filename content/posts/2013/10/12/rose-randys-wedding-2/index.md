---
title: Rose & Randy’s Wedding
date: '2013-10-12T15:21:07+00:00'
format: image
service: flickr
tags:
- randy
- rose
- simonwedding
- vision:car=0888
- vision:city=052
- wedding
image: http://i1.wp.com/dentedreality.com.au/wp-content/uploads/2013/10/12291038865_06c5ab7780_o.jpg?fit=1500%2C1500
---

[![Rose & Randy's Wedding](http://i1.wp.com/dentedreality.com.au/wp-content/uploads/2013/10/12291038865_06c5ab7780_o.jpg?fit=1500%2C1500)](http://dentedreality.com.au/2013/10/12/rose-randys-wedding-2/) 
# [Rose & Randy’s Wedding](http://dentedreality.com.au/2013/10/12/rose-randys-wedding-2/)





* #[randy](http://dentedreality.com.au/tags/randy/)
* #[rose](http://dentedreality.com.au/tags/rose/)
* #[simonwedding](http://dentedreality.com.au/tags/simonwedding/)
* #[vision:car=0888](http://dentedreality.com.au/tags/visioncar0888/)
* #[vision:city=052](http://dentedreality.com.au/tags/visioncity052/)
* #[wedding](http://dentedreality.com.au/tags/wedding/)

Posted on [Flickr](http://www.flickr.com/photos/borkazoid/12291038865/) [3:21 pm, October 12, 2013](http://dentedreality.com.au/2013/10/12/rose-randys-wedding-2/ "3:21 pm") 
jQuery(document).ready(function(){
var gmap\_m8ccd44f1b2c7133c09efbbddc818ed5e = {
positions : {
598 : new google.maps.LatLng( '38.413166', '-122.552' )
},
bounds : new google.maps.LatLngBounds(), // empty for now, we'll dynamically extend it later
map : new google.maps.Map(
document.getElementById( 'gmap\_m8ccd44f1b2c7133c09efbbddc818ed5e' ),
{
mapTypeId: google.maps.MapTypeId.ROADMAP,
center: new google.maps.LatLng( 0, 0 ),
zoom: 16 // Seems to be a good zoom for a single point
}
),
markers : {},
}; // end of gmap
// Extend the bounds of interest based on our positions
for ( var m in gmap\_m8ccd44f1b2c7133c09efbbddc818ed5e.positions ) {
gmap\_m8ccd44f1b2c7133c09efbbddc818ed5e.bounds.extend( gmap\_m8ccd44f1b2c7133c09efbbddc818ed5e.positions[m] );
}
// Render markers
for ( var m in gmap\_m8ccd44f1b2c7133c09efbbddc818ed5e.positions ) {
gmap\_m8ccd44f1b2c7133c09efbbddc818ed5e.markers[m] = new google.maps.Marker( {
clickable: true,
map : gmap\_m8ccd44f1b2c7133c09efbbddc818ed5e.map,
position : gmap\_m8ccd44f1b2c7133c09efbbddc818ed5e.positions[m]
} );
}
// Redraw map to fit our new marker-based bounds
gmap\_m8ccd44f1b2c7133c09efbbddc818ed5e.map.setCenter( gmap\_m8ccd44f1b2c7133c09efbbddc818ed5e.positions[598] );
});