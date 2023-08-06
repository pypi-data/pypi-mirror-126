# ppt-control

An interface for controlling PowerPoint slideshows over the network using WebSocket. With the included HTTP frontend, this package can essentially replicate PowerPoint's presenter view on any computer on the local network, with very low processing latency for commands.

This was originally designed for controlling a PowerPoint slideshow from an instance of OBS (Open Broadcaster Software) running on the same computer (removing the need for an extra monitor to show presenter view).

This package includes three main components:

1. The daemon, which runs in the background, independently of PowerPoint, and listens for WebSocket commands and hosts an HTTP server for the frontend
2. The HTTP frontend, written in JavaScript, which displays status information and sends commands to the daemon through WebSocket (this can be docked in one of OBS's "custom browser docks")
3. The OBS script, which allows a mapping of keyboard shortcuts to commands within OBS in order to control the slideshow from anywhere in OBS (keyboard shortcuts are implemented in the HTTP interface but only work when this is focused in OBS)

## Requirements

Due to the implementation's use of `pywin32` for COM communication, this daemon only works on Windows (but the HTTP and WebSocket interfaces can be accessed from any device).

The server and the OBS script are written for Python 3.6, since at the time of writing, [OBS only supports 3.6](https://obsproject.com/wiki/Getting-Started-With-OBS-Scripting) for scripts. The source module for the built-in HTTP server from 3.9 is included in this project, since the 3.6 module does not allow for setting a custom server root (this feature was [introduced in 3.7](https://docs.python.org/3/library/http.server.html#http.server.SimpleHTTPRequestHandler)). If you are not using the OBS script (or if you don't mind dealing with multiple versions of Python on the same system), the daemon should work fine on 3.9 in theory, but this is not fully tested. When OBS eventually provides support for >=3.7, this package will be updated to use the native HTTP server module, and support for pre-3.7 will be dropped.

This package also requires [pywin32](https://pypi.org/project/pywin32/), [websockets](https://pypi.org/project/websockets/) and [pystray](https://pypi.org/project/pystray/) (all three are required for the server, but only `websockets` is required for the OBS script).


## Installation

`pip install ppt-control`

will install all three components. You can then start the daemon by running 

`python -m ppt_control`

from a command prompt (note the underscore). On first run, Windows Defender will show a warning and attempt to block Python from starting the server. You can safely allow the program through the firewall. You can now start a PowerPoint slideshow and navigate to the server by IP address/hostname (`http://localhost` if on the same machine) and control the slideshow.

There are a few steps to set the package up fully:

### Starting the daemon at bootup

There are several ways to start a Python program at login. Here is one method:

1. Navigate to the directory containing the `pythonw` executable in Explorer (usually in `C:\Program Files\Python36` - run `python -c "import sys, print(sys.executable)"` to check)
2. Right click on `pythonw.exe` and click "Create shortcut"
3. Windows will ask you whether to place a shortcut on the desktop - click yes. Go to the properties of this shortcut, and in the target field, append ` -m ppt_control` (after the quotes, including an initial space). You can also change the name and icon of the shortcut if you like.
4. Copy this shortcut into the Startup folder (`%AppData%\Microsoft\Windows\Start Menu\Programs\Startup`). To quickly navigate to this folder, open an Explorer window and type `startup` in the address bar.

### Using the HTTP interface in OBS

To view the HTTP interface from within OBS, you can add a "custom browser dock" (View -> Docks -> Custom Browser Docks). The location should be the hostname and port number of the daemon (`http://localhost` by default). You can refresh the custom browser dock with Ctrl+R.

### Global keyboard shortcuts in OBS

Keyboard shortcuts in OBS browser docks only work when the browser dock is focused by clicking in it (there is actually no indication of focus in the interface, but if you click away from the browser dock the shortcuts will not work). To resolve this, there is another Python script called `ppt_control_obs.py` which can be added as a custom script in OBS. This script will listen for specific keys (configured in OBS's Hotkeys settings) and send commands to the daemon directly over WebSocket (no HTTP involved). To add the custom script, go to Tools -> Scripts, then click the + and choose the script. This will be located in the package directory which can be found with

`pip show ppt-control`

It is a good idea to turn off the keyboard shortcuts in the HTTP interface after loading the OBS hotkey script, otherwise commands will be sent to the daemon twice when the browser dock is focused.

## Configuration

Various settings can be changed in `%AppData%\ppt-control\ppt-control.ini`. This file is populated with the defaults for all possible settings at installation.

## Todo

- ✔️ Fix multiple-presentation support in JS & OBS clients
- Create desktop/start menu shortcuts on installation with pip
- Refactor/tidy JS code
- Fix "RCP server unavailable" error on server
- ✔️ Config documentation
- ✔️ Re-implement last slide behaviour
- ✔️ Re-implement black white behaviour
- ✔️ JS client show status on last slide
- ✔️ Shortcut to edit config in systray menu
- Export all slides on presentation init
- Abstract pres name in class & underscore `presentation` instance
- Check assertions
- Use `__debug__` flag
- Make constant for static dir
- Comment sys.coinitflags
- Die if error in run_ws or run_http