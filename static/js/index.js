// ;;;;;;;;;;;;;;;;;;;;;;;;;sdlfsd;lfksdlkflsdjfksldfgf
// fdgdfgdfgdfgdf


// var par = $(this).parent();
// var value = $('par h2').val()
//	console.log(value);

$(function()
{
//////////////////////////////////////////////////////////////////////
/////////////////////////////////////////////////////////////////// zaynab //////////
//// LOGIN Name
var loginName = $('#userName').text();
console.log("from Index.js:loginame",loginName);
sessionStorage.setItem('loginName', loginName);
//sessionStorage.setItem('webSocket',webSocket );
//////////////// Function Ajxa -- addfriend //////////

$('a.add').click
(
	function ()
	{
		var owner =$('#userName').text();
		var parentTag = $( this ).parent().children();
		var nameFriend = parentTag[0].innerHTML;
		$(this).parent().hide(); //to hide it and remove from all users
		$.ajax({
		method: 'get',
		async: true,
		url: 'http://localhost:8080/addfriend',
		data: {Owner:owner,NameFriend:nameFriend},
		success:function(res)
		{
			//var js=JSON.parse(res);
        return "sss"

	 }
	});
} //end function
);

////////////////////////// remove friend
$('a.remove').click
(
	function()
	{
		var owner =$('#userName').text();
		var parentTag = $( this ).parent().children();
		var nameFriend = parentTag[0].innerHTML;
	  $(this).parent().hide(); //to hide it and remove from all users
		$.ajax({
		method: 'get',
		async: true,
		url: 'http://localhost:8080/removefriend',
		data: {Owner:owner,NameFriend:nameFriend},
		success:function(res)
		{
        console.log("ffffff");

	  }
	});

} //end function
);

//////////////////////// join group
$('a.join').click
(
	function()
	{

		var owner =$('#userName').text();
		var parentTag = $( this ).parent().children();
		var group = parentTag[0].innerHTML;
	  // console.log(parentTag);
		console.log("grouuuuuuup",group);
		console.log(owner);
		$(this).parent().hide(); //to hide it and remove from all users
		$.ajax({
		method: 'get',
		async: true,
		url: 'http://localhost:8080/joingroup',
		data: {Owner:owner,Group:group},
		success:function(res)
		{
			//var js=JSON.parse(res);
			return res;
	 }

	});

} //end function
);

//////////////////////////// leave group

$('a.leave').click
(
	function()
	{

		var owner =$('#userName').text();
		var parentTag = $( this ).parent().children();
		var group = parentTag[0].innerHTML;
	  // console.log(parentTag);
		console.log("grouuuuuuup",group);
		console.log(owner);
		$(this).parent().hide(); //to hide it and remove from all users
		$.ajax({
		method: 'get',
		async: true,
		url: 'http://localhost:8080/leavegroup',
		data: {Owner:owner,Group:group},
		success:function(res)
		{
			//var js=JSON.parse(res);
			console.log(res);
			console.log("llllllllllll");
			return res;
	 }

	});

} //end function
);

/////////////////////////////////////////create Group /////////////
$('a#create').on('click', function(event) {
		event.preventDefault();
		console.log("file file");
		var x = $("input#myfile").val();
		var owner =$('#userName').text();
		var groupName= $("#groupName").val()
		console.log(x);
		console.log(groupName);
		console.log(owner);
		$.ajax({
		method: 'get',
		async: true,
		url: 'http://localhost:8080/createGroup',
		data: {path:x,Group:groupName,Owner:owner},
		success:function(res)
		{
			//var js=JSON.parse(res);
			return res;
	    }
	});

});
///////////////// Form Of Create Group ////////////
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
//////////////////// Page Scroll ///////////////
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















////////////////////////////

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


//////////////////////////////////// sessionStorage /////////////////////////////////
/////////////////////////////////////////////////////////////////// zaynab //////////

}); // End File Of JS
