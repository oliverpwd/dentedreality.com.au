---
title: ''
date: '2019-08-08T17:43:57-06:00'
format: image
service: instagram
latitude: '38.4547'
longitude: '-107.327'
image: https://i0.wp.com/s3.amazonaws.com/dentedreality-content/wp-content/uploads/2019/08/08192456/68821314_673381853073746_6517469055089161987_n.jpg?fit=640%2C640&ssl=1
---

[![Not sponsored, but happy to rave about the @bigagnes_ Copper Spur UL 2. Freaking love this tent; best one I've ever owned.](https://i0.wp.com/s3.amazonaws.com/dentedreality-content/wp-content/uploads/2019/08/08192456/68821314_673381853073746_6517469055089161987_n.jpg?fit=640%2C640&ssl=1)](https://dentedreality.com.au/2019/08/08/not-sponsored-but-happy-to-rave-about-the-bigagnes_-copper-spur-ul-2-freaking-love-this-tent-best-one-ive-ever-owned/) 

[![Not sponsored, but happy to rave about the @bigagnes_ Copper Spur UL 2. Freaking love this tent; best one I've ever owned.](https://i0.wp.com/s3.amazonaws.com/dentedreality-content/wp-content/uploads/2019/08/08192456/68821314_673381853073746_6517469055089161987_n.jpg?fit=640%2C640&ssl=1)](https://www.instagram.com/p/B07AAIVp7bP/)

Not sponsored, but happy to rave about the @bigagnes\_ Copper Spur UL 2. Freaking love this tent; best one I’ve ever owned.

38.4547-107.327




Posted on [Instagram](https://www.instagram.com/p/B07AAIVp7bP/) [5:43 pm, August 8, 2019](https://dentedreality.com.au/2019/08/08/not-sponsored-but-happy-to-rave-about-the-bigagnes_-copper-spur-ul-2-freaking-love-this-tent-best-one-ive-ever-owned/ "5:43 pm") 
jQuery(document).ready(function(){
var gmap\_m9309d5b6c47741d21e9db49c4d553ddb = {
positions : {
444 : new google.maps.LatLng( '38.4547', '-107.327' )
},
bounds : new google.maps.LatLngBounds(), // empty for now, we'll dynamically extend it later
map : new google.maps.Map(
document.getElementById( 'gmap\_m9309d5b6c47741d21e9db49c4d553ddb' ),
{
mapTypeId: google.maps.MapTypeId.ROADMAP,
center: new google.maps.LatLng( 0, 0 ),
zoom: 16 // Seems to be a good zoom for a single point
}
),
markers : {},
}; // end of gmap
// Extend the bounds of interest based on our positions
for ( var m in gmap\_m9309d5b6c47741d21e9db49c4d553ddb.positions ) {
gmap\_m9309d5b6c47741d21e9db49c4d553ddb.bounds.extend( gmap\_m9309d5b6c47741d21e9db49c4d553ddb.positions[m] );
}
// Render markers
for ( var m in gmap\_m9309d5b6c47741d21e9db49c4d553ddb.positions ) {
gmap\_m9309d5b6c47741d21e9db49c4d553ddb.markers[m] = new google.maps.Marker( {
clickable: true,
map : gmap\_m9309d5b6c47741d21e9db49c4d553ddb.map,
position : gmap\_m9309d5b6c47741d21e9db49c4d553ddb.positions[m]
} );
}
// Redraw map to fit our new marker-based bounds
gmap\_m9309d5b6c47741d21e9db49c4d553ddb.map.setCenter( gmap\_m9309d5b6c47741d21e9db49c4d553ddb.positions[444] );
});