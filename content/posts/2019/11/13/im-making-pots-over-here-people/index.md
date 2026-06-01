---
title: ''
date: '2019-11-13T21:47:49-07:00'
format: image
service: instagram
latitude: '39.70949'
longitude: '-105.002'
image: https://s3.amazonaws.com/dentedreality-content/wp-content/uploads/2019/11/13222456/72099784_578217759386541_1288469216795280815_n.jpg
---

[![I'm making pots over here people.](https://s3.amazonaws.com/dentedreality-content/wp-content/uploads/2019/11/13222456/72099784_578217759386541_1288469216795280815_n.jpg)](https://dentedreality.com.au/2019/11/13/im-making-pots-over-here-people/) 

[![I'm making pots over here people.](https://s3.amazonaws.com/dentedreality-content/wp-content/uploads/2019/11/13222456/72099784_578217759386541_1288469216795280815_n.jpg)](https://www.instagram.com/p/B41T4p4Jt9w/)

I’m making pots over here people.

39.70949-105.002




Posted on [Instagram](https://www.instagram.com/p/B41T4p4Jt9w/) [9:47 pm, November 13, 2019](https://dentedreality.com.au/2019/11/13/im-making-pots-over-here-people/ "9:47 pm") 
jQuery(document).ready(function(){
var gmap\_me806612be5546463d6063ee4a54ca248 = {
positions : {
371 : new google.maps.LatLng( '39.70949', '-105.002' )
},
bounds : new google.maps.LatLngBounds(), // empty for now, we'll dynamically extend it later
map : new google.maps.Map(
document.getElementById( 'gmap\_me806612be5546463d6063ee4a54ca248' ),
{
mapTypeId: google.maps.MapTypeId.ROADMAP,
center: new google.maps.LatLng( 0, 0 ),
zoom: 16 // Seems to be a good zoom for a single point
}
),
markers : {},
}; // end of gmap
// Extend the bounds of interest based on our positions
for ( var m in gmap\_me806612be5546463d6063ee4a54ca248.positions ) {
gmap\_me806612be5546463d6063ee4a54ca248.bounds.extend( gmap\_me806612be5546463d6063ee4a54ca248.positions[m] );
}
// Render markers
for ( var m in gmap\_me806612be5546463d6063ee4a54ca248.positions ) {
gmap\_me806612be5546463d6063ee4a54ca248.markers[m] = new google.maps.Marker( {
clickable: true,
map : gmap\_me806612be5546463d6063ee4a54ca248.map,
position : gmap\_me806612be5546463d6063ee4a54ca248.positions[m]
} );
}
// Redraw map to fit our new marker-based bounds
gmap\_me806612be5546463d6063ee4a54ca248.map.setCenter( gmap\_me806612be5546463d6063ee4a54ca248.positions[371] );
});