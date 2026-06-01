---
title: 1/2 pound burger
date: '2013-01-14T08:50:48-07:00'
format: image
service: flickr
tags:
- cheeburgercheeburger
- flickriosapp:filter=nofilter
- uploaded:by=flickrmobile
latitude: '40.670418'
longitude: '-73.978672'
image: https://dentedreality-content.s3.amazonaws.com/wp-content/uploads/2013/01/14190737/8380222891_9bd3be9872_o.jpg
---

[![1/2 pound burger](https://dentedreality-content.s3.amazonaws.com/wp-content/uploads/2013/01/14190737/8380222891_9bd3be9872_o.jpg)](https://dentedreality.com.au/2013/01/14/12-pound-burger/) 
# [1/2 pound burger](https://dentedreality.com.au/2013/01/14/12-pound-burger/)

[![1/2 pound burger](https://dentedreality-content.s3.amazonaws.com/wp-content/uploads/2013/01/14190737/8380222891_9bd3be9872_o.jpg)](http://www.flickr.com/photos/borkazoid/8380222891/)

With malted almond shake.

40.670418-73.978672




* #[cheeburgercheeburger](https://dentedreality.com.au/tags/cheeburgercheeburger/)
* #[flickriosapp:filter=nofilter](https://dentedreality.com.au/tags/flickriosappfilternofilter/)
* #[uploaded:by=flickrmobile](https://dentedreality.com.au/tags/uploadedbyflickrmobile/)

Posted on [Flickr](http://www.flickr.com/photos/borkazoid/8380222891/) [8:50 am, January 14, 2013](https://dentedreality.com.au/2013/01/14/12-pound-burger/ "8:50 am") 
jQuery(document).ready(function(){
var gmap\_m5fd9027b113605c1f9ce43c5db9378f7 = {
positions : {
637 : new google.maps.LatLng( '40.670418', '-73.978672' )
},
bounds : new google.maps.LatLngBounds(), // empty for now, we'll dynamically extend it later
map : new google.maps.Map(
document.getElementById( 'gmap\_m5fd9027b113605c1f9ce43c5db9378f7' ),
{
mapTypeId: google.maps.MapTypeId.ROADMAP,
center: new google.maps.LatLng( 0, 0 ),
zoom: 16 // Seems to be a good zoom for a single point
}
),
markers : {},
}; // end of gmap
// Extend the bounds of interest based on our positions
for ( var m in gmap\_m5fd9027b113605c1f9ce43c5db9378f7.positions ) {
gmap\_m5fd9027b113605c1f9ce43c5db9378f7.bounds.extend( gmap\_m5fd9027b113605c1f9ce43c5db9378f7.positions[m] );
}
// Render markers
for ( var m in gmap\_m5fd9027b113605c1f9ce43c5db9378f7.positions ) {
gmap\_m5fd9027b113605c1f9ce43c5db9378f7.markers[m] = new google.maps.Marker( {
clickable: true,
map : gmap\_m5fd9027b113605c1f9ce43c5db9378f7.map,
position : gmap\_m5fd9027b113605c1f9ce43c5db9378f7.positions[m]
} );
}
// Redraw map to fit our new marker-based bounds
gmap\_m5fd9027b113605c1f9ce43c5db9378f7.map.setCenter( gmap\_m5fd9027b113605c1f9ce43c5db9378f7.positions[637] );
});