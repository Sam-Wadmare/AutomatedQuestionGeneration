const nextButton = document.getElementById("next-btn");
const statusText = document.getElementById("status-text");
const questionBox = document.getElementById("question-box");
const optionsList = document.getElementById("options-list");

nextButton.addEventListener("click", fetchQuestion);

function setLoading(isLoading) {
    nextButton.disabled = isLoading;
    statusText.innerText = isLoading ? "Loading question..." : "";
}

function renderQuestion(data) {
    questionBox.innerText = data.question;
    optionsList.innerHTML = "";

    data.options.forEach(option => {
        const li = document.createElement("li");
        li.innerText = option;
        optionsList.appendChild(li);
    });
}

async function fetchQuestion() {
    setLoading(true);

    try {
        const response = await fetch('/generate');
        if (!response.ok) {
            throw new Error(`Request failed: ${response.status}`);
        }

        const data = await response.json();
        renderQuestion(data);
    } catch (error) {
        questionBox.innerText = "Unable to load question right now.";
        optionsList.innerHTML = "";
        statusText.innerText = `Error: ${error.message}`;
    } finally {
        if (statusText.innerText === "Loading question...") {
            statusText.innerText = "";
        }
        setLoading(false);
    }
}

fetchQuestion();
