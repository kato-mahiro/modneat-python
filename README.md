[![Build Status](https://travis-ci.org/CodeReclaimers/neat-python.svg)](https://travis-ci.org/CodeReclaimers/neat-python)
[![Coverage Status](https://coveralls.io/repos/CodeReclaimers/neat-python/badge.svg?branch=master&service=github)](https://coveralls.io/github/CodeReclaimers/neat-python?branch=master)

## STATUS NOTE ##

This project is currently in maintenance-only mode. I will make bug fixes, do cleanup, and possibly improve sample code
as I have time, but I will not be adding any new features.  The forks by
[@drallensmith](https://github.com/drallensmith/neat-python) and [@bennr01](https://github.com/bennr01/neat-python) have
been extended beyond this implementation a great deal, so those might be better starting points if you need more
features than what you see here.

## About ##

NEAT (NeuroEvolution of Augmenting Topologies) is a method developed by Kenneth O. Stanley for evolving arbitrary neural
networks. This project is a pure-Python implementation of NEAT with no dependencies beyond the standard library. It was
forked from the excellent project by @MattKallada, and is in the process of being updated to provide more features and a
(hopefully) simpler and documented API.

For further information regarding general concepts and theory, please see
[Selected Publications](http://www.cs.ucf.edu/~kstanley/#publications) on Stanley's website.

`neat-python` is licensed under the [3-clause BSD license](https://opensource.org/licenses/BSD-3-Clause).

## Getting Started ##

If you want to try neat-python, please check out the repository, start playing with the examples (`examples/xor` is
a good place to start) and then try creating your own experiment.

The documentation, is available on [Read The Docs](http://neat-python.readthedocs.io).

## About modneat ##
modneatライブラリはneat-pythonを変更し以下の機能を提供します
- モデルにグローバルなパラメータを追加するための機能
- ヘブ則による重み更新機能
- 拡張ヘブ則による重み更新機能
- 修飾ニューロンを用いた重み更新機能

詳細については、`modneat-examples/README.md` を参考にしてください。

## Setup ##
python 3.8 にて動作確認済み

```
# Install dependencies
sudo apt update && sudo apt install -y graphviz

# Clone this repository
git clone https://github.com/katomasahiro10/modneat-python

# Install python dependencies
cd modneat-python
pip install -r requirements.txt

# Install package
pip install .

# Run example
python ./modneat-examples/run_task.py

```

## Citing ##

Here is a Bibtex entry you can use to cite this project in a publication. The listed authors are the maintainers of
all iterations of the project up to this point. 

```
@misc{neat-python,
    Title = {neat-python},
    Author = {Alan McIntyre and Matt Kallada and Cesar G. Miguel and Carolina Feher da Silva},
    howpublished = {\url{https://github.com/CodeReclaimers/neat-python}}   
  }
```
