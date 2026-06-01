---
title: Second Attempt
date: '2013-01-05T11:23:47-07:00'
format: image
service: flickr
tags:
- flickriosapp:filter=nofilter
- uploaded:by=flickrmobile
latitude: '40.669166'
longitude: '-73.985167'
image: https://dentedreality-content.s3.amazonaws.com/wp-content/uploads/2013/01/14190735/8351154246_7dbcd4d430_o.jpg
---

[![Second Attempt](https://dentedreality-content.s3.amazonaws.com/wp-content/uploads/2013/01/14190735/8351154246_7dbcd4d430_o.jpg)](https://dentedreality.com.au/2013/01/05/second-attempt/) 
# [Second Attempt](https://dentedreality.com.au/2013/01/05/second-attempt/)

[![Second Attempt](https://dentedreality-content.s3.amazonaws.com/wp-content/uploads/2013/01/14190735/8351154246_7dbcd4d430_o.jpg)](http://www.flickr.com/photos/borkazoid/8351154246/)

No-knead bread.

40.669166-73.985167




* #[flickriosapp:filter=nofilter](https://dentedreality.com.au/tags/flickriosappfilternofilter/)
* #[uploaded:by=flickrmobile](https://dentedreality.com.au/tags/uploadedbyflickrmobile/)

Posted on [Flickr](http://www.flickr.com/photos/borkazoid/8351154246/) [11:23 am, January 5, 2013](https://dentedreality.com.au/2013/01/05/second-attempt/ "11:23 am") 
jQuery(document).ready(function(){
var gmap\_m01163a6fab8bf4a70f55b2900962a453 = {
positions : {
950 : new google.maps.LatLng( '40.669166', '-73.985167' )
},
bounds : new google.maps.LatLngBounds(), // empty for now, we'll dynamically extend it later
map : new google.maps.Map(
document.getElementById( 'gmap\_m01163a6fab8bf4a70f55b2900962a453' ),
{
mapTypeId: google.maps.MapTypeId.ROADMAP,
center: new google.maps.LatLng( 0, 0 ),
zoom: 16 // Seems to be a good zoom for a single point
}
),
markers : {},
}; // end of gmap
// Extend the bounds of interest based on our positions
for ( var m in gmap\_m01163a6fab8bf4a70f55b2900962a453.positions ) {
gmap\_m01163a6fab8bf4a70f55b2900962a453.bounds.extend( gmap\_m01163a6fab8bf4a70f55b2900962a453.positions[m] );
}
// Render markers
for ( var m in gmap\_m01163a6fab8bf4a70f55b2900962a453.positions ) {
gmap\_m01163a6fab8bf4a70f55b2900962a453.markers[m] = new google.maps.Marker( {
clickable: true,
map : gmap\_m01163a6fab8bf4a70f55b2900962a453.map,
position : gmap\_m01163a6fab8bf4a70f55b2900962a453.positions[m]
} );
}
// Redraw map to fit our new marker-based bounds
gmap\_m01163a6fab8bf4a70f55b2900962a453.map.setCenter( gmap\_m01163a6fab8bf4a70f55b2900962a453.positions[950] );
});