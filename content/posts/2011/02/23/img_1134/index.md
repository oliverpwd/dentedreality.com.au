---
title: IMG_1134
date: '2011-02-23T09:42:23-07:00'
format: image
service: flickr
tags:
- newyork
- newyorkcity
- NYC
latitude: '40.709'
longitude: '-74.0005'
image: https://dentedreality-content.s3.amazonaws.com/wp-content/uploads/2011/02/14190133/5802059763_52f8b88920_o.jpg
---

[![IMG_1134](https://dentedreality-content.s3.amazonaws.com/wp-content/uploads/2011/02/14190133/5802059763_52f8b88920_o.jpg)](https://dentedreality.com.au/2011/02/23/img_1134/) 
# [IMG\_1134](https://dentedreality.com.au/2011/02/23/img_1134/)

[![IMG_1134](https://dentedreality-content.s3.amazonaws.com/wp-content/uploads/2011/02/14190133/5802059763_52f8b88920_o.jpg)](http://www.flickr.com/photos/borkazoid/5802059763/)

40.709-74.0005




* #[newyork](https://dentedreality.com.au/tags/newyork/)
* #[newyorkcity](https://dentedreality.com.au/tags/newyorkcity/)
* #[NYC](https://dentedreality.com.au/tags/nyc/)

Posted on [Flickr](http://www.flickr.com/photos/borkazoid/5802059763/) [9:42 am, February 23, 2011](https://dentedreality.com.au/2011/02/23/img_1134/ "9:42 am") 
jQuery(document).ready(function(){
var gmap\_m896b53e4f5557c53c30209fe39290ca7 = {
positions : {
82 : new google.maps.LatLng( '40.709', '-74.0005' )
},
bounds : new google.maps.LatLngBounds(), // empty for now, we'll dynamically extend it later
map : new google.maps.Map(
document.getElementById( 'gmap\_m896b53e4f5557c53c30209fe39290ca7' ),
{
mapTypeId: google.maps.MapTypeId.ROADMAP,
center: new google.maps.LatLng( 0, 0 ),
zoom: 16 // Seems to be a good zoom for a single point
}
),
markers : {},
}; // end of gmap
// Extend the bounds of interest based on our positions
for ( var m in gmap\_m896b53e4f5557c53c30209fe39290ca7.positions ) {
gmap\_m896b53e4f5557c53c30209fe39290ca7.bounds.extend( gmap\_m896b53e4f5557c53c30209fe39290ca7.positions[m] );
}
// Render markers
for ( var m in gmap\_m896b53e4f5557c53c30209fe39290ca7.positions ) {
gmap\_m896b53e4f5557c53c30209fe39290ca7.markers[m] = new google.maps.Marker( {
clickable: true,
map : gmap\_m896b53e4f5557c53c30209fe39290ca7.map,
position : gmap\_m896b53e4f5557c53c30209fe39290ca7.positions[m]
} );
}
// Redraw map to fit our new marker-based bounds
gmap\_m896b53e4f5557c53c30209fe39290ca7.map.setCenter( gmap\_m896b53e4f5557c53c30209fe39290ca7.positions[82] );
});