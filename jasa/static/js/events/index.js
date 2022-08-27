// For the like button.
setPostHandler(
    '#like-button',
    'click',
    like_url, 
    ['data-event-id'],
    (data) => {
        let eventId = data['event-id'];
        let article = $(`#event-${eventId}`);
        let likeIcon = article.find('#like-button i');
        let likeCount = article.find('#like-counter');
        let count = parseInt(likeCount.attr('data-count'));

        likeIcon.toggleClass('_selected');
        likeIcon.toggleClass('fa-solid fa-regular text-danger tg-text-color pulse');

        if (likeIcon.hasClass('_selected')) {
            count += 1;
        } else {
            count -= 1;
        }
        likeCount.attr('data-count', count);
        likeCount.text(`${count} likes`);
    },
    (data) => {
        if (data['error']) {
            alert(data['error']);
            return;
        }
        let likeCount = $(`#event-${data['event-id']} #like-counter`);

        likeCount.attr('data-count', data['count']);
        likeCount.text(`${data['count']} likes`);
    }
);

// For the bookmark button.
setPostHandler(
    '#bookmark-button',
    'click',
    bookmark_url,
    ['data-event-id'],
    (data) => {
        let eventId = data['event-id'];
        let article = $(`#event-${eventId}`);
        let bookmarkIcon = article.find('#bookmark-button i');

        bookmarkIcon.toggleClass('_selected');
        bookmarkIcon.toggleClass('fa-solid fa-regular tg-text-color text-warning')
    },
    (data) => {
        if (data['error']) {
            alert(data['error']);
            return;
        }
    }
);