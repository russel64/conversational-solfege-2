from flask import Flask, request, jsonify, make_response
from flask_cors import CORS
from flask_migrate import Migrate
from flask_restful import Api, Resource


# Local imports
from models import db, Course, CourTeacher, SignUp, Blog

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

CORS(app)
db.init_app(app)
migrate = Migrate(app, db)
api = Api(app)


# # Routes for Users Resgistration/Login
# class Users(Resource):
#     def get(self):
#         users = User.query.all()
#         users_dict_list = [user.to_dict() for user in users]
#         response = make_response(
#             users_dict_list,
#             200
#         )
#         return response
    
#     def post(self):
#         form_json = request.get_json()
#         new_user = User(
#             email=form_json['email'],
#             password=form_json['password']
#         )
#         db.session.add(new_user)
#         db.session.commit()
#         session['user_id'] = new_user.id

#         response = make_response(
#             new_user.to_dict(),
#             201
#         )
#         return response
    
# api.add_resource(Users, '/users')



# class UsersById(Resource):
#     def get(self, id):
#         user = User.query.filter_by(id=id).first()
#         if not user:
#             return make_response({
#                 "error": "User not found"
#             }, 404)
#         user_dict = user.to_dict()
#         response = make_response(
#             user_dict,
#             200
#         )
#         return response 
    
#     def patch(self, id):
#         user = User.query.filter_by(id=id).first()
#         data = request.get_json()
#         for attr in data:
#             setattr(user, attr, data[attr])
#         db.session.add(user)
#         db.session.commit()

#         response = make_response(
#             user.to_dict(), 
#             202
#         )
#         return response
    
#     def delete(self, id):
#         user = User.query.filter_by(id=id).first()
#         if not user:
#             return make_response({
#                 "error": "User not found"
#             }, 404)

#         db.session.delete(user)
#         db.session.commit()

# api.add_resource(UsersById, '/users/<int:id>')



# class RegistrationResource(Resource):
#     def post(self):
#         data = request.get_json()
#         new_user = User(
#             email=data['email'],
#             password=data['password']
#         )
#         db.session.add(new_user)
#         db.session.commit()

#         response = make_response(
#             new_user.to_dict(),
#             201
#         )
#         return response

# api.add_resource(RegistrationResource, '/register')





# #Routes for Teachers and Students
# class Teachers(Resource):
#     def get(self):
#         teachers = Teacher.query.all()
#         teachers_dict_list = [teacher.to_dict() for teacher in teachers]
#         response = make_response(
#             teachers_dict_list,
#             200
#         )
#         return response
    
# api.add_resource(Teachers, '/teachers')


# class TeachersById(Resource):
#     def get(self, id):
#         teacher = Teacher.query.filter_by(id=id).first()
#         if not teacher:
#             return make_response({
#                 "error": "Teacher not found"
#             }, 404)
#         teacher_dict = teacher.to_dict()
#         response = make_response(
#             teacher_dict,
#             200
#         )
#         return response
    
#     def patch(self, id):
#         teacher = Teacher.query.filter_by(id=id).first()
#         data = request.get_json()
#         for attr in data:
#             setattr(teacher, attr, data[attr])
#         db.session.add(teacher)
#         db.session.commit()

#         response = make_response(
#             teacher.to_dict(),
#             202)
#         return response
    
#     def delete(self, id):
#         teacher = Teacher.query.filter_by(id=id).first()
#         if not teacher:
#             return make_response({
#                 "error": "Teacher not found"
#             }, 404)

#         db.session.delete(teacher)
#         db.session.commit()

    
# api.add_resource(TeachersById, '/teachers/<int:id>')


# class Students(Resource):
#     def get(self):
#         students = Student.query.all()
#         students_dict_list = [student.to_dict() for student in students]
#         response = make_response(
#             students_dict_list,
#             200
#         )
#         return response

#     def post(self):
#         data = request.get_json()
#         try:
#             student = Student(
#                 name = data['name'],
#                 image = data['image'],
#                 grade_level = data['grade_level']
#             )

#             db.session.add(student)
#             db.session.commit()
#         except Exception as e:
#             return make_response({
#                 "errors": [e.__str__()]
#             }, 422)
#         response = make_response(
#             student.to_dict(only=('name', 'image', 'grade_level')),
#             201
#         )
#         return response

    
# api.add_resource(Students, '/students')


# class StudentsById(Resource):
#     def get(self, id):
#         student = Student.query.filter_by(id=id).first()
#         if not student:
#             return make_response({
#                 "error": "Student not found"
#             }, 404)
#         student_dict = student.to_dict()
#         response = make_response(
#             student_dict,
#             200
#         )
#         return response
    
#     def patch(self, id):
#         student = Student.query.filter_by(id=id).first()
#         data = request.get_json()
#         for attr in data:
#             setattr(student, attr, data[attr])
#         db.session.add(student)
#         db.session.commit()

#         response = make_response(
#             student.to_dict(), 
#             202
#         )
#         return response
    
#     def delete(self, id):
#         student = Student.query.filter_by(id=id).first()
#         if not student:
#             return make_response({
#                 "error": "Teacher not found"
#             }, 404)
        
#         db.session.delete(student)
#         db.session.commit()

    
# api.add_resource(StudentsById, '/students/<int:id>')
       



# #Routes for Homeroom, which is the same as a "class" of students but called a different name to avoid naming convention issues
# class Homerooms(Resource):
#     def get(self):
#         homerooms = Homeroom.query.all()
#         homerooms_dict_list = [homeroom.to_dict() for homeroom in homerooms]
#         response = make_response(
#             homerooms_dict_list,
#             200
#         )
#         return response 
    
#     def post(self):
#         data = request.get_json()
#         try:
#             homeroom = Homeroom(
#                 name = data['name'],
#                 grade_level=data['grade_level']
#             )

#             db.session.add(homeroom)
#             db.session.commit()
#         except Exception as e:
#             return make_response({
#                 "errors": [e.__str__()]
#             }, 422)
#         response = make_response(
#             homeroom.to_dict(),
#             201
#         )
#         return response


# api.add_resource(Homerooms, '/homerooms')


# class HomeroomsById(Resource):
#     def get(self, id):
#         homeroom = Homeroom.query.filter_by(id=id).first()
#         if not homeroom:
#             return make_response({
#                 "error": "Homeroom not found"
#             }, 404)
#         homeroom_dict = homeroom.to_dict()
#         response = make_response(
#             homeroom_dict,
#             200
#         )
#         return response
    
#     def patch(self, id):
#         homeroom = Homeroom.query.filter_by(id=id).first()
#         data = request.get_json()
#         for attr in data:
#             setattr(homeroom, attr, data[attr])
#         db.session.add(homeroom)
#         db.session.commit()

#         response = make_response(
#             homeroom.to_dict(), 
#             202
#         )
#         return response
    
#     def delete(self, id):
#         homeroom = Homeroom.query.filter_by(id=id).first()
#         if not homeroom:
#             return make_response({
#                 "error": "Teacher not found"
#             }, 404)
        
#         db.session.delete(homeroom)
#         db.session.commit()

# api.add_resource(HomeroomsById, '/homerooms/<int:id>')




# # Routes for Assignments and Rubrics
# class Assignments(Resource):
#     def get(self):
#         assignments = Assignment.query.all()
#         assignments_dict_list = [assignment.to_dict() for assignment in assignments]
#         response = make_response(
#             assignments_dict_list,
#             200
#         )
#         return response 
    
#     def post(self):
#         data = request.get_json()
#         try:
#             assignment = Assignment(
#                 title = data['title'],
#                 image = data['image'],
#                 unit = data['unit'],
#                 step = data['step'],
#                 task = data['task']
#             )

#             db.session.add(assignment)
#             db.session.commit()
#         except Exception as e:
#             return make_response({
#                 "errors": [e.__str__()]
#             }, 422)
#         response = make_response(
#             assignment.to_dict(),
#             201
#         )
#         return response
    
# api.add_resource(Assignments, '/assignments')


# class AssignmentsById(Resource):
#     def get(self, id):
#         assignment = Assignment.query.filter_by(id=id).first()
#         if not assignment:
#             return make_response({
#                 "error": "Assignment not found"
#             }, 404)
#         assignment_dict = assignment.to_dict()
#         response = make_response(
#             assignment_dict,
#             200
#         )
#         return response
    
#     def patch(self, id):
#         assignment = Assignment.query.filter_by(id=id).first()
#         data = request.get_json()
#         for attr in data:
#             setattr(assignment, attr, data[attr])
#         db.session.add(assignment)
#         db.session.commit()

#         response = make_response(
#             assignment.to_dict(), 
#             202
#         )
#         return response
    
#     def delete(self, id):
#         assignment = Assignment.query.filter_by(id=id).first()
#         if not assignment:
#             return make_response({
#                 "error": "Assignment not found"
#             }, 404)
        
#         db.session.delete(assignment)
#         db.session.commit()

# api.add_resource(AssignmentsById, '/assignments/<int:id>')


# class Rubrics(Resource):
#     def get(self):
#         rubrics = Rubric.query.all()
#         rubrics_dict_list = [rubric.to_dict() for rubric in rubrics]
#         response = make_response(
#             rubrics_dict_list,
#             200
#         )
#         return response 
    
#     def post(self):
#         data = request.get_json()
#         try:
#             rubric = Rubric(
#                 title = data['title'],
#                 task_description = data['task_description'],
#                 grading_scale = data['grading_scale']
#             )

#             db.session.add(rubric)
#             db.session.commit()
#         except Exception as e:
#             return make_response({
#                 "errors": [e.__str__()]
#             }, 422)
#         response = make_response(
#             rubric.to_dict(),
#             201
#         )
#         return response

# api.add_resource(Rubrics, '/rubrics')


# class RubricsById(Resource):
#     def get(self, id):
#         rubric = Rubric.query.filter_by(id=id).first()
#         if not rubric:
#             return make_response({
#                 "error": "Rubric not found"
#             }, 404)
#         rubric_dict = rubric.to_dict()
#         response = make_response(
#             rubric_dict,
#             200
#         )
#         return response
    
#     def patch(self, id):
#         rubric = Rubric.query.filter_by(id=id).first()
#         data = request.get_json()
#         for attr in data:
#             setattr(rubric, attr, data[attr])
#         db.session.add(rubric)
#         db.session.commit()

#         response = make_response(
#             rubric.to_dict(), 
#             202
#         )
#         return response
    
#     def delete(self, id):
#         rubric = Rubric.query.filter_by(id=id).first()
#         if not rubric:
#             return make_response({
#                 "error": "Rubric not found"
#             }, 404)
        
#         db.session.delete(rubric)
#         db.session.commit()

# api.add_resource(RubricsById, '/rubrics/<int:id>')




# # Routes for Curriculum
# class Curriculums(Resource):
#     def get(self):
#         curriculums = Curriculum.query.all()
#         curriculums_dict_list = [curriculum.to_dict() for curriculum in curriculums]
#         response = make_response(
#             curriculums_dict_list,
#             200
#         )
#         return response
    
#     def post(self):
#         data = request.get_json()
#         try:
#             curriculum = Curriculum(
#                 unit = data['unit'],
#                 step = data['step'],
#                 task = data['task']
#             )

#             db.session.add(curriculum)
#             db.session.commit()
#         except Exception as e:
#             return make_response({
#                 "errors": [e.__str__()]
#             }, 422)
#         response = make_response(
#             curriculum.to_dict(),
#             201
#         )
#         return response

# api.add_resource(Curriculums, '/curriculums')

# class CurriculumsById(Resource):
#     def get(self, id):
#         curriculum = Curriculum.query.filter_by(id=id).first()
#         if not curriculum:
#             return make_response({
#                 "error": "Curriculum not found"
#             }, 404)
#         curriculum_dict = curriculum.to_dict()
#         response = make_response(
#             curriculum_dict,
#             200
#         )
#         return response
    
#     def patch(self, id):
#         curriculum = Curriculum.query.filter_by(id=id).first()
#         data = request.get_json()
#         for attr in data:
#             setattr(curriculum, attr, data[attr])
#         db.session.add(curriculum)
#         db.session.commit()

#         response = make_response(
#             curriculum.to_dict(), 
#             202
#         )
#         return response
    
#     def delete(self, id):
#         curriculum = Curriculum.query.filter_by(id=id).first()
#         if not curriculum:
#             return make_response({
#                 "error": "Curriculum not found"
#             }, 404)
        
#         db.session.delete(curriculum)
#         db.session.commit()

# api.add_resource(CurriculumsById, '/curriculums/<int:id>')


#Routes for Courses
class Courses(Resource):
    def get(self):
        courses = Course.query.all()
        courses_dict_list = [course.to_dict() for course in courses]
        response = make_response(
            courses_dict_list,
            200
        )
        return response
    
    def post(self):
        data = request.get_json()
        try:
            course = Course(
                cover = data['cover'],
                coursesName = data['coursesName'],
                priceAll = data['priceAll'],
                pricePer = data['pricePer']
            )

            db.session.add(course)
            db.session.commit()
        except Exception as e:
            return make_response({
                "errors": [e.__str__()]
            }, 422)
        response = make_response(
            course.to_dict(),
            201
        )
        return response
    
api.add_resource(Courses, '/courses')



class CoursesById(Resource):
    def get(self, id):
        course = Course.query.filter_by(id=id).first()
        if not course:
            return make_response({
                "error": "Course not found"
            }, 404)
        course_dict = course.to_dict()
        response = make_response(
            course_dict,
            200
        )
        return response 
    
    def patch(self, id):
        course = Course.query.filter_by(id=id).first()
        data = request.get_json()
        for attr in data:
            setattr(course, attr, data[attr])
        db.session.add(course)
        db.session.commit()

        response = make_response(
            course.to_dict(), 
            202
        )
        return response
    
    def delete(self, id):
        course = Course.query.filter_by(id=id).first()
        if not course:
            return make_response({
                "error": "Course not found"
            }, 404)
        
        db.session.delete(course)
        db.session.commit()

api.add_resource(CoursesById, '/courses/<int:id>')



#Routes for Teachers
class CourTeachers(Resource):
    def get(self):
        courTeachers = CourTeacher.query.all()
        courTeachers_dict_list = [courTeacher.to_dict() for courTeacher in courTeachers]
        response = make_response(
            courTeachers_dict_list,
            200
        )
        return response
    
    def post(self):
        data = request.get_json()
        try:
            courTeacher = CourTeacher(
                dcover = data['dcover'],
                name = data['name'],
                totalTime = data['totalTime']
            )

            db.session.add(courTeacher)
            db.session.commit()
        except Exception as e:
            return make_response({
                "errors": [e.__str__()]
            }, 422)
        response = make_response(
            courTeacher.to_dict(),
            201
        )
        return response
    
api.add_resource(CourTeachers, '/courteachers')



class CourTeachersById(Resource):
    def get(self, id):
        courTeacher = CourTeacher.query.filter_by(id=id).first()
        if not courTeacher:
            return make_response({
                "error": "Course not found"
            }, 404)
        courTeacher_dict = courTeacher.to_dict()
        response = make_response(
            courTeacher_dict,
            200
        )
        return response 
    
    def patch(self, id):
        courTeacher = CourTeacher.query.filter_by(id=id).first()
        data = request.get_json()
        for attr in data:
            setattr(courTeacher, attr, data[attr])
        db.session.add(courTeacher)
        db.session.commit()

        response = make_response(
            courTeacher.to_dict(), 
            202
        )
        return response

    def delete(self, id):
        courTeacher = CourTeacher.query.filter_by(id=id).first()
        if not courTeacher:
            return make_response({
                "error": "Course not found"
            }, 404)
        
        db.session.delete(courTeacher)
        db.session.commit()

api.add_resource(CourTeachersById, '/courteachers/<int:id>')


#Routes for joiner table of courses and teachers
class SignUps(Resource):
    def get(self):
        signups = SignUp.query.all()
        signups_dict_list = [signup.to_dict() for signup in signups]
        response = make_response(
            signups_dict_list,
            200
        )
        return response
    
    def post(self):
        data = request.get_json()
        try:
            signup = SignUp(
                course_id = data['course_id'],
                courTeacher_id = data['courTeacher_id']
            )

            db.session.add(signup)
            db.session.commit()
        except Exception as e:
            return make_response({
                "errors": [e.__str__()]
            }, 422)
        response = make_response(
            signup.to_dict(),
            201
        )
        return response
    
api.add_resource(SignUps, '/signups')



#Routes for Blogs
class Blogs(Resource):
    def get(self):
        blogs = Blog.query.all()
        blogs_dict_list = [blog.to_dict() for blog in blogs]
        response = make_response(
            blogs_dict_list,
            200
        )
        return response
    
    def post(self):
        data = request.get_json()
        try:
            blog = Blog(
                author = data['author'],
                date = data['date'],
                com = data['com'],
                title = data['title'],
                desc = data['desc'],
                cover = data['cover']
            )

            db.session.add(blog)
            db.session.commit()
        except Exception as e:
            return make_response({
                "errors": [e.__str__()]
            }, 422)
        response = make_response(
            blog.to_dict(),
            201
        )
        return response
    
api.add_resource(Blogs, '/blogs')



if __name__ == '__main__':
    app.run(port=5555, debug=True)
