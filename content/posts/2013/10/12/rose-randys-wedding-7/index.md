---
title: Rose & Randy’s Wedding
date: '2013-10-12T10:43:58+00:00'
format: image
service: flickr
tags:
- randy
- rose
- simonwedding
- vision:car=0517
- vision:mountain=0521
- vision:outdoor=0706
- vision:plant=0582
- vision:sky=0898
- wedding
image: http://i0.wp.com/dentedreality.com.au/wp-content/uploads/2013/10/12291461644_5b78e83ef7_o.jpg?fit=1500%2C1500
---

[![Rose & Randy's Wedding](http://i0.wp.com/dentedreality.com.au/wp-content/uploads/2013/10/12291461644_5b78e83ef7_o.jpg?fit=1500%2C1500)](http://dentedreality.com.au/2013/10/12/rose-randys-wedding-7/) 
# [Rose & Randy’s Wedding](http://dentedreality.com.au/2013/10/12/rose-randys-wedding-7/)





* #[randy](http://dentedreality.com.au/tags/randy/)
* #[rose](http://dentedreality.com.au/tags/rose/)
* #[simonwedding](http://dentedreality.com.au/tags/simonwedding/)
* #[vision:car=0517](http://dentedreality.com.au/tags/visioncar0517/)
* #[vision:mountain=0521](http://dentedreality.com.au/tags/visionmountain0521/)
* #[vision:outdoor=0706](http://dentedreality.com.au/tags/visionoutdoor0706/)
* #[vision:plant=0582](http://dentedreality.com.au/tags/visionplant0582/)
* #[vision:sky=0898](http://dentedreality.com.au/tags/visionsky0898/)
* #[wedding](http://dentedreality.com.au/tags/wedding/)

Posted on [Flickr](http://www.flickr.com/photos/borkazoid/12291461644/) [10:43 am, October 12, 2013](http://dentedreality.com.au/2013/10/12/rose-randys-wedding-7/ "10:43 am") 
jQuery(document).ready(function(){
var gmap\_m59096444eca7a5e6afd034ec6a174694 = {
positions : {
154 : new google.maps.LatLng( '38.417333', '-122.547334' )
},
bounds : new google.maps.LatLngBounds(), // empty for now, we'll dynamically extend it later
map : new google.maps.Map(
document.getElementById( 'gmap\_m59096444eca7a5e6afd034ec6a174694' ),
{
mapTypeId: google.maps.MapTypeId.ROADMAP,
center: new google.maps.LatLng( 0, 0 ),
zoom: 16 // Seems to be a good zoom for a single point
}
),
markers : {},
}; // end of gmap
// Extend the bounds of interest based on our positions
for ( var m in gmap\_m59096444eca7a5e6afd034ec6a174694.positions ) {
gmap\_m59096444eca7a5e6afd034ec6a174694.bounds.extend( gmap\_m59096444eca7a5e6afd034ec6a174694.positions[m] );
}
// Render markers
for ( var m in gmap\_m59096444eca7a5e6afd034ec6a174694.positions ) {
gmap\_m59096444eca7a5e6afd034ec6a174694.markers[m] = new google.maps.Marker( {
clickable: true,
map : gmap\_m59096444eca7a5e6afd034ec6a174694.map,
position : gmap\_m59096444eca7a5e6afd034ec6a174694.positions[m]
} );
}
// Redraw map to fit our new marker-based bounds
gmap\_m59096444eca7a5e6afd034ec6a174694.map.setCenter( gmap\_m59096444eca7a5e6afd034ec6a174694.positions[154] );
});