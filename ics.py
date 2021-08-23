# coding=utf-8
# Author:HuangDongliu
# Start time:
# finally time:

class Ics():
    def __init__(self):
        # 创建ics模板
        self.repeat_temperate = \
            """BEGIN:VEVENT
DTSTART;TZID=Asia/Shanghai:{start_day}T{start_time}00
DTEND;TZID=Asia/Shanghai:{end_day}T{end_time}00
SUMMARY:{summary}
LOCATION:{location}
DESCRIPTION:{description}
BEGIN:VALARM
TRIGGER:-PT15M
ACTION:DISPLAY
END:VALARM
RRULE:FREQ=DAILY;INTERVAL={interval};COUNT={count}
END:VEVENT
"""
        self.non_repeat_temperate = \
            """BEGIN:VEVENT
DTSTART;TZID=Asia/Shanghai:{start_day}T{start_time}00
DTEND;TZID=Asia/Shanghai:{end_day}T{end_time}00
SUMMARY:{summary}
LOCATION:{location}
DESCRIPTION:{description}
BEGIN:VALARM
TRIGGER:-PT15M
ACTION:DISPLAY
END:VALARM
END:VEVENT
"""
        # 最终需要生成的日历数据
        self.calendar_data = \
            """BEGIN:VCALENDAR
VERSION:2.0
CALSCALE:GREGORIAN
X-WR-TIMEZONE:Asia/Shanghai
TZID:Asia/Shanghai
"""
        # 课程长度，一般一节课为45分钟
        self.class_period = ''

    def add_event(self, event_data: dict):
        '''添加事件
        event_data = {
            #开始天，2021年1月1日
            'start_day':'20210101',
            #开始时间：9：22
            'start_time':'0922',
            #结束时间，2021年1月1日
            'end_day':'20210101',
            #结束时间：10：22
            'end_time':'1022',
            # 标题：test
            'summary':'test',
            # 地点：shool
            'location':'shool',
            # 描述，可以用来写上课老师
            'description':'None',
            # 间隔天数：7天（一周）
            'interval':'7',
            # 重复次数
            'count':'10'
        }
        '''
        if event_data['count'] == 0:
            del event_data['count']
            del event_data['interval']
            tem = self.non_repeat_temperate.format(**event_data)
        else:
            tem = self.repeat_temperate.format(**event_data)
        self.calendar_data += tem

    def to_file(self, filename: str):
        self.calendar_data += 'END:VCALENDAR'
        with open(filename + ".ics", 'w', encoding='utf-8') as f:
            f.write(self.calendar_data)
