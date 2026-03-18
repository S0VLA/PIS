var foldBtns = document.getElementsByClassName("fold-button");

for (var i = 0; i < foldBtns.length; i++) {
    foldBtns[i].addEventListener("click", function(event) {
        var post = event.target;
        while (post && !post.classList.contains('one-post')) {
            post = post.parentElement;
        }
        if (!post) return; // если не нашли (маловероятно)

        if (post.classList.contains('folded')) {
            post.classList.remove('folded');
            event.target.innerHTML = "Свернуть";
        } else {
            post.classList.add('folded');
            event.target.innerHTML = "Развернуть";
        }
    });
}