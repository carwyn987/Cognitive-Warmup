// Define global variables
let pc; // Global RTCPeerConnection
let dc; // Global DataChannel
let EPHEMERAL_KEY; // Global Ephemeral key

let currentFileIndex = 0;
const files = [
    "file1.txt", "file2.txt", "file3.txt", // Add your text files here
];
const filePath = "/data/"; // Directory where your files are stored on the server

async function loadFile(fileName) {
    try {
        const response = await fetch(`${filePath}${fileName}`);
        const text = await response.text();
        return text;
    } catch (error) {
        console.error("Error loading file:", error);
        return null;
    }
}

async function overrideConversationAndStartNewPrompt() {
    // Reset the peer connection
    if (pc) {
        pc.close(); // Close the existing peer connection if it's active
    }

    // Reinitialize the WebRTC connection and data channel
    console.log("Requesting new eph key");
    const tokenResponse = await fetch("http://localhost:3000/session");
    const data = await tokenResponse.json();
    EPHEMERAL_KEY = data.client_secret.value;
    console.log("New Ephemeral key received");

    // Set up a new RTCPeerConnection
    pc = new RTCPeerConnection();
    pc.ontrack = (e) => {
        const audioEl = document.createElement("audio");
        audioEl.autoplay = true;
        audioEl.srcObject = e.streams[0];
        document.body.appendChild(audioEl);
    };

    const ms = await navigator.mediaDevices.getUserMedia({ audio: true });
    pc.addTrack(ms.getTracks()[0]);

    // Set up the data channel
    dc = pc.createDataChannel("oai-events");
    dc.onmessage = (e) => console.log("Realtime event:", JSON.parse(e.data));

    dc.onopen = async () => {
        // Load new prompt based on current file index or user selection
        const promptText = await loadFile(files[currentFileIndex]);
        console.log("Loaded new prompt:", promptText);
        if (promptText) {
            const responseCreate = {
                type: "response.create",
                response: {
                    modalities: ["audio", "text"],
                    instructions: promptText,
                },
            };
            dc.send(JSON.stringify(responseCreate));
        }
    };

    // Create and send offer for the new conversation
    const offer = await pc.createOffer();
    await pc.setLocalDescription(offer);

    const baseUrl = "https://api.openai.com/v1/realtime";
    const sdpResponse = await fetch(`${baseUrl}?model=gpt-4o-realtime-preview-2024-12-17`, {
        method: "POST",
        body: offer.sdp,
        headers: {
            Authorization: `Bearer ${EPHEMERAL_KEY}`,
            "Content-Type": "application/sdp",
        },
    });

    const answer = {
        type: "answer",
        sdp: await sdpResponse.text(),
    };
    await pc.setRemoteDescription(answer);

    console.log("New conversation started with fresh prompt.");
}

document.getElementById("start").addEventListener("click", async () => {
    document.getElementById("previous").disabled = true;
    document.getElementById("start").disabled = true;

    // Load file on start
    const promptText = await loadFile(files[currentFileIndex]);
    if (promptText) {
        console.log("Loaded prompt:", promptText);
    }

    await overrideConversationAndStartNewPrompt();  // Initialize WebRTC and the OpenAI interaction
});

document.getElementById("next").addEventListener("click", async () => {
    if (currentFileIndex < files.length - 1) {
        currentFileIndex++;
        const promptText = await loadFile(files[currentFileIndex]);
        if (promptText) {
            console.log("Loaded next prompt:", promptText);
            await overrideConversationAndStartNewPrompt();
        }
    }

    // Reset start button after navigating to the next file
    document.getElementById("previous").disabled = false;
    document.getElementById("next").disabled = currentFileIndex === files.length - 1;
});

document.getElementById("previous").addEventListener("click", async () => {
    if (currentFileIndex > 0) {
        currentFileIndex--;
        const promptText = await loadFile(files[currentFileIndex]);
        if (promptText) {
            console.log("Loaded next prompt:", promptText);
            await overrideConversationAndStartNewPrompt(promptText);
        }
    }
    document.getElementById("previous").disabled = currentFileIndex === 0;
});