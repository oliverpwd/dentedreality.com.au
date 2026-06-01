---
title: Up They Go!
date: '2011-05-21T10:38:41+00:00'
format: image
service: flickr
tags:
- bridge
- meetup
- PDX
- Portland
- teamsocial
- willamette
image: http://i2.wp.com/dentedreality.com.au/wp-content/uploads/2011/05/5802181387_11f361c16a_o.jpg?resize=607%2C452
---

[![Up They Go!](http://i2.wp.com/dentedreality.com.au/wp-content/uploads/2011/05/5802181387_11f361c16a_o.jpg?resize=607%2C452)](http://dentedreality.com.au/2011/05/21/up-they-go/) 
# [Up They Go!](http://dentedreality.com.au/2011/05/21/up-they-go/)

Bridges going up on the Willamette River to let a boat through





* #[bridge](http://dentedreality.com.au/tags/bridge/)
* #[meetup](http://dentedreality.com.au/tags/meetup/)
* #[PDX](http://dentedreality.com.au/tags/pdx/)
* #[Portland](http://dentedreality.com.au/tags/portland/)
* #[teamsocial](http://dentedreality.com.au/tags/teamsocial/)
* #[willamette](http://dentedreality.com.au/tags/willamette/)

Posted on [Flickr](http://www.flickr.com/photos/borkazoid/5802181387/) [10:38 am, May 21, 2011](http://dentedreality.com.au/2011/05/21/up-they-go/ "10:38 am") 
jQuery(document).ready(function(){
var gmap\_me7f347bd8862769a3b813b77b4f12b4f = {
positions : {
717 : new google.maps.LatLng( '45.524499', '-122.669334' )
},
bounds : new google.maps.LatLngBounds(), // empty for now, we'll dynamically extend it later
map : new google.maps.Map(
document.getElementById( 'gmap\_me7f347bd8862769a3b813b77b4f12b4f' ),
{
mapTypeId: google.maps.MapTypeId.ROADMAP,
center: new google.maps.LatLng( 0, 0 ),
zoom: 16 // Seems to be a good zoom for a single point
}
),
markers : {},
}; // end of gmap
// Extend the bounds of interest based on our positions
for ( var m in gmap\_me7f347bd8862769a3b813b77b4f12b4f.positions ) {
gmap\_me7f347bd8862769a3b813b77b4f12b4f.bounds.extend( gmap\_me7f347bd8862769a3b813b77b4f12b4f.positions[m] );
}
// Render markers
for ( var m in gmap\_me7f347bd8862769a3b813b77b4f12b4f.positions ) {
gmap\_me7f347bd8862769a3b813b77b4f12b4f.markers[m] = new google.maps.Marker( {
clickable: true,
map : gmap\_me7f347bd8862769a3b813b77b4f12b4f.map,
position : gmap\_me7f347bd8862769a3b813b77b4f12b4f.positions[m]
} );
}
// Redraw map to fit our new marker-based bounds
gmap\_me7f347bd8862769a3b813b77b4f12b4f.map.setCenter( gmap\_me7f347bd8862769a3b813b77b4f12b4f.positions[717] );
});