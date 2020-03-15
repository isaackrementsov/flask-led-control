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
                this_button.text(id + ' LED Off');
            }
        });
    }else{
        $.ajax({
            url: '/led_off?color=' + id,
            type: 'post',
            success: response => {
                console.log(response);
                this_button.text(id + ' LED On');
            }
        });
    }
});

blinking.click(function(){
    if(blinking.text() == 'Blinking'){
        $.ajax({
            url: '/led_blink',
            type: 'post',
            success: response => {
                console.log(response);
                blinking.text('Stop Blinking')
            }
        })
    }else{
        $.ajax({
            url: '/led_blink_off',
            type: 'post',
            success: response => {
                console.log(response);
                blinking.text('Blinking');
            }
        });
    }
});
