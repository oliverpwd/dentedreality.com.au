---
title: San Diego Meetup
date: '2012-09-12T11:53:21+00:00'
format: image
service: flickr
tags:
- automattic
- grandmeetup
- meetup
- sandiego
- sandiego2012
- work
image: http://i0.wp.com/dentedreality.com.au/wp-content/uploads/2012/09/8459160589_9d988cdd23_o.jpg?resize=607%2C455
---

[![San Diego Meetup](http://i0.wp.com/dentedreality.com.au/wp-content/uploads/2012/09/8459160589_9d988cdd23_o.jpg?resize=607%2C455)](http://dentedreality.com.au/2012/09/12/san-diego-meetup-15/) 
# [San Diego Meetup](http://dentedreality.com.au/2012/09/12/san-diego-meetup-15/)





* #[automattic](http://dentedreality.com.au/tags/automattic/)
* #[grandmeetup](http://dentedreality.com.au/tags/grandmeetup/)
* #[meetup](http://dentedreality.com.au/tags/meetup/)
* #[sandiego](http://dentedreality.com.au/tags/sandiego/)
* #[sandiego2012](http://dentedreality.com.au/tags/sandiego2012/)
* #[work](http://dentedreality.com.au/tags/work/)

Posted on [Flickr](http://www.flickr.com/photos/borkazoid/8459160589/) [11:53 am, September 12, 2012](http://dentedreality.com.au/2012/09/12/san-diego-meetup-15/ "11:53 am") 
jQuery(document).ready(function(){
var gmap\_m8fdf60957056e44284157ccb7f7c6219 = {
positions : {
177 : new google.maps.LatLng( '32.568258', '-116.908742' )
},
bounds : new google.maps.LatLngBounds(), // empty for now, we'll dynamically extend it later
map : new google.maps.Map(
document.getElementById( 'gmap\_m8fdf60957056e44284157ccb7f7c6219' ),
{
mapTypeId: google.maps.MapTypeId.ROADMAP,
center: new google.maps.LatLng( 0, 0 ),
zoom: 16 // Seems to be a good zoom for a single point
}
),
markers : {},
}; // end of gmap
// Extend the bounds of interest based on our positions
for ( var m in gmap\_m8fdf60957056e44284157ccb7f7c6219.positions ) {
gmap\_m8fdf60957056e44284157ccb7f7c6219.bounds.extend( gmap\_m8fdf60957056e44284157ccb7f7c6219.positions[m] );
}
// Render markers
for ( var m in gmap\_m8fdf60957056e44284157ccb7f7c6219.positions ) {
gmap\_m8fdf60957056e44284157ccb7f7c6219.markers[m] = new google.maps.Marker( {
clickable: true,
map : gmap\_m8fdf60957056e44284157ccb7f7c6219.map,
position : gmap\_m8fdf60957056e44284157ccb7f7c6219.positions[m]
} );
}
// Redraw map to fit our new marker-based bounds
gmap\_m8fdf60957056e44284157ccb7f7c6219.map.setCenter( gmap\_m8fdf60957056e44284157ccb7f7c6219.positions[177] );
});