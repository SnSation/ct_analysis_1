from . import bp as api
from flask import jsonify, request, url_for, render_template, redirect
import requests, re, random
from .models import CreateStudent, CreateInstructor, CreateCohort, CreateCurriculum, CreateTopic, Student, Instructor, Cohort, Curriculum, Topic, Event, CreateEvent

@api.route('/', methods=['GET'])
def main():
    return render_template('api/main.html')

@api.route('/populate', methods=['GET', 'POST'])
def populate():
    create_student = CreateStudent()
    # if create_student.validate_on_submit():
    #     loops = create_student.number.data
    #     while loops > 0:
    #         new_student = Student()
    #         byte_names = requests.get('https://random-word-api.herokuapp.com/word?number=2')
    #         decoded_names = byte_names.content.decode('utf-8')
    #         fake_names = re.findall(r'"(\w+)"', decoded_names)
    #         background = random.randint(0, 1000)
    #         student_data = {
    #             'first_name':fake_names[0],
    #             'last_name':fake_names[1],
    #             'intelligence': random.randint(0, 10),
    #             'commitment':random.randint(0, 10),
    #             'background':background,
    #             'understanding':background,
    #             'cohort':create_student.cohort.data
    #         }
    #         loops -= 1
    #         new_student.set_attributes(student_data)
    #         new_student.save_item()
    #         print(new_student)
    create_instructor = CreateInstructor()
    # if create_instructor.validate_on_submit:
    #     new_instructor = Instructor()
    #     instructor_data = {
    #         'first_name':create_instructor.first_name.data,
    #         'last_name':create_instructor.last_name.data,
    #         'quality':create_instructor.quality.data,
    #         'commitment':create_instructor.commitment.data,
    #     }
    #     new_instructor.set_attributes(instructor_data)
    #     new_instructor.save_item()
    create_cohort = CreateCohort()
    # if create_cohort.validate_on_submit:
    #     new_cohort = Cohort()
    #     cohort_data = {
    #         'curriculum':create_cohort.curriculum.data,
    #         'instructor':create_cohort.instructor.data
    #     }
    #     new_cohort.set_attributes(cohort_data)
    #     new_cohort.save_item()

    create_curriculum = CreateCurriculum()
    # if create_curriculum.validate_on_submit:
    #     new_curriculum = Curriculum()
    #     curriculum_data = {
    #         'name':create_curriculum.name.data,
    #         'time_to_complete':create_curriculum.time_to_complete.data
    #     }
    #     new_curriculum.set_attributes(curriculum_data)
    #     new_curriculum.save_item()
    create_topic = CreateTopic()
    if create_topic.validate_on_submit:
        new_topic = Topic()
        topic_data = {
            'name':create_topic.name.data,
            'difficulty':create_topic.difficulty.data,
            'prerequisite':create_topic.prerequisite.data,
            'time_to_cover':create_topic.time_to_cover.data,
        }
        new_topic.set_attributes(topic_data)
        new_topic.save_item()
    create_event = CreateEvent()
    context = {
        'student_form': create_student,
        'instructor_form':create_instructor,
        'cohort_form':create_cohort,
        'curriculum_form':create_curriculum,
        'topic_form':create_topic,
        'event_form':create_event
    }
    return render_template('api/populate.html', **context)