import InstantSearch from "/static/InstantSearch.js";

const searchUsers = document.querySelector("#searchUsers");
const instantSearchUsers = new InstantSearch(searchUsers, {
    searchUrl: new URL("http://localhost/gym/{{gym[0]}}", window.location.origin)
    queryParam: "q",
    resultParser: () => {},
    templateFunction: () => {}
});

console.log(instantSearchUsers);