---
title: The Owens’
date: '2011-05-29T13:55:17+00:00'
format: image
service: flickr
tags:
- owenswedding
- wedding
image: http://i0.wp.com/dentedreality.com.au/wp-content/uploads/2011/05/5803433156_75e099ba8f_o.jpg?resize=607%2C813
---

[![The Owens'](http://i0.wp.com/dentedreality.com.au/wp-content/uploads/2011/05/5803433156_75e099ba8f_o.jpg?resize=607%2C813)](http://dentedreality.com.au/2011/05/29/the-owens/) 
# [The Owens’](http://dentedreality.com.au/2011/05/29/the-owens/)





* #[owenswedding](http://dentedreality.com.au/tags/owenswedding/)
* #[wedding](http://dentedreality.com.au/tags/wedding/)

Posted on [Flickr](http://www.flickr.com/photos/borkazoid/5803433156/) [1:55 pm, May 29, 2011](http://dentedreality.com.au/2011/05/29/the-owens/ "1:55 pm") 
jQuery(document).ready(function(){
var gmap\_m8567fb23687d1d97dc49cabe748ca75a = {
positions : {
468 : new google.maps.LatLng( '37.776333', '-122.394' )
},
bounds : new google.maps.LatLngBounds(), // empty for now, we'll dynamically extend it later
map : new google.maps.Map(
document.getElementById( 'gmap\_m8567fb23687d1d97dc49cabe748ca75a' ),
{
mapTypeId: google.maps.MapTypeId.ROADMAP,
center: new google.maps.LatLng( 0, 0 ),
zoom: 16 // Seems to be a good zoom for a single point
}
),
markers : {},
}; // end of gmap
// Extend the bounds of interest based on our positions
for ( var m in gmap\_m8567fb23687d1d97dc49cabe748ca75a.positions ) {
gmap\_m8567fb23687d1d97dc49cabe748ca75a.bounds.extend( gmap\_m8567fb23687d1d97dc49cabe748ca75a.positions[m] );
}
// Render markers
for ( var m in gmap\_m8567fb23687d1d97dc49cabe748ca75a.positions ) {
gmap\_m8567fb23687d1d97dc49cabe748ca75a.markers[m] = new google.maps.Marker( {
clickable: true,
map : gmap\_m8567fb23687d1d97dc49cabe748ca75a.map,
position : gmap\_m8567fb23687d1d97dc49cabe748ca75a.positions[m]
} );
}
// Redraw map to fit our new marker-based bounds
gmap\_m8567fb23687d1d97dc49cabe748ca75a.map.setCenter( gmap\_m8567fb23687d1d97dc49cabe748ca75a.positions[468] );
});