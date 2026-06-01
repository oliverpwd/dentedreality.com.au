---
title: Grand Meetup 2013
date: '2013-09-26T08:32:53+00:00'
format: image
tags:
- automattic
- grandmeetup
- grandmeetup2013
- meetup
image: http://i0.wp.com/dentedreality.com.au/wp-content/uploads/2013/09/10076861535_ec61d9e1ba_o.jpg?fit=1500%2C1500
---

[![Grand Meetup 2013](http://i0.wp.com/dentedreality.com.au/wp-content/uploads/2013/09/10076861535_ec61d9e1ba_o.jpg?fit=1500%2C1500)](http://dentedreality.com.au/2013/09/26/grand-meetup-2013-7/) 
# [Grand Meetup 2013](http://dentedreality.com.au/2013/09/26/grand-meetup-2013-7/)

Automattic’s annual full-company, week-long hackapalooza.





* #[automattic](http://dentedreality.com.au/tags/automattic/)
* #[grandmeetup](http://dentedreality.com.au/tags/grandmeetup/)
* #[grandmeetup2013](http://dentedreality.com.au/tags/grandmeetup2013/)
* #[meetup](http://dentedreality.com.au/tags/meetup/)

Posted on [Flickr](http://www.flickr.com/photos/borkazoid/10076861535/) [8:32 am, September 26, 2013](http://dentedreality.com.au/2013/09/26/grand-meetup-2013-7/ "8:32 am") 
jQuery(document).ready(function(){
var gmap\_mae2d6cdad08c2f138ccb4d4cd97ddbd5 = {
positions : {
548 : new google.maps.LatLng( '37.784', '-122.397334' )
},
bounds : new google.maps.LatLngBounds(), // empty for now, we'll dynamically extend it later
map : new google.maps.Map(
document.getElementById( 'gmap\_mae2d6cdad08c2f138ccb4d4cd97ddbd5' ),
{
mapTypeId: google.maps.MapTypeId.ROADMAP,
center: new google.maps.LatLng( 0, 0 ),
zoom: 16 // Seems to be a good zoom for a single point
}
),
markers : {},
}; // end of gmap
// Extend the bounds of interest based on our positions
for ( var m in gmap\_mae2d6cdad08c2f138ccb4d4cd97ddbd5.positions ) {
gmap\_mae2d6cdad08c2f138ccb4d4cd97ddbd5.bounds.extend( gmap\_mae2d6cdad08c2f138ccb4d4cd97ddbd5.positions[m] );
}
// Render markers
for ( var m in gmap\_mae2d6cdad08c2f138ccb4d4cd97ddbd5.positions ) {
gmap\_mae2d6cdad08c2f138ccb4d4cd97ddbd5.markers[m] = new google.maps.Marker( {
clickable: true,
map : gmap\_mae2d6cdad08c2f138ccb4d4cd97ddbd5.map,
position : gmap\_mae2d6cdad08c2f138ccb4d4cd97ddbd5.positions[m]
} );
}
// Redraw map to fit our new marker-based bounds
gmap\_mae2d6cdad08c2f138ccb4d4cd97ddbd5.map.setCenter( gmap\_mae2d6cdad08c2f138ccb4d4cd97ddbd5.positions[548] );
});