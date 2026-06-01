---
title: Cards Against Beau Lebens
date: '2013-12-20T10:11:00+00:00'
format: image
service: flickr
tags:
- beaulebens
- cah
- cardsagainsthumanity
image: http://i0.wp.com/dentedreality.com.au/wp-content/uploads/2013/12/13900589456_89c98ef07b_o.jpg?resize=607%2C809
---

[![Cards Against Beau Lebens](http://i0.wp.com/dentedreality.com.au/wp-content/uploads/2013/12/13900589456_89c98ef07b_o.jpg?resize=607%2C809)](http://dentedreality.com.au/2013/12/20/cards-against-beau-lebens/) 
# [Cards Against Beau Lebens](http://dentedreality.com.au/2013/12/20/cards-against-beau-lebens/)





* #[beaulebens](http://dentedreality.com.au/tags/beaulebens/)
* #[cah](http://dentedreality.com.au/tags/cah/)
* #[cardsagainsthumanity](http://dentedreality.com.au/tags/cardsagainsthumanity/)

Posted on [Flickr](http://www.flickr.com/photos/borkazoid/13900589456/) [10:11 am, December 20, 2013](http://dentedreality.com.au/2013/12/20/cards-against-beau-lebens/ "10:11 am") 
jQuery(document).ready(function(){
var gmap\_m90864c37fcc3ec03983f69381bcde7e7 = {
positions : {
125 : new google.maps.LatLng( '40.669472', '-73.984887' )
},
bounds : new google.maps.LatLngBounds(), // empty for now, we'll dynamically extend it later
map : new google.maps.Map(
document.getElementById( 'gmap\_m90864c37fcc3ec03983f69381bcde7e7' ),
{
mapTypeId: google.maps.MapTypeId.ROADMAP,
center: new google.maps.LatLng( 0, 0 ),
zoom: 16 // Seems to be a good zoom for a single point
}
),
markers : {},
}; // end of gmap
// Extend the bounds of interest based on our positions
for ( var m in gmap\_m90864c37fcc3ec03983f69381bcde7e7.positions ) {
gmap\_m90864c37fcc3ec03983f69381bcde7e7.bounds.extend( gmap\_m90864c37fcc3ec03983f69381bcde7e7.positions[m] );
}
// Render markers
for ( var m in gmap\_m90864c37fcc3ec03983f69381bcde7e7.positions ) {
gmap\_m90864c37fcc3ec03983f69381bcde7e7.markers[m] = new google.maps.Marker( {
clickable: true,
map : gmap\_m90864c37fcc3ec03983f69381bcde7e7.map,
position : gmap\_m90864c37fcc3ec03983f69381bcde7e7.positions[m]
} );
}
// Redraw map to fit our new marker-based bounds
gmap\_m90864c37fcc3ec03983f69381bcde7e7.map.setCenter( gmap\_m90864c37fcc3ec03983f69381bcde7e7.positions[125] );
});