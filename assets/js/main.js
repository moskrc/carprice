// const name = "Universe";
//
// console.log(`Hello ${name}! (Javascript ES6)`);

import Aos from "aos";
Aos.init();

$(document).ready(function() {
	if ($(".moving-car")) {
		console.log($(".moving-car")[0].getBoundingClientRect());
	}
});
