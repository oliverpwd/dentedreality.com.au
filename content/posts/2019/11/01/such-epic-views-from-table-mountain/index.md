---
title: ''
date: '2019-11-01T16:26:33-06:00'
format: image
service: instagram
latitude: '-33.9575073'
longitude: '18.4030829'
image: https://s3.amazonaws.com/dentedreality-content/wp-content/uploads/2019/11/01172456/72583298_2612370262139937_7425259011971878982_n.jpg
---

[![Such epic views from Table Mountain!!](https://s3.amazonaws.com/dentedreality-content/wp-content/uploads/2019/11/01172456/72583298_2612370262139937_7425259011971878982_n.jpg)](https://dentedreality.com.au/2019/11/01/such-epic-views-from-table-mountain/) 

[![Such epic views from Table Mountain!!](https://s3.amazonaws.com/dentedreality-content/wp-content/uploads/2019/11/01172456/72583298_2612370262139937_7425259011971878982_n.jpg)](https://www.instagram.com/p/B4VutmQpr6z/)

Such epic views from Table Mountain!!

-33.957507318.4030829




Posted on [Instagram](https://www.instagram.com/p/B4VutmQpr6z/) [4:26 pm, November 1, 2019](https://dentedreality.com.au/2019/11/01/such-epic-views-from-table-mountain/ "4:26 pm") 
jQuery(document).ready(function(){
var gmap\_md6c5f1ffc8c9223d0af2a476ecda4cbd = {
positions : {
268 : new google.maps.LatLng( '-33.9575073', '18.4030829' )
},
bounds : new google.maps.LatLngBounds(), // empty for now, we'll dynamically extend it later
map : new google.maps.Map(
document.getElementById( 'gmap\_md6c5f1ffc8c9223d0af2a476ecda4cbd' ),
{
mapTypeId: google.maps.MapTypeId.ROADMAP,
center: new google.maps.LatLng( 0, 0 ),
zoom: 16 // Seems to be a good zoom for a single point
}
),
markers : {},
}; // end of gmap
// Extend the bounds of interest based on our positions
for ( var m in gmap\_md6c5f1ffc8c9223d0af2a476ecda4cbd.positions ) {
gmap\_md6c5f1ffc8c9223d0af2a476ecda4cbd.bounds.extend( gmap\_md6c5f1ffc8c9223d0af2a476ecda4cbd.positions[m] );
}
// Render markers
for ( var m in gmap\_md6c5f1ffc8c9223d0af2a476ecda4cbd.positions ) {
gmap\_md6c5f1ffc8c9223d0af2a476ecda4cbd.markers[m] = new google.maps.Marker( {
clickable: true,
map : gmap\_md6c5f1ffc8c9223d0af2a476ecda4cbd.map,
position : gmap\_md6c5f1ffc8c9223d0af2a476ecda4cbd.positions[m]
} );
}
// Redraw map to fit our new marker-based bounds
gmap\_md6c5f1ffc8c9223d0af2a476ecda4cbd.map.setCenter( gmap\_md6c5f1ffc8c9223d0af2a476ecda4cbd.positions[268] );
});