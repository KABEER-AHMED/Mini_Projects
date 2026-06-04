# Mini Projects

This folder is a collection of small Python game projects and practice notebooks. The projects are useful for learning object-oriented programming, command-line input, randomization, simple game loops, and basic data-structure usage.

## Why This Is Useful

Mini projects are a good way to turn language basics into working programs. This folder currently demonstrates:

- Creating classes such as `Card`, `Deck`, and `Player`.
- Managing game state with loops and conditionals.
- Accepting command-line user input.
- Using randomness for gameplay.
- Applying simple data structures such as a queue.
- Prototyping ideas in notebooks before turning them into scripts.

## Project Contents

- `BlackJack.py` - Command-line blackjack simulation with cards, a deck, player/dealer hands, betting, hit/stay choices, and bust/win handling.
- `BlackJack.ipynb` - Notebook version of the blackjack simulation.
- `Russian_Roulette.py` - Queue-based elimination game that rotates through player names until one survivor remains.
- `War game .ipynb` - Early notebook prototype for a card game based on War.
- `README.md` - Project documentation.

## Requirements

Use Python 3. The current scripts use the standard library only.

For notebook work:

```bash
pip install jupyter
```

## How To Use

Run blackjack from this folder:

```bash
python BlackJack.py
```

Run the queue-based elimination game:

```bash
python Russian_Roulette.py
```

For notebooks:

```bash
jupyter notebook
```

Then open `BlackJack.ipynb` or `War game .ipynb`.

## Important Notes

- The scripts are interactive and expect terminal input.
- `BlackJack.py` is a learning simulation, not a casino-accurate blackjack engine.
- `Russian_Roulette.py` is implemented as a text-based elimination game using a custom queue class.
- `War game .ipynb` is an early prototype and does not yet contain a complete playable game.
- Some files started as notebook exports, so they may include cell markers such as `# %%`.

## Good Next Improvements

- Add input validation for all interactive prompts.
- Separate reusable classes from game-running code.
- Add a menu for choosing games.
- Complete the War game implementation.
- Add tests for deck creation, card values, queue behavior, and win/loss logic.
