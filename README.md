### Repository Description:

🔐 A lightweight password manager made with Python and Tkinter.

Stores credentials safely in a local file (data.json) and lets you:

Add new credentials (Username, Password, Website).

View credentials by website.

View all credentials at once.

Easily copy credentials from the GUI.

Built with Python 3.13, Tkinter, and PyInstaller.
Executable available for Windows.

Hash (SHA-256) provided to verify downloaded files.

## How to run

The main executable file is "Password Manager.exe" in dist folder inside the repo

just copy the file to any local folder of your windows device and simply run


### Verifying the Executable

To verify the integrity of the downloaded `Password Manager.exe` file, run the following command in your terminal or Command Prompt inside the folder containing the file:

" ```cmd
certutil -hashfile password_manager.exe SHA256" 

You should get an output like this:

" SHA256 hash of password_manager.exe:
41d54a905ccce4ff21f563f0832772824a2bd571c85b15fa1869134d1221a9ae
CertUtil: -hashfile command completed successfully. "

Make sure the hash value matches exactly with the one above to confirm the file is genuine and untampered.

