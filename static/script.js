function rollDice() {
    fetch('/roll')
    .then(response => response.json())
    .then(data => {
        document.getElementById('diceImage').src = data.image_url;
    })
    .catch(error => console.error('Error:', error));
}
