# MCP サーバー ダイスロール (mcp-server-diceroll)

シンプルな MCP (Model Calling Protocol) サーバーのデモプロジェクトです。このサーバーはダイスロール機能と基本的な数値演算機能を提供します。

## 機能

- 数値の加算
- カスタマイズ可能なダイスロール（サイコロの面数と振る回数を指定可能）
- UUID生成（バージョン4またはバージョン1）
- 動的な挨拶メッセージ生成

## 要件

- Python 3.12 以上
- mcp ライブラリ 1.6.0 以上
- uv (Python パッケージマネージャー)

## インストール

1. リポジトリをクローンします：

```bash
git clone https://github.com/yourusername/mcp-server-diceroll.git
cd mcp-server-diceroll
```

2. uvがインストールされていない場合は、インストールします：

```bash
curl -sSf https://astral.sh/uv/install.sh | bash
```

3. uvを使用して仮想環境を作成し、依存関係をインストールします：

```bash
uv venv
source .venv/bin/activate  # macOS/Linuxの場合
# または
.venv\Scripts\activate  # Windowsの場合

uv pip install -e .
```

## 使用方法

サーバーを起動するには：

```bash
python server.py
```

または、uvを使用して実行することもできます：

```bash
uv run python server.py
```

サーバーが起動すると、以下のツールが利用可能になります：

1. **add** - 2つの数値を加算します
2. **roll_dice** - サイコロを振ります（デフォルトは6面体のサイコロを1回）
3. **generate_uuid** - UUIDを生成します（デフォルトはバージョン4、バージョン1も指定可能）
4. **greeting://{name}** - 指定された名前に対する挨拶メッセージを生成します

## 参考資料

- [サイコロから始めるModel Context Protocol (MCP): 生成AIと外部ツールを繋ぐためのプロトコル](https://zenn.dev/herp_inc/articles/00917098b3ffd3)
- [Anthropic MCP公式発表](https://www.anthropic.com/news/model-context-protocol)
- [modelcontextprotocol/python-sdk](https://github.com/modelcontextprotocol/python-sdk)

## 例

サーバーにリクエストを送信する方法については、MCP クライアントのドキュメントを参照してください。
