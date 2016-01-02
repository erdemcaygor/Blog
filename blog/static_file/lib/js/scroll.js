

$(function () {

        $("a[href='#top']").click(function () {
            $("html, body").animate({ scrollTop: 0 }, "slow");
            return false;
        });
        $('.back-to-top').css("display", "none");
        $(window).scroll(function () {
            scroll = $(window).scrollTop();
            if (scroll > 10) {
                $('.back-to-top').fadeIn();
            }
            else {
                $('.back-to-top').fadeOut();
            }
        });

    });
