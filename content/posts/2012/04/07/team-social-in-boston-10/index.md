---
title: Team Social in Boston
date: '2012-04-07T17:59:20-06:00'
format: image
service: flickr
tags:
- automattic
- food
- meetup
- steak
- teamsocial
latitude: '42.362166'
longitude: '-71.100334'
image: https://s3.amazonaws.com/dentedreality-content/wp-content/uploads/2012/04/14190547/7770462682_d293a1d917_o.jpg
---

[![Team Social in Boston](https://s3.amazonaws.com/dentedreality-content/wp-content/uploads/2012/04/14190547/7770462682_d293a1d917_o.jpg)](https://dentedreality.com.au/2012/04/07/team-social-in-boston-10/) 
# [Team Social in Boston](https://dentedreality.com.au/2012/04/07/team-social-in-boston-10/)

[![Team Social in Boston](https://s3.amazonaws.com/dentedreality-content/wp-content/uploads/2012/04/14190547/7770462682_d293a1d917_o.jpg)](http://www.flickr.com/photos/borkazoid/7770462682/)

42.362166-71.100334




* #[automattic](https://dentedreality.com.au/tags/automattic/)
* #[food](https://dentedreality.com.au/tags/food/)
* #[meetup](https://dentedreality.com.au/tags/meetup/)
* #[steak](https://dentedreality.com.au/tags/steak/)
* #[teamsocial](https://dentedreality.com.au/tags/teamsocial/)

Posted on [Flickr](http://www.flickr.com/photos/borkazoid/7770462682/) [5:59 pm, April 7, 2012](https://dentedreality.com.au/2012/04/07/team-social-in-boston-10/ "5:59 pm") 
jQuery(document).ready(function(){
var gmap\_m9a04283db634d34f4c683c5358f2ec41 = {
positions : {
646 : new google.maps.LatLng( '42.362166', '-71.100334' )
},
bounds : new google.maps.LatLngBounds(), // empty for now, we'll dynamically extend it later
map : new google.maps.Map(
document.getElementById( 'gmap\_m9a04283db634d34f4c683c5358f2ec41' ),
{
mapTypeId: google.maps.MapTypeId.ROADMAP,
center: new google.maps.LatLng( 0, 0 ),
zoom: 16 // Seems to be a good zoom for a single point
}
),
markers : {},
}; // end of gmap
// Extend the bounds of interest based on our positions
for ( var m in gmap\_m9a04283db634d34f4c683c5358f2ec41.positions ) {
gmap\_m9a04283db634d34f4c683c5358f2ec41.bounds.extend( gmap\_m9a04283db634d34f4c683c5358f2ec41.positions[m] );
}
// Render markers
for ( var m in gmap\_m9a04283db634d34f4c683c5358f2ec41.positions ) {
gmap\_m9a04283db634d34f4c683c5358f2ec41.markers[m] = new google.maps.Marker( {
clickable: true,
map : gmap\_m9a04283db634d34f4c683c5358f2ec41.map,
position : gmap\_m9a04283db634d34f4c683c5358f2ec41.positions[m]
} );
}
// Redraw map to fit our new marker-based bounds
gmap\_m9a04283db634d34f4c683c5358f2ec41.map.setCenter( gmap\_m9a04283db634d34f4c683c5358f2ec41.positions[646] );
});