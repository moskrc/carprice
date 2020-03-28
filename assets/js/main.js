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
	$("#requestModal").on("hidden.bs.modal", function(e) {
		$(".modal-form-is-send").fadeOut();
		$("form").trigger("reset");
	});

	// event send form data from model
	$('.btnAction[data-action="send-form-data-modal"]').click(function(e) {
		e.preventDefault();
		$.ajax({
			url: config.urlRequest,
			type: "POST",
			dataType: 'json',
			data: $(".form-data-modal").serialize(),
			success: function(result) {
			},
			error: function(xhr, resp, text) {
				console.log(xhr, resp, text);
			}
		});

		$(".modal-form-is-send").fadeIn();
	});


	$('.btnAction[data-action="send-form-data-main"]').click(function(e) {
		e.preventDefault();
		if (window.innerWidth < 1200) {
			$("#requestModal").modal("toggle");
		} else {
			$.ajax({
				url: config.urlRequest,
				type: "POST",
				dataType: 'json',
				data: $(".form-data-main").serialize(),
				success: function(result) {
				},
				error: function(xhr, resp, text) {
					console.log(xhr, resp, text);
				}
			});

			$(".modal-form-is-send").fadeIn(0, () => {
				$("#requestModal").modal("toggle");
			});
		}
	});

	$('.btnAction[data-action="send-form-data-check"]').click(function(e) {
		e.preventDefault();
		$.ajax({
			url: config.urlRequest,
			type: "POST",
			dataType: 'json',
			data: $(".form-data-check").serialize(),
			success: function(result) {
			},
			error: function(xhr, resp, text) {
				console.log(xhr, resp, text);
			}
		});

		$(".modal-form-is-send").fadeIn(0, () => {
			$("#requestModal").modal("toggle");
		});
	});

});
