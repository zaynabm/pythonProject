$(".chatting").hide();
$(function() {
    $('a.page-scroll').bind('click', function(event) {
        var $anchor = $(this);
        $('html, body').stop().animate({
            scrollTop: $($anchor.attr('href')).offset().top
        }, 1500, 'easeInOutExpo');
        event.preventDefault();
    });
});

// Highlight the top nav as scrolling occurs
$('body').scrollspy({
    target: '.navbar-fixed-top'
})

// Closes the Responsive Menu on Menu Item Click
$('.navbar-collapse ul li a').click(function() {
    $('.navbar-toggle:visible').click();
});

var scrol = $("#scroll");    
    
$(window).scroll(function(){
    
    
    if($(this).scrollTop() >= 100)
    {
        $('nav').css("background-color","#222");
        $('ul').css("padding-bottom","20px");
    
    }
    
    else {
       
        $('nav').css("background-color","transparent");
    }
     
    
});

var x = $(".del");
console.log(x);


$(".del").click(
	function()
{
	$(this).parent().hide();
}
);

$(".add").click(
	function()
{
	$(this).parent().hide();
    $("#test").append("<div class='col col-lg-3 col-sm-6 col-xs-12' style='margin-top: -290px ; padding-right: 100px'><div class='groups_box'><h2 class='text-danger'> Fashion </h2><a href='#chatting'><img class='img-thumbnail chat' src='images/111.jpg'> </a><a class='btn btn-danger del'> Leave Group </a></div></div>");
   
}
);

     $(function () {
    $('a[href="#chatting"]').on('click', function(event) {
        event.preventDefault();
        $('#chatting').addClass('open');
       // $('#chatting > form > input[type="search"]').focus();
    });
    
    $('#chatting, #chatting button.close').on('click keyup', function(event) {
        if (event.target == this || event.target.className == 'close' || event.keyCode == 27) {
            $(this).removeClass('open');
        }
    });
});

$(function () {
    $('a[href="#group-form"]').on('click', function(event) {
        event.preventDefault();
        $('#group-form').addClass('open');
       // $('#chatting > form > input[type="search"]').focus();
    });
    
    $('#group-form, #group-form button.close').on('click keyup', function(event) {
        if (event.target == this || event.target.className == 'close' || event.keyCode == 27) {
            $(this).removeClass('open');
        }
    });
});




$(document).on('click', '.panel-heading span.icon_minim', function (e) {
    var $this = $(this);
    if (!$this.hasClass('panel-collapsed')) {
        $this.parents('.panel').find('.panel-body').slideUp();
        $this.addClass('panel-collapsed');
        $this.removeClass('glyphicon-minus').addClass('glyphicon-plus');
    } else {
        $this.parents('.panel').find('.panel-body').slideDown();
        $this.removeClass('panel-collapsed');
        $this.removeClass('glyphicon-plus').addClass('glyphicon-minus');
    }
});
$(document).on('focus', '.panel-footer input.chat_input', function (e) {
    var $this = $(this);
    if ($('#minim_chat_window').hasClass('panel-collapsed')) {
        $this.parents('.panel').find('.panel-body').slideDown();
        $('#minim_chat_window').removeClass('panel-collapsed');
        $('#minim_chat_window').removeClass('glyphicon-plus').addClass('glyphicon-minus');
    }
});
$(document).on('click', '#new_chat', function (e) {
    var size = $( ".chat-window:last-child" ).css("margin-left");
     size_total = parseInt(size) + 400;
    alert(size_total);
    var clone = $( "#chat_window_1" ).clone().appendTo( ".container" );
    clone.css("margin-left", size_total);
});

$(document).on('click', '.icon_close', function (e) {
    //$(this).parent().parent().parent().parent().remove();
    $( "#chat_window_1" ).remove();
});


$("div.base_sent").hide();

$("#btn-chat").click(

	function()
		{
            event.preventDefault();
			value = $("input").val();
			$("div.base_sent").show();
			$("div.base_sent p").append(value + "\n");   
		}
);
