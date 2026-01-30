# Quick Start Guide - PC Server

## Installation

1. **Install Python 3.7+**
   - Windows: Download from python.org
   - Mac: `brew install python3`
   - Linux: `sudo apt install python3 python3-pip`

2. **Install Dependencies**
   ```bash
   pip install -r requirements.txt
   ```

   Or install manually:
   ```bash
   pip install pyautogui pillow
   ```

## Running the Server

**Basic:**
```bash
python server.py
```

**Custom Port:**
```bash
python server.py 8080
```

## What Happens

1. Server starts and displays your IP address
2. Enter this IP in your Android app
3. Android connects and you can control your PC!

## Testing Without Android

You can test the controller independently:
```bash
python controller.py
```

This will move the mouse and type some text to verify everything works.

## Firewall Configuration

### Windows
1. Windows Security → Firewall & network protection
2. Allow an app through firewall
3. Add Python or allow port 5555

### Mac
```bash
# Firewall usually allows local network by default
# If needed, go to System Preferences → Security → Firewall
```

### Linux
```bash
sudo ufw allow 5555
```

## Troubleshooting

**"Module not found" error:**
```bash
pip install pyautogui --user
```

**Permission denied on Linux:**
```bash
# Install X11 dependencies
sudo apt install python3-tk python3-dev
```

**Can't find server IP:**
- Run `ipconfig` (Windows) or `ifconfig` (Mac/Linux)
- Look for IPv4 address starting with 192.168.x.x or 10.x.x.x

## Protocol Example

Send this JSON to test (using netcat or similar):
```json
{"type":"mouse_move","dx":100,"dy":50}
{"type":"mouse_click","button":"left"}
{"type":"key_type","text":"Hello World"}
```

Each command must end with a newline character.

## Next Steps

1. Get the Android app working
2. Test the connection
3. Add features like sensitivity adjustment
4. Package as standalone executable (PyInstaller)

## Security Note

This server accepts connections from ANY device on your local network. 
For production use, add:
- Pairing codes
- Encryption (TLS)
- Device whitelist
