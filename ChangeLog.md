# 📝 Changelog

## 🚀 Version 4.0.0 (February 2025)

> *Complete rewrite and modernization of the project*

### ⚠️ Breaking Changes

- 🔄 Project renamed: `undetected-chromedriver` → `invisible_chromedriver`
- 📦 New import style: 
  ```python
  # Old style
  import undetected_chromedriver as uc
  # New style
  import invisible_chromedriver as ic
  ```
- 🐍 Python requirements:
  - Minimum version: 3.9+
  - Selenium 4.9+
  - Playwright 1.41+

### ✨ New Features

- **Async Support**
  ```python
  async with ic.AsyncChrome() as driver:
      await driver.goto('https://example.com')
  ```
- **Type Hints**
  ```python
  from invisible_chrome.types import ChromeOptions
  
  def setup_driver(options: ChromeOptions) -> Chrome:
      return Chrome(options=options)
  ```
- 🛡️ Enhanced Anti-Detection
  - Improved fingerprint randomization
  - Better CDP protocol usage
  - Advanced stealth techniques

### 🔧 Improvements

- 📊 Modernized Architecture
  - Clean code structure
  - Better error handling
  - Enhanced logging system

- 🐳 Docker Support
  ```bash
  # Run with GUI support
  docker run -it --rm \
    -e DISPLAY=$DISPLAY \
    -v /tmp/.X11-unix:/tmp/.X11-unix \
    invisible-chrome
  ```

### 🗑️ Removed Features

- ❌ Legacy v1/v2 compatibility
- ❌ Old Chrome versions (<90)
- ❌ Deprecated APIs

---

<details>
<summary>📜 Historical Changes (undetected-chromedriver)</summary>

### Version History

| Version | Changes | Date |
|---------|---------|------|
| 3.5.0 | Selenium 4.9+ compatibility | 2024 |
| 3.4.5 | Anti-detection improvements | 2023 |
| 3.4.0 | Core refactoring | 2023 |
| 3.2.0 | New features & examples | 2023 |

> See [original changelog](https://github.com/ultrafunkamsterdam/undetected-chromedriver) for more details
</details>