// Script that fetches and lists the "title" for all movies by using an URL
fetch("https://swapi-api.hbtn.io/api/films/?format=json")
    .then(response => response.json())
    .then(data => {
        const ul = document.getElementById('list_movies');
        data.results.forEach(movie => {
            const li = document.createElement('li');
            li.textContent = movie.title;
            ul.append(li);
        });
    });
