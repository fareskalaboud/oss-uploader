# OSS File Uploader

This script uploads files to Alibaba Cloud OSS (Object Storage Service) while maintaining folder structure.

## Prerequisites

You'll need Python 3.6 or higher installed on your system.

### Installing Python

#### Windows
1. Download Python from [python.org](https://python.org/downloads/)
2. Run the installer
3. **Important**: Check "Add Python to PATH" during installation
4. Verify installation by opening Command Prompt and typing:   ```bash
   python --version   ```

#### macOS
1. Using Homebrew (recommended):   ```bash
   brew install python   ```
   
   Or download from [python.org](https://python.org/downloads/)
2. Verify installation:   ```bash
   python3 --version   ```

#### Linux (Ubuntu/Debian)

```bash
    sudo apt update
    sudo apt install python3 python3-pip
```

For other Linux distributions, use their respective package managers.

## Installation Steps

1. **Clone or download** this repository to your local machine

2. **Install required packages**

   Open terminal/command prompt in the project directory and run:
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

## Running the Script

I provided a folders and files for you to test the script and to make sure the structure copies exactly as is.

1. Open terminal/command prompt in the project directory

2. Run the script:
   ```bash
   # Windows
   python app.py

   # macOS/Linux
   python3 app.py
   ```

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

