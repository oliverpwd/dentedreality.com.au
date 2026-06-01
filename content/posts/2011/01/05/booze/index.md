---
title: Booze!
date: '2011-01-05T09:06:14-06:00'
format: image
service: flickr
tags:
- alcohol
- beer
- booze
- party
latitude: '-32.053'
longitude: '115.846499'
image: https://s3.amazonaws.com/dentedreality-content/wp-content/uploads/2011/01/14185953/5434719720_66b43ae367_o.jpg
---

[![Booze!](https://s3.amazonaws.com/dentedreality-content/wp-content/uploads/2011/01/14185953/5434719720_66b43ae367_o.jpg)](https://dentedreality.com.au/2011/01/05/booze/) 
# [Booze!](https://dentedreality.com.au/2011/01/05/booze/)

[![Booze!](https://s3.amazonaws.com/dentedreality-content/wp-content/uploads/2011/01/14185953/5434719720_66b43ae367_o.jpg)](http://www.flickr.com/photos/borkazoid/5434719720/)

-32.053115.846499




* #[alcohol](https://dentedreality.com.au/tags/alcohol/)
* #[beer](https://dentedreality.com.au/tags/beer/)
* #[booze](https://dentedreality.com.au/tags/booze/)
* #[party](https://dentedreality.com.au/tags/party/)

Posted on [Flickr](http://www.flickr.com/photos/borkazoid/5434719720/) [9:06 am, January 5, 2011](https://dentedreality.com.au/2011/01/05/booze/ "9:06 am") 
jQuery(document).ready(function(){
var gmap\_m2076fd431690a9862930e850ce2e0046 = {
positions : {
831 : new google.maps.LatLng( '-32.053', '115.846499' )
},
bounds : new google.maps.LatLngBounds(), // empty for now, we'll dynamically extend it later
map : new google.maps.Map(
document.getElementById( 'gmap\_m2076fd431690a9862930e850ce2e0046' ),
{
mapTypeId: google.maps.MapTypeId.ROADMAP,
center: new google.maps.LatLng( 0, 0 ),
zoom: 16 // Seems to be a good zoom for a single point
}
),
markers : {},
}; // end of gmap
// Extend the bounds of interest based on our positions
for ( var m in gmap\_m2076fd431690a9862930e850ce2e0046.positions ) {
gmap\_m2076fd431690a9862930e850ce2e0046.bounds.extend( gmap\_m2076fd431690a9862930e850ce2e0046.positions[m] );
}
// Render markers
for ( var m in gmap\_m2076fd431690a9862930e850ce2e0046.positions ) {
gmap\_m2076fd431690a9862930e850ce2e0046.markers[m] = new google.maps.Marker( {
clickable: true,
map : gmap\_m2076fd431690a9862930e850ce2e0046.map,
position : gmap\_m2076fd431690a9862930e850ce2e0046.positions[m]
} );
}
// Redraw map to fit our new marker-based bounds
gmap\_m2076fd431690a9862930e850ce2e0046.map.setCenter( gmap\_m2076fd431690a9862930e850ce2e0046.positions[831] );
});