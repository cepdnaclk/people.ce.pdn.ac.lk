$(document).ready(function () {
  $("#toTopBtn").fadeOut();
  $(window).scroll(function () {
    if ($(this).scrollTop() > 100) {
      $("#toTopBtn").fadeIn();
    } else {
      $("#toTopBtn").fadeOut();
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
