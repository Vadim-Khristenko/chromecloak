# 🛡️ ChromeCloak

> ⚠️ **项目状态：测试版开发中** - API 可能会随时更改

现代化的 Chrome 自动化库，具有高级反检测功能。本项目是 [undetected-chromedriver](https://github.com/ultrafunkamsterdam/undetected-chromedriver) 的精神继承者，增加了异步支持和现代特性。

## ✨ 特性

- 🚀 通过 Playwright 集成实现异步支持
- 🛡️ 高级反检测机制：
  - Cloudflare 绕过
  - Imperva 保护处理
  - DataDome 规避
  - 以及更多...
- 🔄 自动 ChromeDriver 管理
- 📦 selenium.webdriver.Chrome 的简单替代品

## 📥 安装

```bash
pip install chromecloak
```

## 🚀 快速开始

```python
import chromecloak as cc

# 同步使用
driver = cc.Chrome()
driver.get("https://example.com")

# 异步使用
async with cc.AsyncChrome() as driver:
    await driver.goto("https://example.com")
```

## ⚠️ 重要提示

本工具：
- 不会隐藏您的 IP 地址
- 不保证能绕过所有保护系统
- 正在积极开发中

## 🙌 致谢

本项目建立在巨人的肩膀上：

- [undetected-chromedriver](https://github.com/ultrafunkamsterdam/undetected-chromedriver) - 启发 ChromeCloak 的原始项目
- [@ultrafunkamsterdam](https://github.com/ultrafunkamsterdam) - 创建了现代反检测技术的基础
- 感谢原始项目的所有贡献者使这一切成为可能

## 📚 文档

获取详细文档、最佳实践、示例等，请访问：
[vadim-khristenko.github.io/chromecloak](https://vadim-khristenko.github.io/chromecloak)

### 🌍 翻译

README 支持其他语言：
- [English](README.md)
- [Русский](README.RU.md)
- [Українська](README.UK.md)
- [日本語](README.JP.md)

## 📝 许可证

GPL-3.0 许可证 - 详见 [LICENSE](LICENSE) 文件