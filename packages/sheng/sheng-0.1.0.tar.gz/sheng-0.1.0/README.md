# The Sheng Programming Language

[![build](https://img.shields.io/github/workflow/status/luojiahai/sheng/Upload%20Python%20Package?style=flat-square)](https://github.com/luojiahai/sheng/actions/workflows/python-publish.yml)
[![python](https://img.shields.io/pypi/pyversions/sheng?style=flat-square)](https://pypi.org/project/sheng/)
[![pypi](https://img.shields.io/pypi/v/sheng?style=flat-square)](https://pypi.org/project/sheng/)
[![license](https://img.shields.io/pypi/l/sheng?style=flat-square)](https://pypi.org/project/sheng/)

This is a Chinese programming language. The philosophies of the Sheng grammar are interpretable, colloquial, and virtually none punctuation marks. The compiler is implemented in Python with the [PLY (Python Lex-Yacc)](https://github.com/dabeaz/ply) package which processes lexing and parsing in the phases of the compilation.

![sheng-logo](./repository-open-graph.jpg)

---

## Usage

```
sheng [option] [file]
```

---

## Installing and Running

> Note: Sheng requires Python 3.9 or later

### PyPI [Recommended]

Install the Sheng compiler from [The Python Package Index (PyPI)](https://pypi.org/project/sheng/):
> Note: This method requires Internet access.
```
pip install sheng
```
Then, execute command `sheng [option] [file]` to run.

### Other install methods

#### Build and install

Build the code and install the Sheng compiler from the local builds:
> Note: This method does not require Internet access.
```
python3 -m pip install --upgrade pip
python3 -m pip install --upgrade build
python3 -m build
pip install ./dist/<.whl file> --force-reinstall
```
Then, execute command `sheng [option] [file]` to run.

#### Run the compiler module via Python

Run the compiler directly without building and installing in advance:
> Note: This method requires Python 3.9 or later in your environment.
```
python3 -m src [option] [file]
```

---

## Getting Started

This is the Sheng code in `example/helloworld.yn`:
```
语句 赋值 字符串 开始 你好，世界！ 结束
打印 语句
```
where `语句` (phrase) is a variable name which is `赋值` (assign)ed a `字符串` (string) value `你好，世界！` (Hello, World!) surrounded by `开始` (begin) and `结束` (end) keywords.

The above Sheng code can be interpreted in English as:
```
phrase assign string begin Hello, World! end
print phrase
```

This is the Python equivalent of the above Sheng code:
```
phrase = "你好，世界！"
print(phrase)
```

Compile the `.yn` file via `sheng` executable:
```
sheng example/helloworld.yn
```

You should see the following output in `stdout`:
```
你好，世界！
```

---

## Grammar

See the [Sheng Grammar](./GRAMMAR.md) documentation.

---

## Contributing

I am excited to work alongside you to build and enhance the Sheng Programming Language\!

***BEFORE you start work on a feature/fix***, please read and follow the [Contributor's Guide](./CONTRIBUTING.md) to help avoid any wasted or duplicate effort.

---

## Code of Conduct

This project has adopted the [Contributor Covenant Code of Conduct](./CODE_OF_CONDUCT.md). For more information contact [luo@jiahai.co](mailto:luo@jiahai.co) with any additional questions or comments.
