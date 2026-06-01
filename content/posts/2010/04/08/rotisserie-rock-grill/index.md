---
title: Rotisserie + Rock Grill
date: '2010-04-08T08:24:20+00:00'
format: image
service: flickr
tags:
- chicken
- fish
- pork
- rockgrill
- rotisserie
- tombrown
- trackerschool
- tracking
image: http://i1.wp.com/dentedreality.com.au/wp-content/uploads/2010/04/4515812773_b6f7c35957_o.jpg?resize=607%2C455
---

[![Rotisserie + Rock Grill](http://i1.wp.com/dentedreality.com.au/wp-content/uploads/2010/04/4515812773_b6f7c35957_o.jpg?resize=607%2C455)](http://dentedreality.com.au/2010/04/08/rotisserie-rock-grill/) 
# [Rotisserie + Rock Grill](http://dentedreality.com.au/2010/04/08/rotisserie-rock-grill/)

Standard class, Tracker School.





* #[chicken](http://dentedreality.com.au/tags/chicken/)
* #[fish](http://dentedreality.com.au/tags/fish/)
* #[pork](http://dentedreality.com.au/tags/pork/)
* #[rockgrill](http://dentedreality.com.au/tags/rockgrill/)
* #[rotisserie](http://dentedreality.com.au/tags/rotisserie/)
* #[tombrown](http://dentedreality.com.au/tags/tombrown/)
* #[trackerschool](http://dentedreality.com.au/tags/trackerschool/)
* #[tracking](http://dentedreality.com.au/tags/tracking/)

Posted on [Flickr](http://www.flickr.com/photos/borkazoid/4515812773/) [8:24 am, April 8, 2010](http://dentedreality.com.au/2010/04/08/rotisserie-rock-grill/ "8:24 am") 
jQuery(document).ready(function(){
var gmap\_mb97299064df3185bed377b0fe431d715 = {
positions : {
544 : new google.maps.LatLng( '37.177141', '-122.116744' )
},
bounds : new google.maps.LatLngBounds(), // empty for now, we'll dynamically extend it later
map : new google.maps.Map(
document.getElementById( 'gmap\_mb97299064df3185bed377b0fe431d715' ),
{
mapTypeId: google.maps.MapTypeId.ROADMAP,
center: new google.maps.LatLng( 0, 0 ),
zoom: 16 // Seems to be a good zoom for a single point
}
),
markers : {},
}; // end of gmap
// Extend the bounds of interest based on our positions
for ( var m in gmap\_mb97299064df3185bed377b0fe431d715.positions ) {
gmap\_mb97299064df3185bed377b0fe431d715.bounds.extend( gmap\_mb97299064df3185bed377b0fe431d715.positions[m] );
}
// Render markers
for ( var m in gmap\_mb97299064df3185bed377b0fe431d715.positions ) {
gmap\_mb97299064df3185bed377b0fe431d715.markers[m] = new google.maps.Marker( {
clickable: true,
map : gmap\_mb97299064df3185bed377b0fe431d715.map,
position : gmap\_mb97299064df3185bed377b0fe431d715.positions[m]
} );
}
// Redraw map to fit our new marker-based bounds
gmap\_mb97299064df3185bed377b0fe431d715.map.setCenter( gmap\_mb97299064df3185bed377b0fe431d715.positions[544] );
});