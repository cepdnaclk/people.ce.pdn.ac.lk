$(document).ready(function () {
  $(".bottomButtons").fadeOut();
  $(window).scroll(function () {
    if ($(this).scrollTop() > 100) {
      $(".bottomButtons").fadeIn();
    } else {
      $(".bottomButtons").fadeOut();
    }
  });

  $("#toTopBtn").click(function () {
    $("html, body").animate(
      {
        scrollTop: 0,
      },
      10
    );
    return false;
  });
});
