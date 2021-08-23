# coding=utf-8
import sys
import getopt

from schedule_export import schedule_export


def usage():
    print(
        """请输入完整参数
    -h:显示帮助
    -u:学号
    -p:密码
    """.replace(" ", ''))


# 获取参数
argv = sys.argv
# 如果没有获取到任何参数，显示提示
if len(argv) == 1:
    usage()
    sys.exit()

# 检测是否成功获取到参数
try:
    opts, args = getopt.getopt(argv[1:], "u:p:h")
except getopt.GetoptError:
    usage()
    sys.exit()

username, password = None, None
for opt, arg in opts:
    if opt == '-h':
        usage()
        sys.exit()
    elif opt == '-u':
        username = arg
    elif opt == '-p':
        password = arg
# 检测参数是否完整
if None in [username, password]:
    usage()
    sys.exit()
r = schedule_export(username=username, password=password)
if r['status'] == 0:
    print("恭喜您导出成功")
else:
    print("错误：%s" % r['error'])
