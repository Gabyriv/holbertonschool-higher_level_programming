// Script that updates the text of the header element to "New Header!!!" when the user clicks on the element with id "update_header"
document.getElementById('update_header').addEventListener('click', function () {
  const element = document.querySelector('header');
  element.textContent = 'New Header!!!';
});
