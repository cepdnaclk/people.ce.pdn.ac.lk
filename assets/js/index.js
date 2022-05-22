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

// // For Tool Tips
var tooltipTriggerList = [].slice.call(document.querySelectorAll('[data-bs-toggle-tooltip="tooltip"]'))
var tooltipList = tooltipTriggerList.map(function (tooltipTriggerEl) {
  return new bootstrap.Tooltip(tooltipTriggerEl)
})
//
// // Popover
// var popoverTriggerList = [].slice.call(document.querySelectorAll('[data-bs-toggle="popover"]'))
// var popoverList = popoverTriggerList.map(function (popoverTriggerEl) {
//   return new bootstrap.Popover(popoverTriggerEl)
// })
