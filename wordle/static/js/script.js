console.log("Digimon Wordle loaded!");

let digimons = [];

// Loop para filtrar lo que ponga el usuario , necesito poder sleccionarlo 

document.addEventListener('DOMContentLoaded', () => {
    fetch('/static/data/digimons.json')
        .then(res => res.json())
        .then(data => {
            digimons = data;
    });

    const input = document.getElementById('digimon-search');
    const resultsList = document.getElementById('results');

    input.addEventListener('input', () => {
    const value = input.value.trim().toLowerCase();
    resultsList.innerHTML = '';

    if (value === '') return;

    const matches = digimons.filter(d => d.name.toLowerCase().startsWith(value)).slice(0, 20);


    // Fillea el div abajo
    matches.forEach(d => {
        const li = document.createElement('li');
        li.className = 'list-group-item clickable-digimon';
        li.textContent = `${d.name} — Type: ${d.type}, Attribute: ${d.attribute}`;
        li.dataset.id = d.id;
        resultsList.appendChild(li);
    });
    });


    // Even listener para detectar el click en el que seleccione el usario
    resultsList.addEventListener('click', (e) => {
    const clicked = e.target;
    if (clicked.classList.contains('clickable-digimon')) {
        const digimonId = clicked.dataset.id;
        fetchDigimonDetails(digimonId);
    }
  });
});

function fetchDigimonDetails(id) {
  fetch(`https://digi-api.com/api/v1/digimon/${id}`)  // replace with your actual API endpoint
    .then(res => res.json())
    .then(data => {
      console.log("Digimon API response:", data);

      console.log(data['images'][0]['href'])
      // You can now show this info in a new div or modal
      //document.getElementById('digimon-info').innerText = JSON.stringify(data, null, 2);
      document.getElementById('digimon-info').innerHTML = '<img src="' + data['images'][0]['href'] + '"/>'
    })
    .catch(err => {
    document.getElementById('digimon-info').innerHTML = '<img src="https://digi-api.com/images/digimon/w/Gabumon.png" alt="Dinosaur"/>'

      console.error("Error fetching Digimon data:", err);
    });
}
