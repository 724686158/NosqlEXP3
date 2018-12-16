import pymongo
import pandas as pd

if __name__ == '__main__':
    client = pymongo.MongoClient('47.98.124.149', 27017)
    db = client['user201834969']

    # student
    xlsx = pd.ExcelFile('student.xlsx')
    df = pd.read_excel(xlsx)
    data = []
    for row in df.iterrows():
        data.append({'sid': row[1]['SID'],
                           'name': row[1]['NAME'],
                           'sex': row[1]['SEX'],
                           'age': row[1]['AGE'],
                           'birthday': row[1]['BIRTHDAY'],
                           'dname': row[1]['DNAME'],
                           'class_name': row[1]['CLASS'],
                           })
    db['student'].insert_many(data)
    print("student表共{}条数据".format(db['student'].count()))

    #teacher
    xlsx = pd.ExcelFile('teacher.xlsx')
    df = pd.read_excel(xlsx)
    data = []
    for row in df.iterrows():
        data.append({'tid': row[1]['TID'],
                           'name': row[1]['NAME'],
                           'sex': row[1]['SEX'],
                           'age': row[1]['AGE'],
                           'dname': row[1]['DNAME'],
                           })
    db['teacher'].insert_many(data)
    print("teacher表共{}条数据".format(db['teacher'].count()))

    # course
    xlsx = pd.ExcelFile('course.xlsx')
    df = pd.read_excel(xlsx)
    data = []
    for row in df.iterrows():
        data.append({'cid': row[1]['CID'],
                              'name': row[1]['NAME'],
                              'fcid': row[1]['FCID'],
                              'credit': int(row[1]['CREDIT']) if row[1]['CREDIT'] else None,
                              })
    db['course'].insert_many(data)
    print("course表共{}条数据".format(db['course'].count()))

    # student_course
    xlsx = pd.ExcelFile('student_course.xlsx')
    df = pd.read_excel(xlsx)
    data = []
    for row in df.iterrows():
        data.append({'sid': int(row[1]['SID']) if row[1]['SID'] else None,
                             'cid': int(row[1]['CID']) if row[1]['CID'] else None,
                             'score': int(row[1]['SCORE']) if row[1]['SCORE'] else None,
                             'tid': int(row[1]['TID']) if row[1]['TID'] else None,
                             })
    db['student_course'].insert_many(data)
    print("student_course表共{}条数据".format(db['student_course'].count()))

    # teacher_course
    xlsx = pd.ExcelFile('teacher_course.xlsx')
    df = pd.read_excel(xlsx)
    data = []
    for row in df.iterrows():
        data.append({'cid': int(row[1]['CID']) if row[1]['CID'] else None,
                     'tid': int(row[1]['TID']) if row[1]['TID'] else None,
                     })
    db['teacher_course'].insert_many(data)
    print("teacher_course表共{}条数据".format(db['teacher_course'].count()))