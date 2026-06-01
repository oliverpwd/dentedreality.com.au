---
title: Grand Meetup 2013
date: '2013-09-27T10:08:15+00:00'
format: image
tags:
- automattic
- beau
- beaulebens
- grandmeetup
- grandmeetup2013
- me
- meetup
- vision:face=099
- vision:groupshot=099
- vision:people=099
- vision:text=061
image: http://i0.wp.com/dentedreality.com.au/wp-content/uploads/2013/09/10076863595_a2e783feae_o.jpg?fit=1500%2C1500
---

[![Grand Meetup 2013](http://i0.wp.com/dentedreality.com.au/wp-content/uploads/2013/09/10076863595_a2e783feae_o.jpg?fit=1500%2C1500)](http://dentedreality.com.au/2013/09/27/grand-meetup-2013-4/) 
# [Grand Meetup 2013](http://dentedreality.com.au/2013/09/27/grand-meetup-2013-4/)

My 2 mentees, Jeff and Chase.





* #[automattic](http://dentedreality.com.au/tags/automattic/)
* #[beau](http://dentedreality.com.au/tags/beau/)
* #[beaulebens](http://dentedreality.com.au/tags/beaulebens/)
* #[grandmeetup](http://dentedreality.com.au/tags/grandmeetup/)
* #[grandmeetup2013](http://dentedreality.com.au/tags/grandmeetup2013/)
* #[me](http://dentedreality.com.au/tags/me/)
* #[meetup](http://dentedreality.com.au/tags/meetup/)
* #[vision:face=099](http://dentedreality.com.au/tags/visionface099/)
* #[vision:groupshot=099](http://dentedreality.com.au/tags/visiongroupshot099/)
* #[vision:people=099](http://dentedreality.com.au/tags/visionpeople099/)
* #[vision:text=061](http://dentedreality.com.au/tags/visiontext061/)

Posted on [Flickr](http://www.flickr.com/photos/borkazoid/10076863595/) [10:08 am, September 27, 2013](http://dentedreality.com.au/2013/09/27/grand-meetup-2013-4/ "10:08 am") 
jQuery(document).ready(function(){
var gmap\_m70e4fb6e37a64443876678c05b8bb848 = {
positions : {
636 : new google.maps.LatLng( '37.784333', '-122.397501' )
},
bounds : new google.maps.LatLngBounds(), // empty for now, we'll dynamically extend it later
map : new google.maps.Map(
document.getElementById( 'gmap\_m70e4fb6e37a64443876678c05b8bb848' ),
{
mapTypeId: google.maps.MapTypeId.ROADMAP,
center: new google.maps.LatLng( 0, 0 ),
zoom: 16 // Seems to be a good zoom for a single point
}
),
markers : {},
}; // end of gmap
// Extend the bounds of interest based on our positions
for ( var m in gmap\_m70e4fb6e37a64443876678c05b8bb848.positions ) {
gmap\_m70e4fb6e37a64443876678c05b8bb848.bounds.extend( gmap\_m70e4fb6e37a64443876678c05b8bb848.positions[m] );
}
// Render markers
for ( var m in gmap\_m70e4fb6e37a64443876678c05b8bb848.positions ) {
gmap\_m70e4fb6e37a64443876678c05b8bb848.markers[m] = new google.maps.Marker( {
clickable: true,
map : gmap\_m70e4fb6e37a64443876678c05b8bb848.map,
position : gmap\_m70e4fb6e37a64443876678c05b8bb848.positions[m]
} );
}
// Redraw map to fit our new marker-based bounds
gmap\_m70e4fb6e37a64443876678c05b8bb848.map.setCenter( gmap\_m70e4fb6e37a64443876678c05b8bb848.positions[636] );
});