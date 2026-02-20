# YouTube Shorts Downloader (Python)

![Python Version](https://img.shields.io/badge/Python-%3E%3D3.7-blue)
![License](https://img.shields.io/badge/license-MIT-green)
![Maintenance](https://img.shields.io/badge/Maintained-Yes-brightgreen)

> Extract YouTube Shorts video URLs and metadata using Python. No API quota limits. Perfect for content creators and analysts.

## 📋 Overview

**YouTube Shorts Downloader** is a lightweight Python script that extracts direct video URLs and metadata from YouTube Shorts by parsing embedded JSON data. No Google API key required, no quota limits.

**Also available in:**
- **[YouTube Shorts Downloader (PHP)](https://github.com/mikesmith-ge/youtube-shorts-downloader-php)** – PHP version
- **[YouTube Shorts Downloader (Node.js)](https://github.com/mikesmith-ge/youtube-shorts-downloader-nodejs)** – JavaScript version

## ✨ Features

- ✅ **Zero dependencies** – Pure Python 3, standard library only
- 🎬 **Direct video URLs** – Extract downloadable video links
- 🖼️ **Thumbnail extraction** – Get video preview images
- 📝 **Metadata support** – Title, view count, channel info
- 🚀 **No API quota** – Unlimited downloads without Google API restrictions
- 🖥️ **CLI included** – Run directly from command line
- 📦 **Importable module** – Use in your own Python projects

## 📦 Installation

### Option 1: Direct Download
```bash
wget https://raw.githubusercontent.com/mikesmith-ge/youtube-shorts-downloader-python/main/youtube_downloader.py
chmod +x youtube_downloader.py
```

### Option 2: Clone Repository
```bash
git clone https://github.com/mikesmith-ge/youtube-shorts-downloader-python.git
cd youtube-shorts-downloader-python
```

## 🚀 Usage

### Command Line Interface

```bash
# Basic usage
python youtube_downloader.py "https://youtube.com/shorts/ABC123"

# Make executable and run
chmod +x youtube_downloader.py
./youtube_downloader.py "https://youtube.com/shorts/ABC123"
```

### Python Module Usage

```python
from youtube_downloader import YouTubeDownloader

downloader = YouTubeDownloader()

try:
    video = downloader.download('https://youtube.com/shorts/ABC123')
    
    print(f"Title: {video['title']}")
    print(f"Video URL: {video['url']}")
    print(f"Thumbnail: {video['thumbnail']}")
    
except Exception as e:
    print(f"Error: {e}")
```

### Batch Processing

```python
from youtube_downloader import YouTubeDownloader
import time

urls = [
    'https://youtube.com/shorts/ABC123',
    'https://youtube.com/shorts/XYZ789',
]

downloader = YouTubeDownloader()

for url in urls:
    try:
        video = downloader.download(url)
        print(f"✓ {video['title']}")
    except Exception as e:
        print(f"✗ Error: {e}")
    
    time.sleep(1)  # Be respectful to YouTube
```

## ⚙️ Requirements

- Python 3.7 or higher
- No external dependencies

## ⚠️ Limitations

This is a **basic scraper** with limitations:

- ❌ **Public videos only** – Cannot access private or unlisted Shorts
- ⏱️ **Rate limits** – YouTube may throttle requests from the same IP
- 🚫 **No authentication** – Cannot access age-restricted content
- 📉 **Fragile** – YouTube updates may break functionality
- 📊 **Limited metadata** – Cannot extract full analytics or engagement metrics
- 💬 **No comments** – Does not extract comment data

### 🚀 Need More?

**For production use, unlimited downloads, full analytics, or commercial applications**, check out a professional API:

👉 **[Instaboost YouTube Tools](https://instaboost.ge/en/youtube)** – Enterprise API with:
- ✅ Unlimited downloads without rate limits
- ✅ Full video analytics (views, likes, comments)
- ✅ Comment extraction and sentiment analysis
- ✅ Trending Shorts tracking
- ✅ Bulk download capabilities
- ✅ 99.9% uptime SLA
- ✅ Dedicated support

[**Learn more →**](https://instaboost.ge)

## 🔄 Related Projects

**YouTube tools:**
- **[YouTube Shorts Downloader (PHP)](https://github.com/mikesmith-ge/youtube-shorts-downloader-php)** – PHP version
- **[YouTube Shorts Downloader (Node.js)](https://github.com/mikesmith-ge/youtube-shorts-downloader-nodejs)** – JavaScript version

**Other platforms:**
- **[TikTok Downloader (PHP)](https://github.com/mikesmith-ge/tiktok-video-downloader-php)** – Extract TikTok videos
- **[TikTok Downloader (Node.js)](https://github.com/mikesmith-ge/tiktok-video-downloader-nodejs)** – TikTok in JavaScript
- **[Instagram Downloader (Python)](https://github.com/mikesmith-ge/instagram-media-downloader-python)** – Instagram media
- **[Instagram Downloader (PHP)](https://github.com/mikesmith-ge/instagram-media-downloader-php)** – Instagram in PHP
- **[Facebook Post Scraper (Python)](https://github.com/mikesmith-ge/facebook-post-scraper-python)** – Facebook posts
- **[Twitter Thread Downloader (Python)](https://github.com/mikesmith-ge/twitter-thread-downloader-python)** – Archive Twitter threads
- **[Telegram Channel Info (Python)](https://github.com/mikesmith-ge/telegram-channel-info-python)** – Get channel stats

[**See all tools →**](https://github.com/mikesmith-ge?tab=repositories)

## 📄 License

MIT License - see [LICENSE](LICENSE) file for details.

## 🤝 Contributing

Contributions, issues, and feature requests are welcome! Check the [issues page](../../issues).

## ⚡ Disclaimer

**Educational purposes only.** Scraping YouTube may violate their Terms of Service. Use responsibly and respect content creators' rights. For commercial use, always use official APIs or authorized services.

## 📧 Support

- 🐛 **Bug reports:** [Open an issue](../../issues)
- 💡 **Suggestions:** [Start a discussion](../../discussions)
- 🚀 **Enterprise needs:** [Visit Instaboost](https://instaboost.ge)

---

**Made with ❤️ by the Instaboost Team**
