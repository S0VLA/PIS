// parallax.js – эффект параллакса для иконок и логотипа
$(document).ready(function() {
    var $parallaxElements = $('.icons-for-parallax img');
    var $logo = $('.logo');

    $(window).scroll(function() {
        var scrolled = $(window).scrollTop();

        // Иконки движутся с разной скоростью
        $parallaxElements.each(function(index) {
            var speed = 0.15 * (index + 1); // 0.15, 0.3, 0.45
            var yPos = scrolled * speed;
            $(this).css('top', yPos);
        });

        // Логотип движется медленнее
        $logo.css('top', scrolled * 0.05);
    });
});