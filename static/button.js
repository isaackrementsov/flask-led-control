var button = $('#led_button');

button.click(() => {
    console.log(button.text());

    if(button.text() == 'LED On'){
        $.ajax({
            url: '/led_on',
            type: 'post',
            success: response => {
                console.log(response);
                button.text('LED Off');
            }
        });
    }else{
        $.ajax({
            url: '/led_off',
            type: 'post',
            success: response => {
                console.log(response);
                button.text('LED On');
            }
        });
    }
});
