---
title: Standing Desk, With a View
date: '2012-08-25T12:30:17+00:00'
format: image
service: flickr
tags:
- desk
- poster
- standingdesk
- view
- workspace
image: http://i2.wp.com/dentedreality.com.au/wp-content/uploads/2012/08/8245861310_9f6f4ea081_o.jpg?resize=607%2C813
---

[![Standing Desk, With a View](http://i2.wp.com/dentedreality.com.au/wp-content/uploads/2012/08/8245861310_9f6f4ea081_o.jpg?resize=607%2C813)](http://dentedreality.com.au/2012/08/25/standing-desk-with-a-view/) 
# [Standing Desk, With a View](http://dentedreality.com.au/2012/08/25/standing-desk-with-a-view/)





* #[desk](http://dentedreality.com.au/tags/desk/)
* #[poster](http://dentedreality.com.au/tags/poster/)
* #[standingdesk](http://dentedreality.com.au/tags/standingdesk/)
* #[view](http://dentedreality.com.au/tags/view/)
* #[workspace](http://dentedreality.com.au/tags/workspace/)

Posted on [Flickr](http://www.flickr.com/photos/borkazoid/8245861310/) [12:30 pm, August 25, 2012](http://dentedreality.com.au/2012/08/25/standing-desk-with-a-view/ "12:30 pm") 
jQuery(document).ready(function(){
var gmap\_mf456cce98ea1e4b8aa2dca60fb1a06c0 = {
positions : {
582 : new google.maps.LatLng( '40.6695', '-73.985' )
},
bounds : new google.maps.LatLngBounds(), // empty for now, we'll dynamically extend it later
map : new google.maps.Map(
document.getElementById( 'gmap\_mf456cce98ea1e4b8aa2dca60fb1a06c0' ),
{
mapTypeId: google.maps.MapTypeId.ROADMAP,
center: new google.maps.LatLng( 0, 0 ),
zoom: 16 // Seems to be a good zoom for a single point
}
),
markers : {},
}; // end of gmap
// Extend the bounds of interest based on our positions
for ( var m in gmap\_mf456cce98ea1e4b8aa2dca60fb1a06c0.positions ) {
gmap\_mf456cce98ea1e4b8aa2dca60fb1a06c0.bounds.extend( gmap\_mf456cce98ea1e4b8aa2dca60fb1a06c0.positions[m] );
}
// Render markers
for ( var m in gmap\_mf456cce98ea1e4b8aa2dca60fb1a06c0.positions ) {
gmap\_mf456cce98ea1e4b8aa2dca60fb1a06c0.markers[m] = new google.maps.Marker( {
clickable: true,
map : gmap\_mf456cce98ea1e4b8aa2dca60fb1a06c0.map,
position : gmap\_mf456cce98ea1e4b8aa2dca60fb1a06c0.positions[m]
} );
}
// Redraw map to fit our new marker-based bounds
gmap\_mf456cce98ea1e4b8aa2dca60fb1a06c0.map.setCenter( gmap\_mf456cce98ea1e4b8aa2dca60fb1a06c0.positions[582] );
});