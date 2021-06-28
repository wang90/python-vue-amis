# python-vue-amis
#### A quick way to build a Python web

### Getting Started
`````
git clone https://github.com/wang90/python-vue-amis.git
rm -rf .git && git init

# first use app
virtualenv --python=python3.7 venv
source venv/bin/activate
pip install -r requirement.txt
uvicorn projectionist.app:app --reload

# second use app
source venv/bin/activate
uvicorn projectionist.app:app --reload
``````

### Frontend 
* 前端内容可以不做使用，把文件打包至projectionist/dist文件即可
- vue 2.0 +
- node 14 +
```````
cd web
npm install 
npm start
npm run-script build
```````

### Backend

- Python 3.6 +
- FastAPI: https://fastapi.tiangolo.com/
- amis: https://github.com/baidu/amis
