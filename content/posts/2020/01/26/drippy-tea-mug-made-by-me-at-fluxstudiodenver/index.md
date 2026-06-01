---
title: ''
date: '2020-01-26T14:28:53-07:00'
format: image
service: instagram
latitude: '39.70949'
longitude: '-105.002'
image: https://s3.amazonaws.com/dentedreality-content/wp-content/uploads/2020/01/26152501/81600398_117393489599537_2200012376528848189_n.jpg
---

[![Drippy tea mug. Made by me, at @fluxstudiodenver](https://s3.amazonaws.com/dentedreality-content/wp-content/uploads/2020/01/26152501/81600398_117393489599537_2200012376528848189_n.jpg)](https://dentedreality.com.au/2020/01/26/drippy-tea-mug-made-by-me-at-fluxstudiodenver/) 

![Drippy tea mug. Made by me, at @fluxstudiodenver](https://s3.amazonaws.com/dentedreality-content/wp-content/uploads/2020/01/26152501/81600398_117393489599537_2200012376528848189_n.jpg)

[![Drippy tea mug. Made by me, at @fluxstudiodenver](https://scontent.cdninstagram.com/v/t51.2885-15/sh0.08/e35/s640x640/81600398_117393489599537_2200012376528848189_n.jpg?_nc_ht=scontent.cdninstagram.com&_nc_ohc=SaoNJ2xhrrUAX8gTc7t&oh=269d7594ca0e2e4184f5408c9c117417&oe=5EC2FB9F)![Drippy tea mug. Made by me, at @fluxstudiodenver](https://scontent.cdninstagram.com/v/t51.2885-15/sh0.08/e35/s640x640/81600398_117393489599537_2200012376528848189_n.jpg?_nc_ht=scontent.cdninstagram.com&_nc_ohc=SaoNJ2xhrrUAX8gTc7t&oh=269d7594ca0e2e4184f5408c9c117417&oe=5EC2FB9F)](https://www.instagram.com/p/B7zEedKppQ5/)

Drippy tea mug. Made by me, at @fluxstudiodenver

39.70949-105.002




Posted on [Instagram](https://www.instagram.com/p/B7zEedKppQ5/) [2:28 pm, January 26, 2020](https://dentedreality.com.au/2020/01/26/drippy-tea-mug-made-by-me-at-fluxstudiodenver/ "2:28 pm") 
jQuery(document).ready(function(){
var gmap\_mbfb8a33eddad34e631ea3b3c97b0bc66 = {
positions : {
507 : new google.maps.LatLng( '39.70949', '-105.002' )
},
bounds : new google.maps.LatLngBounds(), // empty for now, we'll dynamically extend it later
map : new google.maps.Map(
document.getElementById( 'gmap\_mbfb8a33eddad34e631ea3b3c97b0bc66' ),
{
mapTypeId: google.maps.MapTypeId.ROADMAP,
center: new google.maps.LatLng( 0, 0 ),
zoom: 16 // Seems to be a good zoom for a single point
}
),
markers : {},
}; // end of gmap
// Extend the bounds of interest based on our positions
for ( var m in gmap\_mbfb8a33eddad34e631ea3b3c97b0bc66.positions ) {
gmap\_mbfb8a33eddad34e631ea3b3c97b0bc66.bounds.extend( gmap\_mbfb8a33eddad34e631ea3b3c97b0bc66.positions[m] );
}
// Render markers
for ( var m in gmap\_mbfb8a33eddad34e631ea3b3c97b0bc66.positions ) {
gmap\_mbfb8a33eddad34e631ea3b3c97b0bc66.markers[m] = new google.maps.Marker( {
clickable: true,
map : gmap\_mbfb8a33eddad34e631ea3b3c97b0bc66.map,
position : gmap\_mbfb8a33eddad34e631ea3b3c97b0bc66.positions[m]
} );
}
// Redraw map to fit our new marker-based bounds
gmap\_mbfb8a33eddad34e631ea3b3c97b0bc66.map.setCenter( gmap\_mbfb8a33eddad34e631ea3b3c97b0bc66.positions[507] );
});