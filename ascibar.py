characters = [' ', '_', '-', '+', '#', '^', '>', '|', '0', '·', '□', '▓', '░', '█', '⬜', '▮', '▯', '▱', '▭']

loader = {
    'style_1': {
        'frames': ['▁', '▂', '▃', '▄', '▅', '▆', '▇', '█']
    },
    'style_2': {
        'frames': ['▏', '▎', '▍', '▌', '▋', '▊', '▉', '█']
    },
    'style_3': {
        'frames': ['⠋', '⠙', '⠹', '⠸', '⠼', '⠴', '⠦', '⠧', '⠇', '⠏']
    }
}

boundaries = {
    'style_1': {
        'opening': '(',
        'closing': ')'
    },
    'style_2': {
        'opening': '[',
        'closing': ']'
    },
    'style_3': {
        'opening': '<',
        'closing': '>'
    }
}

loading_text = [
    "Loading...",
    "Processing...",
    "Please wait...",
    "Working on it...",
    "Fetching data...",
    "Initializing...",
    "Uploading...",
    "Downloading...",
    "Preparing...",
    "Almost there...",
    "Saving...",
    "Updating...",
    "Synchronizing...",
    "Generating...",
    "Compiling...",
    "Finalizing...",
    "Connecting...",
    "Setting up...",
    "Validating...",
    "Configuring..."
]

time_counter = {
    'style_1': {
        'counter': '(eta: --:--)'
    },
    'style_2': {
        'counter': '[--:--]'
    },
    'style_': {
        'counter': 'Time to finish 0.0 s'
    }
}

percentage = {
    'style_1': {
        'percentage': '0%'
    },
    'style_2': {
        'percentage': '0.0%'
    }
}

finished_tasks = {
    'style_1': {
        'finished_tasks': '(00/00)'
    }
}

settings = {
    'components': {
        'progress_indicator': {
            'enabled': True,
            'positive_fill': characters[0],
            'negative_fill': characters[0],
            'sort_order': 1
        }

        # custom text
        # custom text

        # time counter reverse property

        # internet speed
    }
}


def build_bar():
    pass
