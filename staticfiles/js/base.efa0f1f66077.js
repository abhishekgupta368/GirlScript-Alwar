$(document).ready(function () {


	let button = $("#show-more")

	if ($('.core-team-li').length > 3) {

		$('.core-team-li').each(function (index) {
			let listItem = $(this);
			if (index > 2) {
				listItem.toggle();
			}
		})
	}

	button.on("click", function (e) {
		if ($('.core-team-li').length > 3) {

			$('.core-team-li').each(function (index) {
				let listItem = $(this);
				if (index > 2) {
					listItem.toggle();
				}
			});
		}
	});
});