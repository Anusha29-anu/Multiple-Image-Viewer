"""
Multi-Image Viewer Application

A Python Tkinter application for viewing multiple images with navigation controls.
Features include file browsing, image display with automatic scaling, and 
keyboard navigation support.

Author: Bolt AI Assistant
"""

import tkinter as tk
import sys
import os

# Add current directory to path for imports
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from image_viewer import ImageViewer


def main():
    """Main entry point for the Image Viewer application."""
    try:
        # Create main window
        root = tk.Tk()
        
        # Create and run image viewer
        app = ImageViewer(root)
        app.run()
        
    except Exception as e:
        print(f"Error starting application: {e}")
        if hasattr(e, '__traceback__'):
            import traceback
            traceback.print_exc()
        
        # Try to show error in a dialog if tkinter is working
        try:
            import tkinter.messagebox as messagebox
            messagebox.showerror("Application Error", f"Failed to start application:\n{str(e)}")
        except:
            pass
        
        sys.exit(1)


if __name__ == "__main__":
    main()