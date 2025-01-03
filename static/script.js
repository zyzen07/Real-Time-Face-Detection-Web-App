document.getElementById('liveTrackBtn').addEventListener('click', function() {
    window.location.href = '/track';  // Navigate to tracking page
});

document.getElementById('stopBtn').addEventListener('click', function() {
    // Stop the video stream and capture the reaction
    const video = document.getElementById('video');
    const stream = video.srcObject;
    
    if (stream) {
        let tracks = stream.getTracks();
        tracks.forEach(track => track.stop());
    }
    
    video.srcObject = null;

    // Capture face reaction
    fetch('/capture_reaction', { method: 'POST' })
        .then(response => response.json())
        .then(data => {
            document.getElementById('suggestion').innerText = data.suggestion;
        })
        .catch(error => {
            console.error('Error capturing reaction:', error);
        });
});

// Start the video stream when the tracking page loads
window.addEventListener('load', function() {
    const video = document.getElementById('video');
    navigator.mediaDevices.getUserMedia({ video: true })
        .then(stream => {
            video.srcObject = stream;
        })
        .catch(err => {
            console.error('Error accessing the camera: ' + err);
        });
});
