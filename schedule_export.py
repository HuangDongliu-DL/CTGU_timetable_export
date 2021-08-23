# coding=utf-8
import time

import requests

from AESCipher import encrypt
from ics import Ics
from config import *


def schedule_export(username, password):
    """
    0. 导出成功
    1. 密码错误或者登入错误
    2. 课表为空
    """
    # 获取AES加密后的密码
    encrypted_password = encrypt(secretkey=cryptoKey, passowrd=password)
    # 创建Session对象
    session = requests.session()
    # 构建登入数据
    login_data = {
        "userName": username,
        "password": encrypted_password,
        "isWeekLogin": False
    }
    # 开始登入
    login_statue = session.post(
        url=login_url,
        headers=request_heads,
        data=login_data
    )
    if 'validate' in login_statue.json():
        pass
    else:
        return {"status": 1, 'error': login_statue.json()['msg']}
    # 获取应用cookie
    session.get(url=get_curriculum_cookies_url)

    curriculum_inquiry_statues = session.post(
        url=curriculum_inquiry_url,
        data={"XNXQDM": "2021-2022-1"}
    )
    courses_data = curriculum_inquiry_statues.json()['datas']['cxxszhxqkb']['rows']
    if not courses_data:
        return {'status': 2, 'error': "您当前学期的课表数据为空，你可以到教务系统检查一下"}
    # 实例化ics对象
    ics = Ics()
    for course in courses_data:
        course_name = course['KCM']  # 课程名称
        course_room = course['JASMC']  # 教室
        course_teacher = course['SKJS']  # 老师
        course_week = course['ZCMC']  # 开课周数
        course_time = [course['KSJC'], course['JSJC']]  # 上课时间
        course_day_of_week = course['SKXQ']

        for single_course_week in course_week.split(','):
            is_single_or_double = 0
            # 开始适配单双周
            if '双' in single_course_week or '单' in single_course_week:
                is_single_or_double = True
                single_course_week = single_course_week.replace("(双)", "")
                single_course_week = single_course_week.replace("(单)", "")
                interval = 14
            else:
                interval = 7

            single_course_week = single_course_week.replace('周', '').split('-')

            # 计算重复次数
            if len(single_course_week) == 2:
                count = eval(single_course_week[1]) - eval(single_course_week[0]) + 1
            elif len(single_course_week) == 1:
                count = 0
            else:
                assert False, '该课程情况未适配'
            if is_single_or_double:
                count = int((count+1) / 2)

            Semester_start_timestamp = time.mktime(time.strptime(Semester_start_time, '%Y-%m-%d %H:%M:%S'))
            start_time_stamp = Semester_start_timestamp + (eval(single_course_week[0]) - 1) * One_week_timestamp
            # 适配第几节课
            if course_time[0] == 3:
                start_time_stamp += 2 * One_hour_timestamp
            elif course_time[0] == 5:
                start_time_stamp += 6 * One_hour_timestamp
            elif course_time[0] == 7:
                start_time_stamp += 8 * One_hour_timestamp
            elif course_time[0] == 9:
                start_time_stamp += 11 * One_hour_timestamp
            # 适配星期几
            start_time_stamp += (course_day_of_week - 1) * One_day_timestamp
            if course_time[1] - course_time[0] == 1:
                break_time = 10 * 60
            elif course_time[1] - course_time[0] == 2:
                break_time = 20 * 60 + 10 * 60
            elif course_time[1] - course_time[0] == 3:
                break_time = 20 * 60 + 20 * 60
            else:
                break_time = (course_time[1] - course_time[0]) * 10 * 60

            end_time_stamp = start_time_stamp + break_time + \
                             ((course_time[1] - course_time[0]) + 1) * One_session_time_timestamp

            start_day = time.strftime("%Y%m%d", time.localtime(start_time_stamp))
            start_time = time.strftime("%H%M", time.localtime(start_time_stamp))
            end_day = time.strftime("%Y%m%d", time.localtime(end_time_stamp))
            end_time = time.strftime("%H%M", time.localtime(end_time_stamp))

            event_data = {
                'start_day': start_day,
                'start_time': start_time,
                'end_day': end_day,
                'end_time': end_time,
                'summary': course_name,
                'location': course_room,
                'description': course_teacher,
                'interval': interval,
                'count': count
            }
            ics.add_event(event_data=event_data)
    ics.to_file(export_file_dic + "%s" % username)
    return {'status': 0, 'error': ics.calendar_data}
