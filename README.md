# burpsuite_hack_plus

基于二开：[depycode/burpsuite_hack: 一款代理扫描器 (github.com)](https://github.com/depycode/burpsuite_hack) 

### 解决问题：

使用sqlite数据库存储，自动创建库、表。删除重启也会自动创建

报错增加读取txt配置文件，方便扩展错误关键字

![image-20241020194738247](.\assets\image-20241020194738247.png)


一款代理扫描器

- 适配python3.6+ 

- 支持 GET/POST/无限嵌套json、list的漏洞探测

- 扫描请求去重

- 基本不会触发WAF，最小化探测

详细请见：https://www.cnblogs.com/depycode/p/17079397.html
# 整体架构
![image](https://github.com/depycode/burpsuite_hack/blob/master/p2.png)

# 使用方法
- burpsuite 插件加载：BurpExtender_ALL_UI.py ，修改socks host、port 为扫描端对应的ip和端口，然后点击set
![image](https://github.com/depycode/burpsuite_hack/blob/master/p1.png)
![image](https://github.com/depycode/burpsuite_hack/blob/master/p4.png)

- 扫描端启动
```
nohup python3 MyUDPHandler_Threads.py &
```

# 实战成果
- TSRC

![image](https://github.com/depycode/burpsuite_hack/blob/master/p3.png)

# 参考
- https://github.com/w-digital-scanner/w13scan
