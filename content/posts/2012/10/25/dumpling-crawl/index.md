---
title: Dumpling Crawl
date: '2012-10-25T14:46:06+00:00'
format: image
service: flickr
tags:
- Chinatown
- dumpling
- dumplingcrawl
- newyork
image: http://i1.wp.com/dentedreality.com.au/wp-content/uploads/2012/10/8244797953_8c6228f621_o.jpg?resize=607%2C452
---

[![Dumpling Crawl](http://i1.wp.com/dentedreality.com.au/wp-content/uploads/2012/10/8244797953_8c6228f621_o.jpg?resize=607%2C452)](http://dentedreality.com.au/2012/10/25/dumpling-crawl/) 
# [Dumpling Crawl](http://dentedreality.com.au/2012/10/25/dumpling-crawl/)

Through Manhattan’s Chinatown





* #[Chinatown](http://dentedreality.com.au/tags/chinatown/)
* #[dumpling](http://dentedreality.com.au/tags/dumpling/)
* #[dumplingcrawl](http://dentedreality.com.au/tags/dumplingcrawl/)
* #[newyork](http://dentedreality.com.au/tags/newyork/)

Posted on [Flickr](http://www.flickr.com/photos/borkazoid/8244797953/) [2:46 pm, October 25, 2012](http://dentedreality.com.au/2012/10/25/dumpling-crawl/ "2:46 pm") 
jQuery(document).ready(function(){
var gmap\_m17a01b887a7764be6f6666362501562a = {
positions : {
680 : new google.maps.LatLng( '40.714333', '-73.998167' )
},
bounds : new google.maps.LatLngBounds(), // empty for now, we'll dynamically extend it later
map : new google.maps.Map(
document.getElementById( 'gmap\_m17a01b887a7764be6f6666362501562a' ),
{
mapTypeId: google.maps.MapTypeId.ROADMAP,
center: new google.maps.LatLng( 0, 0 ),
zoom: 16 // Seems to be a good zoom for a single point
}
),
markers : {},
}; // end of gmap
// Extend the bounds of interest based on our positions
for ( var m in gmap\_m17a01b887a7764be6f6666362501562a.positions ) {
gmap\_m17a01b887a7764be6f6666362501562a.bounds.extend( gmap\_m17a01b887a7764be6f6666362501562a.positions[m] );
}
// Render markers
for ( var m in gmap\_m17a01b887a7764be6f6666362501562a.positions ) {
gmap\_m17a01b887a7764be6f6666362501562a.markers[m] = new google.maps.Marker( {
clickable: true,
map : gmap\_m17a01b887a7764be6f6666362501562a.map,
position : gmap\_m17a01b887a7764be6f6666362501562a.positions[m]
} );
}
// Redraw map to fit our new marker-based bounds
gmap\_m17a01b887a7764be6f6666362501562a.map.setCenter( gmap\_m17a01b887a7764be6f6666362501562a.positions[680] );
});