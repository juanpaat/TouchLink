"""
Controller
Handles actual mouse and keyboard control on the PC
Uses PyAutoGUI for cross-platform input control
"""

import pyautogui
import platform

# Configure PyAutoGUI
pyautogui.FAILSAFE = True  # Move mouse to corner to abort
pyautogui.PAUSE = 0.01     # Small pause between actions for stability

class Controller:
    def __init__(self, sensitivity=1.0):
        self.sensitivity = sensitivity
        self.screen_width, self.screen_height = pyautogui.size()
        
        # Map of special keys
        self.special_keys = {
            'enter': 'enter',
            'return': 'enter',
            'backspace': 'backspace',
            'delete': 'delete',
            'tab': 'tab',
            'esc': 'esc',
            'escape': 'esc',
            'space': 'space',
            'up': 'up',
            'down': 'down',
            'left': 'left',
            'right': 'right',
            'home': 'home',
            'end': 'end',
            'pageup': 'pageup',
            'pagedown': 'pagedown',
            'ctrl': 'ctrl',
            'alt': 'alt',
            'shift': 'shift',
            'win': 'win',
            'cmd': 'command' if platform.system() == 'Darwin' else 'win',
            'f1': 'f1', 'f2': 'f2', 'f3': 'f3', 'f4': 'f4',
            'f5': 'f5', 'f6': 'f6', 'f7': 'f7', 'f8': 'f8',
            'f9': 'f9', 'f10': 'f10', 'f11': 'f11', 'f12': 'f12'
        }
        
        print(f"[*] Controller initialized")
        print(f"[*] Screen size: {self.screen_width}x{self.screen_height}")
        print(f"[*] Platform: {platform.system()}")
    
    def move_mouse(self, dx, dy):
        """
        Move mouse cursor by relative amount
        
        Args:
            dx: Delta X (horizontal movement)
            dy: Delta Y (vertical movement)
        """
        try:
            # Apply sensitivity
            dx = int(dx * self.sensitivity)
            dy = int(dy * self.sensitivity)
            
            # Get current position
            current_x, current_y = pyautogui.position()
            
            # Calculate new position
            new_x = current_x + dx
            new_y = current_y + dy
            
            # Clamp to screen bounds
            new_x = max(0, min(new_x, self.screen_width - 1))
            new_y = max(0, min(new_y, self.screen_height - 1))
            
            # Move mouse
            pyautogui.moveTo(new_x, new_y)
            
        except Exception as e:
            print(f"[!] Error moving mouse: {e}")
    
    def click_mouse(self, button='left'):
        """
        Click mouse button
        
        Args:
            button: 'left', 'right', or 'middle'
        """
        try:
            if button == 'left':
                pyautogui.click()
            elif button == 'right':
                pyautogui.rightClick()
            elif button == 'middle':
                pyautogui.middleClick()
            else:
                print(f"[!] Unknown mouse button: {button}")
                
        except Exception as e:
            print(f"[!] Error clicking mouse: {e}")
    
    def scroll(self, amount):
        """
        Scroll mouse wheel
        
        Args:
            amount: Positive = scroll up, Negative = scroll down
        """
        try:
            # PyAutoGUI scroll: positive = up, negative = down
            pyautogui.scroll(int(amount))
            
        except Exception as e:
            print(f"[!] Error scrolling: {e}")
    
    def press_key(self, key):
        """
        Press a special key or key combination
        
        Args:
            key: Key name (e.g., 'enter', 'ctrl+c', 'alt+tab')
        """
        try:
            key = key.lower().strip()
            
            # Handle key combinations (e.g., 'ctrl+c')
            if '+' in key:
                keys = [k.strip() for k in key.split('+')]
                # Map to special keys
                keys = [self.special_keys.get(k, k) for k in keys]
                # Press combination
                pyautogui.hotkey(*keys)
            else:
                # Single key press
                mapped_key = self.special_keys.get(key, key)
                pyautogui.press(mapped_key)
                
        except Exception as e:
            print(f"[!] Error pressing key '{key}': {e}")
    
    def type_text(self, text):
        """
        Type text string
        
        Args:
            text: String to type
        """
        try:
            if text:
                pyautogui.write(text, interval=0.01)
                
        except Exception as e:
            print(f"[!] Error typing text: {e}")
    
    def set_sensitivity(self, sensitivity):
        """
        Change mouse sensitivity
        
        Args:
            sensitivity: Multiplier for mouse movement (e.g., 1.5 = 50% faster)
        """
        self.sensitivity = max(0.1, min(sensitivity, 5.0))
        print(f"[*] Sensitivity set to {self.sensitivity}")
    
    def get_cursor_position(self):
        """Get current cursor position"""
        try:
            return pyautogui.position()
        except Exception as e:
            print(f"[!] Error getting cursor position: {e}")
            return (0, 0)
    
    def get_screen_size(self):
        """Get screen dimensions"""
        return (self.screen_width, self.screen_height)


# Testing functions
if __name__ == "__main__":
    print("Testing Controller...")
    controller = Controller()
    
    print("\n1. Moving mouse...")
    controller.move_mouse(100, 100)
    
    print("2. Left click...")
    controller.click_mouse('left')
    
    print("3. Typing text...")
    controller.type_text("Hello from PC Remote Control!")
    
    print("4. Pressing Enter...")
    controller.press_key('enter')
    
    print("5. Scrolling...")
    controller.scroll(3)
    
    print("\nTest complete!")
