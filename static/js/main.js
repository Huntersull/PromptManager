// Function to expand or contract a prompt
function togglePrompt(promptId) {
    let prompt = document.getElementById(promptId);
    let promptText = prompt.querySelector(".prompt-text");

    if (promptText.style.display === "none") {
        promptText.style.display = "block";
    } else {
        promptText.style.display = "none";
    }
}

// Function to show the 'Add Prompt' form
function showAddPromptForm() {
    let form = document.getElementById("add-prompt-form");
    form.style.display = "block";
}

// Function to hide the 'Add Prompt' form
function hideAddPromptForm() {
    let form = document.getElementById("add-prompt-form");
    form.reset();
    form.style.display = "none";
}

// Function to show the 'Use Prompt' form
function showUsePromptForm(promptId) {
    let form = document.getElementById("use-prompt-form-" + promptId);
    form.style.display = "block";
}

// Function to hide the 'Use Prompt' form
function hideUsePromptForm(promptId) {
    let form = document.getElementById("use-prompt-form-" + promptId);
    form.reset();
    form.style.display = "none";
}
