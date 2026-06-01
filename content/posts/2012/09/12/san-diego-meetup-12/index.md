---
title: San Diego Meetup
date: '2012-09-12T12:42:13+00:00'
format: image
service: flickr
tags:
- automattic
- grandmeetup
- meetup
- sandiego
- sandiego2012
- work
image: http://i0.wp.com/dentedreality.com.au/wp-content/uploads/2012/09/8460264158_78e2f395bd_o.jpg?resize=607%2C809
---

[![San Diego Meetup](http://i0.wp.com/dentedreality.com.au/wp-content/uploads/2012/09/8460264158_78e2f395bd_o.jpg?resize=607%2C809)](http://dentedreality.com.au/2012/09/12/san-diego-meetup-12/) 
# [San Diego Meetup](http://dentedreality.com.au/2012/09/12/san-diego-meetup-12/)





* #[automattic](http://dentedreality.com.au/tags/automattic/)
* #[grandmeetup](http://dentedreality.com.au/tags/grandmeetup/)
* #[meetup](http://dentedreality.com.au/tags/meetup/)
* #[sandiego](http://dentedreality.com.au/tags/sandiego/)
* #[sandiego2012](http://dentedreality.com.au/tags/sandiego2012/)
* #[work](http://dentedreality.com.au/tags/work/)

Posted on [Flickr](http://www.flickr.com/photos/borkazoid/8460264158/) [12:42 pm, September 12, 2012](http://dentedreality.com.au/2012/09/12/san-diego-meetup-12/ "12:42 pm") 
jQuery(document).ready(function(){
var gmap\_me1fd324d746f5c17a2de7b8b4afd4b75 = {
positions : {
346 : new google.maps.LatLng( '32.569683', '-116.911923' )
},
bounds : new google.maps.LatLngBounds(), // empty for now, we'll dynamically extend it later
map : new google.maps.Map(
document.getElementById( 'gmap\_me1fd324d746f5c17a2de7b8b4afd4b75' ),
{
mapTypeId: google.maps.MapTypeId.ROADMAP,
center: new google.maps.LatLng( 0, 0 ),
zoom: 16 // Seems to be a good zoom for a single point
}
),
markers : {},
}; // end of gmap
// Extend the bounds of interest based on our positions
for ( var m in gmap\_me1fd324d746f5c17a2de7b8b4afd4b75.positions ) {
gmap\_me1fd324d746f5c17a2de7b8b4afd4b75.bounds.extend( gmap\_me1fd324d746f5c17a2de7b8b4afd4b75.positions[m] );
}
// Render markers
for ( var m in gmap\_me1fd324d746f5c17a2de7b8b4afd4b75.positions ) {
gmap\_me1fd324d746f5c17a2de7b8b4afd4b75.markers[m] = new google.maps.Marker( {
clickable: true,
map : gmap\_me1fd324d746f5c17a2de7b8b4afd4b75.map,
position : gmap\_me1fd324d746f5c17a2de7b8b4afd4b75.positions[m]
} );
}
// Redraw map to fit our new marker-based bounds
gmap\_me1fd324d746f5c17a2de7b8b4afd4b75.map.setCenter( gmap\_me1fd324d746f5c17a2de7b8b4afd4b75.positions[346] );
});