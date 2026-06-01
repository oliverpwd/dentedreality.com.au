---
title: ''
date: '2020-05-22T07:49:29-06:00'
format: image
service: instagram
tags:
- sentinel
latitude: '39.4934'
longitude: '-105.38177'
image: https://dentedreality-content.s3.amazonaws.com/wp-content/uploads/2020/05/22082454/98096826_265602801476538_1363929869618734173_n.jpg
---

[![Yesterday’s ride was much-needed. #sentinel](https://dentedreality-content.s3.amazonaws.com/wp-content/uploads/2020/05/22082454/98096826_265602801476538_1363929869618734173_n.jpg)](https://dentedreality.com.au/2020/05/22/yesterdays-ride-was-much-needed-sentinel/) 

![Yesterday’s ride was much-needed. #sentinel](https://dentedreality-content.s3.amazonaws.com/wp-content/uploads/2020/05/22082454/98096826_265602801476538_1363929869618734173_n.jpg)

[![Yesterday’s ride was much-needed. #sentinel](https://scontent.cdninstagram.com/v/t51.2885-15/sh0.08/e35/s640x640/98096826_265602801476538_1363929869618734173_n.jpg?_nc_ht=scontent.cdninstagram.com&_nc_ohc=cB_UfY8VwZoAX_DWbTY&oh=03d4d6d2c5355f237d12fcd560f51567&oe=5EF1BB5B)![Yesterday’s ride was much-needed. #sentinel](https://scontent.cdninstagram.com/v/t51.2885-15/sh0.08/e35/s640x640/98096826_265602801476538_1363929869618734173_n.jpg?_nc_ht=scontent.cdninstagram.com&_nc_ohc=cB_UfY8VwZoAX_DWbTY&oh=03d4d6d2c5355f237d12fcd560f51567&oe=5EF1BB5B)](https://www.instagram.com/p/CAfg6FMJm0b/)

Yesterday’s ride was much-needed. #sentinel

39.4934-105.38177




* #[sentinel](https://dentedreality.com.au/tags/sentinel/)

Posted on [Instagram](https://www.instagram.com/p/CAfg6FMJm0b/) [7:49 am, May 22, 2020](https://dentedreality.com.au/2020/05/22/yesterdays-ride-was-much-needed-sentinel/ "7:49 am") 
jQuery(document).ready(function(){
var gmap\_mb634d302d00ef66c1f606e49c35c1bf0 = {
positions : {
664 : new google.maps.LatLng( '39.4934', '-105.38177' )
},
bounds : new google.maps.LatLngBounds(), // empty for now, we'll dynamically extend it later
map : new google.maps.Map(
document.getElementById( 'gmap\_mb634d302d00ef66c1f606e49c35c1bf0' ),
{
mapTypeId: google.maps.MapTypeId.ROADMAP,
center: new google.maps.LatLng( 0, 0 ),
zoom: 16 // Seems to be a good zoom for a single point
}
),
markers : {},
}; // end of gmap
// Extend the bounds of interest based on our positions
for ( var m in gmap\_mb634d302d00ef66c1f606e49c35c1bf0.positions ) {
gmap\_mb634d302d00ef66c1f606e49c35c1bf0.bounds.extend( gmap\_mb634d302d00ef66c1f606e49c35c1bf0.positions[m] );
}
// Render markers
for ( var m in gmap\_mb634d302d00ef66c1f606e49c35c1bf0.positions ) {
gmap\_mb634d302d00ef66c1f606e49c35c1bf0.markers[m] = new google.maps.Marker( {
clickable: true,
map : gmap\_mb634d302d00ef66c1f606e49c35c1bf0.map,
position : gmap\_mb634d302d00ef66c1f606e49c35c1bf0.positions[m]
} );
}
// Redraw map to fit our new marker-based bounds
gmap\_mb634d302d00ef66c1f606e49c35c1bf0.map.setCenter( gmap\_mb634d302d00ef66c1f606e49c35c1bf0.positions[664] );
});