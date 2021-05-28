// Karta över gym
function initMap() {
    const malmö = {
        lat: 55.60587,
        lng: 13.00073
    };
    const map = new google.maps.Map(document.getElementById("map"), {
        zoom: 11,
        center: malmö,
    });

    const Beijersparkscontent = getInfo('Beijersparks utegym', 'i Kirseberga', '/static/beijerspark-stock.jpg');


    const Beijerspark = new google.maps.Marker({
        position: {
            lat: 55.609810,
            lng: 13.049821
        },
        map: map,
        title: "Beijersparks Utegym"
    });

    const Beijersinfowindow = new google.maps.InfoWindow({
        content: Beijersparkscontent,
    });

    Beijerspark.addListener("click", () => {
        Beijersinfowindow.open(map, Beijerspark);
    });

    const Belluveparkcontent = getInfo('Bellevueparkens utegym', 'i Bellevue', '/static/bellevuepark-stock.jpg');

    const Belluvepark = new google.maps.Marker({
        position: {
            lat: 55.583006,
            lng: 12.973176
        },
        map: map,
        title: "Belluvepark Utegym"
    });

    const Belluveparkinfo = new google.maps.InfoWindow({
        content: Belluveparkcontent,
    });

    Belluvepark.addListener("click", () => {
        Belluveparkinfo.open(map, Belluvepark);
    });

    const Blekeparkcontent = getInfo('Blekeparkens utegym', 'i Oxie', '/static/blekepark-stock.jpg');

    const Blekepark = new google.maps.Marker({
        position: {
        lat: 55.541195,
        lng: 13.103805
        },
        map: map,
        title: "Blekeparken Utegym"
    });

    const Blekeparkinfo = new google.maps.InfoWindow({
    content: Blekeparkcontent,
    });

    Blekepark.addListener("click", () => {
    Blekeparkinfo.open(map, Blekepark);
    });


    const Bulltoftacontent = getInfo('Bulltoftas utegym', 'i Bulltofta', '/static/bulltofta-stock.jpg');

    const Bulltofta = new google.maps.Marker({
        position: {
            lat: 55.597555264364885,
            lng: 13.066041611629956
        },
        map: map,
        title: "Bulltofta Utegym"
    });

    const Bulltoftainfo = new google.maps.InfoWindow({
        content: Bulltoftacontent,
    });

    Bulltofta.addListener("click", () => {
        Bulltoftainfo.open(map, Bulltofta);
    });

    const Djupadalcontent = getInfo('Djupadalsparkens utegym', 'i Djupadal', '/static/Djupadalsparkens_utegym.jpg');

    const Djupadal = new google.maps.Marker({
        position: {
            lat: 55.57688288117254,
            lng: 12.953503018234438
        },
        map: map,
        title: "Djupadal Utegym"
        });

    const Djupadalinfo = new google.maps.InfoWindow({
        content: Djupadalcontent,
    });

    Djupadal.addListener("click", () => {
        Djupadalinfo.open(map, Djupadal);
    });


    const Enskifteshagencontent = getInfo('Enskifteshagens utegym', 'i Östra Sorgenfri', '/static/enskiftehage-stock.jpg');

    const Enskifteshagen = new google.maps.Marker({
        position: {
            lat: 55.588996,
            lng: 13.024644
        },
        map: map,
        title: "Enskifteshagen Utegym"
    });

    const Enskifteshageninfo = new google.maps.InfoWindow({
        content: Enskifteshagencontent,
    });

    Enskifteshagen.addListener("click", () => {
        Enskifteshageninfo.open(map, Enskifteshagen);
    });

    const Söderkullacontent = getInfo('Söderkullas utegym', 'i Söderkulla', '/static/söderkulla-stock.jpg');

    const Söderkulla = new google.maps.Marker({
        position: {
            lat: 55.567234,
            lng: 13.007027
        },
        map: map,
        title: "Söderkulla Utegym"
    });

    const Söderkullainfo = new google.maps.InfoWindow({
        content: Söderkullacontent,
    });

    Söderkulla.addListener("click", () => {
        Söderkullainfo.open(map, Söderkulla);
    });


    const Ymersparkcontent = getInfo('Hyllies utegym', 'i Hyllie', '/static/Hyllies_utegym.jpg');

    const Ymerspark = new google.maps.Marker({
        position: {
            lat: 55.560625,
            lng: 12.977288
        },
        map: map,
        title: "Ymersparks Utegym"
    });

    const Ymersparkinfo = new google.maps.InfoWindow({
        content: Ymersparkcontent,
    });

    Ymerspark.addListener("click", () => {
        Ymersparkinfo.open(map, Ymerspark);
    });

    const Kalkbrottcontent = getInfo('Lilla Kalkbrottsparkens utegym', 'i Klagshamn', '/static/kalkbrott-stock.jpg');

    const Kalkbrott = new google.maps.Marker({
        position: {
            lat: 55.528102,
            lng: 12.935492
        },
        map: map,
        title: "Lilla kalkbrottsparkens Utegym"
    });

    const Kalkbrottinfo = new google.maps.InfoWindow({
        content: Kalkbrottcontent,
    });

    Kalkbrott.addListener("click", () => {
        Kalkbrottinfo.open(map, Kalkbrott);
    });


    const Lindängsparkencontent = getInfo('Lindängsparkens utegym', 'i Lindängen', '/static/lindängpark-stock.jpg');

    const Lindängen = new google.maps.Marker({
        position: {
            lat: 55.561967,
            lng: 13.013856
        },
        map: map,
        title: "Lindängsparkens Utegym"
    });

    const Lindängsparkeninfo = new google.maps.InfoWindow({
        content: Lindängsparkencontent,
    });

    Lindängen.addListener("click", () => {
    Lindängsparkeninfo.open(map, Lindängen);
    });

    const Hylliesportbycontent = getInfo('Hyllie sportbyns utegym', 'i Hyllie', '/static/Hyllie_sportbyns_utegym.jpg');

    const Hylliesportby = new google.maps.Marker({
        position: {
            lat: 55.568967,
            lng: 12.973241
        },
        map: map,
        title: "Hylliesportbyns Utegym"
    });

    const Hylliesportbyinfo = new google.maps.InfoWindow({
        content: Hylliesportbycontent,
    });

    Hylliesportby.addListener("click", () => {
        Hylliesportbyinfo.open(map, Hylliesportby);
    });


    const Skogencontent = getInfo('Skogens utegym', 'i Kronborg', '/static/Skogens_utegym.jpg');

    const Skogen = new google.maps.Marker({
        position: {
            lat: 55.58897299284127,
            lng: 12.987898930625771
        },
        map: map,
        title: "Skogens Utegym"
    });

    const Skogeninfo = new google.maps.InfoWindow({
        content: Skogencontent,
    });

    Skogen.addListener("click", () => {
        Skogeninfo.open(map, Skogen);
    });

    const Gamlavattentornetcontent = getInfo('Gamla vattentornets utegym', 'i Kronborg', '/static/gamla-vattentornet-stock.jpg');

    const Gamlavattentornet = new google.maps.Marker({
        position: {
            lat: 55.590341025830945,
            lng: 12.996623287659554
        },
        map: map,
        title: "Gamlavattentornets Utegym"
    });

    const Gamlavattentornetinfo = new google.maps.InfoWindow({
        content: Gamlavattentornetcontent,
    });

    Gamlavattentornet.addListener("click", () => {
        Gamlavattentornetinfo.open(map, Gamlavattentornet);
    });

    const Ribbersborgsstrandencontent = getInfo('Ribersborgsstrandens utegym', 'i Ribersborgsstranden', '/static/Ribersborgsstrandens_utegym.jpg');

    const Ribbersborgsstranden = new google.maps.Marker({
        position: {
            lat: 55.600400,
            lng: 12.958758
        },
        map: map,
        title: "Ribbersborgsstrandens Utegym"
    });

    const Ribbersborgsstrandinfo = new google.maps.InfoWindow({
        content: Ribbersborgsstrandencontent,
    });

    Ribbersborgsstranden.addListener("click", () => {
        Ribbersborgsstrandinfo.open(map, Ribbersborgsstranden);
    });


    const Öresundcontent = getInfo('Öresunds Funkis', 'i Ribersborgsstranden', '/static/Öresunds_Funkis.jpg');

    const Öresund = new google.maps.Marker({
        position: {
            lat: 55.59875699738492,
            lng: 12.949274826983462
        },
        map: map,
        title: "Öresunds Funkis"
    });

    const Öresundinfo = new google.maps.InfoWindow({
        content: Öresundcontent,
    });

    Öresund.addListener("click", () => {
        Öresundinfo.open(map, Öresund);
    });

    const Videdalsparkencontent = getInfo('Videdalsparkens utegym', 'i Videdal', '/static/videdalspark-stock.jpg');

    const Videdal = new google.maps.Marker({
        position: {
            lat: 55.58954060339584,
            lng: 13.068683236125226
        },
        map: map,
        title: "Videdalsparkens Utegym"
    });

    const Videdalsparkeninfo = new google.maps.InfoWindow({
        content: Videdalsparkencontent,
    });

    Videdal.addListener("click", () => {
        Videdalsparkeninfo.open(map, Videdal);
    });
    const Tygelsjöcontent = getInfo('Tygelsjös utegym', 'i Tygelsjö', '/static/tygelsjö-stock.jpg');

    const Tygelsjö = new google.maps.Marker({
        position: {
            lat: 55.519289241048554,
            lng: 12.992806989751623
        },
        
        map: map,
        title: "Tygelsjös Utegym"
    });

    const Tygelsjöinfo = new google.maps.InfoWindow({
        content: Tygelsjöcontent,
    });

    Tygelsjö.addListener("click", () => {
        Tygelsjöinfo.open(map, Tygelsjö);
    });


    const Sundsbroparkencontent = getInfo('Sundsbroparkens utegym', 'i Bunkeflostrand', '/static/sundsbropark-stock.jpg');

    const Sundsbroparken = new google.maps.Marker({
        position: {
            lat: 55.55165794361024,
            lng: 12.923123805726464
        },
        map: map,
        title: "Sundsbroparkens Utegym"
    });

    const Sundsbroparkeninfo = new google.maps.InfoWindow({
        content: Sundsbroparkencontent,
    });

    Sundsbroparken.addListener("click", () => {
        Sundsbroparkeninfo.open(map, Sundsbroparken);
    });

    const Stapelbäddsparkencontent = getInfo('Stapelbäddsparkens utegym','i Västra Hamnen','/static/Stapelbäddsparkens_utegym.jpg');
       

    const Stapelbäddsparken = new google.maps.Marker({
        position: {
            lat: 55.61347201682777,
            lng: 12.983495279665261
        },
        map: map,
        title: "Stapelbäddsparkens Utegym"
    });

    const Stapelbäddsparkeninfo = new google.maps.InfoWindow({
        content: Stapelbäddsparkencontent,
    });

    Stapelbäddsparken.addListener("click", () => {
        Stapelbäddsparkeninfo.open(map, Stapelbäddsparken);
    });

    const Nydalacontent = getInfo('Nydalaparkens utegym','i Nydala','/static/nydalapark-stock.jpg');
    

    const Nydala = new google.maps.Marker({
        position: {
            lat: 55.572060,
            lng: 13.018071
        },
        map: map,
        title: "Nyadalas Utegym"
    });

    const Nydalainfo = new google.maps.InfoWindow({
        content: Nydalacontent,
    });

    Nydala.addListener("click", () => {
        Nydalainfo.open(map, Nydala);
    });

    const Spillepengcontent = getInfo('Spillepengs fritidsområde','i Spillepengen','/static/spillepeng-stock.jpg');
    

    const Spillepeng = new google.maps.Marker({
        position: {
            lat: 55.63511765975724,
            lng: 13.053903425796904
        },
        map: map,
        title: "Spillepengs fritidsområde"
    });

    const Spillepenginfo = new google.maps.InfoWindow({
        content: Spillepengcontent,
    });

    Spillepeng.addListener("click", () => {
        Spillepenginfo.open(map, Spillepeng);
    });


    const Sibbarpcontent = getInfo('Sibbarps utegym','i Sibbarp','/static/sibbarp-stock.jpg');
    

    const Sibbarp = new google.maps.Marker({
        position: {
            lat: 55.57286108007267,
            lng: 12.90537346362973
        },
        map: map,
        title: "Sibbarps Utegym"
    });

    const Sibbarpinfo = new google.maps.InfoWindow({
        content: Sibbarpcontent,
    });

    Sibbarp.addListener("click", () => {
        Sibbarpinfo.open(map, Sibbarp);
    });

    const Scaniaparkencontent = getInfo('Scaniaparkens utegym','i Västra Hamnen','/static/Scaniaparkens_utegym.jpg');
    

    const Scaniaparken = new google.maps.Marker({
        position: {
            lat: 55.61798566320127,
            lng: 12.9758972847988
        },
        map: map,
        title: "Scania parkens Utegym"
    });

    const Scaniaparkeninfo = new google.maps.InfoWindow({
        content: Scaniaparkencontent,
    });

    Scaniaparken.addListener("click", () => {
        Scaniaparkeninfo.open(map, Scaniaparken);
    });


    const Rörsjöparkencont = getInfo('Rörsjöparkens utegym','i Rörsjöstaden','/static/rörsjöpark-stock.jpg');
   


    const Rörsjöparken = new google.maps.Marker({
        position: {
            lat: 55.60487664119926,
            lng: 13.016942573153438
        },
        map: map,
        title: "Rörsjöparkens Utegym"
    });

    const Rörsjöparkeninfo = new google.maps.InfoWindow({
        content: Rörsjöparkencont,
    });

    Rörsjöparken.addListener("click", () => {
        Rörsjöparkeninfo.open(map, Rörsjöparken);
    });  
    
    const Torupcontent= getInfo('Torups utegym', 'i Torup', '/static/Torups_skogsgym.jpg');

    const Torup = new google.maps.Marker({
        position:{
            lat: 55.56678260698355,
            lng: 13.213829009659957
        },
        map: map,
        title: "Torups Utegym"
    })

    const Torupinfo = new google.maps.InfoWindow({
        content: Torupcontent,
    });

    Torup.addListener("click", () => {
        Torupinfo.open(map, Torup);
    });


    const Rosengårdcontent = getInfo('Rosengårds utegym', 'i Rosengård','/static/rosengård-stock.jpg');
    

    const Rosengård = new google.maps.Marker({
        position: {
            lat: 55.585510589798055,
            lng: 13.042115040224564
        },
        map: map,
        title: "Rosengårds Utegym"
    });

    const Rosengårdinfo = new google.maps.InfoWindow({
        content: Rosengårdcontent,
    });

    Rosengård.addListener("click", () => {
        Rosengårdinfo.open(map, Rosengård);
    });
}

function getInfo(name, description, picture) {    
    info =
    '<div id="content">' +
    '<img id="pictureongym" src="' + picture + '">' +
    '<a href="http://localhost:8000/gym/' + encodeURI(name) +'">' + name + '</a>' +
    '<p>'+ description + '</p>' +
    '</div>';
    console.log(info)
    return info 
} 
// Sökfunktion
function search_gym() {
    let input = document.getElementById('searchbar').value
    input=input.toLowerCase();
    let x = document.getElementsByClassName('gym');
      
    for (i = 0; i < x.length; i++) { 
        if (!x[i].innerHTML.toLowerCase().includes(input)) {
            x[i].style.display="none";
        }
        else {
            x[i].style.display="list-item";                 
        }
    }
}

// Knapp som tar dig längst upp på sidan
const ScrollToTop = document.querySelector("#ScrollToTop");

ScrollToTop.addEventListener("click", function (){
    window.scrollTo({
        top: 0,
        left: 0,
        behavior: "smooth"
    });
});

function popup_review() {
    alert("Tack för din recension!")
}

// Filtreringsknapp
/* When the user clicks on the button,
toggle between hiding and showing the dropdown content */
function dropdownFilterForAverage() {
    document.getElementById("myDropdown").classList.toggle("show");
  }
  
  // Close the dropdown menu if the user clicks outside of it
  window.onclick = function(event) {
    if (!event.target.matches('.dropbtn')) {
      var dropdowns = document.getElementsByClassName("dropdown-content");
      var i;
      for (i = 0; i < dropdowns.length; i++) {
        var openDropdown = dropdowns[i];
        if (openDropdown.classList.contains('show')) {
          openDropdown.classList.remove('show');
        }
      }
    }
  }