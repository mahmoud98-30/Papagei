<div align="center">
    <img src="https://github.com/mahmoud98-30/Papagei/blob/main/static/assets/images/logo.png" alt="Papagei Logo" width="250"/>
</div>

# Papagei 🎙️📝 - Lecture Transcription Companion

## 🌟 Project Overview

Papagei is an advanced open-source Django application designed to revolutionize how students capture and process lecture content. By converting video and audio recordings into precise text transcriptions, Papagei empowers students to:

- 📚 Transform lecture recordings into searchable text
- 🎧 Support multiple audio and video formats
- 📝 Enhance learning accessibility
- 💻 Provide a user-friendly transcription experience

## 📋 System Requirements

### Supported Operating Systems
- Windows 10/11
- macOS (Catalina and later)
- Linux (Ubuntu 20.04 LTS or later)

## 🔧 Comprehensive Installation Guide

### 1. Install Python

#### Windows
1. Download Python Installer:
   - Visit: [Python Official Downloads](https://www.python.org/downloads/windows/)
   - Choose the latest Python 3.x version
   - **Important**: Check "Add Python to PATH" during installation

2. Verify Installation
   ```bash
   python --version
   pip --version
   ```

#### macOS
1. Install via Homebrew (Recommended):
   ```bash
   # Install Homebrew (if not already installed)
   /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"

   # Install Python
   brew install python
   ```

2. Alternatively, download from [Python Official Website](https://www.python.org/downloads/macos/)

#### Linux (Ubuntu/Debian)
```bash
# Update package list
sudo apt update

# Install Python and pip
sudo apt install python3 python3-pip python3-venv
```

### 2. Install Git

#### Windows
1. Download Installer:
   - Visit: [Git for Windows](https://git-scm.com/download/win)
   - Choose 64-bit version
   - Follow installation wizard
   - Select "Use Git from the Windows Command Prompt"

#### macOS
1. Install via Homebrew:
   ```bash
   brew install git
   ```

2. Alternatively, download from [Git Official Website](https://git-scm.com/download/mac)

#### Linux (Ubuntu/Debian)
```bash
sudo apt update
sudo apt install git
```

### 3. Clone Papagei Repository

```bash
# Clone the repository
git clone https://github.com/mahmoud98-30/Papagei.git

# Navigate to project directory
cd Papagei
```

### 4. Create Virtual Environment

```bash
# Windows
python -m venv venv

# macOS/Linux
python3 -m venv venv
```

### 5. Activate Virtual Environment

#### Windows
```bash
venv\Scripts\activate
```

#### macOS/Linux
```bash
source venv/bin/activate
```

### 6. Install Project Dependencies

```bash
# Upgrade pip
pip install --upgrade pip

# Install project requirements
pip install -r requirements.txt
```

### 7. Database Setup

```bash
# Run migrations
python manage.py migrate

# Create superuser (optional)
python manage.py createsuperuser
```

### 8. Run Development Server

```bash
python manage.py runserver
```

## 🚀 Usage Guide

1. Open browser and navigate to `http://127.0.0.1:8000`
2. Upload lecture video/audio file
3. Select transcription settings
4. Generate and download transcript

## 🔍 Troubleshooting

### Common Installation Issues
- Ensure Python PATH is correctly set
- Check virtual environment activation
- Verify all dependencies are installed
- Consult project issues on GitHub

## 🤝 Contributing

1. Fork Repository
2. Create Feature Branch
   ```bash
   git checkout -b feature/AmazingFeature
   ```
3. Commit Changes
   ```bash
   git commit -m 'Add specific feature description'
   ```
4. Push to Branch
   ```bash
   git push origin feature/AmazingFeature
   ```
5. Open Pull Request

## 📋 Technology Stack
- Django
- Python
- Faster Whisper
- HTML/CSS/JavaScript

## 📄 Licensing
Distributed under MIT License. See `LICENSE` for details.

## 👥 Project Community
- GitHub Repository: [Papagei Project](https://github.com/mahmoud98-30/Papagei)
- Report Issues: [GitHub Issues](https://github.com/mahmoud98-30/Papagei/issues)

## 🌐 Additional Resources
- [Django Documentation](https://docs.djangoproject.com/)
- [Python Official Docs](https://docs.python.org/)
- [Faster Whisper Library Docs](https://github.com/SYSTRAN/faster-whisper)

## 💖 Support the Project
If you find Papagei helpful, consider:
- ⭐ Starring the GitHub repository
- 📣 Sharing with fellow students
- 🐛 Reporting bugs and suggesting improvements
