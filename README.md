# <img src="roadmap.png" width="35" align="top" /> Caching Proxy

Caching Proxy project from [roadmap.sh](https://roadmap.sh/projects/caching-server) Backend Developer Roadmap. 

## 📝 About the Project

A CLI tool that starts a caching proxy server. It forwards requests to the actual server and caches the responses. If the same request is made again, it'll return the cached response instead of forwarding the request to the server.

## 🛠️ Built With
[![Python][Python]][Python-url]
[![Flask][Flask]][Flask-url]
[![SQLite][SQLite]][SQLite-url]
[![Requests][Requests]][Requests-url]

## 📌 Installation
1. First, clone the repository and cd into the project:
```
git clone https://github.com/syssefim/roadmap.sh-Caching-Proxy
cd roadmap.sh-Caching-Proxy
```
2. Next, create a virtual environment and activate it:
```
python3 -m venv .venv
source .venv/bin/activate
```
3. Then, install the CLI tool:
```
pip install .
```

## 💻 Usage
Start the proxy server by pointing it at an origin server:
```
caching-proxy --port 3000 --origin http://dummyjson.com
```
This starts a caching proxy on port `3000`. Any request made to it, such as `http://localhost:3000/products` is forwarded to `http://dummyjson.com/products`, and the response is cached in a local SQLite database named `cache.db`. 

The next time the same request is made, the cached response is returned instead of forwarding it again. Additionally, you can clear the cache at any time with:

```
caching-proxy --clear-cache
```











---

<div align="center">
  <p>
    Serafim Sharkov • 2026
  </p>
  <p>
    <a href="https://github.com/syssefim">GitHub</a> • 
    <a href="https://www.linkedin.com/in/serafim-sharkov/">LinkedIn</a>
  </p>
</div>

<!-- MARKDOWN LINKS & IMAGES -->
[Python]: https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white
[Python-url]: https://www.python.org/
[Flask]: https://img.shields.io/badge/Flask-000000?style=for-the-badge&logo=flask&logoColor=white
[Flask-url]: https://flask.palletsprojects.com/
[SQLite]: https://img.shields.io/badge/SQLite-003B57?style=for-the-badge&logo=sqlite&logoColor=white
[SQLite-url]: https://www.sqlite.org/
[Requests]: https://img.shields.io/badge/Requests-000000?style=for-the-badge&logo=python&logoColor=white
[Requests-url]: https://requests.readthedocs.io/
