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
        //fetchDigimonDetails(digimonId);
        checkGuess(digimonId)




    }
  });
});

// Depecrated!!!!
function fetchDigimonDetails(id) {
  fetch(`https://digi-api.com/api/v1/digimon/${id}`) 
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


function checkGuess(digimonId) {
  fetch(`/check_guess/?digimon_id=${encodeURIComponent(digimonId)}`)
  .then(res => res.json())
  .then(data => {
      //console.log("Respuesta:", data);
      add_guess_row(data);
    });
}

//Hay que hacer una funcion para checkGuess que agrege el ROW de la GUESS y dibuje los colorcitos!!!
// Va a recibir la data de checkGuess, es decir, el array de comrpacion y el array del digimon que fue guessed.
function add_guess_row(data){
      // data es un objeto con la info del Digimon + flags correct/incorrect
    // Ejemplo:
    // {
    //   img: "https://digi-api.com/images/digimon/w/Agumon.png",
    //   name: "Agumon",
    //   level: { value: "Rookie/Child", correct: true },
    //   attribute: { value: "Vaccine", correct: false },
    //   type: { value: "Reptile", correct: true },
    //   is_main: { value: "Yes", correct: false },
    //   is_evil: { value: "No", correct: true },
    //   year: { value: "1999", correct: false }
    // }

    info = data['info']
    console.log(info)


    const tbody = document.getElementById("guesses-body");
    const tr = document.createElement("tr");

    /* Adentro del td tien que star esto
    <td><img style="width: 150px;" src="https://digi-api.com/images/digimon/w/Gabumon.png" alt="Dinosaur" /> <br> Gabumon</td>
    <td>Rookie/Child</td>
    <td>Data</td>
    <td>Reptile</td>
    <td>Yes</td>
    <td>No</td>
    <td>1997</td>
    */


    // Columna 1: Imagen + nombre
    const tdImg = document.createElement("td");
    tdImg.innerHTML = `<img style="width: 150px;" src="${info.img}" alt="${info.name}" /> <br>${info.name}`;
    tr.appendChild(tdImg);
    



 

    // Crear y agregar columnas dinámicas
    tr.appendChild(createTd(info.level));
    tr.appendChild(createTd(info.attribute));
    tr.appendChild(createTd(info.type));
    tr.appendChild(createTd(info.priorEvolution));
    tr.appendChild(createTd(info.nextEvolution));
    tr.appendChild(createTd(info.release_date));

    tbody.appendChild(tr);
}

// Funcion que crea un TD y le pone el backgroudn tmb
function createTd(info) {
  const td = document.createElement("td");
  td.textContent = info.value;
  td.classList.add(info.correct ? "correct" : "incorrect");
  return td;
}