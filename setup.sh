mkdir -p ~/.streamlit/

echo "\
[server]\n\
headless = true\n\
port = $PORT\n\
enableCORS = false\n\
" > ~/.streamlit/config.toml

# Instalação das dependências Python
pip install asgiref==3.8.1 \
            beautifulsoup4==4.12.3 \
            blinker==1.7.0 \
            certifi==2024.2.2 \
            charset-normalizer==3.3.2 \
            click==8.1.7 \
            colorama==0.4.6 \
            defusedxml==0.7.1 \
            Django==4.2.11 \
            django-bootstrap-icons==0.8.7 \
            django-bootstrap-v5==1.0.11 \
            django-bootstrap4==24.1 \
            Flask==3.0.1 \
            idna==3.6 \
            iniconfig==2.0.0 \
            itsdangerous==2.1.2 \
            Jinja2==3.1.3 \
            MarkupSafe==2.1.4 \
            packaging==23.2 \
            pillow==10.2.0 \
            pluggy==1.4.0 \
            pytest==8.1.0 \
            python-dotenv==1.0.1 \
            requests==2.31.0 \
            soupsieve==2.5 \
            sqlparse==0.4.4 \
            tzdata==2024.1 \
            urllib3==2.2.1 \
            Werkzeug==3.0.1
