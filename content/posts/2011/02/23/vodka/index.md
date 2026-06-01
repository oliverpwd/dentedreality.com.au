---
title: Vodka
date: '2011-02-23T17:27:51+00:00'
format: image
service: flickr
tags:
- newyork
- newyorkcity
- NYC
- vodka
image: http://i1.wp.com/dentedreality.com.au/wp-content/uploads/2011/02/5802617602_563bd9ded9_o.jpg?resize=607%2C452
---

[![Vodka](http://i1.wp.com/dentedreality.com.au/wp-content/uploads/2011/02/5802617602_563bd9ded9_o.jpg?resize=607%2C452)](http://dentedreality.com.au/2011/02/23/vodka/) 
# [Vodka](http://dentedreality.com.au/2011/02/23/vodka/)

Everyone’s drinking it.





* #[newyork](http://dentedreality.com.au/tags/newyork/)
* #[newyorkcity](http://dentedreality.com.au/tags/newyorkcity/)
* #[NYC](http://dentedreality.com.au/tags/nyc/)
* #[vodka](http://dentedreality.com.au/tags/vodka/)

Posted on [Flickr](http://www.flickr.com/photos/borkazoid/5802617602/) [5:27 pm, February 23, 2011](http://dentedreality.com.au/2011/02/23/vodka/ "5:27 pm") 
jQuery(document).ready(function(){
var gmap\_m9f967fcf0bf7d2de924f8cb3239fe6ea = {
positions : {
706 : new google.maps.LatLng( '40.759166', '-73.9825' )
},
bounds : new google.maps.LatLngBounds(), // empty for now, we'll dynamically extend it later
map : new google.maps.Map(
document.getElementById( 'gmap\_m9f967fcf0bf7d2de924f8cb3239fe6ea' ),
{
mapTypeId: google.maps.MapTypeId.ROADMAP,
center: new google.maps.LatLng( 0, 0 ),
zoom: 16 // Seems to be a good zoom for a single point
}
),
markers : {},
}; // end of gmap
// Extend the bounds of interest based on our positions
for ( var m in gmap\_m9f967fcf0bf7d2de924f8cb3239fe6ea.positions ) {
gmap\_m9f967fcf0bf7d2de924f8cb3239fe6ea.bounds.extend( gmap\_m9f967fcf0bf7d2de924f8cb3239fe6ea.positions[m] );
}
// Render markers
for ( var m in gmap\_m9f967fcf0bf7d2de924f8cb3239fe6ea.positions ) {
gmap\_m9f967fcf0bf7d2de924f8cb3239fe6ea.markers[m] = new google.maps.Marker( {
clickable: true,
map : gmap\_m9f967fcf0bf7d2de924f8cb3239fe6ea.map,
position : gmap\_m9f967fcf0bf7d2de924f8cb3239fe6ea.positions[m]
} );
}
// Redraw map to fit our new marker-based bounds
gmap\_m9f967fcf0bf7d2de924f8cb3239fe6ea.map.setCenter( gmap\_m9f967fcf0bf7d2de924f8cb3239fe6ea.positions[706] );
});