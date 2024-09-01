# Ascibar

Ascibar is a lightweight Python library designed for creating customizable ASCII-based progress bars in terminal applications. It offers an easy way to enhance your command-line interface with visually appealing and informative progress indicators.

## Version

Current version: **0.1**

## Installation

You can install `ascibar` via pip. Run the following command in your terminal:

```bash
pip install ascibar
```

## Usage

A basic example of how to use `ascibar`:

```python
from ascibar import CustomProgressBar
import time

total = 100

# Define your custom styles
custom_loader_style = ['⠋', '⠙', '⠹', '⠸', '⠼', '⠴', '⠦', '⠧', '⠇', '⠏']
custom_bar_style = '█'

# Enable components
enable_components = {
    "loader": True,
    "bar": True,
    "percentage": True,
    "finished_tasks": True,
}

# Create the progress bar with custom settings
progress = CustomProgressBar(
    total,
    loading_text="Processing...",
    done_text="Task completed!",
    loader_style=custom_loader_style,
    bar_style=custom_bar_style,
    enable_components=enable_components
)

# Run the progress bar
for i in range(total + 1):
    progress.print_progress_bar(i)
    time.sleep(0.1)
```

### Parameters

- **`total`**: The total number of iterations (e.g., 100).
- **`loading_text`**: Text to display while loading (default: `"Loading..."`).
- **`done_text`**: Text to display when done (default: `"Done!"`).
- **`loader_style`**: List of characters for the loader animation (default: `['-', '\\', '|', '/']`).
- **`bar_style`**: Character to use for the progress bar (default: `'#'`).
- **`enable_components`**: Dictionary to enable/disable components:
  - `"loader"`: Show loader animation (default: `True`).
  - `"bar"`: Show progress bar (default: `True`).
  - `"percentage"`: Show percentage complete (default: `False`).
  - `"finished_tasks"`: Show finished tasks count (default: `False`).

## License

This project is licensed under the GNU License. See the [LICENSE](LICENSE) file for details.

## Contributing

Contributions are welcome! If you have suggestions, bug reports, or pull requests, please submit them via GitHub issues or pull requests.
