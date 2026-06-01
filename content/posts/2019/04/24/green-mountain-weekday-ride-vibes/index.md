---
title: ''
date: '2019-04-24T19:53:45-06:00'
format: image
service: instagram
latitude: '39.7008'
longitude: '-105.178'
image: https://i1.wp.com/s3.amazonaws.com/dentedreality-content/wp-content/uploads/2019/04/24202505/56716436_432718327287660_917534547218324475_n.jpg?fit=640%2C640&ssl=1
---

[![Green Mountain Weekday Ride Vibes](https://i1.wp.com/s3.amazonaws.com/dentedreality-content/wp-content/uploads/2019/04/24202505/56716436_432718327287660_917534547218324475_n.jpg?fit=640%2C640&ssl=1)](https://dentedreality.com.au/2019/04/24/green-mountain-weekday-ride-vibes/) 

[![Green Mountain Weekday Ride Vibes](https://i1.wp.com/s3.amazonaws.com/dentedreality-content/wp-content/uploads/2019/04/24202505/56716436_432718327287660_917534547218324475_n.jpg?fit=640%2C640&ssl=1)](https://www.instagram.com/p/BwqSmCfpn84/)

Green Mountain Weekday Ride Vibes

39.7008-105.178




Posted on [Instagram](https://www.instagram.com/p/BwqSmCfpn84/) [7:53 pm, April 24, 2019](https://dentedreality.com.au/2019/04/24/green-mountain-weekday-ride-vibes/ "7:53 pm") 
jQuery(document).ready(function(){
var gmap\_m96a65feb5008399ffc9a02509513bd1b = {
positions : {
915 : new google.maps.LatLng( '39.7008', '-105.178' )
},
bounds : new google.maps.LatLngBounds(), // empty for now, we'll dynamically extend it later
map : new google.maps.Map(
document.getElementById( 'gmap\_m96a65feb5008399ffc9a02509513bd1b' ),
{
mapTypeId: google.maps.MapTypeId.ROADMAP,
center: new google.maps.LatLng( 0, 0 ),
zoom: 16 // Seems to be a good zoom for a single point
}
),
markers : {},
}; // end of gmap
// Extend the bounds of interest based on our positions
for ( var m in gmap\_m96a65feb5008399ffc9a02509513bd1b.positions ) {
gmap\_m96a65feb5008399ffc9a02509513bd1b.bounds.extend( gmap\_m96a65feb5008399ffc9a02509513bd1b.positions[m] );
}
// Render markers
for ( var m in gmap\_m96a65feb5008399ffc9a02509513bd1b.positions ) {
gmap\_m96a65feb5008399ffc9a02509513bd1b.markers[m] = new google.maps.Marker( {
clickable: true,
map : gmap\_m96a65feb5008399ffc9a02509513bd1b.map,
position : gmap\_m96a65feb5008399ffc9a02509513bd1b.positions[m]
} );
}
// Redraw map to fit our new marker-based bounds
gmap\_m96a65feb5008399ffc9a02509513bd1b.map.setCenter( gmap\_m96a65feb5008399ffc9a02509513bd1b.positions[915] );
});