---
title: Grand Meetup 2013
date: '2013-10-03T05:10:22+00:00'
format: image
tags:
- automattic
- grandmeetup
- grandmeetup2013
- meetup
- vision:beach=094
- vision:sunset=054
image: http://i0.wp.com/dentedreality.com.au/wp-content/uploads/2013/10/10076905896_4a78312bff_o.jpg?fit=1500%2C1500
---

[![Grand Meetup 2013](http://i0.wp.com/dentedreality.com.au/wp-content/uploads/2013/10/10076905896_4a78312bff_o.jpg?fit=1500%2C1500)](http://dentedreality.com.au/2013/10/03/grand-meetup-2013-2/) 
# [Grand Meetup 2013](http://dentedreality.com.au/2013/10/03/grand-meetup-2013-2/)

Automattic’s annual full-company, week-long hackapalooza.





* #[automattic](http://dentedreality.com.au/tags/automattic/)
* #[grandmeetup](http://dentedreality.com.au/tags/grandmeetup/)
* #[grandmeetup2013](http://dentedreality.com.au/tags/grandmeetup2013/)
* #[meetup](http://dentedreality.com.au/tags/meetup/)
* #[vision:beach=094](http://dentedreality.com.au/tags/visionbeach094/)
* #[vision:sunset=054](http://dentedreality.com.au/tags/visionsunset054/)

Posted on [Flickr](http://www.flickr.com/photos/borkazoid/10076905896/) [5:10 am, October 3, 2013](http://dentedreality.com.au/2013/10/03/grand-meetup-2013-2/ "5:10 am") 
jQuery(document).ready(function(){
var gmap\_m95f2282bd0c688c3e87805aec658e95e = {
positions : {
448 : new google.maps.LatLng( '36.961333', '-122.026334' )
},
bounds : new google.maps.LatLngBounds(), // empty for now, we'll dynamically extend it later
map : new google.maps.Map(
document.getElementById( 'gmap\_m95f2282bd0c688c3e87805aec658e95e' ),
{
mapTypeId: google.maps.MapTypeId.ROADMAP,
center: new google.maps.LatLng( 0, 0 ),
zoom: 16 // Seems to be a good zoom for a single point
}
),
markers : {},
}; // end of gmap
// Extend the bounds of interest based on our positions
for ( var m in gmap\_m95f2282bd0c688c3e87805aec658e95e.positions ) {
gmap\_m95f2282bd0c688c3e87805aec658e95e.bounds.extend( gmap\_m95f2282bd0c688c3e87805aec658e95e.positions[m] );
}
// Render markers
for ( var m in gmap\_m95f2282bd0c688c3e87805aec658e95e.positions ) {
gmap\_m95f2282bd0c688c3e87805aec658e95e.markers[m] = new google.maps.Marker( {
clickable: true,
map : gmap\_m95f2282bd0c688c3e87805aec658e95e.map,
position : gmap\_m95f2282bd0c688c3e87805aec658e95e.positions[m]
} );
}
// Redraw map to fit our new marker-based bounds
gmap\_m95f2282bd0c688c3e87805aec658e95e.map.setCenter( gmap\_m95f2282bd0c688c3e87805aec658e95e.positions[448] );
});