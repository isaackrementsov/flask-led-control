var button = $('.led_button');

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
