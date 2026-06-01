---
title: Grand Meetup 2013
date: '2013-09-25T09:54:37+00:00'
format: image
tags:
- automattic
- grandmeetup
- grandmeetup2013
- meetup
- vision:beach=071
- vision:mountain=062
image: http://i1.wp.com/dentedreality.com.au/wp-content/uploads/2013/09/10076837325_783b5f739b_o.jpg?fit=1500%2C1500
---

[![Grand Meetup 2013](http://i1.wp.com/dentedreality.com.au/wp-content/uploads/2013/09/10076837325_783b5f739b_o.jpg?fit=1500%2C1500)](http://dentedreality.com.au/2013/09/25/grand-meetup-2013/) 
# [Grand Meetup 2013](http://dentedreality.com.au/2013/09/25/grand-meetup-2013/)

Automattic’s annual full-company, week-long hackapalooza.





* #[automattic](http://dentedreality.com.au/tags/automattic/)
* #[grandmeetup](http://dentedreality.com.au/tags/grandmeetup/)
* #[grandmeetup2013](http://dentedreality.com.au/tags/grandmeetup2013/)
* #[meetup](http://dentedreality.com.au/tags/meetup/)
* #[vision:beach=071](http://dentedreality.com.au/tags/visionbeach071/)
* #[vision:mountain=062](http://dentedreality.com.au/tags/visionmountain062/)

Posted on [Flickr](http://www.flickr.com/photos/borkazoid/10076837325/) [9:54 am, September 25, 2013](http://dentedreality.com.au/2013/09/25/grand-meetup-2013/ "9:54 am") 
jQuery(document).ready(function(){
var gmap\_m9a2770ba684abb04845c3301d34519bc = {
positions : {
141 : new google.maps.LatLng( '38.154833', '-122.452334' )
},
bounds : new google.maps.LatLngBounds(), // empty for now, we'll dynamically extend it later
map : new google.maps.Map(
document.getElementById( 'gmap\_m9a2770ba684abb04845c3301d34519bc' ),
{
mapTypeId: google.maps.MapTypeId.ROADMAP,
center: new google.maps.LatLng( 0, 0 ),
zoom: 16 // Seems to be a good zoom for a single point
}
),
markers : {},
}; // end of gmap
// Extend the bounds of interest based on our positions
for ( var m in gmap\_m9a2770ba684abb04845c3301d34519bc.positions ) {
gmap\_m9a2770ba684abb04845c3301d34519bc.bounds.extend( gmap\_m9a2770ba684abb04845c3301d34519bc.positions[m] );
}
// Render markers
for ( var m in gmap\_m9a2770ba684abb04845c3301d34519bc.positions ) {
gmap\_m9a2770ba684abb04845c3301d34519bc.markers[m] = new google.maps.Marker( {
clickable: true,
map : gmap\_m9a2770ba684abb04845c3301d34519bc.map,
position : gmap\_m9a2770ba684abb04845c3301d34519bc.positions[m]
} );
}
// Redraw map to fit our new marker-based bounds
gmap\_m9a2770ba684abb04845c3301d34519bc.map.setCenter( gmap\_m9a2770ba684abb04845c3301d34519bc.positions[141] );
});