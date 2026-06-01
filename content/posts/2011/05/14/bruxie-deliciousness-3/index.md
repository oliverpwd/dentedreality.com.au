---
title: Bruxie-deliciousness
date: '2011-05-14T14:12:44+00:00'
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
image: http://i0.wp.com/dentedreality.com.au/wp-content/uploads/2011/05/5802178307_80316c5c0a_o.jpg?resize=607%2C452
---

[![Bruxie-deliciousness](http://i0.wp.com/dentedreality.com.au/wp-content/uploads/2011/05/5802178307_80316c5c0a_o.jpg?resize=607%2C452)](http://dentedreality.com.au/2011/05/14/bruxie-deliciousness-3/) 
# [Bruxie-deliciousness](http://dentedreality.com.au/2011/05/14/bruxie-deliciousness-3/)

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

Posted on [Flickr](http://www.flickr.com/photos/borkazoid/5802178307/) [2:12 pm, May 14, 2011](http://dentedreality.com.au/2011/05/14/bruxie-deliciousness-3/ "2:12 pm") 
jQuery(document).ready(function(){
var gmap\_md694f3327ee916ab0c55484df8972792 = {
positions : {
737 : new google.maps.LatLng( '33.791333', '-117.853167' )
},
bounds : new google.maps.LatLngBounds(), // empty for now, we'll dynamically extend it later
map : new google.maps.Map(
document.getElementById( 'gmap\_md694f3327ee916ab0c55484df8972792' ),
{
mapTypeId: google.maps.MapTypeId.ROADMAP,
center: new google.maps.LatLng( 0, 0 ),
zoom: 16 // Seems to be a good zoom for a single point
}
),
markers : {},
}; // end of gmap
// Extend the bounds of interest based on our positions
for ( var m in gmap\_md694f3327ee916ab0c55484df8972792.positions ) {
gmap\_md694f3327ee916ab0c55484df8972792.bounds.extend( gmap\_md694f3327ee916ab0c55484df8972792.positions[m] );
}
// Render markers
for ( var m in gmap\_md694f3327ee916ab0c55484df8972792.positions ) {
gmap\_md694f3327ee916ab0c55484df8972792.markers[m] = new google.maps.Marker( {
clickable: true,
map : gmap\_md694f3327ee916ab0c55484df8972792.map,
position : gmap\_md694f3327ee916ab0c55484df8972792.positions[m]
} );
}
// Redraw map to fit our new marker-based bounds
gmap\_md694f3327ee916ab0c55484df8972792.map.setCenter( gmap\_md694f3327ee916ab0c55484df8972792.positions[737] );
});