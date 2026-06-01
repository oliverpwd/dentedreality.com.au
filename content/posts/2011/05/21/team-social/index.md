---
title: Team Social
date: '2011-05-21T08:15:28+00:00'
format: image
service: flickr
tags:
- meetup
- PDX
- Portland
- teamsocial
image: http://i1.wp.com/dentedreality.com.au/wp-content/uploads/2011/05/5802736152_3c1549f1a6_o.jpg?resize=607%2C452
---

[![Team Social](http://i1.wp.com/dentedreality.com.au/wp-content/uploads/2011/05/5802736152_3c1549f1a6_o.jpg?resize=607%2C452)](http://dentedreality.com.au/2011/05/21/team-social/) 
# [Team Social](http://dentedreality.com.au/2011/05/21/team-social/)

minus mdawaffe





* #[meetup](http://dentedreality.com.au/tags/meetup/)
* #[PDX](http://dentedreality.com.au/tags/pdx/)
* #[Portland](http://dentedreality.com.au/tags/portland/)
* #[teamsocial](http://dentedreality.com.au/tags/teamsocial/)

Posted on [Flickr](http://www.flickr.com/photos/borkazoid/5802736152/) [8:15 am, May 21, 2011](http://dentedreality.com.au/2011/05/21/team-social/ "8:15 am") 
jQuery(document).ready(function(){
var gmap\_m27bf4d3a87b20487f19c23a90eb06565 = {
positions : {
606 : new google.maps.LatLng( '45.522166', '-122.674667' )
},
bounds : new google.maps.LatLngBounds(), // empty for now, we'll dynamically extend it later
map : new google.maps.Map(
document.getElementById( 'gmap\_m27bf4d3a87b20487f19c23a90eb06565' ),
{
mapTypeId: google.maps.MapTypeId.ROADMAP,
center: new google.maps.LatLng( 0, 0 ),
zoom: 16 // Seems to be a good zoom for a single point
}
),
markers : {},
}; // end of gmap
// Extend the bounds of interest based on our positions
for ( var m in gmap\_m27bf4d3a87b20487f19c23a90eb06565.positions ) {
gmap\_m27bf4d3a87b20487f19c23a90eb06565.bounds.extend( gmap\_m27bf4d3a87b20487f19c23a90eb06565.positions[m] );
}
// Render markers
for ( var m in gmap\_m27bf4d3a87b20487f19c23a90eb06565.positions ) {
gmap\_m27bf4d3a87b20487f19c23a90eb06565.markers[m] = new google.maps.Marker( {
clickable: true,
map : gmap\_m27bf4d3a87b20487f19c23a90eb06565.map,
position : gmap\_m27bf4d3a87b20487f19c23a90eb06565.positions[m]
} );
}
// Redraw map to fit our new marker-based bounds
gmap\_m27bf4d3a87b20487f19c23a90eb06565.map.setCenter( gmap\_m27bf4d3a87b20487f19c23a90eb06565.positions[606] );
});