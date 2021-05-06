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

    new google.maps.Marker({
        position: {
            lat: 55.609810,
            lng: 13.049821
        },
        map: map,
        title: "Beijersparks Utegym"
    });

    new google.maps.Marker({
        position: {
            lat: 55.583006,
            lng: 12.973176
        },
        map: map,
        title: "Belluvepark Utegym"
    });

    new google.maps.Marker({
        position: {
            lat: 55.541195,
            lng: 13.103805
        },
        map: map,
        title: "Blekeparken Utegym"
    });

    new google.maps.Marker({
        position: {
            lat: 55.597555264364885,
            lng: 13.066041611629956
        },
        map: map,
        title: "Bulltofta Utegym"
    });

    new google.maps.Marker({
        position: {
            lat: 55.57688288117254,
            lng: 12.953503018234438
        },
        map: map,
        title: "Djupadal Utegym"
    });

    new google.maps.Marker({
        position: {
            lat: 55.588996,
            lng: 13.024644
        },
        map: map,
        title: "Enskifteshagen Utegym"
    });

    new google.maps.Marker({
        position: {
            lat: 55.567234,
            lng: 13.007027
        },
        map: map,
        title: "Söderkulla Utegym"
    });

    new google.maps.Marker({
        position: {
            lat: 55.560625,
            lng: 12.977288
        },
        map: map,
        title: "Ymesparks Utegym"
    });

    new google.maps.Marker({
        position: {
            lat: 55.528102,
            lng: 12.935492
        },
        map: map,
        title: "Lilla kalkbrottsparkens Utegym"
    });

    new google.maps.Marker({
        position: {
            lat: 55.561967,
            lng: 13.013856
        },
        map: map,
        title: "Lindängsparkens Utegym"
    });

    new google.maps.Marker({
        position: {
            lat: 55.568967,
            lng: 12.973241
        },
        map: map,
        title: "Hylliesportbyns Utegym"
    });

    new google.maps.Marker({
        position: {
            lat: 55.58897299284127,
            lng: 12.987898930625771
        },
        map: map,
        title: "Skogens Utegym"
    });

    new google.maps.Marker({
        position: {
            lat: 55.590341025830945,
            lng: 12.996623287659554
        },
        map: map,
        title: "Gamlavattentornets Utegym"
    });

    new google.maps.Marker({
        position: {
            lat: 55.600400,
            lng: 12.958758
        },
        map: map,
        title: "Ribbersborgsstrandens Utegym"
    });

    new google.maps.Marker({
        position: {
            lat: 55.59875699738492,
            lng: 12.949274826983462
        },
        map: map,
        title: "Öresunds Funkis"
    });

    new google.maps.Marker({
        position: {
            lat: 55.58954060339584,
            lng: 13.068683236125226
        },
        map: map,
        title: "Videdalsparkens utegym"
    });

    new google.maps.Marker({
        position: {
            lat: 55.519289241048554,
            lng: 12.992806989751623
        },
        map: map,
        title: "Tygelsjös Utegym"
    });

    new google.maps.Marker({
        position: {
            lat: 55.55165794361024,
            lng: 12.923123805726464
        },
        map: map,
        title: "Sundsbroparkens Utegym"
    });

    new google.maps.Marker({
        position: {
            lat: 55.61347201682777,
            lng: 12.983495279665261
        },
        map: map,
        title: "Stapelbäddsparkens Utegym"
    });

    new google.maps.Marker({
        position: {
            lat: 55.60147561963585,
            lng: 13.019981306923125
        },
        map: map,
        title: "Sorgenfris Utegym"
    });

    new google.maps.Marker({
        position: {
            lat: 55.63511765975724,
            lng: 13.053903425796904
        },
        map: map,
        title: "Spillefrids fritidsområde"
    });

    new google.maps.Marker({
        position: {
            lat: 55.57286108007267,
            lng: 12.90537346362973
        },
        map: map,
        title: "Sibbarps Utegym"
    });

    new google.maps.Marker({
        position: {
            lat: 55.61798566320127,
            lng: 12.9758972847988
        },
        map: map,
        title: "Scania parkens Utegym"
    });

    new google.maps.Marker({
        position: {
            lat: 55.60487664119926,
            lng: 13.016942573153438
        },
        map: map,
        title: "Rörsjöparkens Utegym"
    });

    new google.maps.Marker({
        position: {
            lat: 55.585510589798055,
            lng: 13.042115040224564
        },
        map: map,
        title: "Rosengårds Utegym"
    });
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