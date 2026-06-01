---
title: ''
date: '2020-01-25T17:55:37-07:00'
format: image
service: instagram
latitude: '39.70949'
longitude: '-105.002'
image: https://s3.amazonaws.com/dentedreality-content/wp-content/uploads/2020/01/25182458/82553873_264247597882574_7396340477698834822_n.jpg
---

[![We had so much fun making all this stuff (and a few more, not pictured) at @fluxstudiodenver, will definitely be doing some more! Thanks Derek!](https://s3.amazonaws.com/dentedreality-content/wp-content/uploads/2020/01/25182458/82553873_264247597882574_7396340477698834822_n.jpg)](https://dentedreality.com.au/2020/01/25/we-had-so-much-fun-making-all-this-stuff-and-a-few-more-not-pictured-at-fluxstudiodenver-will-definitely-be-doing-some-more-thanks-derek/) 

![We had so much fun making all this stuff (and a few more, not pictured) at @fluxstudiodenver, will definitely be doing some more! Thanks Derek!](https://s3.amazonaws.com/dentedreality-content/wp-content/uploads/2020/01/25182458/82553873_264247597882574_7396340477698834822_n.jpg)

[![We had so much fun making all this stuff (and a few more, not pictured) at @fluxstudiodenver, will definitely be doing some more! Thanks Derek!](https://scontent.cdninstagram.com/v/t51.2885-15/sh0.08/e35/s640x640/82553873_264247597882574_7396340477698834822_n.jpg?_nc_ht=scontent.cdninstagram.com&_nc_ohc=c-vtZom1Yy8AX-OU_77&oh=dbd46eca2fa80eb2a6ca0d3cf713dff0&oe=5EC97518)![We had so much fun making all this stuff (and a few more, not pictured) at @fluxstudiodenver, will definitely be doing some more! Thanks Derek!](https://scontent.cdninstagram.com/v/t51.2885-15/sh0.08/e35/s640x640/82553873_264247597882574_7396340477698834822_n.jpg?_nc_ht=scontent.cdninstagram.com&_nc_ohc=c-vtZom1Yy8AX-OU_77&oh=dbd46eca2fa80eb2a6ca0d3cf713dff0&oe=5EC97518)](https://www.instagram.com/p/B7w3V0BJH3c/)

We had so much fun making all this stuff (and a few more, not pictured) at @fluxstudiodenver, will definitely be doing some more! Thanks Derek!

39.70949-105.002




Posted on [Instagram](https://www.instagram.com/p/B7w3V0BJH3c/) [5:55 pm, January 25, 2020](https://dentedreality.com.au/2020/01/25/we-had-so-much-fun-making-all-this-stuff-and-a-few-more-not-pictured-at-fluxstudiodenver-will-definitely-be-doing-some-more-thanks-derek/ "5:55 pm") 
jQuery(document).ready(function(){
var gmap\_m26ed06f0a336430a9723783e0a378a19 = {
positions : {
423 : new google.maps.LatLng( '39.70949', '-105.002' )
},
bounds : new google.maps.LatLngBounds(), // empty for now, we'll dynamically extend it later
map : new google.maps.Map(
document.getElementById( 'gmap\_m26ed06f0a336430a9723783e0a378a19' ),
{
mapTypeId: google.maps.MapTypeId.ROADMAP,
center: new google.maps.LatLng( 0, 0 ),
zoom: 16 // Seems to be a good zoom for a single point
}
),
markers : {},
}; // end of gmap
// Extend the bounds of interest based on our positions
for ( var m in gmap\_m26ed06f0a336430a9723783e0a378a19.positions ) {
gmap\_m26ed06f0a336430a9723783e0a378a19.bounds.extend( gmap\_m26ed06f0a336430a9723783e0a378a19.positions[m] );
}
// Render markers
for ( var m in gmap\_m26ed06f0a336430a9723783e0a378a19.positions ) {
gmap\_m26ed06f0a336430a9723783e0a378a19.markers[m] = new google.maps.Marker( {
clickable: true,
map : gmap\_m26ed06f0a336430a9723783e0a378a19.map,
position : gmap\_m26ed06f0a336430a9723783e0a378a19.positions[m]
} );
}
// Redraw map to fit our new marker-based bounds
gmap\_m26ed06f0a336430a9723783e0a378a19.map.setCenter( gmap\_m26ed06f0a336430a9723783e0a378a19.positions[423] );
});