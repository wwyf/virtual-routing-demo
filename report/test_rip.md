# RIP协议测试报告

RIP协议能够使用距离向量算法，自动的配置路由表

## 测试项目 ：

1. 路由表的自动配置
1. 网络拓扑的改变对路由表的影响


## 样例:test文件夹



### 测试步骤一

该步骤主要说明路由器的自动配置可用。

1. 使用脚本对每一台路由器发送查看路由表的指令
1. 对路由器设置延时，在此延时阶段，测试路由器的连通情况
1. 延时结束后，路由器自动开启rip协议，同时路由器由我手动开启，并适时关闭本路由器的调试信息输出
1. 自动配置完成后，此时所有路由器的自动脚本已经运行完成，此后手动关闭所有路由器的调试信息输出
1. 手动展示部分
    1. 展示路由表
    1. send 信息，表示已连通

#### 测试结果

放一个视频

### 测试步骤二

由于RIP协议能够对网络拓扑的变化，及时作出回应。对路由器的下线， RIP应该能够发现路由器的下线，并将该下线信息广播出来，让其他的路由器都知道到达该下线路由器不可达。并将这变化通过距离向量表体现出来

下面进行测试

<!-- 
### 测试步骤三

即使拓扑结构不变，链路费用的大小对路由表同样会有影响，原本在最短路中经过的链路如果费用突然变得特别大，应该需要将这个信息反映到本机的距离向量表中，并将这个信息广播到其他路由器，让其他路由器的距离向量表根据这个RIP更新报文进行适应和修改，并更新最短路径。
 -->




