// Blinking code is included from lines 33-57

var button = $('.led_button');
var blinking = $('#led_blink');

button.click(function(){
    let this_button = $(this);
    let id = this_button.attr('id');

    if(this_button.text() == id + ' LED On'){
        $.ajax({
            url: '/led_on?color=' + id,
            type: 'post',
            success: response => {
                console.log(response);
		this_button.addClass('active');
                this_button.text(id + ' LED Off');
            }
        });
    }else{
        $.ajax({
            url: '/led_off?color=' + id,
            type: 'post',
            success: response => {
                console.log(response);
		this_button.removeClass('active');
                this_button.text(id + ' LED On');
            }
        });
    }
});

// Blinking code
blinking.click(function(){
    if(blinking.text() == 'Blinking'){
        $.ajax({
            url: '/led_blink',
            type: 'post',
            success: response => {
                console.log(response);
		blinking.addClass('active');
                blinking.text('Stop Blinking');
            }
        })
    }else{
        $.ajax({
            url: '/led_blink_off',
            type: 'post',
            success: response => {
                console.log(response);
		blinking.removeClass('active');
                blinking.text('Blinking');
            }
        });
    }
});
