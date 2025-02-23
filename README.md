# 🛡️ ChromeCloak

> ⚠️ **Project Status: Beta Development** - API may change without notice

Modern Chrome automation library with advanced anti-detection capabilities. A spiritual successor to [undetected-chromedriver](https://github.com/ultrafunkamsterdam/undetected-chromedriver), enhanced with async support and modern features.

## ✨ Features

- 🚀 Async support via Playwright integration
- 🛡️ Advanced anti-detection mechanisms:
  - Cloudflare bypass
  - Imperva protection handling
  - DataDome evasion
  - And more...
- 🔄 Automatic ChromeDriver management
- 📦 Simple drop-in replacement for selenium.webdriver.Chrome

## 📥 Installation

```bash
pip install chromecloak
```

## 🚀 Quick Start

```python
import chromecloak as cc

# Synchronous usage
driver = cc.Chrome()
driver.get("https://example.com")

# Async usage
async with cc.AsyncChrome() as driver:
    await driver.goto("https://example.com")
```

## ⚠️ Important Notes

This tool:
- Does NOT hide your IP address
- Does NOT guarantee bypass of all protection systems
- Is under active development

## 🙌 Credits & Inspiration

This project stands on the shoulders of giants:

- [undetected-chromedriver](https://github.com/ultrafunkamsterdam/undetected-chromedriver) - The original project that inspired ChromeCloak
- [@ultrafunkamsterdam](https://github.com/ultrafunkamsterdam) - For creating the foundation of modern anti-detection techniques
- All contributors of the original project who made this possible

## 📚 Documentation

For detailed documentation, best practices, examples and more, visit:
[vadim-khristenko.github.io/chromecloak](https://vadim-khristenko.github.io/chromecloak)

### 🌍 Translations

README is also available in other languages:
- [Русский](README.RU.md)
- [Українська](README.UK.md)
- [中文](README.ZH.md)
- [日本語](README.JP.md)

## 📝 License

GPL-3.0 License - See [LICENSE](LICENSE) for details
