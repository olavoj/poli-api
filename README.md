# poli-api
API para processar produtos Poli em XML

## Gerador de descri\xc3\xa7\xc3\xb5es

O reposit\xc3\xb3rio inclui um pequeno aplicativo em **Streamlit** que usa a API da OpenAI (vers\xc3\xa3o 1.x) para gerar descri\xc3\xa7\xc3\xb5es de produtos. Para execut\xc3\xa1-lo:

```bash
pip install -r requirements.txt
streamlit run streamlit_app.py
```

A dependência **openai** deve estar na versão 1.x (por exemplo `openai>=1.0,<2.0`).

\xc3\x89 necess\xc3\xa1rio definir a vari\xc3\xa1vel de ambiente `OPENAI_API_KEY` com sua chave antes de rodar.
