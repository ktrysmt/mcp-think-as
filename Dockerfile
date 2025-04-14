# ベースイメージ
FROM python:3.13-slim

# 作業ディレクトリ作成
WORKDIR /app

# 依存ファイルコピー
COPY pyproject.toml uv.lock ./

# uvで依存インストール
RUN pip install uv && uv pip install --system

# アプリケーションコードコピー
COPY . .

# エントリポイント
CMD ["python", "main.py"]
