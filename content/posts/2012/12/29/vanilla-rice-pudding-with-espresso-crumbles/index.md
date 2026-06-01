---
title: Vanilla Rice Pudding with espresso crumbles.
date: '2012-12-29T14:12:11-07:00'
format: image
service: flickr
tags:
- flickriosapp:filter=iguana
- iguanafilter
- ricetoriches
- uploaded:by=flickrmobile
latitude: '40.721736'
longitude: '-73.995936'
image: https://dentedreality-content.s3.amazonaws.com/wp-content/uploads/2012/12/14190734/8322812847_b89f9d4323_o.jpg
---

[![Vanilla Rice Pudding with espresso crumbles.](https://dentedreality-content.s3.amazonaws.com/wp-content/uploads/2012/12/14190734/8322812847_b89f9d4323_o.jpg)](https://dentedreality.com.au/2012/12/29/vanilla-rice-pudding-with-espresso-crumbles/) 
# [Vanilla Rice Pudding with espresso crumbles.](https://dentedreality.com.au/2012/12/29/vanilla-rice-pudding-with-espresso-crumbles/)

[![Vanilla Rice Pudding with espresso crumbles.](https://dentedreality-content.s3.amazonaws.com/wp-content/uploads/2012/12/14190734/8322812847_b89f9d4323_o.jpg)](http://www.flickr.com/photos/borkazoid/8322812847/)

40.721736-73.995936




* #[flickriosapp:filter=iguana](https://dentedreality.com.au/tags/flickriosappfilteriguana/)
* #[iguanafilter](https://dentedreality.com.au/tags/iguanafilter/)
* #[ricetoriches](https://dentedreality.com.au/tags/ricetoriches/)
* #[uploaded:by=flickrmobile](https://dentedreality.com.au/tags/uploadedbyflickrmobile/)

Posted on [Flickr](http://www.flickr.com/photos/borkazoid/8322812847/) [2:12 pm, December 29, 2012](https://dentedreality.com.au/2012/12/29/vanilla-rice-pudding-with-espresso-crumbles/ "2:12 pm") 
jQuery(document).ready(function(){
var gmap\_m0fe2f15557dec44f88fafd3ece992c89 = {
positions : {
649 : new google.maps.LatLng( '40.721736', '-73.995936' )
},
bounds : new google.maps.LatLngBounds(), // empty for now, we'll dynamically extend it later
map : new google.maps.Map(
document.getElementById( 'gmap\_m0fe2f15557dec44f88fafd3ece992c89' ),
{
mapTypeId: google.maps.MapTypeId.ROADMAP,
center: new google.maps.LatLng( 0, 0 ),
zoom: 16 // Seems to be a good zoom for a single point
}
),
markers : {},
}; // end of gmap
// Extend the bounds of interest based on our positions
for ( var m in gmap\_m0fe2f15557dec44f88fafd3ece992c89.positions ) {
gmap\_m0fe2f15557dec44f88fafd3ece992c89.bounds.extend( gmap\_m0fe2f15557dec44f88fafd3ece992c89.positions[m] );
}
// Render markers
for ( var m in gmap\_m0fe2f15557dec44f88fafd3ece992c89.positions ) {
gmap\_m0fe2f15557dec44f88fafd3ece992c89.markers[m] = new google.maps.Marker( {
clickable: true,
map : gmap\_m0fe2f15557dec44f88fafd3ece992c89.map,
position : gmap\_m0fe2f15557dec44f88fafd3ece992c89.positions[m]
} );
}
// Redraw map to fit our new marker-based bounds
gmap\_m0fe2f15557dec44f88fafd3ece992c89.map.setCenter( gmap\_m0fe2f15557dec44f88fafd3ece992c89.positions[649] );
});