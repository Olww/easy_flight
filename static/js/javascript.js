<script type="text/javascript" src="http://yandex.st/jquery/1.6.0/jquery.min.js"></script>
<script>
alert("ывыв");
$(document).ready(function(){

var pattern = /^([а-я]|[а-я]+-[а-я])/i;

var login = $('#login');



login.blur(function(){

if(login.val() != ''){

if(login.val().search(pattern) == 0){

$('#valid').text('✓');

$('#submit').attr('disabled', false);

login.removeClass('error').addClass('ok');

}else{

$('#valid').text('*Неверный формат');

$('#submit').attr('disabled', true);

login.addClass('error');

}

}else{

$('#valid').text('*Поле не должно быть пустым!');
login.addClass('error');
$('#submit').attr('disabled', true);

}
});
});

$(document).ready(function(){

var pattern = /^[a-z0-9_-]{6,18}$/;

var password = $('#password');



password.blur(function(){

if(password.val() != ''){

if(password.val().search(pattern) == 0){

$('#valid1').text('✓');

$('#submit').attr('disabled', false);

password.removeClass('error1').addClass('ok1');

}else{

$('#valid1').text('*Неверный формат');

$('#submit').attr('disabled', true);

password.addClass('error1');

}

}else{

$('#valid1').text('*Поле не должно быть пустым!');
password.addClass('error1');
$('#submit').attr('disabled', true);

}
});
});

</script>
