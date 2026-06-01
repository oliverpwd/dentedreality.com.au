---
title: Inverted WordPress MacBook Pros
date: '2013-05-20T07:07:30+00:00'
format: image
tags:
- automattic
- laptop
- learnup
- wordpress
image: http://i0.wp.com/dentedreality.com.au/wp-content/uploads/2013/05/9436932191_733eac60b6_o.jpg?resize=607%2C452
---

[![Inverted WordPress MacBook Pros](http://i0.wp.com/dentedreality.com.au/wp-content/uploads/2013/05/9436932191_733eac60b6_o.jpg?resize=607%2C452)](http://dentedreality.com.au/2013/05/20/inverted-wordpress-macbook-pros/) 
# [Inverted WordPress MacBook Pros](http://dentedreality.com.au/2013/05/20/inverted-wordpress-macbook-pros/)





* #[automattic](http://dentedreality.com.au/tags/automattic/)
* #[laptop](http://dentedreality.com.au/tags/laptop/)
* #[learnup](http://dentedreality.com.au/tags/learnup/)
* #[wordpress](http://dentedreality.com.au/tags/wordpress/)

Posted on [Flickr](http://www.flickr.com/photos/borkazoid/9436932191/) [7:07 am, May 20, 2013](http://dentedreality.com.au/2013/05/20/inverted-wordpress-macbook-pros/ "7:07 am") 
jQuery(document).ready(function(){
var gmap\_m97b42d4bd7137661337e615d7742ebec = {
positions : {
944 : new google.maps.LatLng( '37.783833', '-122.397501' )
},
bounds : new google.maps.LatLngBounds(), // empty for now, we'll dynamically extend it later
map : new google.maps.Map(
document.getElementById( 'gmap\_m97b42d4bd7137661337e615d7742ebec' ),
{
mapTypeId: google.maps.MapTypeId.ROADMAP,
center: new google.maps.LatLng( 0, 0 ),
zoom: 16 // Seems to be a good zoom for a single point
}
),
markers : {},
}; // end of gmap
// Extend the bounds of interest based on our positions
for ( var m in gmap\_m97b42d4bd7137661337e615d7742ebec.positions ) {
gmap\_m97b42d4bd7137661337e615d7742ebec.bounds.extend( gmap\_m97b42d4bd7137661337e615d7742ebec.positions[m] );
}
// Render markers
for ( var m in gmap\_m97b42d4bd7137661337e615d7742ebec.positions ) {
gmap\_m97b42d4bd7137661337e615d7742ebec.markers[m] = new google.maps.Marker( {
clickable: true,
map : gmap\_m97b42d4bd7137661337e615d7742ebec.map,
position : gmap\_m97b42d4bd7137661337e615d7742ebec.positions[m]
} );
}
// Redraw map to fit our new marker-based bounds
gmap\_m97b42d4bd7137661337e615d7742ebec.map.setCenter( gmap\_m97b42d4bd7137661337e615d7742ebec.positions[944] );
});