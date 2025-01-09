Here’s the updated `README` with instructions to install `venv`, create, and activate a virtual environment called `venv`:

---

# OSS File Uploader

This script uploads files to Alibaba Cloud OSS (Object Storage Service) while maintaining folder structure.

## Prerequisites

You'll need Python 3.6 or higher installed on your system.

### Installing Python

#### Windows
1. Download Python from [python.org](https://python.org/downloads/)
2. Run the installer
3. **Important**: Check "Add Python to PATH" during installation
4. Verify installation by opening Command Prompt and typing:
   ```bash
   python --version
   ```

#### macOS
1. Using Homebrew (recommended):
   ```bash
   brew install python
   ```
   Or download from [python.org](https://python.org/downloads/)
2. Verify installation:
   ```bash
   python3 --version
   ```

#### Linux (Ubuntu/Debian)
```bash
    sudo apt update
    sudo apt install python3 python3-pip
```

For other Linux distributions, use their respective package managers.

## Setting Up a Virtual Environment

1. **Install `venv` (if not already installed)**

   - For **Windows** and **macOS/Linux**: `venv` comes bundled with Python 3.6+.
   
   To verify it's available:
   ```bash
   python -m venv --help
   ```

2. **Create a virtual environment** in the project directory:

   Open your terminal/command prompt in the project folder and run:
   ```bash
   # Windows
   python -m venv venv

   # macOS/Linux
   python3 -m venv venv
   ```

3. **Activate the virtual environment**

   - On **Windows**:
     ```bash
     .\venv\Scripts\activate
     ```
   - On **macOS/Linux**:
     ```bash
     source venv/bin/activate
     ```

   After activation, you’ll see the environment name in the terminal prompt, indicating you’re working inside the virtual environment.

## Installation Steps

1. **Clone or download** this repository to your local machine

2. **Install required packages** within the virtual environment

   With the virtual environment activated, run:
   ```bash
   # Windows
   pip install oss2 tqdm

   # macOS/Linux
   pip3 install oss2 tqdm
   ```

## Configuration

1. Open `app.py` and update your OSS credentials:
   ```python
   ACCESS_KEY_ID = 'your_access_key_id'
   ACCESS_KEY_SECRET = 'your_access_key_secret'
   ENDPOINT = 'your_endpoint'
   BUCKET_NAME = 'your_bucket_name'
   ```

## Testing the Script

I provided folders and files for you to test the script and ensure the structure is copied exactly as is.

1. Open terminal/command prompt in the project directory

2. Run the script:
   ```bash
   # Windows
   python app.py

   # macOS/Linux
   python3 app.py
   ```

3. You will see the full visual progress on the terminal.
 
## Running the Script

Please use follow the test instructions in the previous section to test the script to make sure it works, then follow the instructions below.

1. Delete the test folders (`folder1` and `folder2`).

2. Copy all your files and folders to the same folder as the script. 

3. Run the script:
   ```bash
   # Windows
   python app.py

   # macOS/Linux
   python3 app.py
   ```

4. You will see the full visual progress on the terminal.

## Security Note

⚠️ **Important**: Never commit your actual OSS credentials to version control. Consider using environment variables or a configuration file for sensitive information.

## Troubleshooting

If you encounter "command not found" errors:
- Windows: Ensure Python is added to PATH
- macOS/Linux: Try using `python3` instead of `python`

For permission errors:
- Windows: Run Command Prompt as administrator
- macOS/Linux: Use `sudo` if necessary for installation

For package installation issues:
- Try upgrading pip:
```bash
    # Windows
    python -m pip install --upgrade pip

    # macOS/Linux
    python3 -m pip install --upgrade pip
```

--- 

This version now includes instructions for setting up and using a virtual environment (`venv`).
