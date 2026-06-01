---
title: Denver Meetup
date: '2013-11-17T11:47:58+00:00'
format: image
service: flickr
tags:
- automattic
- colorado
- Denver
- meetup
- mercury
- vision:clouds=099
- vision:mountain=0706
- vision:ocean=0728
- vision:outdoor=099
- vision:sky=099
- vision:sunset=0914
image: http://i2.wp.com/dentedreality.com.au/wp-content/uploads/2013/11/12291564314_7b4f27de7e_o.jpg?resize=607%2C455
---

[![Denver Meetup](http://i2.wp.com/dentedreality.com.au/wp-content/uploads/2013/11/12291564314_7b4f27de7e_o.jpg?resize=607%2C455)](http://dentedreality.com.au/2013/11/17/denver-meetup-23/) 
# [Denver Meetup](http://dentedreality.com.au/2013/11/17/denver-meetup-23/)

Team Mercury meetup (and a few days after) in Denver, Colorado.





* #[automattic](http://dentedreality.com.au/tags/automattic/)
* #[colorado](http://dentedreality.com.au/tags/colorado/)
* #[Denver](http://dentedreality.com.au/tags/denver/)
* #[meetup](http://dentedreality.com.au/tags/meetup/)
* #[mercury](http://dentedreality.com.au/tags/mercury/)
* #[vision:clouds=099](http://dentedreality.com.au/tags/visionclouds099/)
* #[vision:mountain=0706](http://dentedreality.com.au/tags/visionmountain0706/)
* #[vision:ocean=0728](http://dentedreality.com.au/tags/visionocean0728/)
* #[vision:outdoor=099](http://dentedreality.com.au/tags/visionoutdoor099/)
* #[vision:sky=099](http://dentedreality.com.au/tags/visionsky099/)
* #[vision:sunset=0914](http://dentedreality.com.au/tags/visionsunset0914/)

Posted on [Flickr](http://www.flickr.com/photos/borkazoid/12291564314/) [11:47 am, November 17, 2013](http://dentedreality.com.au/2013/11/17/denver-meetup-23/ "11:47 am") 
jQuery(document).ready(function(){
var gmap\_m6b09f774951c8a5c80f8b41dde713dce = {
positions : {
711 : new google.maps.LatLng( '39.712263', '-104.998245' )
},
bounds : new google.maps.LatLngBounds(), // empty for now, we'll dynamically extend it later
map : new google.maps.Map(
document.getElementById( 'gmap\_m6b09f774951c8a5c80f8b41dde713dce' ),
{
mapTypeId: google.maps.MapTypeId.ROADMAP,
center: new google.maps.LatLng( 0, 0 ),
zoom: 16 // Seems to be a good zoom for a single point
}
),
markers : {},
}; // end of gmap
// Extend the bounds of interest based on our positions
for ( var m in gmap\_m6b09f774951c8a5c80f8b41dde713dce.positions ) {
gmap\_m6b09f774951c8a5c80f8b41dde713dce.bounds.extend( gmap\_m6b09f774951c8a5c80f8b41dde713dce.positions[m] );
}
// Render markers
for ( var m in gmap\_m6b09f774951c8a5c80f8b41dde713dce.positions ) {
gmap\_m6b09f774951c8a5c80f8b41dde713dce.markers[m] = new google.maps.Marker( {
clickable: true,
map : gmap\_m6b09f774951c8a5c80f8b41dde713dce.map,
position : gmap\_m6b09f774951c8a5c80f8b41dde713dce.positions[m]
} );
}
// Redraw map to fit our new marker-based bounds
gmap\_m6b09f774951c8a5c80f8b41dde713dce.map.setCenter( gmap\_m6b09f774951c8a5c80f8b41dde713dce.positions[711] );
});