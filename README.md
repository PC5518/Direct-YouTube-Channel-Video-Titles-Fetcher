#  YouTube Channel Video Titles Fetcher (using yt-dlp) 🎥

This Python script connects to any YouTube channel (in any format: `@handle`, `/c/`, or `/channel/`) and retrieves the **titles of all videos** on that channel using the `yt-dlp` library.

---
Note that it's totally based on Python  
##  Features

- ✅ Extracts all video titles using `yt-dlp` (supports @handle, /c/, and /channel/ URLs)
-  Intelligent handling of playlists and flat extraction
- ❗ Gracefully handles errors like invalid URLs or missing videos
-  Command-line interface to interactively enter the URL
- 🔐 Does not download videos — only metadata (safe and lightweight)

---

## 🛠️ Requirements

- Python 3.7+
- `yt-dlp`

```bash
pip install yt-dlp
