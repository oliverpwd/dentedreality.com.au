---
title: jQuery Conf, Portland
date: '2013-06-12T09:28:03+00:00'
format: image
service: flickr
tags:
- conference
- javascript
- jquery
- PDX
- Portland
image: http://i2.wp.com/dentedreality.com.au/wp-content/uploads/2013/06/9439832374_3f6e456a0c_o.jpg?resize=607%2C813
---

[![jQuery Conf, Portland](http://i2.wp.com/dentedreality.com.au/wp-content/uploads/2013/06/9439832374_3f6e456a0c_o.jpg?resize=607%2C813)](http://dentedreality.com.au/2013/06/12/jquery-conf-portland-3/) 
# [jQuery Conf, Portland](http://dentedreality.com.au/2013/06/12/jquery-conf-portland-3/)





* #[conference](http://dentedreality.com.au/tags/conference/)
* #[javascript](http://dentedreality.com.au/tags/javascript/)
* #[jquery](http://dentedreality.com.au/tags/jquery/)
* #[PDX](http://dentedreality.com.au/tags/pdx/)
* #[Portland](http://dentedreality.com.au/tags/portland/)

Posted on [Flickr](http://www.flickr.com/photos/borkazoid/9439832374/) [9:28 am, June 12, 2013](http://dentedreality.com.au/2013/06/12/jquery-conf-portland-3/ "9:28 am") 
jQuery(document).ready(function(){
var gmap\_m67f08cbcb2ca93b339401844b19da03f = {
positions : {
890 : new google.maps.LatLng( '45.5275', '-122.662334' )
},
bounds : new google.maps.LatLngBounds(), // empty for now, we'll dynamically extend it later
map : new google.maps.Map(
document.getElementById( 'gmap\_m67f08cbcb2ca93b339401844b19da03f' ),
{
mapTypeId: google.maps.MapTypeId.ROADMAP,
center: new google.maps.LatLng( 0, 0 ),
zoom: 16 // Seems to be a good zoom for a single point
}
),
markers : {},
}; // end of gmap
// Extend the bounds of interest based on our positions
for ( var m in gmap\_m67f08cbcb2ca93b339401844b19da03f.positions ) {
gmap\_m67f08cbcb2ca93b339401844b19da03f.bounds.extend( gmap\_m67f08cbcb2ca93b339401844b19da03f.positions[m] );
}
// Render markers
for ( var m in gmap\_m67f08cbcb2ca93b339401844b19da03f.positions ) {
gmap\_m67f08cbcb2ca93b339401844b19da03f.markers[m] = new google.maps.Marker( {
clickable: true,
map : gmap\_m67f08cbcb2ca93b339401844b19da03f.map,
position : gmap\_m67f08cbcb2ca93b339401844b19da03f.positions[m]
} );
}
// Redraw map to fit our new marker-based bounds
gmap\_m67f08cbcb2ca93b339401844b19da03f.map.setCenter( gmap\_m67f08cbcb2ca93b339401844b19da03f.positions[890] );
});