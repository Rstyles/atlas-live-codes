const pokeapiUrl = "https://pokeapi.co/api/v2/pokemon/";

// get the html elements
const searchButton = document.getElementById("search-btn");
const searchInput = document.getElementById("search-box");
const pokemonName = document.querySelector(".pokemon-name");
const pokemonImg = document.querySelector(".pokemon-img");

// add event listener to the search button
searchButton.addEventListener("click", () => {
  let pokemonNameValue = searchInput.value.toLowerCase();
  // check if input is empty
  if (pokemonNameValue === "") {
    alert("Please enter a valid pokemon name");
    return;
  }
  // fetch the pokemon data from the api
  fetch(`${pokeapiUrl}${pokemonNameValue}`)
    // if the response is ok, return the json data
    .then((response) => response.json())
    // and update the html elements
    .then((data) => {
      console.log(data);
      pokemonName.innerHTML = data.name;
      pokemonImg.src = data.sprites.front_default;
    });
});
