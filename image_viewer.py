"""
Main image viewer GUI component with navigation and display functionality.
"""

import tkinter as tk
from tkinter import ttk, filedialog, messagebox
from PIL import Image, ImageTk
from typing import Optional

from image_handler import ImageHandler
import constants


class ImageViewer:
    """Main image viewer application with GUI components."""
    
    def __init__(self, root: tk.Tk):
        self.root = root
        self.image_handler = ImageHandler()
        self.setup_window()
        self.create_widgets()
        self.setup_bindings()
        
    def setup_window(self):
        """Configure the main window properties."""
        self.root.title(constants.WINDOW_TITLE)
        self.root.geometry(f"{constants.DEFAULT_WINDOW_WIDTH}x{constants.DEFAULT_WINDOW_HEIGHT}")
        self.root.minsize(constants.MIN_WINDOW_WIDTH, constants.MIN_WINDOW_HEIGHT)
        self.root.configure(bg=constants.BG_COLOR)
        
        # Configure grid weights for resizing
        self.root.grid_rowconfigure(1, weight=1)
        self.root.grid_columnconfigure(0, weight=1)
    
    def create_widgets(self):
        """Create and layout all GUI widgets."""
        self.create_toolbar()
        self.create_image_display()
        self.create_navigation_controls()
        self.create_status_bar()
        
    def create_toolbar(self):
        """Create the toolbar with file operations."""
        toolbar_frame = tk.Frame(self.root, bg=constants.BG_COLOR, height=50)
        toolbar_frame.grid(row=0, column=0, sticky="ew", padx=constants.PADDING, pady=(constants.PADDING, 0))
        toolbar_frame.grid_columnconfigure(1, weight=1)
        
        # Open files button
        self.open_button = tk.Button(
            toolbar_frame,
            text="Open Images",
            command=self.open_images,
            width=constants.BUTTON_WIDTH,
            height=1,
            bg=constants.BUTTON_COLOR,
            fg=constants.TEXT_COLOR,
            relief="raised",
            cursor="hand2"
        )
        self.open_button.grid(row=0, column=0, padx=(0, constants.PADDING))
        
        # Add hover effects
        self.add_button_hover_effects(self.open_button)
        
        # Info label
        self.info_label = tk.Label(
            toolbar_frame,
            text="No images loaded. Click 'Open Images' to get started.",
            bg=constants.BG_COLOR,
            fg=constants.TEXT_COLOR,
            font=("Arial", 10)
        )
        self.info_label.grid(row=0, column=1, sticky="w", padx=constants.PADDING)
    
    def create_image_display(self):
        """Create the main image display area."""
        # Create frame for image display
        self.image_frame = tk.Frame(self.root, bg="white", relief="sunken", bd=2)
        self.image_frame.grid(row=1, column=0, sticky="nsew", padx=constants.PADDING, pady=constants.PADDING)
        self.image_frame.grid_rowconfigure(0, weight=1)
        self.image_frame.grid_columnconfigure(0, weight=1)
        
        # Image label
        self.image_label = tk.Label(
            self.image_frame,
            text="No image to display",
            bg="white",
            fg="gray",
            font=("Arial", 14)
        )
        self.image_label.grid(row=0, column=0, sticky="nsew")
        
        # Bind resize event
        self.image_frame.bind("<Configure>", self.on_frame_resize)
    
    def create_navigation_controls(self):
        """Create navigation buttons and controls."""
        nav_frame = tk.Frame(self.root, bg=constants.BG_COLOR, height=60)
        nav_frame.grid(row=2, column=0, sticky="ew", padx=constants.PADDING, pady=(0, constants.PADDING))
        nav_frame.grid_columnconfigure(1, weight=1)
        
        # Previous button
        self.prev_button = tk.Button(
            nav_frame,
            text="◀ Previous",
            command=self.previous_image,
            width=constants.BUTTON_WIDTH,
            height=constants.BUTTON_HEIGHT,
            bg=constants.BUTTON_COLOR,
            fg=constants.TEXT_COLOR,
            relief="raised",
            cursor="hand2",
            state="disabled"
        )
        self.prev_button.grid(row=0, column=0, padx=(0, constants.PADDING))
        
        # Image counter
        self.counter_label = tk.Label(
            nav_frame,
            text="",
            bg=constants.BG_COLOR,
            fg=constants.TEXT_COLOR,
            font=("Arial", 12, "bold")
        )
        self.counter_label.grid(row=0, column=1, sticky="")
        
        # Next button
        self.next_button = tk.Button(
            nav_frame,
            text="Next ▶",
            command=self.next_image,
            width=constants.BUTTON_WIDTH,
            height=constants.BUTTON_HEIGHT,
            bg=constants.BUTTON_COLOR,
            fg=constants.TEXT_COLOR,
            relief="raised",
            cursor="hand2",
            state="disabled"
        )
        self.next_button.grid(row=0, column=2, padx=(constants.PADDING, 0))
        
        # Add hover effects to navigation buttons
        self.add_button_hover_effects(self.prev_button)
        self.add_button_hover_effects(self.next_button)
    
    def create_status_bar(self):
        """Create the status bar at the bottom."""
        self.status_frame = tk.Frame(self.root, bg=constants.STATUS_BG_COLOR, height=constants.STATUS_BAR_HEIGHT)
        self.status_frame.grid(row=3, column=0, sticky="ew")
        self.status_frame.grid_columnconfigure(0, weight=1)
        
        self.status_label = tk.Label(
            self.status_frame,
            text="Ready",
            bg=constants.STATUS_BG_COLOR,
            fg=constants.TEXT_COLOR,
            font=("Arial", 9),
            anchor="w"
        )
        self.status_label.grid(row=0, column=0, sticky="ew", padx=constants.PADDING)
    
    def add_button_hover_effects(self, button: tk.Button):
        """Add hover effects to buttons."""
        def on_enter(event):
            if button['state'] != 'disabled':
                button.configure(bg=constants.BUTTON_HOVER_COLOR)
        
        def on_leave(event):
            if button['state'] != 'disabled':
                button.configure(bg=constants.BUTTON_COLOR)
        
        def on_click(event):
            if button['state'] != 'disabled':
                button.configure(bg=constants.BUTTON_ACTIVE_COLOR)
        
        button.bind("<Enter>", on_enter)
        button.bind("<Leave>", on_leave)
        button.bind("<Button-1>", on_click)
    
    def setup_bindings(self):
        """Setup keyboard bindings for navigation."""
        self.root.bind("<Left>", lambda e: self.previous_image())
        self.root.bind("<Right>", lambda e: self.next_image())
        self.root.bind("<space>", lambda e: self.next_image())
        self.root.bind("<Return>", lambda e: self.next_image())
        self.root.bind("<Control-o>", lambda e: self.open_images())
        
        # Make window focusable for keyboard events
        self.root.focus_set()
    
    def open_images(self):
        """Open file dialog to select multiple images."""
        file_paths = filedialog.askopenfilenames(
            title="Select Images",
            filetypes=constants.SUPPORTED_FORMATS
        )
        
        if file_paths:
            if self.image_handler.load_images(list(file_paths)):
                self.update_display()
                self.update_status(f"Loaded {len(file_paths)} images")
                self.update_navigation_buttons()
            else:
                messagebox.showerror("Error", "No valid images could be loaded.")
                self.update_status("Error loading images")
        else:
            self.update_status("No files selected")
    
    def next_image(self):
        """Navigate to the next image."""
        if self.image_handler.next_image():
            self.update_display()
            self.update_navigation_buttons()
            self.update_status("Next image")
    
    def previous_image(self):
        """Navigate to the previous image."""
        if self.image_handler.previous_image():
            self.update_display()
            self.update_navigation_buttons()
            self.update_status("Previous image")
    
    def update_display(self):
        """Update the image display with current image."""
        if not self.image_handler.has_images():
            self.image_label.configure(image="", text="No image to display")
            self.info_label.configure(text="No images loaded")
            self.counter_label.configure(text="")
            return
        
        # Get display area dimensions
        self.image_frame.update_idletasks()
        frame_width = self.image_frame.winfo_width() - 20  # Account for padding
        frame_height = self.image_frame.winfo_height() - 20
        
        if frame_width <= 1 or frame_height <= 1:
            # Frame not ready yet, try again after a short delay
            self.root.after(100, self.update_display)
            return
        
        # Load and display image
        photo_image = self.image_handler.load_current_image(frame_width, frame_height)
        
        if photo_image:
            self.image_label.configure(image=photo_image, text="")
            
            # Update info
            filename, total, position = self.image_handler.get_current_image_info()
            self.info_label.configure(text=f"Current: {filename}")
            self.counter_label.configure(text=f"{position} of {total}")
            
            # Update status with image details
            original_size = self.image_handler.get_original_size()
            if original_size:
                self.update_status(f"{filename} - {original_size[0]}×{original_size[1]} pixels")
        else:
            self.image_label.configure(image="", text="Error loading image")
            self.update_status("Error loading current image")
    
    def update_navigation_buttons(self):
        """Update the state of navigation buttons."""
        if not self.image_handler.has_images():
            self.prev_button.configure(state="disabled")
            self.next_button.configure(state="disabled")
            return
        
        # Update previous button
        if self.image_handler.has_previous():
            self.prev_button.configure(state="normal")
        else:
            self.prev_button.configure(state="disabled")
        
        # Update next button
        if self.image_handler.has_next():
            self.next_button.configure(state="normal")
        else:
            self.next_button.configure(state="disabled")
    
    def update_status(self, message: str):
        """Update the status bar message."""
        self.status_label.configure(text=message)
    
    def on_frame_resize(self, event):
        """Handle image frame resize events."""
        if self.image_handler.has_images():
            # Debounce resize events
            if hasattr(self, '_resize_after'):
                self.root.after_cancel(self._resize_after)
            self._resize_after = self.root.after(250, self.update_display)
    
    def run(self):
        """Start the application main loop."""
        self.root.mainloop()