document.getElementById('scroll-right').addEventListener('click', function(e) {
  e.preventDefault();
  document.querySelector('.challenge-box').scrollLeft += 440;
});

document.getElementById('scroll-left').addEventListener('click', function(e) {
  e.preventDefault();
  document.querySelector('.challenge-box').scrollLeft -= 440;
});