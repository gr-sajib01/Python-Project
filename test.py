import time
import threading
import ipywidgets as widgets
from IPython.display import display

GAME_TIME = 10

# Game state
p1_score = 0
p2_score = 0
game_running = False
timer_thread = None

# UI
timer_label = widgets.Label(value=f"⏱️ Time left: {GAME_TIME}s")
score_label = widgets.Label(value="Player 1: 0 | Player 2: 0")
result_label = widgets.Label(value="")

p1_button = widgets.Button(description="👆 Player 1 Click", button_style="primary")
p2_button = widgets.Button(description="👆 Player 2 Click", button_style="danger")
start_button = widgets.Button(description="🚀 Start Game", button_style="success")


def update_score():
    score_label.value = f"Player 1: {p1_score} | Player 2: {p2_score}"


def p1_click(b):
    global p1_score
    if game_running:
        p1_score += 1
        update_score()


def p2_click(b):
    global p2_score
    if game_running:
        p2_score += 1
        update_score()


def run_timer():
    global game_running

    for t in range(GAME_TIME, -1, -1):
        if not game_running:
            return  # Game was restarted or stopped early
        timer_label.value = f"⏱️ Time left: {t}s"
        if t == 0:
            break
        time.sleep(1)

    # Game over
    game_running = False
    timer_label.value = "⏰ Time's Up!"

    if p1_score > p2_score:
        result_label.value = "🏆 Player 1 Wins!"
    elif p2_score > p1_score:
        result_label.value = "🏆 Player 2 Wins!"
    else:
        result_label.value = "🤝 It's a Draw!"


def start_game(b):
    global p1_score, p2_score, game_running, timer_thread

    # Stop previous thread if running
    game_running = False
    if timer_thread and timer_thread.is_alive():
        timer_thread.join(timeout=1)

    # Reset state
    p1_score = 0
    p2_score = 0
    game_running = True

    result_label.value = ""
    timer_label.value = f"⏱️ Time left: {GAME_TIME}s"
    update_score()

    # Start timer in a background thread
    timer_thread = threading.Thread(target=run_timer, daemon=True)
    timer_thread.start()


# Bind buttons
p1_button.on_click(p1_click)
p2_button.on_click(p2_click)
start_button.on_click(start_game)

display(
    widgets.VBox([
        timer_label,
        score_label,
        widgets.HBox([p1_button, p2_button]),
        start_button,
        result_label
    ])
)
