---
title: Delicious in Progress
date: '2013-05-05T11:15:40+00:00'
format: image
service: flickr
tags:
- aardvarkfilter
- fettesau
- flickriosapp:filter=aardvark
- uploaded:by=flickrmobile
image: http://dentedreality.com.au/wp-content/uploads/2013/05/8710637969_58797580d5_o-1024x764.jpg
---

[![Delicious in Progress](http://dentedreality.com.au/wp-content/uploads/2013/05/8710637969_58797580d5_o-1024x764.jpg)](https://dentedreality.com.au/2013/05/05/delicious-in-progress/) 
# [Delicious in Progress](https://dentedreality.com.au/2013/05/05/delicious-in-progress/)

[![Delicious in Progress](http://dentedreality.com.au/wp-content/uploads/2013/05/8710637969_58797580d5_o-1024x764.jpg)](http://www.flickr.com/photos/borkazoid/8710637969/)





* #[aardvarkfilter](https://dentedreality.com.au/tags/aardvarkfilter/)
* #[fettesau](https://dentedreality.com.au/tags/fettesau/)
* #[flickriosapp:filter=aardvark](https://dentedreality.com.au/tags/flickriosappfilteraardvark/)
* #[uploaded:by=flickrmobile](https://dentedreality.com.au/tags/uploadedbyflickrmobile/)

Posted on [Flickr](http://www.flickr.com/photos/borkazoid/8710637969/) [11:15 am, May 5, 2013](https://dentedreality.com.au/2013/05/05/delicious-in-progress/ "11:15 am") 
jQuery(document).ready(function(){
var gmap\_m85fe5dfb2d428d799aabb101044751f5 = {
positions : {
113 : new google.maps.LatLng( '40.714118', '-73.956399' )
},
bounds : new google.maps.LatLngBounds(), // empty for now, we'll dynamically extend it later
map : new google.maps.Map(
document.getElementById( 'gmap\_m85fe5dfb2d428d799aabb101044751f5' ),
{
mapTypeId: google.maps.MapTypeId.ROADMAP,
center: new google.maps.LatLng( 0, 0 ),
zoom: 16 // Seems to be a good zoom for a single point
}
),
markers : {},
}; // end of gmap
// Extend the bounds of interest based on our positions
for ( var m in gmap\_m85fe5dfb2d428d799aabb101044751f5.positions ) {
gmap\_m85fe5dfb2d428d799aabb101044751f5.bounds.extend( gmap\_m85fe5dfb2d428d799aabb101044751f5.positions[m] );
}
// Render markers
for ( var m in gmap\_m85fe5dfb2d428d799aabb101044751f5.positions ) {
gmap\_m85fe5dfb2d428d799aabb101044751f5.markers[m] = new google.maps.Marker( {
clickable: true,
map : gmap\_m85fe5dfb2d428d799aabb101044751f5.map,
position : gmap\_m85fe5dfb2d428d799aabb101044751f5.positions[m]
} );
}
// Redraw map to fit our new marker-based bounds
gmap\_m85fe5dfb2d428d799aabb101044751f5.map.setCenter( gmap\_m85fe5dfb2d428d799aabb101044751f5.positions[113] );
});