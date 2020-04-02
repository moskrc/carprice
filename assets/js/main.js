// const name = "Universe";
//
// console.log(`Hello ${name}! (Javascript ES6)`);

import Aos from "aos";
Aos.init();

import PhotoSwipe from "photoswipe";
import PhotoSwipeUI_Default from "photoswipe/dist/photoswipe-ui-default";

import config from "./config";



var openPhotoSwipe = function(num = -1) {
	var pswpElement = document.querySelectorAll('.pswp')[0];
	var options = {
		// history & focus options are disabled on CodePen
		index: num,
		history: false,
		focus: false,

		getThumbBoundsFn: function(index) {
			console.log(index)
			// find thumbnail element
			var thumbnail = document.querySelectorAll('.block-cars-wrapper-list__item')[index];

			// get window scroll Y
			var pageYScroll = window.pageYOffset || document.documentElement.scrollTop;
			var rect = thumbnail.getBoundingClientRect();
			console.log({
				x:rect.left,
				y:rect.top + pageYScroll,
				w:rect.width
			})
			return {
				x:rect.left,
				y:rect.top + pageYScroll,
				w:rect.width
			};
		}
	};
	var gallery = new PhotoSwipe( pswpElement, PhotoSwipeUI_Default, carSlidesWithPictures, options);
	gallery.init();
};

// document.getElementById('btn').onclick = openPhotoSwipe;



$(document).ready(function() {
	// modal map
	$('.btnAction[data-action="open-map"]').click(function(e) {
		$("#map-modal").modal("toggle");
	});

	// hook for close modal
	$(".modal").on("hidden.bs.modal", function(e) {
		$(".modal-form-is-send").fadeOut();
		$("form").trigger("reset");
	});

	// event send form data from model
	$(".form-data-modal").submit(function(e) {
		e.preventDefault();

		var formDataModal = new FormData($(".form-data-modal")[0]);
		$.ajax({
			url: config.urlRequest,
			type: "POST",
			dataType: "json",
			data: formDataModal,
			processData: false,
			contentType: false,
			xsrfCookieName: "csrftoken",
			xsrfHeaderName: "X-CSRFToken",
			success: function(result) {
				$(".modal-form-is-send").fadeIn();
			},
			error: function(xhr, resp, text) {
				console.log(xhr, resp, text);
			}
		});
	});

	$('.btnAction[data-action="send-form-data-main"]').click(function(e) {
		e.preventDefault();
		if (window.innerWidth < 1200) {
			$("#requestModal").modal("toggle");
		} else {
			$(".form-data-main").submit();
		}
	});

	$(".form-data-main").submit(function(e) {
		e.preventDefault();
		var formDataMain = new FormData($(".form-data-main")[0]);
		$.ajax({
			url: config.urlRequest,
			type: "POST",
			dataType: "json",
			data: formDataMain,
			processData: false,
			contentType: false,
			xsrfCookieName: "csrftoken",
			xsrfHeaderName: "X-CSRFToken",
			success: function(result) {
				$(".modal-form-is-send").fadeIn(0, () => {
					$("#requestModal").modal("toggle");
				});
			},
			error: function(xhr, resp, text) {
				console.log(xhr, resp, text);
			}
		});
	});

	$(".form-data-check").submit(function(e) {
		e.preventDefault();
		var formDataMain = new FormData($(".form-data-check")[0]);
		$.ajax({
			url: config.urlRequest,
			type: "POST",
			dataType: "json",
			data: formDataMain,
			processData: false,
			contentType: false,
			xsrfCookieName: "csrftoken",
			xsrfHeaderName: "X-CSRFToken",
			success: function(result) {
				$(".modal-form-is-send").fadeIn(0, () => {
					$("#requestModal").modal("toggle");
				});
			},
			error: function(xhr, resp, text) {
				console.log(xhr, resp, text);
			}
		});
	});

	$('.btnAction[data-action="open-callback-form"]').click(function(e) {
		$("#callbackModal").modal("toggle");
	});

	$(".form-data-modal-callback").submit(function(e) {
		e.preventDefault();
		var formDataMain = new FormData($(".form-data-modal-callback")[0]);
		$.ajax({
			url: config.urlRequest,
			type: "POST",
			dataType: "json",
			data: formDataMain,
			processData: false,
			contentType: false,
			xsrfCookieName: "csrftoken",
			xsrfHeaderName: "X-CSRFToken",
			success: function(result) {
				$(".modal-form-is-send").fadeIn();
			},
			error: function(xhr, resp, text) {
				console.log(xhr, resp, text);
			}
		});
	});

	$('.btnAction[data-open-slider="true"]').click(function(e) {
		// $("#modalSliderCars").modal("show");
		// $("#carouselCars").carousel(
		// 	parseInt($(this).attr("data-open-slider-number"), 10)
		// );
		openPhotoSwipe(
			parseInt($(this).attr("data-open-slider-number"), 10)
		);
	});
});
