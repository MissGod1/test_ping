### 简介

> 这是一个简单的延迟测试脚本，主要是测试本地主机与vps之间的网络延迟，  便于选择与本机延迟最低的vps节点。

### 使用

> 由于是自用，所以并没有设置过多的命令行参数，也没有设置多线程，所以  使用时运行过慢是正常的。脚本默认发10个包如需修改请更改25行的count值。  

- 使用命令：
```shell
python test_ping.py [filename]
```

- 结果说明：
```
per: 丢包率
max: 最高延迟
avg: 最低延迟
```

### 注意

- 使用python脚本执行前倾安装ping模块
```shell
pip install ping
```

- 假如你的系统并未安装python环境 请使用dist/test_ping目录下打包好  的test_ping.exe

- 如果测试结果出现中文乱码请自行修改扫描文件的编码格式

- 如需添加新的vps地址文件请参照它提供的txt文件，自带的文件为[搬瓦工](https://bwh1.net/index.php)  与[vutrl](https://www.vultr.com/)的测试地址