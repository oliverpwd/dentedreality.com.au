---
title: Time To Get Going
date: '2008-04-10T16:24:59+00:00'
format: image
service: flickr
tags:
- australia
- kai
- kayaking
- sydney
image: http://i0.wp.com/dentedreality.com.au/wp-content/uploads/2008/04/2437455574_3b634b243b_o.jpg?resize=607%2C455
---

[![Time To Get Going](http://i0.wp.com/dentedreality.com.au/wp-content/uploads/2008/04/2437455574_3b634b243b_o.jpg?resize=607%2C455)](http://dentedreality.com.au/2008/04/10/time-to-get-going/) 
# [Time To Get Going](http://dentedreality.com.au/2008/04/10/time-to-get-going/)

We rented kayaks at Rose Bay and kayaked around the point to get a snack.





* #[australia](http://dentedreality.com.au/tags/australia/)
* #[kai](http://dentedreality.com.au/tags/kai/)
* #[kayaking](http://dentedreality.com.au/tags/kayaking/)
* #[sydney](http://dentedreality.com.au/tags/sydney/)

Posted on [Flickr](http://www.flickr.com/photos/borkazoid/2437455574/) [4:24 pm, April 10, 2008](http://dentedreality.com.au/2008/04/10/time-to-get-going/ "4:24 pm") 
jQuery(document).ready(function(){
var gmap\_m8cd9906370adbf9ea257c703a482104c = {
positions : {
251 : new google.maps.LatLng( '-33.874548', '151.261997' )
},
bounds : new google.maps.LatLngBounds(), // empty for now, we'll dynamically extend it later
map : new google.maps.Map(
document.getElementById( 'gmap\_m8cd9906370adbf9ea257c703a482104c' ),
{
mapTypeId: google.maps.MapTypeId.ROADMAP,
center: new google.maps.LatLng( 0, 0 ),
zoom: 16 // Seems to be a good zoom for a single point
}
),
markers : {},
}; // end of gmap
// Extend the bounds of interest based on our positions
for ( var m in gmap\_m8cd9906370adbf9ea257c703a482104c.positions ) {
gmap\_m8cd9906370adbf9ea257c703a482104c.bounds.extend( gmap\_m8cd9906370adbf9ea257c703a482104c.positions[m] );
}
// Render markers
for ( var m in gmap\_m8cd9906370adbf9ea257c703a482104c.positions ) {
gmap\_m8cd9906370adbf9ea257c703a482104c.markers[m] = new google.maps.Marker( {
clickable: true,
map : gmap\_m8cd9906370adbf9ea257c703a482104c.map,
position : gmap\_m8cd9906370adbf9ea257c703a482104c.positions[m]
} );
}
// Redraw map to fit our new marker-based bounds
gmap\_m8cd9906370adbf9ea257c703a482104c.map.setCenter( gmap\_m8cd9906370adbf9ea257c703a482104c.positions[251] );
});