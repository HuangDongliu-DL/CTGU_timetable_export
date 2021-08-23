# CTGU课表导出

一个将教务处课表导出为ICS的小工具，ICS是一种通用的日历文件格式可以导入到几乎所有的日历软件与大多数的课表软件中。你可以直接到这个网站上使用[课表导出 (dongliu.online)](https://dongliu.online/curriculum),也可以下载源码使用。

## 一、开始使用

#### 1. 安装依赖

```shell
pip3 install -r requirements.txt
```

#### 2. 生成课表

```shell
# username为学号，password为教务处密码
python3 main.py -u <username> -p <password>
```

## 二、示例

- Google Calendar

  ![Google Calendar](https://dongliu-1301367244.cos.ap-shanghai.myqcloud.com/img/20210822185330.png)

- Windows Calendar

  ![Windows Calendar](https://dongliu-1301367244.cos.ap-shanghai.myqcloud.com/img/20210822185416.png)

- Samsung Phone

  ![](https://dongliu-1301367244.cos.ap-shanghai.myqcloud.com/img/20210822184637.jpg)