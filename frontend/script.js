async function classify() {
    const sepalLength = document.getElementById('sepal_length').value;
    const sepalWidth = document.getElementById('sepal_width').value;
    const petalLength = document.getElementById('petal_length').value;
    const petalWidth = document.getElementById('petal_width').value;

    const url = `https://<your-azure-backend-url>/predict?sepal_length=${sepalLength}&sepal_width=${sepalWidth}&petal_length=${petalLength}&petal_width=${petalWidth}`;

    try {
        const response = await fetch(url);
        const data = await response.json();
        document.getElementById('result').innerText = `Prediction: ${data.prediction}`;
    } catch (error) {
        document.getElementById('result').innerText = 'Error in prediction';
    }
}
