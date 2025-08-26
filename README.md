# Multi-Image Viewer

A professional Python Tkinter application for viewing multiple images with intuitive navigation controls and a responsive user interface.

## Features

- **Multi-Image Support**: Select and load multiple images at once
- **Navigation Controls**: Next/Previous buttons with visual feedback
- **Keyboard Shortcuts**: Use arrow keys, spacebar, or Enter for navigation
- **Responsive Design**: Automatic image scaling and window resizing support
- **Image Information**: Display current image details and position counter
- **Format Support**: Handles JPG, PNG, GIF, BMP, TIFF, and WebP formats
- **User-Friendly Interface**: Clean layout with hover effects and status updates

## Requirements

- Python 3.6+
- PIL (Pillow) library - included in most Python distributions
- Tkinter - included with Python

## Usage

1. **Run the application**:
   ```bash
   python main.py
   ```

2. **Load Images**:
   - Click "Open Images" button or press Ctrl+O
   - Select multiple image files from the file dialog
   - Images will be loaded and the first one displayed

3. **Navigate**:
   - Use "Previous" and "Next" buttons
   - Keyboard shortcuts:
     - Left Arrow: Previous image
     - Right Arrow: Next image  
     - Spacebar: Next image
     - Enter: Next image

4. **Window Controls**:
   - Resize the window - images automatically scale to fit
   - Status bar shows current image information
   - Counter displays current position (e.g., "3 of 10")

## File Structure

- `main.py` - Application entry point and initialization
- `image_viewer.py` - Main GUI components and user interface
- `image_handler.py` - Image loading, processing, and management
- `constants.py` - Configuration constants and settings

## Architecture

The application follows a modular design with clear separation of concerns:

- **ImageViewer**: Manages the GUI, user interactions, and display
- **ImageHandler**: Handles image loading, processing, and navigation logic
- **Constants**: Centralizes configuration for easy customization

## Customization

Edit `constants.py` to customize:
- Window dimensions and minimum sizes
- Supported image formats
- UI colors and styling
- Button dimensions and padding