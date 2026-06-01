---
title: San Diego Meetup
date: '2012-09-12T13:05:17+00:00'
format: image
service: flickr
tags:
- automattic
- grandmeetup
- meetup
- sandiego
- sandiego2012
- work
image: http://i1.wp.com/dentedreality.com.au/wp-content/uploads/2012/09/8460264356_bbe8cee838_o.jpg?resize=607%2C809
---

[![San Diego Meetup](http://i1.wp.com/dentedreality.com.au/wp-content/uploads/2012/09/8460264356_bbe8cee838_o.jpg?resize=607%2C809)](http://dentedreality.com.au/2012/09/12/san-diego-meetup-11/) 
# [San Diego Meetup](http://dentedreality.com.au/2012/09/12/san-diego-meetup-11/)





* #[automattic](http://dentedreality.com.au/tags/automattic/)
* #[grandmeetup](http://dentedreality.com.au/tags/grandmeetup/)
* #[meetup](http://dentedreality.com.au/tags/meetup/)
* #[sandiego](http://dentedreality.com.au/tags/sandiego/)
* #[sandiego2012](http://dentedreality.com.au/tags/sandiego2012/)
* #[work](http://dentedreality.com.au/tags/work/)

Posted on [Flickr](http://www.flickr.com/photos/borkazoid/8460264356/) [1:05 pm, September 12, 2012](http://dentedreality.com.au/2012/09/12/san-diego-meetup-11/ "1:05 pm") 
jQuery(document).ready(function(){
var gmap\_m49b906bd4463540dce9fef297c1a5846 = {
positions : {
986 : new google.maps.LatLng( '32.569722', '-116.911928' )
},
bounds : new google.maps.LatLngBounds(), // empty for now, we'll dynamically extend it later
map : new google.maps.Map(
document.getElementById( 'gmap\_m49b906bd4463540dce9fef297c1a5846' ),
{
mapTypeId: google.maps.MapTypeId.ROADMAP,
center: new google.maps.LatLng( 0, 0 ),
zoom: 16 // Seems to be a good zoom for a single point
}
),
markers : {},
}; // end of gmap
// Extend the bounds of interest based on our positions
for ( var m in gmap\_m49b906bd4463540dce9fef297c1a5846.positions ) {
gmap\_m49b906bd4463540dce9fef297c1a5846.bounds.extend( gmap\_m49b906bd4463540dce9fef297c1a5846.positions[m] );
}
// Render markers
for ( var m in gmap\_m49b906bd4463540dce9fef297c1a5846.positions ) {
gmap\_m49b906bd4463540dce9fef297c1a5846.markers[m] = new google.maps.Marker( {
clickable: true,
map : gmap\_m49b906bd4463540dce9fef297c1a5846.map,
position : gmap\_m49b906bd4463540dce9fef297c1a5846.positions[m]
} );
}
// Redraw map to fit our new marker-based bounds
gmap\_m49b906bd4463540dce9fef297c1a5846.map.setCenter( gmap\_m49b906bd4463540dce9fef297c1a5846.positions[986] );
});