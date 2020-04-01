# apibot

### API tools, support post/get

### get source code
    git clone git@github.com:freeddser/apibot.git



### setup env
    pyenv activate py3.7.0
    
    pip install -i https://pypi.douban.com/simple -r requirements.txt 
    
    python main.py 

### example
    response:
        [url]--->http://127.0.0.1:8080/
        [method]--->POST
        [Content-Type]--->application/x-www-form-urlencoded
        [json]--->None
        [query_string]--->b''
        [form]-->ImmutableMultiDict([('k1k', 'abc')])
        
    response:
        [url]--->http://127.0.0.1:8080/
        [method]--->POST
        [Content-Type]--->application/x-www-form-urlencoded
        [json]--->None
        [query_string]--->b''
        [form]-->ImmutableMultiDict([('{"id":"1"}\n', '')])