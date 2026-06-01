---
title: Filipino Brunch
date: '2011-05-30T07:40:55+00:00'
format: image
service: flickr
tags:
- filipino
- iris
- jenn
- pocketlisa
- rick
- sisig
image: http://i0.wp.com/dentedreality.com.au/wp-content/uploads/2011/05/5803435088_9a072f943a_o.jpg?resize=607%2C452
---

[![Filipino Brunch](http://i0.wp.com/dentedreality.com.au/wp-content/uploads/2011/05/5803435088_9a072f943a_o.jpg?resize=607%2C452)](http://dentedreality.com.au/2011/05/30/filipino-brunch/) 
# [Filipino Brunch](http://dentedreality.com.au/2011/05/30/filipino-brunch/)





* #[filipino](http://dentedreality.com.au/tags/filipino/)
* #[iris](http://dentedreality.com.au/tags/iris/)
* #[jenn](http://dentedreality.com.au/tags/jenn/)
* #[pocketlisa](http://dentedreality.com.au/tags/pocketlisa/)
* #[rick](http://dentedreality.com.au/tags/rick/)
* #[sisig](http://dentedreality.com.au/tags/sisig/)

Posted on [Flickr](http://www.flickr.com/photos/borkazoid/5803435088/) [7:40 am, May 30, 2011](http://dentedreality.com.au/2011/05/30/filipino-brunch/ "7:40 am") 
jQuery(document).ready(function(){
var gmap\_m094e34a8dd17cedac638321999e57784 = {
positions : {
767 : new google.maps.LatLng( '37.693333', '-122.471334' )
},
bounds : new google.maps.LatLngBounds(), // empty for now, we'll dynamically extend it later
map : new google.maps.Map(
document.getElementById( 'gmap\_m094e34a8dd17cedac638321999e57784' ),
{
mapTypeId: google.maps.MapTypeId.ROADMAP,
center: new google.maps.LatLng( 0, 0 ),
zoom: 16 // Seems to be a good zoom for a single point
}
),
markers : {},
}; // end of gmap
// Extend the bounds of interest based on our positions
for ( var m in gmap\_m094e34a8dd17cedac638321999e57784.positions ) {
gmap\_m094e34a8dd17cedac638321999e57784.bounds.extend( gmap\_m094e34a8dd17cedac638321999e57784.positions[m] );
}
// Render markers
for ( var m in gmap\_m094e34a8dd17cedac638321999e57784.positions ) {
gmap\_m094e34a8dd17cedac638321999e57784.markers[m] = new google.maps.Marker( {
clickable: true,
map : gmap\_m094e34a8dd17cedac638321999e57784.map,
position : gmap\_m094e34a8dd17cedac638321999e57784.positions[m]
} );
}
// Redraw map to fit our new marker-based bounds
gmap\_m094e34a8dd17cedac638321999e57784.map.setCenter( gmap\_m094e34a8dd17cedac638321999e57784.positions[767] );
});