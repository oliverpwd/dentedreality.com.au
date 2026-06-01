---
title: Toph’s Glasses
date: '2011-05-29T16:46:25+00:00'
format: image
service: flickr
tags:
- beau
- beaulebens
- me
- owenswedding
- wedding
image: http://i0.wp.com/dentedreality.com.au/wp-content/uploads/2011/05/5803433484_81fed474dc_o.jpg?resize=480%2C640
---

[![Toph's Glasses](http://i0.wp.com/dentedreality.com.au/wp-content/uploads/2011/05/5803433484_81fed474dc_o.jpg?resize=480%2C640)](http://dentedreality.com.au/2011/05/29/tophs-glasses/) 
# [Toph’s Glasses](http://dentedreality.com.au/2011/05/29/tophs-glasses/)





* #[beau](http://dentedreality.com.au/tags/beau/)
* #[beaulebens](http://dentedreality.com.au/tags/beaulebens/)
* #[me](http://dentedreality.com.au/tags/me/)
* #[owenswedding](http://dentedreality.com.au/tags/owenswedding/)
* #[wedding](http://dentedreality.com.au/tags/wedding/)

Posted on [Flickr](http://www.flickr.com/photos/borkazoid/5803433484/) [4:46 pm, May 29, 2011](http://dentedreality.com.au/2011/05/29/tophs-glasses/ "4:46 pm") 
jQuery(document).ready(function(){
var gmap\_m4455b6d6ffa135180288015ea2eb97a8 = {
positions : {
703 : new google.maps.LatLng( '37.790666', '-122.42' )
},
bounds : new google.maps.LatLngBounds(), // empty for now, we'll dynamically extend it later
map : new google.maps.Map(
document.getElementById( 'gmap\_m4455b6d6ffa135180288015ea2eb97a8' ),
{
mapTypeId: google.maps.MapTypeId.ROADMAP,
center: new google.maps.LatLng( 0, 0 ),
zoom: 16 // Seems to be a good zoom for a single point
}
),
markers : {},
}; // end of gmap
// Extend the bounds of interest based on our positions
for ( var m in gmap\_m4455b6d6ffa135180288015ea2eb97a8.positions ) {
gmap\_m4455b6d6ffa135180288015ea2eb97a8.bounds.extend( gmap\_m4455b6d6ffa135180288015ea2eb97a8.positions[m] );
}
// Render markers
for ( var m in gmap\_m4455b6d6ffa135180288015ea2eb97a8.positions ) {
gmap\_m4455b6d6ffa135180288015ea2eb97a8.markers[m] = new google.maps.Marker( {
clickable: true,
map : gmap\_m4455b6d6ffa135180288015ea2eb97a8.map,
position : gmap\_m4455b6d6ffa135180288015ea2eb97a8.positions[m]
} );
}
// Redraw map to fit our new marker-based bounds
gmap\_m4455b6d6ffa135180288015ea2eb97a8.map.setCenter( gmap\_m4455b6d6ffa135180288015ea2eb97a8.positions[703] );
});