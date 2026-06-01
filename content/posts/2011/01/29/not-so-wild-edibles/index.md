---
title: Not-So-Wild Edibles
date: '2011-01-29T08:11:15+00:00'
format: image
service: flickr
tags:
- food
- minerslettuce
- plants
- salad
- sorrel
- wildedibles
image: http://i0.wp.com/dentedreality.com.au/wp-content/uploads/2011/01/5802609134_d2fc4d58f3_o.jpg?resize=607%2C813
---

[![Not-So-Wild Edibles](http://i0.wp.com/dentedreality.com.au/wp-content/uploads/2011/01/5802609134_d2fc4d58f3_o.jpg?resize=607%2C813)](http://dentedreality.com.au/2011/01/29/not-so-wild-edibles/) 
# [Not-So-Wild Edibles](http://dentedreality.com.au/2011/01/29/not-so-wild-edibles/)

I learned about these 2 edible "weeds" during Tracker School… and apparently you can now buy them at the Ferry Building Farmer’s Market





* #[food](http://dentedreality.com.au/tags/food/)
* #[minerslettuce](http://dentedreality.com.au/tags/minerslettuce/)
* #[plants](http://dentedreality.com.au/tags/plants/)
* #[salad](http://dentedreality.com.au/tags/salad/)
* #[sorrel](http://dentedreality.com.au/tags/sorrel/)
* #[wildedibles](http://dentedreality.com.au/tags/wildedibles/)

Posted on [Flickr](http://www.flickr.com/photos/borkazoid/5802609134/) [8:11 am, January 29, 2011](http://dentedreality.com.au/2011/01/29/not-so-wild-edibles/ "8:11 am") 
jQuery(document).ready(function(){
var gmap\_m5665754819adf6c55602307ae3df41f1 = {
positions : {
392 : new google.maps.LatLng( '37.795166', '-122.392167' )
},
bounds : new google.maps.LatLngBounds(), // empty for now, we'll dynamically extend it later
map : new google.maps.Map(
document.getElementById( 'gmap\_m5665754819adf6c55602307ae3df41f1' ),
{
mapTypeId: google.maps.MapTypeId.ROADMAP,
center: new google.maps.LatLng( 0, 0 ),
zoom: 16 // Seems to be a good zoom for a single point
}
),
markers : {},
}; // end of gmap
// Extend the bounds of interest based on our positions
for ( var m in gmap\_m5665754819adf6c55602307ae3df41f1.positions ) {
gmap\_m5665754819adf6c55602307ae3df41f1.bounds.extend( gmap\_m5665754819adf6c55602307ae3df41f1.positions[m] );
}
// Render markers
for ( var m in gmap\_m5665754819adf6c55602307ae3df41f1.positions ) {
gmap\_m5665754819adf6c55602307ae3df41f1.markers[m] = new google.maps.Marker( {
clickable: true,
map : gmap\_m5665754819adf6c55602307ae3df41f1.map,
position : gmap\_m5665754819adf6c55602307ae3df41f1.positions[m]
} );
}
// Redraw map to fit our new marker-based bounds
gmap\_m5665754819adf6c55602307ae3df41f1.map.setCenter( gmap\_m5665754819adf6c55602307ae3df41f1.positions[392] );
});