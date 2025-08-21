# SocialMapper

An OSINT (Open-Source Intelligence) tool for educational and research purposes. It demonstrates how publicly available information from different platforms can be correlated using a common identifier like a phone number.

## Features
- Checks phone number association against Facebook, Instagram, and Twitter.
- Modular design for easy addition of new platforms.
- Clean command-line interface with colored output.

**Disclaimer:**
This tool is intended for security professionals and researchers to understand public data exposure and improve privacy settings. It must only be used on phone numbers you own or have explicit permission to test. The developers are not responsible for misuse of this tool.

## Installation
1. Clone the repository: `git clone https://github.com/your_github/SocialMapper.git`
2. Navigate to the directory: `cd SocialMapper`
3. Install dependencies: `pip install -r requirements.txt`

## Usage
`python3 main.py [+][country code][number]`

Example:
`python3 main.py +12345678900`
