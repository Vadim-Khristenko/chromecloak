# 🛡️ ChromeCloak

> ⚠️ **プロジェクトステータス：ベータ開発中** - APIは予告なく変更される場合があります

最新のChrome自動化ライブラリーで、高度な検出回避機能を搭載。[undetected-chromedriver](https://github.com/ultrafunkamsterdam/undetected-chromedriver)の精神的後継であり、非同期サポートとモダンな機能を追加しています。

## ✨ 特徴

- 🚀 Playwright統合による非同期サポート
- 🛡️ 高度な検出回避メカニズム：
  - Cloudflareバイパス
  - Imperva保護の処理
  - DataDome回避
  - その他多数...
- 🔄 ChromeDriverの自動管理
- 📦 selenium.webdriver.Chromeの簡単な代替

## 📥 インストール

```bash
pip install chromecloak
```

## 🚀 クイックスタート

```python
import chromecloak as cc

# 同期使用
driver = cc.Chrome()
driver.get("https://example.com")

# 非同期使用
async with cc.AsyncChrome() as driver:
    await driver.goto("https://example.com")
```

## ⚠️ 重要な注意事項

このツールは：
- IPアドレスを隠すことはできません
- すべての保護システムのバイパスを保証するものではありません
- 活発に開発中です

## 🙌 謝辞

このプロジェクトは巨人の肩の上に立っています：

- [undetected-chromedriver](https://github.com/ultrafunkamsterdam/undetected-chromedriver) - ChromeCloakのインスピレーション元となった元のプロジェクト
- [@ultrafunkamsterdam](https://github.com/ultrafunkamsterdam) - モダンな検出回避技術の基礎を作成
- オリジナルプロジェクトのすべてのコントリビューターに感謝します

## 📚 ドキュメント

詳細なドキュメント、ベストプラクティス、例など詳しくはこちら：
[vadim-khristenko.github.io/chromecloak](https://vadim-khristenko.github.io/chromecloak)

### 🌍 翻訳

READMEは他の言語でもご利用いただけます：
- [English](README.md)
- [Русский](README.RU.md)
- [Українська](README.UK.md)
- [中文](README.ZH.md)

## 📝 ライセンス

GPL-3.0 ライセンス - 詳細は[LICENSE](LICENSE)ファイルをご覧ください