// Get references to video element and capture button
const video = document.getElementById('video');
const captureButton = document.getElementById('capture-btn');

// Access user's camera
navigator.mediaDevices.getUserMedia({ video: true })
    .then(function(stream) {
        // Display camera stream in video element
        video.srcObject = stream;
    })
    .catch(function(err) {
        console.error('Error accessing camera:', err);
    });

// Capture image from video stream
captureButton.addEventListener('click', function() {
    // Create a canvas element to hold the captured image
    const canvas = document.createElement('canvas');
    canvas.width = video.videoWidth;
    canvas.height = video.videoHeight;
    canvas.getContext('2d').drawImage(video, 0, 0, canvas.width, canvas.height);

    // Convert canvas content to base64 data URL
    const imageDataUrl = canvas.toDataURL('image/jpeg');

    // Send captured image to Flask server using AJAX
    $.ajax({
        type: 'POST',
        url: '/capture',
        data: { image_data: imageDataUrl },
        success: function(response) {
            console.log('Image captured successfully:', response);
        },
        error: function(xhr, status, error) {
            console.error('Error capturing image:', error);
        }
    });
});