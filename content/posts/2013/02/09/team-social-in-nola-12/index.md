---
title: Team Social in NOLA
date: '2013-02-09T13:46:54+00:00'
format: image
service: flickr
tags:
- automattic
- meetup
- neworleans
- nola
- teamsocial
image: http://i2.wp.com/dentedreality.com.au/wp-content/uploads/2013/02/8460390974_0843c6aa33_o.jpg?resize=607%2C452
---

[![Team Social in NOLA](http://i2.wp.com/dentedreality.com.au/wp-content/uploads/2013/02/8460390974_0843c6aa33_o.jpg?resize=607%2C452)](http://dentedreality.com.au/2013/02/09/team-social-in-nola-12/) 
# [Team Social in NOLA](http://dentedreality.com.au/2013/02/09/team-social-in-nola-12/)





* #[automattic](http://dentedreality.com.au/tags/automattic/)
* #[meetup](http://dentedreality.com.au/tags/meetup/)
* #[neworleans](http://dentedreality.com.au/tags/neworleans/)
* #[nola](http://dentedreality.com.au/tags/nola/)
* #[teamsocial](http://dentedreality.com.au/tags/teamsocial/)

Posted on [Flickr](http://www.flickr.com/photos/borkazoid/8460390974/) [1:46 pm, February 9, 2013](http://dentedreality.com.au/2013/02/09/team-social-in-nola-12/ "1:46 pm") 
jQuery(document).ready(function(){
var gmap\_m9c6d3c70403648e741c88f1fdf982833 = {
positions : {
620 : new google.maps.LatLng( '29.9615', '-90.0355' )
},
bounds : new google.maps.LatLngBounds(), // empty for now, we'll dynamically extend it later
map : new google.maps.Map(
document.getElementById( 'gmap\_m9c6d3c70403648e741c88f1fdf982833' ),
{
mapTypeId: google.maps.MapTypeId.ROADMAP,
center: new google.maps.LatLng( 0, 0 ),
zoom: 16 // Seems to be a good zoom for a single point
}
),
markers : {},
}; // end of gmap
// Extend the bounds of interest based on our positions
for ( var m in gmap\_m9c6d3c70403648e741c88f1fdf982833.positions ) {
gmap\_m9c6d3c70403648e741c88f1fdf982833.bounds.extend( gmap\_m9c6d3c70403648e741c88f1fdf982833.positions[m] );
}
// Render markers
for ( var m in gmap\_m9c6d3c70403648e741c88f1fdf982833.positions ) {
gmap\_m9c6d3c70403648e741c88f1fdf982833.markers[m] = new google.maps.Marker( {
clickable: true,
map : gmap\_m9c6d3c70403648e741c88f1fdf982833.map,
position : gmap\_m9c6d3c70403648e741c88f1fdf982833.positions[m]
} );
}
// Redraw map to fit our new marker-based bounds
gmap\_m9c6d3c70403648e741c88f1fdf982833.map.setCenter( gmap\_m9c6d3c70403648e741c88f1fdf982833.positions[620] );
});