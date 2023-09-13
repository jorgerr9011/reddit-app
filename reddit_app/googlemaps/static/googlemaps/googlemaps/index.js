
function initMap() {
    const map = new google.maps.Map(document.getElementById("map"), {
      zoom: 2,
      center: { lat: 0, lng: 0 },
    });
  
    // Array de países de Europa
    const paisesEuropa = [
        { name: "Reino Unido", lat: 55.3781, lng: -3.4360, subreddit: "r/UK" },
        { name: "España", lat: 40.4637, lng: -3.7492, subreddit: "r/Spain" },
        { name: "Francia", lat: 46.6031, lng: 1.8883, subreddit: "r/France" },
        { name: "Italia", lat: 41.8719, lng: 12.5674, subreddit: "r/Italy" },
        { name: "Portugal", lat: 39.3999, lng: -8.2245, subreddit: "r/Portugal" },
        { name: "Grecia", lat: 39.0742, lng: 21.8243, subreddit: "r/Greece" },
        { name: "Turquía", lat: 38.9637, lng: 35.2433, subreddit: "r/Turkey" },
    ];
  
    // Array de países de Sudamérica
    const paisesSudamerica = [
      { nombre: "Argentina", coordenadas: { lat: -38.416097, lng: -63.616672 }, subreddit: "argentina" },
      // Añadir más países de Sudamérica aquí
    ];
  
    // Función para crear un marcador y enlace para cada país
    function crearMarcador(coordenadas, subreddit) {
      const marker = new google.maps.Marker({
        position: coordenadas,
        map: map,
      });
  
      const infowindow = new google.maps.InfoWindow({
        content: `<a href="https://www.reddit.com/r/${subreddit}" target="_blank">${subreddit}</a>`,
      });
  
      marker.addListener("click", () => {
        infowindow.open(map, marker);
      });
    }
  
    // Crear marcadores y enlaces para los países de Europa
    paisesEuropa.forEach((pais) => {
      crearMarcador(pais.coordenadas, pais.subreddit);
    });
  
    // Crear marcadores y enlaces para los países de Sudamérica
    paisesSudamerica.forEach((pais) => {
      crearMarcador(pais.coordenadas, pais.subreddit);
    });
  }
  
  window.initMap = initMap;
  