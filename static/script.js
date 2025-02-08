// document.getElementById("predictionForm").addEventListener("submit", function(event) {
//     event.preventDefault();

//     let formData = {
//         age: document.getElementById("age").value,
//         gpa: document.getElementById("gpa").value,
//         gender: document.getElementById("gender").value,
//         python: document.getElementById("python").value,
//         sql: document.getElementById("sql").value,
//         java: document.getElementById("java").value,
//         domain: document.getElementById("domain").value,
//         projects: document.getElementById("projects").value
//     };

//     fetch("predict", {  // Change this URL when deploying
//         method: "POST",
//         headers: { "Content-Type": "application/json" },
//         body: JSON.stringify(formData)
//     })
//     .then(response => response.json())
//     .then(data => {
//         document.getElementById("result").innerHTML = "Predicted Career: " + data.prediction;
//     })
//     .catch(error => {
//         console.error("Error:", error);
//         document.getElementById("result").innerHTML = "Error: Could not connect to the server.";
//     });
// });


document.getElementById("predictionForm").addEventListener("submit", function(event) {
    event.preventDefault();  // Prevent default form submission

    // Collect form data
    let formData = {
        age: document.getElementById("age").value,
        gpa: document.getElementById("gpa").value,
        gender: document.getElementById("gender").value,
        python: document.getElementById("python").value,
        sql: document.getElementById("sql").value,
        java: document.getElementById("java").value,
        domain: document.getElementById("domain").value,
        projects: document.getElementById("projects").value
    };

    // Make API request to Flask
    fetch("/predict", {  // 🔹 Make sure Flask API is running
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify(formData)
    })
    .then(response => {
        if (!response.ok) {  // Check for errors
            throw new Error("Server error. Please try again later.");
        }
        return response.json();
    })
    .then(data => {
        document.getElementById("result").innerHTML = 
            `<span style="color:purple; font-weight:bold;">Predicted Career:</span> ${data.prediction}`;
    })
    .catch(error => {
        console.error("Error:", error);
        document.getElementById("result").innerHTML = 
            `<span style="color:red;">Error: Could not connect to the server.</span>`;
    });
});
