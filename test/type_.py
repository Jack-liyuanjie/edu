def say(self, txt):
    print('hi,%s' % txt)


# type(class_name, bases, attrs)
# class_name 类名
# bases 类的继承的父类，是元组类，空元组()
# attrs 类的属性成员(方法和属性)， 是字典类型
User = type('User', (), {
    'say': say
})

u = User()
u.say('lingua')

User = type('User', (), {
    'say': lambda self, msg: 'hi, %s' % msg
})
u = User()
print(u.say('Jack'))


"""
    type元类实现的ORm映射
    Person()
        id = Column(String,max_length=20)
        name = Column(String,max_length=20)
    create table table_name(field_name Integer...)
"""