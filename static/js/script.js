document.addEventListener('DOMContentLoaded', () => {
    const urlInput = document.getElementById('urlInput');
    const downloadBtn = document.getElementById('downloadBtn');
    const loader = document.getElementById('loader');
    const resultSection = document.getElementById('resultSection');
    const errorMsg = document.getElementById('errorMsg');
    const errorText = document.getElementById('errorText');

    const videoCover = document.getElementById('videoCover');
    const authorName = document.getElementById('authorName');
    const videoTitle = document.getElementById('videoTitle');
    const downloadVideo = document.getElementById('downloadVideo');
    const downloadMusic = document.getElementById('downloadMusic');

    downloadBtn.addEventListener('click', async () => {
        const url = urlInput.value.trim();

        if (!url) {
            showError("Please paste a valid TikTok link.");
            return;
        }

        // Reset UI
        hideError();
        resultSection.classList.add('hidden');
        loader.classList.remove('hidden');

        try {
            const response = await fetch('/download', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify({ url: url })
            });

            const data = await response.json();

            if (data.success) {
                showResult(data.data);
            } else {
                showError(data.message || "Failed to fetch video.");
            }

        } catch (error) {
            showError("An error occurred. Please try again later.");
            console.error(error);
        } finally {
            loader.classList.add('hidden');
        }
    });

    function showResult(data) {
        videoCover.src = data.cover;
        authorName.textContent = data.author || "@unknown";
        videoTitle.textContent = data.title || "No Title";

        downloadVideo.href = data.play;
        downloadMusic.href = data.music;

        resultSection.classList.remove('hidden');
    }

    function showError(msg) {
        errorText.textContent = msg;
        errorMsg.classList.remove('hidden');
    }

    function hideError() {
        errorMsg.classList.add('hidden');
    }
});
