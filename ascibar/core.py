# ascibar/core.py
import time
import itertools


class CustomProgressBar:
    def __init__(self, total, loading_text=None, done_text=None, loader_style=None, bar_style=None, enable_components=None):
        self.total = total
        self.iteration = 0

        # Set default values if not provided
        self.loading_text = loading_text or "Loading..."
        self.done_text = done_text or "Done!"

        # Set loaders
        self.loader_frames = loader_style or ['-', '\\', '|', '/']
        self.loader = itertools.cycle(self.loader_frames)

        # Set bar
        self.bar_characters = bar_style or '#'

        # Set percentage
        self.percentage_style = "0%"

        # Set finished tasks
        self.finished_tasks_style = "(00/100)"

        # Enable/disable components
        self.enable_components = enable_components or {
            "loader": True,
            "bar": True,
            "percentage": False,
            "finished_tasks": False,
        }

    def print_progress_bar(self, iteration):
        self.iteration = iteration
        percent = 100 * (iteration / float(self.total))
        filled_length = int(50 * iteration // self.total)

        bar = self.bar_characters * filled_length + '-' * (50 - filled_length)
        loader_char = next(self.loader)
        percentage_info = f"{
            percent:.1f}%" if self.enable_components["percentage"] else ""
        tasks_info = f"({
            iteration}/{self.total})" if self.enable_components["finished_tasks"] else ""

        # Print the progress bar with selected components
        print(f'\r{self.loading_text} {loader_char if self.enable_components["loader"] else ""} |{
              bar if self.enable_components["bar"] else ""}| {percentage_info} {tasks_info}', end='\r')
        if iteration == self.total:
            print(f'\n{self.done_text}')
