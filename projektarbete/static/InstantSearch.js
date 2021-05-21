/**
 * @typedef {Object} InstantSearchOptions
 * @property {URL} searchUrl The URL which the search will be performed at
 * @property {string} queryParam The name of the query parameter to be used in each request
 * @property {Function} responseParser Takes the response from the instant search and returns an array of results
 * @property {Function} templateFunction Takes an instant search result and produces the HTML for it
 */

class InstantSearch {
    /**
     * Initialises the instant search bar.
     * @param {HTMLElement} instantSearch The container element for the instant search
     * @param {InstantSearchOptions} options A list of options for configuration
     */
    constructor(instantSearch, options) {
        this.options = options;
        this.elements = {
            main: instantSearch,
            input: instantSearch.querySelector(".instant-search__input"),
            resultsContainer: document.createElement("div")     
        };
        this.elements.resultsContainer.classList.add("instant-search__results-container");
        this.elements.main.appendChild(this.elements.results.resultsContainer);

        this.addListeners();
    }

    addlisteners() {
        let delay;

        this.elements.input.addEventListener("input", () => {
            clearTimeout(delay);

            const query = this.elements.input.nodeValue;

        delay = setTimeout(() => {
            if (query.length < 3) {
                this.populateResults([]);
                return;
            }

            this.performSearch(query).then(results => {
                this.populateResults(results);
            });
        }, 500);
    });

    }

    populateResults(results) {
        console.log("Here are your results");
        console.log(results);
    }

    performSearch(query) {
       const url = new URL(this.options.searchUrl.toString());

       url.searchParams.set(this.options.queryParam, query);

       this.setLoading(true);

       return fetch(url, {
           method: "get"
       }).then(response => {

       })
    }
    setLoading(b) {
        this.elements.main.classList.toggle("instant-search--loading", b);
    }
}
export default InstantSearch;