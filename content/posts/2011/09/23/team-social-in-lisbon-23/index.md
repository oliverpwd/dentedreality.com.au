---
title: Team Social in Lisbon
date: '2011-09-23T07:02:55-06:00'
format: image
service: flickr
tags:
- automattic
- Lisbon
- meetup
- portugal
- teamsocial
- view
latitude: '38.7155'
longitude: '-9.1445'
image: https://s3.amazonaws.com/dentedreality-content/wp-content/uploads/2011/09/14190317/6812111156_4c8b28e590_o.jpg
---

[![Team Social in Lisbon](https://s3.amazonaws.com/dentedreality-content/wp-content/uploads/2011/09/14190317/6812111156_4c8b28e590_o.jpg)](https://dentedreality.com.au/2011/09/23/team-social-in-lisbon-23/) 
# [Team Social in Lisbon](https://dentedreality.com.au/2011/09/23/team-social-in-lisbon-23/)

[![Team Social in Lisbon](https://s3.amazonaws.com/dentedreality-content/wp-content/uploads/2011/09/14190317/6812111156_4c8b28e590_o.jpg)](http://www.flickr.com/photos/borkazoid/6812111156/)

38.7155-9.1445




* #[automattic](https://dentedreality.com.au/tags/automattic/)
* #[Lisbon](https://dentedreality.com.au/tags/lisbon/)
* #[meetup](https://dentedreality.com.au/tags/meetup/)
* #[portugal](https://dentedreality.com.au/tags/portugal/)
* #[teamsocial](https://dentedreality.com.au/tags/teamsocial/)
* #[view](https://dentedreality.com.au/tags/view/)

Posted on [Flickr](http://www.flickr.com/photos/borkazoid/6812111156/) [7:02 am, September 23, 2011](https://dentedreality.com.au/2011/09/23/team-social-in-lisbon-23/ "7:02 am") 
jQuery(document).ready(function(){
var gmap\_md0324a0a6a5831a970e07dc277f8e66d = {
positions : {
141 : new google.maps.LatLng( '38.7155', '-9.1445' )
},
bounds : new google.maps.LatLngBounds(), // empty for now, we'll dynamically extend it later
map : new google.maps.Map(
document.getElementById( 'gmap\_md0324a0a6a5831a970e07dc277f8e66d' ),
{
mapTypeId: google.maps.MapTypeId.ROADMAP,
center: new google.maps.LatLng( 0, 0 ),
zoom: 16 // Seems to be a good zoom for a single point
}
),
markers : {},
}; // end of gmap
// Extend the bounds of interest based on our positions
for ( var m in gmap\_md0324a0a6a5831a970e07dc277f8e66d.positions ) {
gmap\_md0324a0a6a5831a970e07dc277f8e66d.bounds.extend( gmap\_md0324a0a6a5831a970e07dc277f8e66d.positions[m] );
}
// Render markers
for ( var m in gmap\_md0324a0a6a5831a970e07dc277f8e66d.positions ) {
gmap\_md0324a0a6a5831a970e07dc277f8e66d.markers[m] = new google.maps.Marker( {
clickable: true,
map : gmap\_md0324a0a6a5831a970e07dc277f8e66d.map,
position : gmap\_md0324a0a6a5831a970e07dc277f8e66d.positions[m]
} );
}
// Redraw map to fit our new marker-based bounds
gmap\_md0324a0a6a5831a970e07dc277f8e66d.map.setCenter( gmap\_md0324a0a6a5831a970e07dc277f8e66d.positions[141] );
});