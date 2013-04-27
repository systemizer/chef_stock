$(document).ready(function() {
    init();
})

function init() {
    $('li a.expander').click(function(e) {
	e.preventDefault();
	$(e.target).next().toggle();
	});
}
