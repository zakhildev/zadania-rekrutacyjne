const imageUpload = document.getElementById('imageUpload'); 
const uploadedImage = document.getElementById('uploadedImage'); 
const grayscaleCanvas = document.getElementById('grayscaleImage');
const convertButton = document.getElementById('convertGrayscale'); 

// Task 1: Add event listener for image upload
// When an image is uploaded, you need to display it in the <img> element.
imageUpload.addEventListener('change', function(event) {
    // TODO: Implement logic to handle the file upload and display the image.
    // Hint: Use FileReader to read the uploaded file and set the src of the uploadedImage.
    console.log("Image uploaded"); // For debugging: make sure this fires when an image is selected
});

// Task 2: Add event listener for grayscale conversion
// When the button is clicked, convert the displayed image to grayscale and show it in the canvas.
convertButton.addEventListener('click', function() {
    // TODO: Implement grayscale conversion logic.
    // Hint: Draw the image to the canvas, manipulate pixel data to apply grayscale.
    console.log("Grayscale button clicked"); // For debugging: make sure this fires when button is clicked
});