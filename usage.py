# example_usage.py
import time
from ascibar import CustomProgressBar

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
