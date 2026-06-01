---
title: Bay Bridge
date: '2013-05-18T07:48:29+00:00'
format: image
service: flickr
tags:
- automattic
- baybridge
- sanfrancisco
image: http://i2.wp.com/dentedreality.com.au/wp-content/uploads/2013/05/9436931047_18c1e0e972_o.jpg?resize=607%2C452
---

[![Bay Bridge](http://i2.wp.com/dentedreality.com.au/wp-content/uploads/2013/05/9436931047_18c1e0e972_o.jpg?resize=607%2C452)](http://dentedreality.com.au/2013/05/18/bay-bridge/) 
# [Bay Bridge](http://dentedreality.com.au/2013/05/18/bay-bridge/)





* #[automattic](http://dentedreality.com.au/tags/automattic/)
* #[baybridge](http://dentedreality.com.au/tags/baybridge/)
* #[sanfrancisco](http://dentedreality.com.au/tags/sanfrancisco/)

Posted on [Flickr](http://www.flickr.com/photos/borkazoid/9436931047/) [7:48 am, May 18, 2013](http://dentedreality.com.au/2013/05/18/bay-bridge/ "7:48 am") 
jQuery(document).ready(function(){
var gmap\_me151a39fae0759e388dbd0b8bcbd4483 = {
positions : {
852 : new google.maps.LatLng( '37.7935', '-122.391834' )
},
bounds : new google.maps.LatLngBounds(), // empty for now, we'll dynamically extend it later
map : new google.maps.Map(
document.getElementById( 'gmap\_me151a39fae0759e388dbd0b8bcbd4483' ),
{
mapTypeId: google.maps.MapTypeId.ROADMAP,
center: new google.maps.LatLng( 0, 0 ),
zoom: 16 // Seems to be a good zoom for a single point
}
),
markers : {},
}; // end of gmap
// Extend the bounds of interest based on our positions
for ( var m in gmap\_me151a39fae0759e388dbd0b8bcbd4483.positions ) {
gmap\_me151a39fae0759e388dbd0b8bcbd4483.bounds.extend( gmap\_me151a39fae0759e388dbd0b8bcbd4483.positions[m] );
}
// Render markers
for ( var m in gmap\_me151a39fae0759e388dbd0b8bcbd4483.positions ) {
gmap\_me151a39fae0759e388dbd0b8bcbd4483.markers[m] = new google.maps.Marker( {
clickable: true,
map : gmap\_me151a39fae0759e388dbd0b8bcbd4483.map,
position : gmap\_me151a39fae0759e388dbd0b8bcbd4483.positions[m]
} );
}
// Redraw map to fit our new marker-based bounds
gmap\_me151a39fae0759e388dbd0b8bcbd4483.map.setCenter( gmap\_me151a39fae0759e388dbd0b8bcbd4483.positions[852] );
});