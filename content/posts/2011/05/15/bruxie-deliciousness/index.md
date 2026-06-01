---
title: Bruxie-deliciousness
date: '2011-05-15T14:02:04+00:00'
format: image
service: flickr
tags:
- bruxie
- california
- delicious
- orangecounty
- sandwich
- waffle
- WCOC
- wordcamp
- wordcampoc
- wordpress
image: http://i1.wp.com/dentedreality.com.au/wp-content/uploads/2011/05/5802734918_3697c6ab20_o.jpg?resize=607%2C452
---

[![Bruxie-deliciousness](http://i1.wp.com/dentedreality.com.au/wp-content/uploads/2011/05/5802734918_3697c6ab20_o.jpg?resize=607%2C452)](http://dentedreality.com.au/2011/05/15/bruxie-deliciousness/) 
# [Bruxie-deliciousness](http://dentedreality.com.au/2011/05/15/bruxie-deliciousness/)

This place Bruxie is amazing. Go there. Eat.





* #[bruxie](http://dentedreality.com.au/tags/bruxie/)
* #[california](http://dentedreality.com.au/tags/california/)
* #[delicious](http://dentedreality.com.au/tags/delicious-2/)
* #[orangecounty](http://dentedreality.com.au/tags/orangecounty/)
* #[sandwich](http://dentedreality.com.au/tags/sandwich/)
* #[waffle](http://dentedreality.com.au/tags/waffle/)
* #[WCOC](http://dentedreality.com.au/tags/wcoc/)
* #[wordcamp](http://dentedreality.com.au/tags/wordcamp/)
* #[wordcampoc](http://dentedreality.com.au/tags/wordcampoc/)
* #[wordpress](http://dentedreality.com.au/tags/wordpress/)

Posted on [Flickr](http://www.flickr.com/photos/borkazoid/5802734918/) [2:02 pm, May 15, 2011](http://dentedreality.com.au/2011/05/15/bruxie-deliciousness/ "2:02 pm") 
jQuery(document).ready(function(){
var gmap\_m1e7642cd27c722e4883ae3ccc5456c54 = {
positions : {
322 : new google.maps.LatLng( '33.7915', '-117.853167' )
},
bounds : new google.maps.LatLngBounds(), // empty for now, we'll dynamically extend it later
map : new google.maps.Map(
document.getElementById( 'gmap\_m1e7642cd27c722e4883ae3ccc5456c54' ),
{
mapTypeId: google.maps.MapTypeId.ROADMAP,
center: new google.maps.LatLng( 0, 0 ),
zoom: 16 // Seems to be a good zoom for a single point
}
),
markers : {},
}; // end of gmap
// Extend the bounds of interest based on our positions
for ( var m in gmap\_m1e7642cd27c722e4883ae3ccc5456c54.positions ) {
gmap\_m1e7642cd27c722e4883ae3ccc5456c54.bounds.extend( gmap\_m1e7642cd27c722e4883ae3ccc5456c54.positions[m] );
}
// Render markers
for ( var m in gmap\_m1e7642cd27c722e4883ae3ccc5456c54.positions ) {
gmap\_m1e7642cd27c722e4883ae3ccc5456c54.markers[m] = new google.maps.Marker( {
clickable: true,
map : gmap\_m1e7642cd27c722e4883ae3ccc5456c54.map,
position : gmap\_m1e7642cd27c722e4883ae3ccc5456c54.positions[m]
} );
}
// Redraw map to fit our new marker-based bounds
gmap\_m1e7642cd27c722e4883ae3ccc5456c54.map.setCenter( gmap\_m1e7642cd27c722e4883ae3ccc5456c54.positions[322] );
});