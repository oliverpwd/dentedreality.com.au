---
title: ''
date: '2016-06-28T00:53:16-06:00'
format: image
service: instagram
tags:
- quokkaselfie
latitude: '-31.996255'
longitude: '115.5415947'
image: http://i1.wp.com/dentedreality.com.au/wp-content/uploads/2016/06/13402680_556101997923435_76648092_n.jpg?fit=640%2C640
---

[![#quokkaselfie](http://i1.wp.com/dentedreality.com.au/wp-content/uploads/2016/06/13402680_556101997923435_76648092_n.jpg?fit=640%2C640)](https://dentedreality.com.au/2016/06/28/quokkaselfie/) 

[![#quokkaselfie](http://i1.wp.com/dentedreality.com.au/wp-content/uploads/2016/06/13402680_556101997923435_76648092_n.jpg?fit=640%2C640)](https://www.instagram.com/p/BHMFTnTgRzt/)

#quokkaselfie

-31.996255115.5415947




* #[quokkaselfie](https://dentedreality.com.au/tags/quokkaselfie/)

Posted on [Instagram](https://www.instagram.com/p/BHMFTnTgRzt/) [12:53 am, June 28, 2016](https://dentedreality.com.au/2016/06/28/quokkaselfie/ "12:53 am") 
jQuery(document).ready(function(){
var gmap\_md586cf4556221b6fe12f92c256e6183e = {
positions : {
743 : new google.maps.LatLng( '-31.996254968353', '115.54159471343' )
},
bounds : new google.maps.LatLngBounds(), // empty for now, we'll dynamically extend it later
map : new google.maps.Map(
document.getElementById( 'gmap\_md586cf4556221b6fe12f92c256e6183e' ),
{
mapTypeId: google.maps.MapTypeId.ROADMAP,
center: new google.maps.LatLng( 0, 0 ),
zoom: 16 // Seems to be a good zoom for a single point
}
),
markers : {},
}; // end of gmap
// Extend the bounds of interest based on our positions
for ( var m in gmap\_md586cf4556221b6fe12f92c256e6183e.positions ) {
gmap\_md586cf4556221b6fe12f92c256e6183e.bounds.extend( gmap\_md586cf4556221b6fe12f92c256e6183e.positions[m] );
}
// Render markers
for ( var m in gmap\_md586cf4556221b6fe12f92c256e6183e.positions ) {
gmap\_md586cf4556221b6fe12f92c256e6183e.markers[m] = new google.maps.Marker( {
clickable: true,
map : gmap\_md586cf4556221b6fe12f92c256e6183e.map,
position : gmap\_md586cf4556221b6fe12f92c256e6183e.positions[m]
} );
}
// Redraw map to fit our new marker-based bounds
gmap\_md586cf4556221b6fe12f92c256e6183e.map.setCenter( gmap\_md586cf4556221b6fe12f92c256e6183e.positions[743] );
});