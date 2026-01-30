"""
Connection Handler
Manages socket communication and parses commands from Android device
"""

import json
import time

class ConnectionHandler:
    def __init__(self, client_socket, address, controller):
        self.socket = client_socket
        self.address = address
        self.controller = controller
        self.running = True
        self.buffer = ""
        
    def handle(self):
        """Main handler loop for client connection"""
        try:
            # Send welcome message
            self.send_message({
                "type": "connected",
                "message": "Connected to PC Remote Server",
                "timestamp": time.time()
            })
            
            while self.running:
                try:
                    # Receive data from client
                    data = self.socket.recv(4096).decode('utf-8')
                    
                    if not data:
                        print(f"[-] Client {self.address[0]} disconnected")
                        break
                    
                    # Add to buffer and process complete messages
                    self.buffer += data
                    self.process_buffer()
                    
                except Exception as e:
                    print(f"[!] Error receiving data: {e}")
                    break
                    
        except Exception as e:
            print(f"[!] Connection error: {e}")
        finally:
            self.close()
    
    def process_buffer(self):
        """Process complete JSON messages from buffer"""
        while '\n' in self.buffer:
            # Extract one complete message
            message, self.buffer = self.buffer.split('\n', 1)
            
            if message.strip():
                try:
                    self.handle_message(message.strip())
                except Exception as e:
                    print(f"[!] Error processing message: {e}")
    
    def handle_message(self, message):
        """Parse and execute command from Android device"""
        try:
            # Parse JSON command
            command = json.loads(message)
            cmd_type = command.get('type', '')
            
            # Route to appropriate handler
            if cmd_type == 'mouse_move':
                dx = command.get('dx', 0)
                dy = command.get('dy', 0)
                self.controller.move_mouse(dx, dy)
                
            elif cmd_type == 'mouse_click':
                button = command.get('button', 'left')
                self.controller.click_mouse(button)
                
            elif cmd_type == 'mouse_scroll':
                amount = command.get('amount', 0)
                self.controller.scroll(amount)
                
            elif cmd_type == 'key_press':
                key = command.get('key', '')
                self.controller.press_key(key)
                
            elif cmd_type == 'key_type':
                text = command.get('text', '')
                self.controller.type_text(text)
                
            elif cmd_type == 'ping':
                # Respond to keep-alive ping
                self.send_message({"type": "pong", "timestamp": time.time()})
                
            elif cmd_type == 'disconnect':
                print(f"[-] Client {self.address[0]} requested disconnect")
                self.running = False
                
            else:
                print(f"[?] Unknown command type: {cmd_type}")
                
        except json.JSONDecodeError:
            print(f"[!] Invalid JSON received: {message[:100]}")
        except Exception as e:
            print(f"[!] Error handling message: {e}")
    
    def send_message(self, data):
        """Send JSON message to Android device"""
        try:
            message = json.dumps(data) + '\n'
            self.socket.sendall(message.encode('utf-8'))
        except Exception as e:
            print(f"[!] Error sending message: {e}")
            self.running = False
    
    def close(self):
        """Close the connection"""
        try:
            self.socket.close()
        except:
            pass
        print(f"[-] Connection closed: {self.address[0]}")


# Message Protocol Documentation
"""
Command Format (JSON):

1. Mouse Movement:
{
    "type": "mouse_move",
    "dx": 10,      // Delta X (relative movement)
    "dy": -5       // Delta Y (relative movement)
}

2. Mouse Click:
{
    "type": "mouse_click",
    "button": "left"   // "left", "right", or "middle"
}

3. Mouse Scroll:
{
    "type": "mouse_scroll",
    "amount": 3    // Positive = scroll up, Negative = scroll down
}

4. Key Press (special keys):
{
    "type": "key_press",
    "key": "enter"   // "enter", "backspace", "tab", "esc", etc.
}

5. Type Text:
{
    "type": "key_type",
    "text": "Hello World"
}

6. Ping (keep-alive):
{
    "type": "ping"
}

7. Disconnect:
{
    "type": "disconnect"
}

All messages must end with newline character (\n)
"""
