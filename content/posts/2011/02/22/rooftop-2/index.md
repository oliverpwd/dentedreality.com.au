---
title: Rooftop
date: '2011-02-22T08:14:42+00:00'
format: image
service: flickr
tags:
- newyork
- newyorkcity
- NYC
- rooftop
- snow
image: http://i0.wp.com/dentedreality.com.au/wp-content/uploads/2011/02/5802057783_0bfda3a698_o.jpg?resize=607%2C452
---

[![Rooftop](http://i0.wp.com/dentedreality.com.au/wp-content/uploads/2011/02/5802057783_0bfda3a698_o.jpg?resize=607%2C452)](http://dentedreality.com.au/2011/02/22/rooftop-2/) 
# [Rooftop](http://dentedreality.com.au/2011/02/22/rooftop-2/)

The rooftop of our apartment while we were in NYC for a week.





* #[newyork](http://dentedreality.com.au/tags/newyork/)
* #[newyorkcity](http://dentedreality.com.au/tags/newyorkcity/)
* #[NYC](http://dentedreality.com.au/tags/nyc/)
* #[rooftop](http://dentedreality.com.au/tags/rooftop/)
* #[snow](http://dentedreality.com.au/tags/snow/)

Posted on [Flickr](http://www.flickr.com/photos/borkazoid/5802057783/) [8:14 am, February 22, 2011](http://dentedreality.com.au/2011/02/22/rooftop-2/ "8:14 am") 
jQuery(document).ready(function(){
var gmap\_m0a67104f5f3142644273a5ee80286d8f = {
positions : {
158 : new google.maps.LatLng( '40.725666', '-73.994834' )
},
bounds : new google.maps.LatLngBounds(), // empty for now, we'll dynamically extend it later
map : new google.maps.Map(
document.getElementById( 'gmap\_m0a67104f5f3142644273a5ee80286d8f' ),
{
mapTypeId: google.maps.MapTypeId.ROADMAP,
center: new google.maps.LatLng( 0, 0 ),
zoom: 16 // Seems to be a good zoom for a single point
}
),
markers : {},
}; // end of gmap
// Extend the bounds of interest based on our positions
for ( var m in gmap\_m0a67104f5f3142644273a5ee80286d8f.positions ) {
gmap\_m0a67104f5f3142644273a5ee80286d8f.bounds.extend( gmap\_m0a67104f5f3142644273a5ee80286d8f.positions[m] );
}
// Render markers
for ( var m in gmap\_m0a67104f5f3142644273a5ee80286d8f.positions ) {
gmap\_m0a67104f5f3142644273a5ee80286d8f.markers[m] = new google.maps.Marker( {
clickable: true,
map : gmap\_m0a67104f5f3142644273a5ee80286d8f.map,
position : gmap\_m0a67104f5f3142644273a5ee80286d8f.positions[m]
} );
}
// Redraw map to fit our new marker-based bounds
gmap\_m0a67104f5f3142644273a5ee80286d8f.map.setCenter( gmap\_m0a67104f5f3142644273a5ee80286d8f.positions[158] );
});