// Function to copy the filled prompt to clipboard
function copyToClipboard(text) {
    let dummy = document.createElement("textarea");
    document.body.appendChild(dummy);
    dummy.value = text;
    dummy.select();
    document.execCommand("copy");
    document.body.removeChild(dummy);

    showCopiedMessage();
}

// Function to show the 'Copied to Clipboard' message
function showCopiedMessage() {
    let message = document.getElementById("copied-message");
    message.style.display = "block";

    setTimeout(function() {
        message.style.display = "none";
    }, 2000);
}
