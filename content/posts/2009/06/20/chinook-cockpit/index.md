---
title: Chinook Cockpit
date: '2009-06-20T08:53:24+00:00'
format: image
service: flickr
tags:
- airshow
- challenge
- chinook
- helicopters
- redbull
- sancarlos
- vertical
- verticalchallenge
- verticalchallenge09
image: http://i0.wp.com/dentedreality.com.au/wp-content/uploads/2009/06/3651749190_5ac26e0aba_o.jpg?resize=607%2C455
---

[![Chinook Cockpit](http://i0.wp.com/dentedreality.com.au/wp-content/uploads/2009/06/3651749190_5ac26e0aba_o.jpg?resize=607%2C455)](http://dentedreality.com.au/2009/06/20/chinook-cockpit/) 
# [Chinook Cockpit](http://dentedreality.com.au/2009/06/20/chinook-cockpit/)

San Carlos Airport, CA





* #[airshow](http://dentedreality.com.au/tags/airshow/)
* #[challenge](http://dentedreality.com.au/tags/challenge/)
* #[chinook](http://dentedreality.com.au/tags/chinook/)
* #[helicopters](http://dentedreality.com.au/tags/helicopters/)
* #[redbull](http://dentedreality.com.au/tags/redbull/)
* #[sancarlos](http://dentedreality.com.au/tags/sancarlos/)
* #[vertical](http://dentedreality.com.au/tags/vertical/)
* #[verticalchallenge](http://dentedreality.com.au/tags/verticalchallenge/)
* #[verticalchallenge09](http://dentedreality.com.au/tags/verticalchallenge09/)

Posted on [Flickr](http://www.flickr.com/photos/borkazoid/3651749190/) [8:53 am, June 20, 2009](http://dentedreality.com.au/2009/06/20/chinook-cockpit/ "8:53 am") 
jQuery(document).ready(function(){
var gmap\_m7e41fda19e204beaa52d791914ecd16c = {
positions : {
554 : new google.maps.LatLng( '37.5115', '-122.2505' )
},
bounds : new google.maps.LatLngBounds(), // empty for now, we'll dynamically extend it later
map : new google.maps.Map(
document.getElementById( 'gmap\_m7e41fda19e204beaa52d791914ecd16c' ),
{
mapTypeId: google.maps.MapTypeId.ROADMAP,
center: new google.maps.LatLng( 0, 0 ),
zoom: 16 // Seems to be a good zoom for a single point
}
),
markers : {},
}; // end of gmap
// Extend the bounds of interest based on our positions
for ( var m in gmap\_m7e41fda19e204beaa52d791914ecd16c.positions ) {
gmap\_m7e41fda19e204beaa52d791914ecd16c.bounds.extend( gmap\_m7e41fda19e204beaa52d791914ecd16c.positions[m] );
}
// Render markers
for ( var m in gmap\_m7e41fda19e204beaa52d791914ecd16c.positions ) {
gmap\_m7e41fda19e204beaa52d791914ecd16c.markers[m] = new google.maps.Marker( {
clickable: true,
map : gmap\_m7e41fda19e204beaa52d791914ecd16c.map,
position : gmap\_m7e41fda19e204beaa52d791914ecd16c.positions[m]
} );
}
// Redraw map to fit our new marker-based bounds
gmap\_m7e41fda19e204beaa52d791914ecd16c.map.setCenter( gmap\_m7e41fda19e204beaa52d791914ecd16c.positions[554] );
});