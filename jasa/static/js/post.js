function setPostHandler(selector, url, attr_data, setUp, checkUp) {
    $(document).on('click', selector, function (e) {
        e.preventDefault();

        var $this = $(this);
        var data = {};
        for (var key of attr_data) {
            console.log(key);
            console.log($this.attr(key))
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
                checkUp(data);
            }
        });
    });
}