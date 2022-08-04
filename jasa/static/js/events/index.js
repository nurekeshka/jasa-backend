// For the like button.
setPostHandler(
    '#like-button', 
    like_url, 
    ['event-id'],
    (data) => {
        if (data.error) {
            alert(data.error);
            return;
        }

        likeButton = $(`#event-${data.eventId} #like-button`);
        likeCount = $(`#event-${data.eventId} .like-count`);

        if (data.state == 'liked') {
            likeButton.html(`<i class="fa-solid fa-heart fa-lg text-danger"></i>`);
        }
        if (data.state == 'unliked') {
            likeButton.html(`<i class="fa-regular fa-heart fa-lg tg-text"></i>`);
        }
        likeCount.text(`${data.likeCount} likes`);
    }
);

// For the bookmark button.
setPostHandler(
    '#bookmark-button', 
    bookmark_url, 
    ['event-id'],
    (data) => {
        if (data.error) {
            alert(data.error);
            return;
        }

        bookmarkButton = $(`#event-${data.eventId} #bookmark-button`);

        if (data.state == 'bookmarked') {
            bookmarkButton.html(`<i class="fa-solid fa-bookmark fa-lg text-warning"></i>`);
        }
        if (data.state == 'unbookmarked') {
            bookmarkButton.html(`<i class="fa-regular fa-bookmark fa-lg tg-text"></i>`);
        }
    }
);