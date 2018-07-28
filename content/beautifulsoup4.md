Title: Beautiful Soup 4 
Date: 2017-10-21 10:20
Category: Python
Tags: python, web scrapping
Authors: José Aniceto
Summary: Python Web scrapping with Beautiful Soup 4 


## Required modules
```
pip install beautifulsoup4
pip install lxml
pip instal html5lib
pip install requests
```

## Usage

```python
from bs4 import BeautifulSoup
import requests

source = requests.get('http://example.com').text
soup = BeautifulSoup(source, 'lxml')
```

## References

https://www.youtube.com/watch?v=ng2o98k983k
