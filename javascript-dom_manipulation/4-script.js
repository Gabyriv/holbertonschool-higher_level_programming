// Script that add a "li" element to a list when the user clicks on the element with id "add_item"
document.getElementById('add_item').addEventListener('click', function () {
  const newElement = document.createElement('li');
  const ul = document.querySelector('ul');
  newElement.textContent = 'Item';
  ul.append(newElement);
});
