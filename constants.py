"""
Configuration constants for the Image Viewer application.
"""

# Window configuration
WINDOW_TITLE = "Multi-Image Viewer"
MIN_WINDOW_WIDTH = 800
MIN_WINDOW_HEIGHT = 600
DEFAULT_WINDOW_WIDTH = 1000
DEFAULT_WINDOW_HEIGHT = 700

# Image configuration
SUPPORTED_FORMATS = [
    ("Image files", "*.jpg *.jpeg *.png *.gif *.bmp *.tiff *.webp"),
    ("JPEG files", "*.jpg *.jpeg"),
    ("PNG files", "*.png"),
    ("GIF files", "*.gif"),
    ("BMP files", "*.bmp"),
    ("All files", "*.*")
]

# UI configuration
BUTTON_WIDTH = 12
BUTTON_HEIGHT = 2
PADDING = 10
STATUS_BAR_HEIGHT = 25

# Colors
BG_COLOR = "#f0f0f0"
BUTTON_COLOR = "#e1e1e1"
BUTTON_HOVER_COLOR = "#d4d4d4"
BUTTON_ACTIVE_COLOR = "#c0c0c0"
STATUS_BG_COLOR = "#e8e8e8"
TEXT_COLOR = "#333333"