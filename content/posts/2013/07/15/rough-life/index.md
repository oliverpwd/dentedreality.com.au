---
title: Rough Life
date: '2013-07-15T04:23:43+00:00'
format: image
service: flickr
tags:
- beach
- costarica
- palms
- palmtrees
image: http://i1.wp.com/dentedreality.com.au/wp-content/uploads/2013/07/9437410943_6382b69e45_o.jpg?resize=607%2C452
---

[![Rough Life](http://i1.wp.com/dentedreality.com.au/wp-content/uploads/2013/07/9437410943_6382b69e45_o.jpg?resize=607%2C452)](http://dentedreality.com.au/2013/07/15/rough-life/) 
# [Rough Life](http://dentedreality.com.au/2013/07/15/rough-life/)





* #[beach](http://dentedreality.com.au/tags/beach/)
* #[costarica](http://dentedreality.com.au/tags/costarica/)
* #[palms](http://dentedreality.com.au/tags/palms/)
* #[palmtrees](http://dentedreality.com.au/tags/palmtrees/)

Posted on [Flickr](http://www.flickr.com/photos/borkazoid/9437410943/) [4:23 am, July 15, 2013](http://dentedreality.com.au/2013/07/15/rough-life/ "4:23 am") 
jQuery(document).ready(function(){
var gmap\_m98dad675b9b16959357cebd1a717fa63 = {
positions : {
923 : new google.maps.LatLng( '9.881166', '-85.5265' )
},
bounds : new google.maps.LatLngBounds(), // empty for now, we'll dynamically extend it later
map : new google.maps.Map(
document.getElementById( 'gmap\_m98dad675b9b16959357cebd1a717fa63' ),
{
mapTypeId: google.maps.MapTypeId.ROADMAP,
center: new google.maps.LatLng( 0, 0 ),
zoom: 16 // Seems to be a good zoom for a single point
}
),
markers : {},
}; // end of gmap
// Extend the bounds of interest based on our positions
for ( var m in gmap\_m98dad675b9b16959357cebd1a717fa63.positions ) {
gmap\_m98dad675b9b16959357cebd1a717fa63.bounds.extend( gmap\_m98dad675b9b16959357cebd1a717fa63.positions[m] );
}
// Render markers
for ( var m in gmap\_m98dad675b9b16959357cebd1a717fa63.positions ) {
gmap\_m98dad675b9b16959357cebd1a717fa63.markers[m] = new google.maps.Marker( {
clickable: true,
map : gmap\_m98dad675b9b16959357cebd1a717fa63.map,
position : gmap\_m98dad675b9b16959357cebd1a717fa63.positions[m]
} );
}
// Redraw map to fit our new marker-based bounds
gmap\_m98dad675b9b16959357cebd1a717fa63.map.setCenter( gmap\_m98dad675b9b16959357cebd1a717fa63.positions[923] );
});