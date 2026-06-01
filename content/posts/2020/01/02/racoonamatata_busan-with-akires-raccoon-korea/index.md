---
title: ''
date: '2020-01-02T04:02:02-07:00'
format: image
service: instagram
tags:
- korea
- raccoon
latitude: '35.1360178'
longitude: '129.1001975'
image: https://s3.amazonaws.com/dentedreality-content/wp-content/uploads/2020/01/02042501/80723173_171714634194052_6786452206266349512_n.jpg
---

[![@racoonamatata_busan with @akires #raccoon #korea](https://s3.amazonaws.com/dentedreality-content/wp-content/uploads/2020/01/02042501/80723173_171714634194052_6786452206266349512_n.jpg)](https://dentedreality.com.au/2020/01/02/racoonamatata_busan-with-akires-raccoon-korea/) 

![@racoonamatata_busan with @akires #raccoon #korea](https://s3.amazonaws.com/dentedreality-content/wp-content/uploads/2020/01/02042501/80723173_171714634194052_6786452206266349512_n.jpg)

[![@racoonamatata_busan with @akires #raccoon #korea](https://scontent.cdninstagram.com/v/t51.2885-15/sh0.08/e35/s640x640/80723173_171714634194052_6786452206266349512_n.jpg?_nc_ht=scontent.cdninstagram.com&_nc_ohc=28ePGR7e_YgAX-6caur&oh=99cc5f0cf87afa00cc1b8f23e0d25233&oe=5EAB0317)![@racoonamatata_busan with @akires #raccoon #korea](https://scontent.cdninstagram.com/v/t51.2885-15/sh0.08/e35/s640x640/80723173_171714634194052_6786452206266349512_n.jpg?_nc_ht=scontent.cdninstagram.com&_nc_ohc=28ePGR7e_YgAX-6caur&oh=99cc5f0cf87afa00cc1b8f23e0d25233&oe=5EAB0317)](https://www.instagram.com/p/B60JqRCpup5/)

@racoonamatata\_busan with @akires #raccoon #korea

35.1360178129.1001975




* #[korea](https://dentedreality.com.au/tags/korea/)
* #[raccoon](https://dentedreality.com.au/tags/raccoon/)

Posted on [Instagram](https://www.instagram.com/p/B60JqRCpup5/) [4:02 am, January 2, 2020](https://dentedreality.com.au/2020/01/02/racoonamatata_busan-with-akires-raccoon-korea/ "4:02 am") 
jQuery(document).ready(function(){
var gmap\_m3e25bbc9b29ffc2b852f2c884378b36f = {
positions : {
316 : new google.maps.LatLng( '35.1360178', '129.1001975' )
},
bounds : new google.maps.LatLngBounds(), // empty for now, we'll dynamically extend it later
map : new google.maps.Map(
document.getElementById( 'gmap\_m3e25bbc9b29ffc2b852f2c884378b36f' ),
{
mapTypeId: google.maps.MapTypeId.ROADMAP,
center: new google.maps.LatLng( 0, 0 ),
zoom: 16 // Seems to be a good zoom for a single point
}
),
markers : {},
}; // end of gmap
// Extend the bounds of interest based on our positions
for ( var m in gmap\_m3e25bbc9b29ffc2b852f2c884378b36f.positions ) {
gmap\_m3e25bbc9b29ffc2b852f2c884378b36f.bounds.extend( gmap\_m3e25bbc9b29ffc2b852f2c884378b36f.positions[m] );
}
// Render markers
for ( var m in gmap\_m3e25bbc9b29ffc2b852f2c884378b36f.positions ) {
gmap\_m3e25bbc9b29ffc2b852f2c884378b36f.markers[m] = new google.maps.Marker( {
clickable: true,
map : gmap\_m3e25bbc9b29ffc2b852f2c884378b36f.map,
position : gmap\_m3e25bbc9b29ffc2b852f2c884378b36f.positions[m]
} );
}
// Redraw map to fit our new marker-based bounds
gmap\_m3e25bbc9b29ffc2b852f2c884378b36f.map.setCenter( gmap\_m3e25bbc9b29ffc2b852f2c884378b36f.positions[316] );
});