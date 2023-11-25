document.addEventListener("DOMContentLoaded", function () {
    const wordList = document.getElementById("wordList");
    const searchInput = document.getElementById("searchInput");

    // fetch words based on the given search input
    function fetchWords(filter) {
        let endpoint = `/getWords/${filter}`;
        if (!filter) {
            endpoint = "/getWords";
        }

        // Fetch words from endpoint
        fetch(endpoint)
            .then(response => response.json())
            .then(words => {
                // Clear existing word list
                wordList.innerHTML = "";

                words.forEach(word => {
                    const wordElement = document.createElement("div");
                    wordElement.textContent = word.english_word + " - " + word.hungarian_word;
                    wordElement.classList.add("word-card");
                    wordElement.addEventListener("click", () => {
                        console.log("Clicked on word: " + word.english_word);
                    });
                    wordList.appendChild(wordElement);
                });
            })
            .catch(error => console.error("Error fetching words:", error));
    }

    // Initial fetch
    fetchWords("");

    // Event listener for input changes
    searchInput.addEventListener("input", function () {
        const filterValue = this.value.trim();
        fetchWords(filterValue);
    });
});
