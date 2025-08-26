"""
Image handling utilities for loading, processing, and managing images.
"""

import os
from PIL import Image, ImageTk
from typing import List, Optional, Tuple


class ImageHandler:
    """Handles image loading, processing, and management operations."""
    
    def __init__(self):
        self.images: List[str] = []
        self.current_index = 0
        self.current_image: Optional[ImageTk.PhotoImage] = None
        self.original_image: Optional[Image.Image] = None
    
    def load_images(self, file_paths: List[str]) -> bool:
        """
        Load multiple image file paths and validate them.
        
        Args:
            file_paths: List of image file paths
            
        Returns:
            bool: True if images were loaded successfully
        """
        valid_images = []
        
        for path in file_paths:
            if self.is_valid_image(path):
                valid_images.append(path)
        
        if valid_images:
            self.images = valid_images
            self.current_index = 0
            return True
        
        return False
    
    def is_valid_image(self, file_path: str) -> bool:
        """
        Check if the file is a valid image that can be opened.
        
        Args:
            file_path: Path to the image file
            
        Returns:
            bool: True if the file is a valid image
        """
        try:
            if not os.path.exists(file_path):
                return False
            
            with Image.open(file_path) as img:
                img.verify()
            return True
        except Exception:
            return False
    
    def get_current_image_path(self) -> Optional[str]:
        """Get the path of the current image."""
        if not self.images or self.current_index >= len(self.images):
            return None
        return self.images[self.current_index]
    
    def get_current_image_info(self) -> Tuple[str, int, int]:
        """
        Get information about the current image.
        
        Returns:
            Tuple of (filename, total_images, current_position)
        """
        if not self.images:
            return "", 0, 0
        
        current_path = self.images[self.current_index]
        filename = os.path.basename(current_path)
        total = len(self.images)
        position = self.current_index + 1
        
        return filename, total, position
    
    def load_current_image(self, target_width: int, target_height: int) -> Optional[ImageTk.PhotoImage]:
        """
        Load and resize the current image to fit the target dimensions.
        
        Args:
            target_width: Target width for the image
            target_height: Target height for the image
            
        Returns:
            PhotoImage object or None if loading fails
        """
        if not self.images or self.current_index >= len(self.images):
            return None
        
        try:
            image_path = self.images[self.current_index]
            
            # Open and store original image
            with Image.open(image_path) as img:
                self.original_image = img.copy()
                
                # Calculate resize dimensions maintaining aspect ratio
                img_width, img_height = img.size
                ratio = min(target_width / img_width, target_height / img_height)
                
                if ratio < 1:  # Only resize if image is larger than target
                    new_width = int(img_width * ratio)
                    new_height = int(img_height * ratio)
                    resized_img = img.resize((new_width, new_height), Image.Resampling.LANCZOS)
                else:
                    resized_img = img.copy()
                
                # Convert to PhotoImage
                self.current_image = ImageTk.PhotoImage(resized_img)
                return self.current_image
                
        except Exception as e:
            print(f"Error loading image: {e}")
            return None
    
    def next_image(self) -> bool:
        """
        Move to the next image.
        
        Returns:
            bool: True if successfully moved to next image
        """
        if not self.images:
            return False
        
        if self.current_index < len(self.images) - 1:
            self.current_index += 1
            return True
        
        return False
    
    def previous_image(self) -> bool:
        """
        Move to the previous image.
        
        Returns:
            bool: True if successfully moved to previous image
        """
        if not self.images:
            return False
        
        if self.current_index > 0:
            self.current_index -= 1
            return True
        
        return False
    
    def has_images(self) -> bool:
        """Check if any images are loaded."""
        return len(self.images) > 0
    
    def has_next(self) -> bool:
        """Check if there's a next image available."""
        return self.current_index < len(self.images) - 1
    
    def has_previous(self) -> bool:
        """Check if there's a previous image available."""
        return self.current_index > 0
    
    def get_original_size(self) -> Optional[Tuple[int, int]]:
        """Get the original size of the current image."""
        if self.original_image:
            return self.original_image.size
        return None