---
title: Amazing Cazuela
date: '2009-12-26T09:48:17-07:00'
format: image
service: flickr
tags:
- argentina
- beer
- buenosaires
- cazuela
- cumana
- food
- quilmes
latitude: '-34.602167'
longitude: '-58.386667'
image: https://dentedreality-content.s3.amazonaws.com/wp-content/uploads/2009/12/14185430/4221916887_9ecdbeaf9d_o-768x1024.jpg
---

[![Amazing Cazuela](https://dentedreality-content.s3.amazonaws.com/wp-content/uploads/2009/12/14185430/4221916887_9ecdbeaf9d_o-768x1024.jpg)](https://dentedreality.com.au/2009/12/26/amazing-cazuela/) 
# [Amazing Cazuela](https://dentedreality.com.au/2009/12/26/amazing-cazuela/)

[![Amazing Cazuela](https://dentedreality-content.s3.amazonaws.com/wp-content/uploads/2009/12/14185430/4221916887_9ecdbeaf9d_o-768x1024.jpg)](http://www.flickr.com/photos/borkazoid/4221916887/)

DK suggested I go to this place, Cumana, because it had good, authentic food. I had no idea what I was getting, but I ordered what turned out to be lentil cazuela + a Quilmes (beer). It was freaking amazing. I ate the whole thing, and drank most of the beer, then waddled off to find Robin later 🙂

-34.602167-58.386667




* #[argentina](https://dentedreality.com.au/tags/argentina/)
* #[beer](https://dentedreality.com.au/tags/beer/)
* #[buenosaires](https://dentedreality.com.au/tags/buenosaires/)
* #[cazuela](https://dentedreality.com.au/tags/cazuela/)
* #[cumana](https://dentedreality.com.au/tags/cumana/)
* #[food](https://dentedreality.com.au/tags/food/)
* #[quilmes](https://dentedreality.com.au/tags/quilmes/)

Posted on [Flickr](http://www.flickr.com/photos/borkazoid/4221916887/) [9:48 am, December 26, 2009](https://dentedreality.com.au/2009/12/26/amazing-cazuela/ "9:48 am") 
jQuery(document).ready(function(){
var gmap\_m9360b8d0ae3207121b479b813f2ef633 = {
positions : {
432 : new google.maps.LatLng( '-34.602167', '-58.386667' )
},
bounds : new google.maps.LatLngBounds(), // empty for now, we'll dynamically extend it later
map : new google.maps.Map(
document.getElementById( 'gmap\_m9360b8d0ae3207121b479b813f2ef633' ),
{
mapTypeId: google.maps.MapTypeId.ROADMAP,
center: new google.maps.LatLng( 0, 0 ),
zoom: 16 // Seems to be a good zoom for a single point
}
),
markers : {},
}; // end of gmap
// Extend the bounds of interest based on our positions
for ( var m in gmap\_m9360b8d0ae3207121b479b813f2ef633.positions ) {
gmap\_m9360b8d0ae3207121b479b813f2ef633.bounds.extend( gmap\_m9360b8d0ae3207121b479b813f2ef633.positions[m] );
}
// Render markers
for ( var m in gmap\_m9360b8d0ae3207121b479b813f2ef633.positions ) {
gmap\_m9360b8d0ae3207121b479b813f2ef633.markers[m] = new google.maps.Marker( {
clickable: true,
map : gmap\_m9360b8d0ae3207121b479b813f2ef633.map,
position : gmap\_m9360b8d0ae3207121b479b813f2ef633.positions[m]
} );
}
// Redraw map to fit our new marker-based bounds
gmap\_m9360b8d0ae3207121b479b813f2ef633.map.setCenter( gmap\_m9360b8d0ae3207121b479b813f2ef633.positions[432] );
});