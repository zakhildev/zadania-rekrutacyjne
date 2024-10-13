// Getting DOM elements
const imageUpload = document.getElementById('imageUpload');
const uploadedImage = document.getElementById('uploadedImage');
const grayscaleCanvas = document.getElementById('grayscaleImage');
const convertButton = document.getElementById('convertGrayscale');

// Event listener for image upload
imageUpload.addEventListener('change', function (event) {
    const file = event.target.files[0];
    if (file) {
        const reader = new FileReader();
        reader.onload = function (e) {
            uploadedImage.src = e.target.result;
        };
        reader.readAsDataURL(file);
    }
});

// Event listener for grayscale conversion
convertButton.addEventListener('click', function () {
    if (uploadedImage.src) {
        const canvas = grayscaleCanvas;
        const ctx = canvas.getContext('2d');
        const image = new Image();
        image.src = uploadedImage.src;

        image.onload = function () {
            canvas.width = image.width;
            canvas.height = image.height;
            ctx.drawImage(image, 0, 0);

            const imageData = ctx.getImageData(0, 0, canvas.width, canvas.height);
            const data = imageData.data;

            // Convert each pixel to grayscale
            for (let i = 0; i < data.length; i += 4) {
                const red = data[i];
                const green = data[i + 1];
                const blue = data[i + 2];
                const gray = 0.3 * red + 0.59 * green + 0.11 * blue;

                data[i] = data[i + 1] = data[i + 2] = gray;
            }

            ctx.putImageData(imageData, 0, 0);
        };
    }
});
