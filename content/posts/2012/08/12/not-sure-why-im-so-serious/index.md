---
title: Not Sure Why I’m So Serious
date: '2012-08-12T14:40:03+00:00'
format: image
service: flickr
tags:
- beau
- beaulebens
- me
image: http://i0.wp.com/dentedreality.com.au/wp-content/uploads/2012/08/7770421662_db53996db6_o.jpg?resize=480%2C480
---

[![Not Sure Why I'm So Serious](http://i0.wp.com/dentedreality.com.au/wp-content/uploads/2012/08/7770421662_db53996db6_o.jpg?resize=480%2C480)](http://dentedreality.com.au/2012/08/12/not-sure-why-im-so-serious/) 
# [Not Sure Why I’m So Serious](http://dentedreality.com.au/2012/08/12/not-sure-why-im-so-serious/)





* #[beau](http://dentedreality.com.au/tags/beau/)
* #[beaulebens](http://dentedreality.com.au/tags/beaulebens/)
* #[me](http://dentedreality.com.au/tags/me/)

Posted on [Flickr](http://www.flickr.com/photos/borkazoid/7770421662/) [2:40 pm, August 12, 2012](http://dentedreality.com.au/2012/08/12/not-sure-why-im-so-serious/ "2:40 pm") 
jQuery(document).ready(function(){
var gmap\_m0451171c30dc487673e04239321cd757 = {
positions : {
987 : new google.maps.LatLng( '37.791333', '0.000000' )
},
bounds : new google.maps.LatLngBounds(), // empty for now, we'll dynamically extend it later
map : new google.maps.Map(
document.getElementById( 'gmap\_m0451171c30dc487673e04239321cd757' ),
{
mapTypeId: google.maps.MapTypeId.ROADMAP,
center: new google.maps.LatLng( 0, 0 ),
zoom: 16 // Seems to be a good zoom for a single point
}
),
markers : {},
}; // end of gmap
// Extend the bounds of interest based on our positions
for ( var m in gmap\_m0451171c30dc487673e04239321cd757.positions ) {
gmap\_m0451171c30dc487673e04239321cd757.bounds.extend( gmap\_m0451171c30dc487673e04239321cd757.positions[m] );
}
// Render markers
for ( var m in gmap\_m0451171c30dc487673e04239321cd757.positions ) {
gmap\_m0451171c30dc487673e04239321cd757.markers[m] = new google.maps.Marker( {
clickable: true,
map : gmap\_m0451171c30dc487673e04239321cd757.map,
position : gmap\_m0451171c30dc487673e04239321cd757.positions[m]
} );
}
// Redraw map to fit our new marker-based bounds
gmap\_m0451171c30dc487673e04239321cd757.map.setCenter( gmap\_m0451171c30dc487673e04239321cd757.positions[987] );
});