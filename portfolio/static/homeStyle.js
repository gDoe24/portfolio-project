
  $(document).ready(function(){
    var wind = $(window);
    wind.scroll(function(){
    $('header nav').toggleClass('scrolled', $(this).scrollTop()> 400);
     /*$('body').*/
  });
    wind.scroll(function(){
      $('.arrow').toggleClass('scrolled', $(this).scrollTop()> 50);
    });
    $("ul a").hover(function(){
      $(this).toggleClass('hover');
    });
    $('.arrow').click(function(e){
      $('html, body').animate({
        scrollTop: $('#about').offset().top
    },1000);
    })
});