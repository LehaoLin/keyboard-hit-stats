## Introduction
A small Python script to get the number of daily keyboard hits. (To push myself to work more.)
一个记录每日键盘敲击次数的小脚本(用来督促自己)

At last, everyday's keyboard press stats are in the "./data/" directory.
最后每日的键盘敲击次数都在data目录下

This script is only for recording the number of daily hits, not for specific key.
本脚本仅记录次数，不记录具体按键。

## Usage

```bash
pip3 install -r requirements.txt
```

```bash
python3 main.py
```

Or you can use pm2 to manage it

```bash
pm2 start main.py -x --interpreter python3
```


