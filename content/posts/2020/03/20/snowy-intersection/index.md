---
title: ''
date: '2020-03-20T19:02:58-06:00'
format: image
service: instagram
latitude: '39.7391'
longitude: '-104.9836'
image: https://dentedreality-content.s3.amazonaws.com/wp-content/uploads/2020/03/20192455/90090293_2855281537871868_76507884343263029_n.jpg
---

[![Snowy Intersection](https://dentedreality-content.s3.amazonaws.com/wp-content/uploads/2020/03/20192455/90090293_2855281537871868_76507884343263029_n.jpg)](https://dentedreality.com.au/2020/03/20/snowy-intersection/) 

![Snowy Intersection](https://dentedreality-content.s3.amazonaws.com/wp-content/uploads/2020/03/20192455/90090293_2855281537871868_76507884343263029_n.jpg)

[![Snowy Intersection](https://scontent.cdninstagram.com/v/t51.2885-15/sh0.08/e35/s640x640/90090293_2855281537871868_76507884343263029_n.jpg?_nc_ht=scontent.cdninstagram.com&_nc_ohc=m8cfnRIa8mcAX_xGmud&oh=11b59cddabd69fc01960971be4592096&oe=5EA10BC3)![Snowy Intersection](https://scontent.cdninstagram.com/v/t51.2885-15/sh0.08/e35/s640x640/90090293_2855281537871868_76507884343263029_n.jpg?_nc_ht=scontent.cdninstagram.com&_nc_ohc=m8cfnRIa8mcAX_xGmud&oh=11b59cddabd69fc01960971be4592096&oe=5EA10BC3)](https://www.instagram.com/p/B9-f5wbpOoM/)

Snowy Intersection

39.7391-104.9836




Posted on [Instagram](https://www.instagram.com/p/B9-f5wbpOoM/) [7:02 pm, March 20, 2020](https://dentedreality.com.au/2020/03/20/snowy-intersection/ "7:02 pm") 
jQuery(document).ready(function(){
var gmap\_m0d32f446a417e1da543523f0c9453249 = {
positions : {
750 : new google.maps.LatLng( '39.7391', '-104.9836' )
},
bounds : new google.maps.LatLngBounds(), // empty for now, we'll dynamically extend it later
map : new google.maps.Map(
document.getElementById( 'gmap\_m0d32f446a417e1da543523f0c9453249' ),
{
mapTypeId: google.maps.MapTypeId.ROADMAP,
center: new google.maps.LatLng( 0, 0 ),
zoom: 16 // Seems to be a good zoom for a single point
}
),
markers : {},
}; // end of gmap
// Extend the bounds of interest based on our positions
for ( var m in gmap\_m0d32f446a417e1da543523f0c9453249.positions ) {
gmap\_m0d32f446a417e1da543523f0c9453249.bounds.extend( gmap\_m0d32f446a417e1da543523f0c9453249.positions[m] );
}
// Render markers
for ( var m in gmap\_m0d32f446a417e1da543523f0c9453249.positions ) {
gmap\_m0d32f446a417e1da543523f0c9453249.markers[m] = new google.maps.Marker( {
clickable: true,
map : gmap\_m0d32f446a417e1da543523f0c9453249.map,
position : gmap\_m0d32f446a417e1da543523f0c9453249.positions[m]
} );
}
// Redraw map to fit our new marker-based bounds
gmap\_m0d32f446a417e1da543523f0c9453249.map.setCenter( gmap\_m0d32f446a417e1da543523f0c9453249.positions[750] );
});