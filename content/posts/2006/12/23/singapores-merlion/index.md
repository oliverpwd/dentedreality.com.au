---
title: Singapore’s Merlion
date: '2006-12-23T17:47:02+00:00'
format: image
service: flickr
tags:
- merlion
- river
- singapore
- thailand06
image: http://i2.wp.com/dentedreality.com.au/wp-content/uploads/2006/12/348115217_ce8809a64d_o.jpg?resize=607%2C455
---

[![Singapore's Merlion](http://i2.wp.com/dentedreality.com.au/wp-content/uploads/2006/12/348115217_ce8809a64d_o.jpg?resize=607%2C455)](http://dentedreality.com.au/2006/12/23/singapores-merlion/) 
# [Singapore’s Merlion](http://dentedreality.com.au/2006/12/23/singapores-merlion/)





* #[merlion](http://dentedreality.com.au/tags/merlion/)
* #[river](http://dentedreality.com.au/tags/river/)
* #[singapore](http://dentedreality.com.au/tags/singapore/)
* #[thailand06](http://dentedreality.com.au/tags/thailand06/)

Posted on [Flickr](http://www.flickr.com/photos/borkazoid/348115217/) [5:47 pm, December 23, 2006](http://dentedreality.com.au/2006/12/23/singapores-merlion/ "5:47 pm") 
jQuery(document).ready(function(){
var gmap\_m206dced227112160c44c1b015e263bdb = {
positions : {
459 : new google.maps.LatLng( '1.300394', '103.873157' )
},
bounds : new google.maps.LatLngBounds(), // empty for now, we'll dynamically extend it later
map : new google.maps.Map(
document.getElementById( 'gmap\_m206dced227112160c44c1b015e263bdb' ),
{
mapTypeId: google.maps.MapTypeId.ROADMAP,
center: new google.maps.LatLng( 0, 0 ),
zoom: 16 // Seems to be a good zoom for a single point
}
),
markers : {},
}; // end of gmap
// Extend the bounds of interest based on our positions
for ( var m in gmap\_m206dced227112160c44c1b015e263bdb.positions ) {
gmap\_m206dced227112160c44c1b015e263bdb.bounds.extend( gmap\_m206dced227112160c44c1b015e263bdb.positions[m] );
}
// Render markers
for ( var m in gmap\_m206dced227112160c44c1b015e263bdb.positions ) {
gmap\_m206dced227112160c44c1b015e263bdb.markers[m] = new google.maps.Marker( {
clickable: true,
map : gmap\_m206dced227112160c44c1b015e263bdb.map,
position : gmap\_m206dced227112160c44c1b015e263bdb.positions[m]
} );
}
// Redraw map to fit our new marker-based bounds
gmap\_m206dced227112160c44c1b015e263bdb.map.setCenter( gmap\_m206dced227112160c44c1b015e263bdb.positions[459] );
});