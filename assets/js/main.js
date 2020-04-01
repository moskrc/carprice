// const name = "Universe";
//
// console.log(`Hello ${name}! (Javascript ES6)`);

import Aos from "aos";
Aos.init();

import config from "./config";

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
			dataType: 'json',
			data: formDataModal,
			processData: false,
			contentType: false,
			headers: { 'Content-Type': 'multipart/form-data' },
			xsrfCookieName: 'csrftoken',
			xsrfHeaderName: 'X-CSRFToken',
			success: function(result) {
				$(".modal-form-is-send").fadeIn();
			},
			error: function(xhr, resp, text) {
				console.log(xhr, resp, text);
			}
		});
	});



	$(".form-data-main").submit(function(e) {
		e.preventDefault();
		if (window.innerWidth < 1200) {
			$("#requestModal").modal("toggle");
		} else {
			var formDataMain = new FormData($(".form-data-main")[0]);
			$.ajax({
				url: config.urlRequest,
				type: "POST",
				dataType: 'json',
				data: formDataMain,
				processData: false,
				contentType: false,
				headers: { 'Content-Type': 'multipart/form-data' },
				xsrfCookieName: 'csrftoken',
				xsrfHeaderName: 'X-CSRFToken',
				success: function(result) {
					$(".modal-form-is-send").fadeIn(0, () => {
						$("#requestModal").modal("toggle");
					});
				},
				error: function(xhr, resp, text) {
					console.log(xhr, resp, text);
				}
			});
		}
	});

	$(".form-data-check").submit(function(e) {
		e.preventDefault();
		var formDataMain = new FormData($(".form-data-check")[0]);
		$.ajax({
			url: config.urlRequest,
			type: "POST",
			dataType: 'json',
			data: formDataMain,
			processData: false,
			contentType: false,
			headers: { 'Content-Type': 'multipart/form-data' },
			xsrfCookieName: 'csrftoken',
			xsrfHeaderName: 'X-CSRFToken',
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
		var formDataMain = new FormData($(".form-data-modal-callback")[0]);
		$.ajax({
			url: config.urlRequest,
			type: "POST",
			dataType: 'json',
			data: formDataMain,
			processData: false,
			contentType: false,
			headers: {'Content-Type': 'multipart/form-data'},
			xsrfCookieName: 'csrftoken',
			xsrfHeaderName: 'X-CSRFToken',
			success: function (result) {
				$(".modal-form-is-send").fadeIn();
			},
			error: function (xhr, resp, text) {
				console.log(xhr, resp, text);
			}
		});
	});
});
