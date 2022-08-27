function setPostHandler(selector, fire_event, url, attr_data, setUp, checkUp) {
    $(document).on(fire_event, selector, function (e) {
        e.preventDefault();

        var $this = $(this);
        var data = {};
        for (var key of attr_data) {
            var value = $this.attr(key);
            if (value) data[key] = value;
        }

        setUp(data);

        $.ajax({
            type: 'POST',
            url: url,
            data: {
                ...data,
                csrfmiddlewaretoken: $('input[name=csrfmiddlewaretoken]').val(),
                action: 'POST'
            },
            success: function(data) {
                switch(data.status) {
                    case 'OK':
                        checkUp(data);
                        break;
                    default:
                        window.location.href = data.redirect;
                        break;
                }
            },
        });
    });
}