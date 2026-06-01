---
title: Ye Olde WordPress Pumpkin
date: '2010-10-25T16:13:46+00:00'
format: image
service: flickr
tags:
- hydrant
- instagram
- jackolantern
- pumpkin
- sanfrancisco
- wordpress
image: http://i2.wp.com/dentedreality.com.au/wp-content/uploads/2010/10/5183767606_aae7843e1b_o.jpg?resize=600%2C600
---

[![Ye Olde WordPress Pumpkin](http://i2.wp.com/dentedreality.com.au/wp-content/uploads/2010/10/5183767606_aae7843e1b_o.jpg?resize=600%2C600)](http://dentedreality.com.au/2010/10/25/ye-olde-wordpress-pumpkin/) 
# [Ye Olde WordPress Pumpkin](http://dentedreality.com.au/2010/10/25/ye-olde-wordpress-pumpkin/)

Proudly perched streetside, in San Francisco





* #[hydrant](http://dentedreality.com.au/tags/hydrant/)
* #[instagram](http://dentedreality.com.au/tags/instagram-2/)
* #[jackolantern](http://dentedreality.com.au/tags/jackolantern/)
* #[pumpkin](http://dentedreality.com.au/tags/pumpkin/)
* #[sanfrancisco](http://dentedreality.com.au/tags/sanfrancisco/)
* #[wordpress](http://dentedreality.com.au/tags/wordpress/)

Posted on [Flickr](http://www.flickr.com/photos/borkazoid/5183767606/) [4:13 pm, October 25, 2010](http://dentedreality.com.au/2010/10/25/ye-olde-wordpress-pumpkin/ "4:13 pm") 
jQuery(document).ready(function(){
var gmap\_m029fe7e712195f93b40fbe1819b20d74 = {
positions : {
720 : new google.maps.LatLng( '37.791166', '-122.4175' )
},
bounds : new google.maps.LatLngBounds(), // empty for now, we'll dynamically extend it later
map : new google.maps.Map(
document.getElementById( 'gmap\_m029fe7e712195f93b40fbe1819b20d74' ),
{
mapTypeId: google.maps.MapTypeId.ROADMAP,
center: new google.maps.LatLng( 0, 0 ),
zoom: 16 // Seems to be a good zoom for a single point
}
),
markers : {},
}; // end of gmap
// Extend the bounds of interest based on our positions
for ( var m in gmap\_m029fe7e712195f93b40fbe1819b20d74.positions ) {
gmap\_m029fe7e712195f93b40fbe1819b20d74.bounds.extend( gmap\_m029fe7e712195f93b40fbe1819b20d74.positions[m] );
}
// Render markers
for ( var m in gmap\_m029fe7e712195f93b40fbe1819b20d74.positions ) {
gmap\_m029fe7e712195f93b40fbe1819b20d74.markers[m] = new google.maps.Marker( {
clickable: true,
map : gmap\_m029fe7e712195f93b40fbe1819b20d74.map,
position : gmap\_m029fe7e712195f93b40fbe1819b20d74.positions[m]
} );
}
// Redraw map to fit our new marker-based bounds
gmap\_m029fe7e712195f93b40fbe1819b20d74.map.setCenter( gmap\_m029fe7e712195f93b40fbe1819b20d74.positions[720] );
});