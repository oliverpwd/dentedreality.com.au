---
title: Grand Meetup 2013
date: '2013-09-26T16:13:38+00:00'
format: image
tags:
- automattic
- grandmeetup
- grandmeetup2013
- meetup
image: http://i0.wp.com/dentedreality.com.au/wp-content/uploads/2013/09/10076861905_d93385efe7_o.jpg?fit=1500%2C1500
---

[![Grand Meetup 2013](http://i0.wp.com/dentedreality.com.au/wp-content/uploads/2013/09/10076861905_d93385efe7_o.jpg?fit=1500%2C1500)](http://dentedreality.com.au/2013/09/26/grand-meetup-2013-6/) 
# [Grand Meetup 2013](http://dentedreality.com.au/2013/09/26/grand-meetup-2013-6/)

Automattic’s annual full-company, week-long hackapalooza.





* #[automattic](http://dentedreality.com.au/tags/automattic/)
* #[grandmeetup](http://dentedreality.com.au/tags/grandmeetup/)
* #[grandmeetup2013](http://dentedreality.com.au/tags/grandmeetup2013/)
* #[meetup](http://dentedreality.com.au/tags/meetup/)

Posted on [Flickr](http://www.flickr.com/photos/borkazoid/10076861905/) [4:13 pm, September 26, 2013](http://dentedreality.com.au/2013/09/26/grand-meetup-2013-6/ "4:13 pm") 
jQuery(document).ready(function(){
var gmap\_ma9c0c6d59cc26ca3754e683dc38c469a = {
positions : {
88 : new google.maps.LatLng( '37.784333', '-122.397334' )
},
bounds : new google.maps.LatLngBounds(), // empty for now, we'll dynamically extend it later
map : new google.maps.Map(
document.getElementById( 'gmap\_ma9c0c6d59cc26ca3754e683dc38c469a' ),
{
mapTypeId: google.maps.MapTypeId.ROADMAP,
center: new google.maps.LatLng( 0, 0 ),
zoom: 16 // Seems to be a good zoom for a single point
}
),
markers : {},
}; // end of gmap
// Extend the bounds of interest based on our positions
for ( var m in gmap\_ma9c0c6d59cc26ca3754e683dc38c469a.positions ) {
gmap\_ma9c0c6d59cc26ca3754e683dc38c469a.bounds.extend( gmap\_ma9c0c6d59cc26ca3754e683dc38c469a.positions[m] );
}
// Render markers
for ( var m in gmap\_ma9c0c6d59cc26ca3754e683dc38c469a.positions ) {
gmap\_ma9c0c6d59cc26ca3754e683dc38c469a.markers[m] = new google.maps.Marker( {
clickable: true,
map : gmap\_ma9c0c6d59cc26ca3754e683dc38c469a.map,
position : gmap\_ma9c0c6d59cc26ca3754e683dc38c469a.positions[m]
} );
}
// Redraw map to fit our new marker-based bounds
gmap\_ma9c0c6d59cc26ca3754e683dc38c469a.map.setCenter( gmap\_ma9c0c6d59cc26ca3754e683dc38c469a.positions[88] );
});