# PC Remote Control

An Android application that transforms your phone into a wireless mouse and keyboard for your PC over your local network.

## Features

- **Mouse Control**: Use your phone's touchscreen as a trackpad
- **Keyboard Input**: Send text and keystrokes from your phone to your PC
- **Cross-Platform**: Compatible with Windows, macOS, and Linux
- **Low Latency**: Optimized for responsive control over local network
- **Gesture Support**: Multi-touch gestures for scrolling and right-click
- **Secure Connection**: Encrypted communication between devices

## Requirements

### Android App
- Android 6.0 (Marshmallow) or higher
- WiFi connection

### PC Server
- Windows 7/10/11, macOS 10.12+, or Linux
- Python 3.7+ (or standalone executable)
- Same local network as Android device

## Installation

### Android App
1. Download the APK from the [Releases](releases) page
2. Enable "Install from Unknown Sources" in your Android settings
3. Install the APK on your device

### PC Server
1. Download the appropriate server application for your OS
2. Extract the files to a folder
3. Run the server executable

**Or install from source:**
```bash
git clone https://github.com/yourusername/pc-remote-control.git
cd pc-remote-control/server
pip install -r requirements.txt
python server.py
```

## Setup

1. **Start the PC Server**
   - Launch the server application on your computer
   - Note the IP address displayed (e.g., 192.168.1.100)
   - Ensure your firewall allows connections on port 5555

2. **Connect from Android**
   - Open the app on your phone
   - Tap "Add Device" or "Connect"
   - Enter your PC's IP address
   - Tap "Connect"

3. **Pairing** (First Time)
   - A pairing code will appear on both devices
   - Verify the codes match and confirm

## Usage

### Mouse Control
- **Move Cursor**: Swipe on the touchpad area
- **Left Click**: Single tap
- **Right Click**: Two-finger tap or long press
- **Scroll**: Two-finger swipe up/down
- **Drag**: Tap and hold, then swipe

### Keyboard
- Tap the keyboard icon to open the input panel
- Type normally - text will be sent to your PC
- Use special key buttons for Enter, Backspace, etc.

### Settings
- **Sensitivity**: Adjust cursor speed
- **Scroll Speed**: Change scroll sensitivity
- **Auto-Connect**: Automatically connect to last used PC
- **Haptic Feedback**: Enable/disable vibration on tap

## Troubleshooting

### Can't Connect to PC
- Ensure both devices are on the same WiFi network
- Check that the PC server is running
- Verify the IP address is correct
- Disable VPN on either device
- Check firewall settings on PC

### Laggy or Unresponsive
- Move closer to your WiFi router
- Close background apps on your phone
- Reduce sensitivity settings
- Check for network congestion

### Connection Drops
- Enable "Keep WiFi on during sleep" in Android settings
- Disable battery optimization for the app
- Check for router issues

## Security

- All communication is encrypted using TLS 1.3
- Pairing codes prevent unauthorized access
- Server only accepts connections from paired devices
- No data is sent outside your local network

## Technical Details

**Communication Protocol**: TCP Socket
**Port**: 5555 (configurable)
**Encryption**: AES-256 + TLS
**Latency**: ~10-30ms on typical local networks

## Building from Source

### Android App
```bash
git clone https://github.com/yourusername/pc-remote-control.git
cd pc-remote-control/android
./gradlew assembleDebug
```

### PC Server
```bash
cd server
pip install -r requirements.txt
python server.py
```

## Contributing

Contributions are welcome! Please:
1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Submit a pull request

## Roadmap

- [ ] Media controls (play, pause, volume)
- [ ] Multi-monitor support
- [ ] Custom gesture mapping
- [ ] File transfer capability
- [ ] Presentation mode with laser pointer
- [ ] Bluetooth connection option
- [ ] Web-based configuration interface

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

- Uses [PyAutoGUI](https://github.com/asweigart/pyautogui) for mouse/keyboard control on PC
- Icon design by [Your Designer Name]
- Inspired by Unified Remote and Remote Mouse

## Support

- **Issues**: Report bugs on [GitHub Issues](issues)
- **Email**: support@yourapp.com
- **Discord**: [Join our community](discord-link)

## Privacy Policy

This app does not collect, store, or transmit any personal data outside your local network. All input data is sent directly to your PC and is not logged or stored.

---

**Made with ❤️ for remote workers and couch surfers**
