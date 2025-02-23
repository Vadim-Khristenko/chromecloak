# 🛡️ ChromeCloak

> ⚠️ **Статус проекта: Бета-разработка** - API может измениться без предупреждения

Современная библиотека автоматизации Chrome с продвинутыми механизмами антидетекта. Духовный наследник [undetected-chromedriver](https://github.com/ultrafunkamsterdam/undetected-chromedriver), дополненный асинхронной поддержкой и современными функциями.

## ✨ Возможности

- 🚀 Асинхронная поддержка через интеграцию с Playwright
- 🛡️ Продвинутые механизмы антидетекта:
  - Обход Cloudflare
  - Обработка защиты Imperva
  - Обход DataDome
  - И многое другое...
- 🔄 Автоматическое управление ChromeDriver
- 📦 Простая замена для selenium.webdriver.Chrome

## 📥 Установка

```bash
pip install chromecloak
```

## 🚀 Быстрый старт

```python
import chromecloak as cc

# Синхронное использование
driver = cc.Chrome()
driver.get("https://example.com")

# Асинхронное использование
async with cc.AsyncChrome() as driver:
    await driver.goto("https://example.com")
```

## ⚠️ Важные замечания

Этот инструмент:
- НЕ скрывает ваш IP-адрес
- НЕ гарантирует обход всех систем защиты
- Находится в активной разработке

## 🙌 Благодарности

Этот проект стоит на плечах гигантов:

- [undetected-chromedriver](https://github.com/ultrafunkamsterdam/undetected-chromedriver) - Оригинальный проект, вдохновивший ChromeCloak
- [@ultrafunkamsterdam](https://github.com/ultrafunkamsterdam) - За создание основы современных методов антидетекта
- Всем контрибьюторам оригинального проекта, сделавшим это возможным

## 📚 Документация

Для подробной документации, лучших практик, примеров и многого другого посетите:
[vadim-khristenko.github.io/chromecloak](https://vadim-khristenko.github.io/chromecloak)

### 🌍 Переводы

README доступен на других языках:
- [English](README.md)
- [Українська](README.UK.md)
- [中文](README.ZH.md)
- [日本語](README.JP.md)

## 📝 Лицензия

GPL-3.0 License - Подробности в файле [LICENSE](LICENSE)