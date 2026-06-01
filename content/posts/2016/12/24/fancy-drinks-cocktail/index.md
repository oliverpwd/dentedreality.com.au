---
title: ''
date: '2016-12-24T09:20:57+00:00'
format: image
service: instagram
tags:
- cocktail
image: https://i0.wp.com/dentedreality.com.au/wp-content/uploads/2016/12/15535045_113918262440869_6862526439497924608_n.jpg?fit=640%2C640
---

[![Fancy drinks. #cocktail](https://i0.wp.com/dentedreality.com.au/wp-content/uploads/2016/12/15535045_113918262440869_6862526439497924608_n.jpg?fit=640%2C640)](http://dentedreality.com.au/2016/12/24/fancy-drinks-cocktail/) 

Fancy drinks. #cocktail





* #[cocktail](http://dentedreality.com.au/tags/cocktail/)

Posted on [Instagram](https://www.instagram.com/p/BOaAkLHDWyL/) [9:20 am, December 24, 2016](http://dentedreality.com.au/2016/12/24/fancy-drinks-cocktail/ "9:20 am") 
jQuery(document).ready(function(){
var gmap\_mbbfd1799e7bdd1216490d39b476cdb1f = {
positions : {
895 : new google.maps.LatLng( '39.7558597', '-105.2223768' )
},
bounds : new google.maps.LatLngBounds(), // empty for now, we'll dynamically extend it later
map : new google.maps.Map(
document.getElementById( 'gmap\_mbbfd1799e7bdd1216490d39b476cdb1f' ),
{
mapTypeId: google.maps.MapTypeId.ROADMAP,
center: new google.maps.LatLng( 0, 0 ),
zoom: 16 // Seems to be a good zoom for a single point
}
),
markers : {},
}; // end of gmap
// Extend the bounds of interest based on our positions
for ( var m in gmap\_mbbfd1799e7bdd1216490d39b476cdb1f.positions ) {
gmap\_mbbfd1799e7bdd1216490d39b476cdb1f.bounds.extend( gmap\_mbbfd1799e7bdd1216490d39b476cdb1f.positions[m] );
}
// Render markers
for ( var m in gmap\_mbbfd1799e7bdd1216490d39b476cdb1f.positions ) {
gmap\_mbbfd1799e7bdd1216490d39b476cdb1f.markers[m] = new google.maps.Marker( {
clickable: true,
map : gmap\_mbbfd1799e7bdd1216490d39b476cdb1f.map,
position : gmap\_mbbfd1799e7bdd1216490d39b476cdb1f.positions[m]
} );
}
// Redraw map to fit our new marker-based bounds
gmap\_mbbfd1799e7bdd1216490d39b476cdb1f.map.setCenter( gmap\_mbbfd1799e7bdd1216490d39b476cdb1f.positions[895] );
});