# 🛡️ ChromeCloak

> ⚠️ **Статус проекту: Бета-розробка** - API може змінитися без попередження

Сучасна бібліотека автоматизації Chrome з просунутими механізмами антидетекту. Духовний спадкоємець [undetected-chromedriver](https://github.com/ultrafunkamsterdam/undetected-chromedriver), доповнений асинхронною підтримкою та сучасними функціями.

## ✨ Можливості

- 🚀 Асинхронна підтримка через інтеграцію з Playwright
- 🛡️ Просунуті механізми антидетекту:
  - Обхід Cloudflare
  - Обробка захисту Imperva
  - Обхід DataDome
  - Та багато іншого...
- 🔄 Автоматичне керування ChromeDriver
- 📦 Проста заміна для selenium.webdriver.Chrome

## 📥 Встановлення

```bash
pip install chromecloak
```

## 🚀 Швидкий старт

```python
import chromecloak as cc

# Синхронне використання
driver = cc.Chrome()
driver.get("https://example.com")

# Асинхронне використання
async with cc.AsyncChrome() as driver:
    await driver.goto("https://example.com")
```

## ⚠️ Важливі примітки

Цей інструмент:
- НЕ приховує вашу IP-адресу
- НЕ гарантує обхід усіх систем захисту
- Знаходиться в активній розробці

## 🙌 Подяки

Цей проект стоїть на плечах гігантів:

- [undetected-chromedriver](https://github.com/ultrafunkamsterdam/undetected-chromedriver) - Оригінальний проект, що надихнув ChromeCloak
- [@ultrafunkamsterdam](https://github.com/ultrafunkamsterdam) - За створення основи сучасних методів антидетекту
- Усім контриб'юторам оригінального проекту, що зробили це можливим

## 📚 Документація

Для детальної документації, найкращих практик, прикладів та багато іншого відвідайте:
[vadim-khristenko.github.io/chromecloak](https://vadim-khristenko.github.io/chromecloak)

### 🌍 Переклади

README доступний іншими мовами:
- [English](README.md)
- [Русский](README.RU.md)
- [中文](README.ZH.md)
- [日本語](README.JP.md)

## 📝 Ліцензія

GPL-3.0 License - Подробиці у файлі [LICENSE](LICENSE)