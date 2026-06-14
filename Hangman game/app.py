import random
from flask import Flask, jsonify, render_template, request

app = Flask(__name__)

# Game data
WORDS = [
    "create",
    "hangman",
    "game",
    "python",
    "developer",
    "javascript",
    "database",
    "interface",
    "software",
    "algorithm",
]
MAX_LIVES = 6

# In-memory storage for the current game session
game_state = {
    "secret_word": "",
    "guessed_letters": [],
    "lives_left": MAX_LIVES,
}


def get_masked_word():
    """Returns the word with underscores for unguessed letters."""
    return [
        letter if letter in game_state["guessed_letters"] else "_"
        for letter in game_state["secret_word"]
    ]


@app.route("/")
def index():
    # Serves the main HTML webpage
    return render_template("index.html")


@app.route("/api/new-game", methods=["POST"])
def new_game():
    """Resets the game state with a new word."""
    game_state["secret_word"] = random.choice(WORDS).lower()
    game_state["guessed_letters"] = []
    game_state["lives_left"] = MAX_LIVES

    return jsonify(
        {
            "word_display": get_masked_word(),
            "lives_left": game_state["lives_left"],
            "max_lives": MAX_LIVES,
            "status": "playing",
        }
    )


@app.route("/api/guess", methods=["POST"])
def guess_letter():
    """Processes a single letter guess."""
    data = request.get_json()
    letter = data.get("letter", "").lower().strip()

    # Validations
    if not letter or len(letter) != 1 or not letter.isalpha():
        return jsonify({"error": "Invalid letter input"}), 400

    if letter in game_state["guessed_letters"]:
        return jsonify({"error": "Letter already guessed"}), 400

    # Process guess
    game_state["guessed_letters"].append(letter)
    if letter not in game_state["secret_word"]:
        game_state["lives_left"] -= 1

    # Check Win / Loss Status
    word_display = get_masked_word()
    if "_" not in word_display:
        status = "won"
    elif game_state["lives_left"] <= 0:
        status = "lost"
    else:
        status = "playing"

    response = {
        "word_display": word_display,
        "lives_left": game_state["lives_left"],
        "status": status,
        "correct": letter in game_state["secret_word"],
    }

    # If lost, reveal the word
    if status == "lost":
        response["secret_word"] = game_state["secret_word"]

    return jsonify(response)


if __name__ == "__main__":
    app.run(debug=True, port=5000)