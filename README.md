# flask202303

Develop-Tool : VSCode </br>
Database : Sqlite3 </br>
Back-end : Flask、Python </br>
Front-end : Html5、CSS、jinja2 </br>

# 技術介紹

使用flask創建出的微服務。</br>


# 環境建置
  1. $env:FLASK_APP = "myapp"←資料夾位置  
  2. $env:FLASK_ENV = "development"
  3. $env:FLASK_DEBUG =1
  4. pip install -e . 
  5. flask run
  
# 大型基礎架構

/flask202303 </br>
- requirements.txt 
- runtime.txt 
- setup.py 
- myapp 
  - init.py
  - model.py
  - database.py
  - api
    - init.py
    - routes.py
    - templates
      - api
        - index.html
  - site
    - init.py
    - routes.py
    - templates
      - site
        - index.html 

# 進度
- 預訂新增資料庫連結(2023/3/30~)