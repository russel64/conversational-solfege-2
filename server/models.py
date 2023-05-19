from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import MetaData
from sqlalchemy_serializer import SerializerMixin
from sqlalchemy.orm import validates
from sqlalchemy.ext.associationproxy import association_proxy

metadata = MetaData(naming_convention={
    "fk": "fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s",
})

db = SQLAlchemy(metadata=metadata)


# class User(db.Model, SerializerMixin):
#     __tablename__ = 'users'

#     id = db.Column(db.Integer, primary_key=True)
#     admin = db.Column(db.Boolean)
#     email = db.Column(db.String)
#     password = db.Column(db.String)

#     teacher_id = db.Column(db.Integer, db.ForeignKey('teachers.id'))
#     student_id = db.Column(db.Integer, db.ForeignKey('students.id'))

#     teachers = db.relationship('Teacher', back_populates = 'users')
#     students = db.relationship('Student', back_populates = 'users')

#     serialize_rules = ('-teachers', '-students')



# class Teacher(db.Model, SerializerMixin):
#     __tablename__ = 'teachers'

#     id = db.Column(db.Integer, primary_key=True)
#     name = db.Column(db.String)
#     image = db.Column(db.String)
#     # homeroom_id = db.Column(db.Integer, db.ForeignKey('homerooms.id'))
#     # user_id = db.Column(db.Integer, db.ForeignKey('users.id'))

#     users = db.relationship('User', back_populates = 'teachers')
#     homerooms = db.relationship('Homeroom', back_populates = 'teacher')
#     students = association_proxy('homerooms', 'students')
#     assignments = association_proxy('homerooms', 'assignments')
#     rubrics = association_proxy('homerooms', 'rubrics')
#     curriculums = association_proxy('homerooms', 'curriculums')

#     serialize_rules = ('-homerooms', '-students', '-assignments', '-rubrics', '-curriculums')



# #     user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
# #     assignment_id = db.Column(db.Integer, db.ForeignKey('assignments.id'))
# #     rubric_id = db.Column(db.Integer, db.ForeignKey('rubrics.id'))
# #     curriculum_id = db.Column(db.Integer, db.ForeignKey('curriculums.id'))

# #     user = db.relationship('User', back_populates = 'teachers')
# #     assignments = db.relationship('Assignment', back_populates ='teacher')
# #     rubrics = db.relationship('Rubric', back_populates = 'teacher')
# #     curriculums = db.relationship('Curriculum', back_populates = 'teacher')

    
# #     serialize_rules = ()




# class Student(db.Model, SerializerMixin):
#     __tablename__= 'students'

#     id = db.Column(db.Integer, primary_key=True)
#     name = db.Column(db.String)
#     image = db.Column(db.String)
#     grade_level = db.Column(db.Integer)
#     # homeroom_id = db.Column(db.Integer, db.ForeignKey('homerooms.id'))
#     # user_id = db.Column(db.Integer, db.ForeignKey('users.id'))

#     homeroom = db.relationship('Homeroom', back_populates = 'students')
#     users = db.relationship('User', back_populates= 'students')
#     assignments = association_proxy('homerooms', 'assignments')
#     curriculums = association_proxy('homerooms', 'curriculums')

#     serialize_rules = ('-homeroom', '-assignments', '-curriculum')



    
# #     assignment_id = db.Column(db.Integer, db.ForeignKey('assignments.id'))
# #     curriculum_id = db.Column(db.Integer, db.ForeignKey('curriculums.id'))

# #     
# #     assigments = db.relationship('Assignment', back_populates = 'students')
# #     curriculums = db.relationship('Curriculum', back_populates = 'students')

# #     serialize_rules = ()



# class Homeroom(db.Model, SerializerMixin):
#     __tablename__= 'homerooms'

#     id = db.Column(db.Integer, primary_key=True)
#     name = db.Column(db.String)
#     grade_level = db.Column(db.Integer)
#     created_at = db.Column(db.DateTime, server_default=db.func.now())
#     updated_at = db.Column(db.DateTime, server_onupdate=db.func.now())

#     teacher_id = db.Column(db.Integer, db.ForeignKey('teachers.id'))
#     student_id = db.Column(db.Integer, db.ForeignKey('students.id'))
#     assignment_id = db.Column(db.Integer, db.ForeignKey('assignments.id'))
#     rubric_id = db.Column(db.Integer, db.ForeignKey('rubrics.id'))
#     curriculum_id = db.Column(db.Integer, db.ForeignKey('curriculums.id'))

#     teacher = db.relationship('Teacher', back_populates = 'homerooms')
#     students = db.relationship('Student', back_populates = 'homeroom')
#     assignments = db.relationship('Assignment', back_populates = 'homerooms')
#     rubrics = db.relationship('Rubric', back_populates = 'homerooms')
#     curriculums = db.relationship('Curriculum', back_populates = 'homerooms')

#     serialize_rules = ('-created_at', '-updated_at', '-teacher', '-students', '-assignments', '-rubrics', '-curriculums')



# class Assignment(db.Model, SerializerMixin):
#     __tablename__= 'assignments'

#     id = db.Column(db.Integer, primary_key=True)
#     title = db.Column(db.String)
#     image = db.Column(db.String)
#     unit = db.Column(db.Integer)
#     step = db.Column(db.Integer)
#     task = db.Column(db.String)
#     grade = db.Column(db.Integer)
#     created_at = db.Column(db.DateTime, server_default=db.func.now())
#     updated_at = db.Column(db.DateTime, server_onupdate=db.func.now())
#     # homeroom_id = db.Column(db.Integer, db.ForeignKey('homerooms.id'))

#     homerooms = db.relationship('Homeroom', back_populates = 'assignments')

#     serialize_rules = ('-created_at', '-updated-at', '-homerooms')

# #     teacher_id = db.Column(db.Integer, db.ForeignKey('teachers.id'))
# #     student_id = db.Column(db.Integer, db.ForeignKey('students.id'))
# #     rubric_id = db.Column(db.Integer, db.ForeignKey('rubrics.id'))
# #     curriculum_id = db.Column(db.Integer, db.ForeignKey('curriculums.id'))

# #     teacher = db.relationship('Teacher', back_populates = 'assignments')
# #     students = db.relationship('Student', back_populates = 'assignments')
# #     rubric = db.relationship('Rubric', back_populates = 'assignment')
# #     curriculums = db.relationship('Curriculum', back_populates = 'assignments')

# #     serialize_rules = ()



# class Rubric(db.Model, SerializerMixin):
#     __tablename__= 'rubrics'

#     id = db.Column(db.Integer, primary_key=True)
#     title = db.Column(db.String)
#     task_descriptions = db.Column(db.String)
#     grading_scale = db.Column(db.Integer)
#     created_at = db.Column(db.DateTime, server_default=db.func.now())
#     updated_at = db.Column(db.DateTime, server_onupdate=db.func.now())
#     # homeroom_id = db.Column(db.Integer, db.ForeignKey('homerooms.id'))

#     homerooms = db.relationship('Homeroom', back_populates = 'rubrics')

#     serialize_rules = ('-created_at', '-updated_at', '-homerooms')


# #     teacher_id = db.Column(db.Integer, db.ForeignKey('teachers.id'))
# #     assignment_id = db.Column(db.Integer, db.ForeignKey('assignments.id'))

# #     teacher = db.relationship('Teacher', back_populates = 'rubrics')
# #     assignment = db.relationship('Assignment', back_populates = 'rubric')





# class Curriculum(db.Model, SerializerMixin):
#     __tablename__= 'curriculums'

#     id = db.Column(db.Integer, primary_key=True)
#     unit = db.Column(db.Integer)
#     step = db.Column(db.Integer)
#     task = db.Column(db.String)
#     # homeroom_id = db.Column(db.Integer, db.ForeignKey('homerooms.id'))

#     homerooms = db.relationship('Homeroom', back_populates = 'curriculums')

#     serialize_rules = ('-homerooms')

# #     teacher_id = db.Column(db.Integer, db.ForeignKey('teachers.id'))
# #     student_id = db.Column(db.Integer, db.ForeignKey('students.id'))
# #     assignment_id = db.Column(db.Integer, db.ForeignKey('assignments.id'))

# #     teacher = db.relationship('Teacher', back_populates = 'curriculums')
# #     students = db.relationship('Student', back_populates = 'curriculums')
# #     assignments = db.relationship('Assignment', back_populates = 'curriculums')

# #     serialize_rules = ()


class Course(db.Model, SerializerMixin):
    __tablename__= 'courses'

    id = db.Column(db.Integer, primary_key=True)
    cover = db.Column(db.String)
    coursesName = db.Column(db.String)
    priceAll = db.Column(db.String)
    pricePer = db.Column(db.String)

    signups = db.relationship('SignUp', back_populates ='course')
    courTeachers = association_proxy('signups', 'courTeacher')

    serialize_rules = ('-signups', 'courTeachers')



class CourTeacher(db.Model, SerializerMixin):
    __tablename__= 'courTeachers'

    id = db.Column(db.Integer, primary_key=True)
    dcover = db.Column(db.String)
    name = db.Column(db.String)
    totalTime = db.Column(db.String)

    signups = db.relationship('SignUp', back_populates='courTeacher')
    courses = association_proxy('signups', 'course')

    serialize_rules = ('-signups', '-courses')

    

class SignUp(db.Model, SerializerMixin):
    __tablename__= 'signups'

    id = db.Column(db.Integer, primary_key=True)
    course_id = db.Column(db.Integer, db.ForeignKey('courses.id'))
    courTeacher_id = db.Column(db.Integer, db.ForeignKey('courTeachers.id'))

    course = db.relationship('Course', back_populates='signups')
    courTeacher = db.relationship('CourTeacher', back_populates='signups')
 


class Blog(db.Model, SerializerMixin):
    __tablename__= 'blogs'

    id = db.Column(db.Integer, primary_key=True)
    author = db.Column(db.String)
    date = db.Column(db.String)
    com = db.Column(db.String)
    title = db.Column(db.String)
    desc = db.Column(db.String)
    cover = db.Column(db.String)




class Specialist(db.Model, SerializerMixin):
    __tablename__= 'specialists'

    id = db.Column(db.Integer, primary_key=True)
    cover = db.Column(db.String)
    name = db.Column(db.String)
    bio = db.Column(db.String)


    

    



    




    



