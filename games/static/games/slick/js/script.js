$(document).ready(function(){
	$('.slider').slick({
		arrows:true,
		dots:true,
		slidesToShow:3,
		adaptiveHeight: true,
		autoplay:false,
		speed:500,
		autoplaySpeed:800,
		draggable: false,
		infinite: false,
		waitforanimate: false,
		responsive:[
			{
				breakpoint: 768,
				settings: {
					slidesToShow:2
				}
			},
			{
				breakpoint: 550,
				settings: {
					slidesToShow:1
				}
			}
		]
	});
});

