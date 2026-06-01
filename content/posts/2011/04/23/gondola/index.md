---
title: Gondola
date: '2011-04-23T08:03:57+00:00'
format: image
service: flickr
tags:
- beau
- beaulebens
- california
- gondola
- me
- skiing
- tahoe
image: http://i1.wp.com/dentedreality.com.au/wp-content/uploads/2011/04/5802147511_92a179c9df_o.jpg?resize=607%2C452
---

[![Gondola](http://i1.wp.com/dentedreality.com.au/wp-content/uploads/2011/04/5802147511_92a179c9df_o.jpg?resize=607%2C452)](http://dentedreality.com.au/2011/04/23/gondola/) 
# [Gondola](http://dentedreality.com.au/2011/04/23/gondola/)

Going skiing for the first time ever.





* #[beau](http://dentedreality.com.au/tags/beau/)
* #[beaulebens](http://dentedreality.com.au/tags/beaulebens/)
* #[california](http://dentedreality.com.au/tags/california/)
* #[gondola](http://dentedreality.com.au/tags/gondola/)
* #[me](http://dentedreality.com.au/tags/me/)
* #[skiing](http://dentedreality.com.au/tags/skiing/)
* #[tahoe](http://dentedreality.com.au/tags/tahoe/)

Posted on [Flickr](http://www.flickr.com/photos/borkazoid/5802147511/) [8:03 am, April 23, 2011](http://dentedreality.com.au/2011/04/23/gondola/ "8:03 am") 
jQuery(document).ready(function(){
var gmap\_m56af74cbdc6cc583e5c8442ccae5fafb = {
positions : {
620 : new google.maps.LatLng( '39.198166', '-120.239167' )
},
bounds : new google.maps.LatLngBounds(), // empty for now, we'll dynamically extend it later
map : new google.maps.Map(
document.getElementById( 'gmap\_m56af74cbdc6cc583e5c8442ccae5fafb' ),
{
mapTypeId: google.maps.MapTypeId.ROADMAP,
center: new google.maps.LatLng( 0, 0 ),
zoom: 16 // Seems to be a good zoom for a single point
}
),
markers : {},
}; // end of gmap
// Extend the bounds of interest based on our positions
for ( var m in gmap\_m56af74cbdc6cc583e5c8442ccae5fafb.positions ) {
gmap\_m56af74cbdc6cc583e5c8442ccae5fafb.bounds.extend( gmap\_m56af74cbdc6cc583e5c8442ccae5fafb.positions[m] );
}
// Render markers
for ( var m in gmap\_m56af74cbdc6cc583e5c8442ccae5fafb.positions ) {
gmap\_m56af74cbdc6cc583e5c8442ccae5fafb.markers[m] = new google.maps.Marker( {
clickable: true,
map : gmap\_m56af74cbdc6cc583e5c8442ccae5fafb.map,
position : gmap\_m56af74cbdc6cc583e5c8442ccae5fafb.positions[m]
} );
}
// Redraw map to fit our new marker-based bounds
gmap\_m56af74cbdc6cc583e5c8442ccae5fafb.map.setCenter( gmap\_m56af74cbdc6cc583e5c8442ccae5fafb.positions[620] );
});