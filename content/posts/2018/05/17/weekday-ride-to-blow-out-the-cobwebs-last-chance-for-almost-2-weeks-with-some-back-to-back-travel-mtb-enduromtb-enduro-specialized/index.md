---
title: ''
date: '2018-05-17T19:47:55-06:00'
format: image
service: instagram
tags:
- enduro
- enduromtb
- mtb
- specialized
latitude: '39.6678136'
longitude: '-105.2578443'
image: https://i1.wp.com/s3.amazonaws.com/dentedreality-content/wp-content/uploads/2018/05/14182155/32135471_1571637556292063_4550702284597624832_n.jpg?resize=607%2C607&ssl=1
---

[![Weekday ride to blow out the cobwebs. Last chance for almost 2 weeks, with some back to back travel. #mtb #enduromtb #enduro #specialized](https://i1.wp.com/s3.amazonaws.com/dentedreality-content/wp-content/uploads/2018/05/14182155/32135471_1571637556292063_4550702284597624832_n.jpg?resize=607%2C607&ssl=1)](https://dentedreality.com.au/2018/05/17/weekday-ride-to-blow-out-the-cobwebs-last-chance-for-almost-2-weeks-with-some-back-to-back-travel-mtb-enduromtb-enduro-specialized/) 

[![Weekday ride to blow out the cobwebs. Last chance for almost 2 weeks, with some back to back travel. #mtb #enduromtb #enduro #specialized](https://i1.wp.com/s3.amazonaws.com/dentedreality-content/wp-content/uploads/2018/05/14182155/32135471_1571637556292063_4550702284597624832_n.jpg?resize=607%2C607&ssl=1)](https://www.instagram.com/p/Bi5qECsFMNz/)

Weekday ride to blow out the cobwebs. Last chance for almost 2 weeks, with some back to back travel. #mtb #enduromtb #enduro #specialized

39.6678136-105.2578443




* #[enduro](https://dentedreality.com.au/tags/enduro/)
* #[enduromtb](https://dentedreality.com.au/tags/enduromtb/)
* #[mtb](https://dentedreality.com.au/tags/mtb/)
* #[specialized](https://dentedreality.com.au/tags/specialized/)

Posted on [Instagram](https://www.instagram.com/p/Bi5qECsFMNz/) [7:47 pm, May 17, 2018](https://dentedreality.com.au/2018/05/17/weekday-ride-to-blow-out-the-cobwebs-last-chance-for-almost-2-weeks-with-some-back-to-back-travel-mtb-enduromtb-enduro-specialized/ "7:47 pm") 
jQuery(document).ready(function(){
var gmap\_m8180875b22b43fbb92ac3431ac3116f9 = {
positions : {
451 : new google.maps.LatLng( '39.667813594234', '-105.25784430977' )
},
bounds : new google.maps.LatLngBounds(), // empty for now, we'll dynamically extend it later
map : new google.maps.Map(
document.getElementById( 'gmap\_m8180875b22b43fbb92ac3431ac3116f9' ),
{
mapTypeId: google.maps.MapTypeId.ROADMAP,
center: new google.maps.LatLng( 0, 0 ),
zoom: 16 // Seems to be a good zoom for a single point
}
),
markers : {},
}; // end of gmap
// Extend the bounds of interest based on our positions
for ( var m in gmap\_m8180875b22b43fbb92ac3431ac3116f9.positions ) {
gmap\_m8180875b22b43fbb92ac3431ac3116f9.bounds.extend( gmap\_m8180875b22b43fbb92ac3431ac3116f9.positions[m] );
}
// Render markers
for ( var m in gmap\_m8180875b22b43fbb92ac3431ac3116f9.positions ) {
gmap\_m8180875b22b43fbb92ac3431ac3116f9.markers[m] = new google.maps.Marker( {
clickable: true,
map : gmap\_m8180875b22b43fbb92ac3431ac3116f9.map,
position : gmap\_m8180875b22b43fbb92ac3431ac3116f9.positions[m]
} );
}
// Redraw map to fit our new marker-based bounds
gmap\_m8180875b22b43fbb92ac3431ac3116f9.map.setCenter( gmap\_m8180875b22b43fbb92ac3431ac3116f9.positions[451] );
});