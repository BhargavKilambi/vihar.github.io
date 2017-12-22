$(document).ready(function(){   
	var scroll_start = 0;
	var startchange = $('#startchange');
	var offset = startchange.offset();
	if (startchange.length){
		$(document).scroll(function() { 
	  		scroll_start = $(this).scrollTop();
	  		if(scroll_start > offset.top) {
	      		$(".navbar-default").css('background-color', '#333');
	      		
	   		} else {
	     		$('.navbar-default').css('background-color', 'transparent');
	     		$(".nav-bar-buttons").css('color', '#fff');
	   		}
		});
	}

	$(".navbar-nav li a").on('click', function(event) {
		// Make sure this.hash has a value before overriding default behavior
		if (this.hash !== "") {
			// Prevent default anchor click behavior
	    	event.preventDefault();
	    	// Store hash
	    	var hash = this.hash;
	    	$('html, body').animate({
	      		scrollTop: $(hash).offset().top
	    	}, 800, function(){
	    	// Add hash (#) to URL when done scrolling (default click behavior)
	      	window.location.hash = hash;
	    });
	  }
	});
});