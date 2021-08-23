# coding=utf-8

# 登入url
login_url = "http://jwxt.ctgu.edu.cn/jwapp/sys/emapfunauth/loginValidate.do"
# 获取应用cookie的url
get_curriculum_cookies_url = "http://jwxt.ctgu.edu.cn/jwapp/sys/emaphome/appShow.do?id=db7d398917944552b99cde73ce5d7d4a"

# 课表查询url
curriculum_inquiry_url = "http://jwxt.ctgu.edu.cn/jwapp/sys/wdkb/modules/xskcb/cxxszhxqkb.do"
# 上课时间未确定课程查询url
undefined_curriculum_inquiry_url = "http://jwxt.ctgu.edu.cn/jwapp/sys/wdkb/modules/xskcb/xswpkc.do"


# AES加密密钥
cryptoKey = "r0aNwZvApKlj9C0r"

# 本学期的开学时间
term_begin_time = '20210905'

# 导出文件存放地址
export_file_dic = "./"

# 请求头
request_heads = {
            "Accept": "application/json, text/javascript, */*; q=0.01",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.61 Safari/537.36",
            "Accept-Encoding": "gzip, deflate",
            "Accept-Language": "zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6,zh-TW;q=0.5",
            "Cache-Control": "no-cache",
            "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
            "Connection": "keep-alive",
            "Pragma": "no-cache",
        }

# 一个课间的秒数
One_break_time_timestamp = 10 * 60
# 一个session的秒数
One_session_time_timestamp = 45 * 60
# 一个小时的秒数
One_hour_timestamp = 60 * 60
# 一天的时秒数
One_day_timestamp = 24 * One_hour_timestamp
# 一周的秒数
One_week_timestamp = 7 * One_day_timestamp
# 学期开始时间
Semester_start_time = "2021-09-06 08:00:00"
