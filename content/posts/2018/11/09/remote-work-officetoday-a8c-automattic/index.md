---
title: ''
date: '2018-11-09T16:31:56-07:00'
format: image
service: instagram
tags:
- a8c
- automattic
- OfficeToday
latitude: '45.5888698'
longitude: '-122.5962222'
image: https://dentedreality.com.au/wp-content/uploads/2018/11/44691808_288969811732007_7767962330615127774_n.jpg
---

[![Remote work. #officetoday #a8c #automattic](https://dentedreality.com.au/wp-content/uploads/2018/11/44691808_288969811732007_7767962330615127774_n.jpg)](https://dentedreality.com.au/2018/11/09/remote-work-officetoday-a8c-automattic/) 

[![Remote work. #officetoday #a8c #automattic](https://dentedreality.com.au/wp-content/uploads/2018/11/44691808_288969811732007_7767962330615127774_n.jpg)](https://www.instagram.com/p/Bp-maJ1g2q2/)

Remote work. #officetoday #a8c #automattic

45.5888698-122.5962222




* #[a8c](https://dentedreality.com.au/tags/a8c/)
* #[automattic](https://dentedreality.com.au/tags/automattic/)
* #[OfficeToday](https://dentedreality.com.au/tags/officetoday/)

Posted on [Instagram](https://www.instagram.com/p/Bp-maJ1g2q2/) [4:31 pm, November 9, 2018](https://dentedreality.com.au/2018/11/09/remote-work-officetoday-a8c-automattic/ "4:31 pm") 
jQuery(document).ready(function(){
var gmap\_m5dd92be0f305503dd6670783e4042907 = {
positions : {
287 : new google.maps.LatLng( '45.5888698', '-122.5962222' )
},
bounds : new google.maps.LatLngBounds(), // empty for now, we'll dynamically extend it later
map : new google.maps.Map(
document.getElementById( 'gmap\_m5dd92be0f305503dd6670783e4042907' ),
{
mapTypeId: google.maps.MapTypeId.ROADMAP,
center: new google.maps.LatLng( 0, 0 ),
zoom: 16 // Seems to be a good zoom for a single point
}
),
markers : {},
}; // end of gmap
// Extend the bounds of interest based on our positions
for ( var m in gmap\_m5dd92be0f305503dd6670783e4042907.positions ) {
gmap\_m5dd92be0f305503dd6670783e4042907.bounds.extend( gmap\_m5dd92be0f305503dd6670783e4042907.positions[m] );
}
// Render markers
for ( var m in gmap\_m5dd92be0f305503dd6670783e4042907.positions ) {
gmap\_m5dd92be0f305503dd6670783e4042907.markers[m] = new google.maps.Marker( {
clickable: true,
map : gmap\_m5dd92be0f305503dd6670783e4042907.map,
position : gmap\_m5dd92be0f305503dd6670783e4042907.positions[m]
} );
}
// Redraw map to fit our new marker-based bounds
gmap\_m5dd92be0f305503dd6670783e4042907.map.setCenter( gmap\_m5dd92be0f305503dd6670783e4042907.positions[287] );
});