document.getElementById("printbutton").addEventListener("click", function() {
    // Fetch the data from the server
    fetch('/download-data')
        .then(response => response.json())
        .then(data => {
            const filename = createName(data);

            // Use the data in your JavaScript logic
            const jsonData = JSON.stringify(data, null, 2);

            // Create an invisible anchor element with the custom filename
            const a = document.createElement("a");
            a.href = "data:application/json;charset=utf-8," + encodeURIComponent(jsonData);
            a.download = filename; // Set the filename from the JSON data
            a.style.display = "none";

            // Add the anchor to the document and trigger the download
            document.body.appendChild(a);
            a.click();

            // Clean up the anchor element
            document.body.removeChild(a);
        });
});

function createName(data) {
    const today = new Date();
    let year = today.getFullYear();
    let month = today.getMonth() + 1;
    let day = today.getDate();
    return `${data["Felhasználó"]} ${year}.${month}.${day}. VerbVenture Eredmény.json`;
}