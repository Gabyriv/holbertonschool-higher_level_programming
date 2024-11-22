// Script that toggles the class of the header element when the user clicks on the tag id "toggle_header"
document.getElementById('toggle_header').addEventListener('click', function () {
  const element = document.querySelector('header');
  if (element.classList.contains('green')) {
    element.classList.remove('green');
    element.classList.add('red');
  } else {
    element.classList.remove('red');
    element.classList.add('green');
  }
});
