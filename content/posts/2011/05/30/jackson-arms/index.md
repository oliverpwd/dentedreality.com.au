---
title: Jackson Arms
date: '2011-05-30T09:12:25+00:00'
format: image
service: flickr
tags:
- jacksonarms
- lisa
- memorialday
- pocketlisa
- shooting
image: http://i1.wp.com/dentedreality.com.au/wp-content/uploads/2011/05/5802879043_1d0a872079_o.jpg?resize=607%2C813
---

[![Jackson Arms](http://i1.wp.com/dentedreality.com.au/wp-content/uploads/2011/05/5802879043_1d0a872079_o.jpg?resize=607%2C813)](http://dentedreality.com.au/2011/05/30/jackson-arms/) 
# [Jackson Arms](http://dentedreality.com.au/2011/05/30/jackson-arms/)

Memorial Day at the range





* #[jacksonarms](http://dentedreality.com.au/tags/jacksonarms/)
* #[lisa](http://dentedreality.com.au/tags/lisa/)
* #[memorialday](http://dentedreality.com.au/tags/memorialday/)
* #[pocketlisa](http://dentedreality.com.au/tags/pocketlisa/)
* #[shooting](http://dentedreality.com.au/tags/shooting/)

Posted on [Flickr](http://www.flickr.com/photos/borkazoid/5802879043/) [9:12 am, May 30, 2011](http://dentedreality.com.au/2011/05/30/jackson-arms/ "9:12 am") 
jQuery(document).ready(function(){
var gmap\_mbd8eddae20ae37f55b7cd24b21e0c9e4 = {
positions : {
515 : new google.maps.LatLng( '37.645166', '-122.4025' )
},
bounds : new google.maps.LatLngBounds(), // empty for now, we'll dynamically extend it later
map : new google.maps.Map(
document.getElementById( 'gmap\_mbd8eddae20ae37f55b7cd24b21e0c9e4' ),
{
mapTypeId: google.maps.MapTypeId.ROADMAP,
center: new google.maps.LatLng( 0, 0 ),
zoom: 16 // Seems to be a good zoom for a single point
}
),
markers : {},
}; // end of gmap
// Extend the bounds of interest based on our positions
for ( var m in gmap\_mbd8eddae20ae37f55b7cd24b21e0c9e4.positions ) {
gmap\_mbd8eddae20ae37f55b7cd24b21e0c9e4.bounds.extend( gmap\_mbd8eddae20ae37f55b7cd24b21e0c9e4.positions[m] );
}
// Render markers
for ( var m in gmap\_mbd8eddae20ae37f55b7cd24b21e0c9e4.positions ) {
gmap\_mbd8eddae20ae37f55b7cd24b21e0c9e4.markers[m] = new google.maps.Marker( {
clickable: true,
map : gmap\_mbd8eddae20ae37f55b7cd24b21e0c9e4.map,
position : gmap\_mbd8eddae20ae37f55b7cd24b21e0c9e4.positions[m]
} );
}
// Redraw map to fit our new marker-based bounds
gmap\_mbd8eddae20ae37f55b7cd24b21e0c9e4.map.setCenter( gmap\_mbd8eddae20ae37f55b7cd24b21e0c9e4.positions[515] );
});