document.getElementById("inputForm").addEventListener("submit", async (e) => {
    e.preventDefault();

    // Get input data
    const duration = document.getElementById("duration").value;
    const protocol_type = document.getElementById("protocol_type").value;
    const service = document.getElementById("service").value;
    const flag = document.getElementById("flag").value;

    // Send data to the backend API
    const response = await fetch("http://localhost:5000/predict", {
        method: "POST",
        headers: {
            "Content-Type": "application/json",
        },
        body: JSON.stringify({
            duration: duration,
            protocol_type: protocol_type,
            service: service,
            flag: flag,
        }),
    });

    const result = await response.json();
    document.getElementById("result").innerText = `Prediction: ${result.prediction}`;
});