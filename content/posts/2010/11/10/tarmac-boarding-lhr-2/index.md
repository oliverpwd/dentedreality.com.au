---
title: Tarmac Boarding, LHR
date: '2010-11-10T11:42:48+00:00'
format: image
service: flickr
tags:
- Athens
- automattic
- greece
- teamsocial
image: http://i0.wp.com/dentedreality.com.au/wp-content/uploads/2010/11/5183192485_93c1e31602_o.jpg?resize=607%2C452
---

[![Tarmac Boarding, LHR](http://i0.wp.com/dentedreality.com.au/wp-content/uploads/2010/11/5183192485_93c1e31602_o.jpg?resize=607%2C452)](http://dentedreality.com.au/2010/11/10/tarmac-boarding-lhr-2/) 
# [Tarmac Boarding, LHR](http://dentedreality.com.au/2010/11/10/tarmac-boarding-lhr-2/)





* #[Athens](http://dentedreality.com.au/tags/athens/)
* #[automattic](http://dentedreality.com.au/tags/automattic/)
* #[greece](http://dentedreality.com.au/tags/greece/)
* #[teamsocial](http://dentedreality.com.au/tags/teamsocial/)

Posted on [Flickr](http://www.flickr.com/photos/borkazoid/5183192485/) [11:42 am, November 10, 2010](http://dentedreality.com.au/2010/11/10/tarmac-boarding-lhr-2/ "11:42 am") 
jQuery(document).ready(function(){
var gmap\_m7285e3a5e4ba94f7244641111c34df70 = {
positions : {
826 : new google.maps.LatLng( '51.469666', '-0.475167' )
},
bounds : new google.maps.LatLngBounds(), // empty for now, we'll dynamically extend it later
map : new google.maps.Map(
document.getElementById( 'gmap\_m7285e3a5e4ba94f7244641111c34df70' ),
{
mapTypeId: google.maps.MapTypeId.ROADMAP,
center: new google.maps.LatLng( 0, 0 ),
zoom: 16 // Seems to be a good zoom for a single point
}
),
markers : {},
}; // end of gmap
// Extend the bounds of interest based on our positions
for ( var m in gmap\_m7285e3a5e4ba94f7244641111c34df70.positions ) {
gmap\_m7285e3a5e4ba94f7244641111c34df70.bounds.extend( gmap\_m7285e3a5e4ba94f7244641111c34df70.positions[m] );
}
// Render markers
for ( var m in gmap\_m7285e3a5e4ba94f7244641111c34df70.positions ) {
gmap\_m7285e3a5e4ba94f7244641111c34df70.markers[m] = new google.maps.Marker( {
clickable: true,
map : gmap\_m7285e3a5e4ba94f7244641111c34df70.map,
position : gmap\_m7285e3a5e4ba94f7244641111c34df70.positions[m]
} );
}
// Redraw map to fit our new marker-based bounds
gmap\_m7285e3a5e4ba94f7244641111c34df70.map.setCenter( gmap\_m7285e3a5e4ba94f7244641111c34df70.positions[826] );
});