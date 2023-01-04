# ！/user/bin/env python
# -*- coding:utf-8 -*-
from flask import Flask, current_app, jsonify, session
from TODOLIST_CREATE_LIST import db, todolist, app
import datetime

if __name__ == "__main__":
    with app.app_context():
        print(current_app.name)

        # 添加待办事项
        @app.route("/add", methods=["POST"])
        def my_add():
            now = datetime.datetime.now()
            one1 = todolist(id=1, title="Linear Math Examination", content="Linear Math Online Final Exam",
                            status="complete", add_time=now.date(),
                            deadline=20221231)
            one2 = todolist(id=2, title="Math Examination", content="Math Online Final Exam", status="incomplete", add_time=now.date(), deadline=20230108)
            one3 = todolist(id=3, title="West2 Online ddl", content="West2 Online learning", status="incomplete", add_time=now.date(),
                            deadline=20230112)

            # 法一：单独增加
            db.session.add(one1)
            db.session.add(one2)
            db.session.add(one3)
            db.session.commit()

            # 法二：添加一个列表
            # db.session.add_all([one1, one2, one3])
            # db.session.commit()

            return jsonify(msg="successful")

        # 查找待办事项
        @app.route("/search", methods=["GET"])
        def my_search():
            # 法一：get(id),查找一条事项
            one_item = todolist.query.get(2)
            print(one_item.title)
            # 结果：<todolist 2>

            # 法二：all(),查找所有事项
            all_item = todolist.query.all()
            print(all_item)
            # 结果：[<todolist 1>, <todolist 2>, <todolist 3>]

            # 法三：filter(条件),按照条件查询(查找所有已完成事项/所有待办事项)
            one_item = todolist.query.filter(todolist.id >= 2).all()
            # first()返回实例对象，all()返回实例对象的列表，否则返回SQL语句
            for i in one_item:
                print(i.id, i.title, i.content, i.status, i.add_time, i.deadline)
            # 结果：打印第二条和第三条待办事项

            # 法四：filter_by()
            one_item = todolist.query.filter_by(title="West2Online ddl")
            print(one_item)
            # cls.query.filter(类名.属性名 条件操作符 条件) 过滤特定条件，返回的是query对象
            # cls.query.filter_by(关键字参数对) 单条件查询，条件必须关键字参数，而且and连接

            return jsonify(msg="successful")

        # 修改待办事项（根据条件修改）
        @app.route("/modify", methods=["POST"])
        def my_modify():
            # 法一：update(),单项或多项（全部改为待办/已完成）
            one_item = todolist.query.filter(todolist.status == "complete").update({"status": "incomplete"})
            db.session.commit()
            print(one_item)  # 返回修改数据的个数

            # 法二：直接修改
            one_item = todolist.query.filter(todolist.status == "incomplete").first()
            one_item.status = "complete"
            db.session.add(one_item)
            db.session.commit()

            return jsonify(msg="successful")

        # 删除待办事项
        @app.route("/delete", methods=["POST"])
        def my_delete():
            one_item = todolist.query.filter(todolist.status == "complete").delete()
            db.session.commit()
            print(one_item)  # 返回修改数据的个数
            return jsonify(msg="successful")

        app.run(host="0.0.0.0")
