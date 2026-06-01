---
title: My Bike
date: '2012-12-11T11:35:34+00:00'
format: image
service: flickr
tags:
- bicycle
- bike
- cannondale
- flickriosapp:filter=iguana
- iguana
- uploaded:by=flickrmobile
image: http://i1.wp.com/dentedreality.com.au/wp-content/uploads/2012/12/8266168669_7d5a5d5866_o.jpg?resize=607%2C452
---

[![My Bike](http://i1.wp.com/dentedreality.com.au/wp-content/uploads/2012/12/8266168669_7d5a5d5866_o.jpg?resize=607%2C452)](http://dentedreality.com.au/2012/12/11/my-bike-2/) 
# [My Bike](http://dentedreality.com.au/2012/12/11/my-bike-2/)





* #[bicycle](http://dentedreality.com.au/tags/bicycle/)
* #[bike](http://dentedreality.com.au/tags/bike/)
* #[cannondale](http://dentedreality.com.au/tags/cannondale/)
* #[flickriosapp:filter=iguana](http://dentedreality.com.au/tags/flickriosappfilteriguana/)
* #[iguana](http://dentedreality.com.au/tags/iguana/)
* #[uploaded:by=flickrmobile](http://dentedreality.com.au/tags/uploadedbyflickrmobile/)

Posted on [Flickr](http://www.flickr.com/photos/borkazoid/8266168669/) [11:35 am, December 11, 2012](http://dentedreality.com.au/2012/12/11/my-bike-2/ "11:35 am") 
jQuery(document).ready(function(){
var gmap\_ma8f20d85362f33fecef769bdef44e2c3 = {
positions : {
146 : new google.maps.LatLng( '40.671333', '-73.985' )
},
bounds : new google.maps.LatLngBounds(), // empty for now, we'll dynamically extend it later
map : new google.maps.Map(
document.getElementById( 'gmap\_ma8f20d85362f33fecef769bdef44e2c3' ),
{
mapTypeId: google.maps.MapTypeId.ROADMAP,
center: new google.maps.LatLng( 0, 0 ),
zoom: 16 // Seems to be a good zoom for a single point
}
),
markers : {},
}; // end of gmap
// Extend the bounds of interest based on our positions
for ( var m in gmap\_ma8f20d85362f33fecef769bdef44e2c3.positions ) {
gmap\_ma8f20d85362f33fecef769bdef44e2c3.bounds.extend( gmap\_ma8f20d85362f33fecef769bdef44e2c3.positions[m] );
}
// Render markers
for ( var m in gmap\_ma8f20d85362f33fecef769bdef44e2c3.positions ) {
gmap\_ma8f20d85362f33fecef769bdef44e2c3.markers[m] = new google.maps.Marker( {
clickable: true,
map : gmap\_ma8f20d85362f33fecef769bdef44e2c3.map,
position : gmap\_ma8f20d85362f33fecef769bdef44e2c3.positions[m]
} );
}
// Redraw map to fit our new marker-based bounds
gmap\_ma8f20d85362f33fecef769bdef44e2c3.map.setCenter( gmap\_ma8f20d85362f33fecef769bdef44e2c3.positions[146] );
});