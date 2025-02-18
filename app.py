from flask import Flask, render_template, jsonify, url_for
import random

app = Flask(__name__)

@app.route('/')
def index():
    """Render the main dice rolling page."""
    return render_template('index.html')

@app.route('/roll')
def roll_dice():
    """Generate a random dice roll and return the corresponding image."""
    dice_value = random.randint(1, 6)
    image_filename = f'Dice/Dice{dice_value}.jpeg'  # Match your filenames
    image_url = url_for('static', filename=image_filename)
    return jsonify({'dice_value': dice_value, 'image_url': image_url})

if __name__ == '__main__':
    app.run(debug=True)
