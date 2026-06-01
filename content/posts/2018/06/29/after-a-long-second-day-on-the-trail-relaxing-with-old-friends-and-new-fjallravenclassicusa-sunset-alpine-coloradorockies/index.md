---
title: ''
date: '2018-06-29T22:35:50-06:00'
format: image
service: instagram
tags:
- alpine
- coloradorockies
- fjallravenclassicusa
- sunset
latitude: '39.464029'
longitude: '-106.2302171'
image: https://i1.wp.com/s3.amazonaws.com/dentedreality-content/wp-content/uploads/2018/06/14182136/35617423_391136544719867_1259466260102512640_n.jpg?resize=607%2C607&ssl=1
---

[![After a long second day on the trail; relaxing with old friends and new. #fjallravenclassicusa #sunset #alpine #coloradorockies](https://i1.wp.com/s3.amazonaws.com/dentedreality-content/wp-content/uploads/2018/06/14182136/35617423_391136544719867_1259466260102512640_n.jpg?resize=607%2C607&ssl=1)](https://dentedreality.com.au/2018/06/29/after-a-long-second-day-on-the-trail-relaxing-with-old-friends-and-new-fjallravenclassicusa-sunset-alpine-coloradorockies/) 

[![After a long second day on the trail; relaxing with old friends and new. #fjallravenclassicusa #sunset #alpine #coloradorockies](https://i1.wp.com/s3.amazonaws.com/dentedreality-content/wp-content/uploads/2018/06/14182136/35617423_391136544719867_1259466260102512640_n.jpg?resize=607%2C607&ssl=1)](https://www.instagram.com/p/BkordmWFFjl/)

After a long second day on the trail; relaxing with old friends and new. #fjallravenclassicusa #sunset #alpine #coloradorockies

39.464029-106.2302171




* #[alpine](https://dentedreality.com.au/tags/alpine/)
* #[coloradorockies](https://dentedreality.com.au/tags/coloradorockies/)
* #[fjallravenclassicusa](https://dentedreality.com.au/tags/fjallravenclassicusa/)
* #[sunset](https://dentedreality.com.au/tags/sunset/)

Posted on [Instagram](https://www.instagram.com/p/BkordmWFFjl/) [10:35 pm, June 29, 2018](https://dentedreality.com.au/2018/06/29/after-a-long-second-day-on-the-trail-relaxing-with-old-friends-and-new-fjallravenclassicusa-sunset-alpine-coloradorockies/ "10:35 pm") 
jQuery(document).ready(function(){
var gmap\_mec77cb90ea8c3b368959f294c42984c9 = {
positions : {
238 : new google.maps.LatLng( '39.464029042068', '-106.23021707212' )
},
bounds : new google.maps.LatLngBounds(), // empty for now, we'll dynamically extend it later
map : new google.maps.Map(
document.getElementById( 'gmap\_mec77cb90ea8c3b368959f294c42984c9' ),
{
mapTypeId: google.maps.MapTypeId.ROADMAP,
center: new google.maps.LatLng( 0, 0 ),
zoom: 16 // Seems to be a good zoom for a single point
}
),
markers : {},
}; // end of gmap
// Extend the bounds of interest based on our positions
for ( var m in gmap\_mec77cb90ea8c3b368959f294c42984c9.positions ) {
gmap\_mec77cb90ea8c3b368959f294c42984c9.bounds.extend( gmap\_mec77cb90ea8c3b368959f294c42984c9.positions[m] );
}
// Render markers
for ( var m in gmap\_mec77cb90ea8c3b368959f294c42984c9.positions ) {
gmap\_mec77cb90ea8c3b368959f294c42984c9.markers[m] = new google.maps.Marker( {
clickable: true,
map : gmap\_mec77cb90ea8c3b368959f294c42984c9.map,
position : gmap\_mec77cb90ea8c3b368959f294c42984c9.positions[m]
} );
}
// Redraw map to fit our new marker-based bounds
gmap\_mec77cb90ea8c3b368959f294c42984c9.map.setCenter( gmap\_mec77cb90ea8c3b368959f294c42984c9.positions[238] );
});