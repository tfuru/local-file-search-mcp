# local-file-search-mcp

# 概要
環境変数(.env)指定したディレクトリ内を全文検索してファイル内容とリンクを提供するPythonスクリプト。Rancher Desktop(Docker Desktop) 環境で動作する

# 一式をダウンロード
git clone して一式をローカルに保存する  

```
git clone https://github.com/tfuru/local-file-search-mcp.git
cd local-file-search-mcp
```

# 検索対象ドキュメントダウンロード
再帰的に取得して検索対象のドキュメントをローカルにダウンロードする
```
cd local-file-search-mcp/app/data
wget -r -l 3 -L https://docs.cluster.mu/script/ -P ClusterCreatorKitScriptReference/
```

# 起動方法
Rancher Desktop(Docker Desktop) を起動した環境でイメージ作成,起動ができる

```
cd local-file-search-mcp
# 環境変数を修正する
code .env

# イメージの作成と起動
docker compose build
docker compose up -d

docker compose logs -f
```

# ローカルでのテスト実行
```
cd local-file-search-mcp/app
python test.py
```

# VSCode エージェント(MCPクライアント)での設定

```:.vscode/mcp.json
{
  "servers": {
    "local-file-search-mcp": {
      "type": "sse",
      "url": "http://127.0.0.1:8000/sse",
    }
  }
}
```