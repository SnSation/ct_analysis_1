from app import db
from flask_wtf import FlaskForm
from wtforms import StringField, FloatField, IntegerField, SubmitField

# Database Tables

class Student(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(50))
    last_name = db.Column(db.String(50))
    intelligence = db.Column(db.Integer) # Base understanding gained per time spent
    commitment = db.Column(db.Integer) # Time spent gaining understanding outside of class
    background = db.Column(db.Integer) # Understanding start value
    understanding = db.Column(db.Float) # Measure of course learned
    cohort_id = db.Column(db.Integer, db.ForeignKey('cohort.id')) # Foreign Key to Cohort.id

    def __repr__(self):
        return f'< Student | Name: {self.first_name} {self.last_name} | ID: {self.id} >'

    def set_attributes(self, data):
        for attribute in ['first_name', 'last_name', 'intelligence', 'commitment', 'background', 'understanding', 'cohort']:
            if attribute in data:
                setattr(self, attribute, data[attribute])

    def attributes_as_dictionary(self):
        dictionary = {
            'id':self.id,
            'first_name':self.first_name,
            'last_name':self.last_name,
            'intelligence':self.intelligence,
            'commitment':self.commitment,
            'background':self.background,
            'understanding':self.understanding,
            'cohort_id':self.cohort
        }
        return dictionary

    def save_item(self):
        db.session.add(self)
        db.session.commit()
    
    def remove_item(self):
        db.session.delete(self)
        db.session.commit()

    def update_item(self):
        db.session.commit()

class Instructor(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(50))
    last_name = db.Column(db.String(50))
    quality = db.Column(db.Integer) # Base understanding given per time spent
    commitment = db.Column(db.Integer) # Time spent giving understanding outside of class (equvalent to boost from a TA)

    def __repr__(self):
        return f'< Instructor | Name: {self.first_name} {self.last_name} | ID: {self.id} >'

    def set_attributes(self, data):
        for attribute in ['first_name', 'last_name', 'quality', 'commitment']:
            if attribute in data:
                setattr(self, attribute, data[attribute])

    def attributes_as_dictionary(self):
        dictionary = {
            'id':self.id,
            'first_name':self.first_name,
            'last_name':self.last_name,
            'quality':self.quality,
            'commitment':self.commitment
        }
        return dictionary

    def save_item(self):
        db.session.add(self)
        db.session.commit()
    
    def remove_item(self):
        db.session.delete(self)
        db.session.commit()

    def update_item(self):
        db.session.commit()

class Cohort(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50))
    curriculum = db.Column(db.Integer, db.ForeignKey('curriculum.id')) # Foreign Key to Curriculum.id
    instructor = db.Column(db.Integer, db.ForeignKey('instructor.id')) # Foreign Key to Instructor.id
    students = db.relationship("Student", backref="cohort") # One to Many: Students.id

    def __repr__(self):
        return f'< Cohort | Name: {self.curriculum} | ID: {self.id} >'

    def set_attributes(self, data):
        for attribute in ['curriculum', 'instructor', 'name']:
            if attribute in data:
                setattr(self, attribute, data[attribute])

    def attributes_as_dictionary(self):
        dictionary = {
            'id':self.id,
            'name':self.name,
            'curriculum':self.curriculum,
            'instructor':self.instructor,
            'students':self.students
        }
        return dictionary

    def save_item(self):
        db.session.add(self)
        db.session.commit()
    
    def remove_item(self):
        db.session.delete(self)
        db.session.commit()

    def update_item(self):
        db.session.commit()

classes = db.Table('classes', 
    db.Column('topic_id', db.Integer, db.ForeignKey('topic.id')), #Foreign Key Topic.id
    db.Column('curriculum_id', db.Integer, db.ForeignKey('curriculum.id')) #Foreign Key Curriculum.id
)

class Curriculum(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50))
    time_to_complete = db.Column(db.Integer) # Time to complete
    topics = db.relationship('Topic', secondary=classes, backref=db.backref('curriculums', lazy='dynamic'))

    def __repr__(self):
        return f'< Curriculum | Name: {self.name} | ID: {self.id} >'

    def set_attributes(self, data):
        for attribute in ['name', 'time_to_complete', 'topics']:
            if attribute in data:
                setattr(self, attribute, data[attribute])

    def attributes_as_dictionary(self):
        dictionary = {
            'id':self.id,
            'name':self.name,
            'topics':self.topics
        }
        return dictionary

    def save_item(self):
        db.session.add(self)
        db.session.commit()
    
    def remove_item(self):
        db.session.delete(self)
        db.session.commit()

    def update_item(self):
        db.session.commit()

class Topic(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50))
    difficulty = db.Column(db.Float) # Modifies understanding gain per time spent
    prerequisite = db.Column(db.Integer) # Understanding required before additional understanding is gained from this topic
    time_to_cover = db.Column(db.Integer) # Time spent covering this topic in class

    def __repr__(self):
        return f'< Topic | Name: {self.name} | ID: {self.id} >'

    def set_attributes(self, data):
        for attribute in ['name', 'difficulty', 'prerequisite', 'time_to_cover']:
            if attribute in data:
                setattr(self, attribute, data[attribute])

    def attributes_as_dictionary(self):
        dictionary = {
            'id':self.id,
            'name':self.name,
            'difficulty':self.difficulty,
            'prerequisite':self.prerequisite,
            'time_to_cover':self.time_to_cover
        }
        return dictionary

    def save_item(self):
        db.session.add(self)
        db.session.commit()
    
    def remove_item(self):
        db.session.delete(self)
        db.session.commit()

    def update_item(self):
        db.session.commit()

class Event(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50))
    time_to_pass = db.Column(db.Integer) # Time used interrupting understanding gain
    likelihood = db.Column(db.Float) # Likelihood of event occurance per time spent in class

    def __repr__(self):
        return f'< Event | Name: {self.name} | ID: {self.id} >'

    def set_attributes(self, data):
        for attribute in ['name', 'time_to_pass', 'likelihood']:
            if attribute in data:
                setattr(self, attribute, data[attribute])

    def attributes_as_dictionary(self):
        dictionary = {
            'id':self.id,
            'name':self.name,
            'time_to_pass':self.time_to_pass,
            'likelihood':self.likelihood
        }
        return dictionary

    def save_item(self):
        db.session.add(self)
        db.session.commit()
    
    def remove_item(self):
        db.session.delete(self)
        db.session.commit()

    def update_item(self):
        db.session.commit()

# Calculations:
# - Understanding Gain: Base Understanding * Student.Intelligence * Instructor Modifier * Topic Modifier * Event Modifier * Work Modifier
# - Instructor Modifier: 1 + Instructor.Quality * (Is instructor present? 0/1)
# - Topic Modifier: Topic.Difficulty * (Student.Understanding / Topic.Prerequisite)
# - Event Modifier: Is Happening? 0/1
# - Work Modifier: Is Working? 0/1 => always 1 during class, else: 24h / Student.Commitment

# Flask Forms

class CreateStudent(FlaskForm):
    number = IntegerField("Number of Students")
    cohort = IntegerField("Cohort ID")
    student_submit = SubmitField("Create Students")

class CreateInstructor(FlaskForm):
    first_name = StringField("First Name")
    last_name = StringField("Last Name")
    quality = IntegerField("Instructor Quality")
    commitment = IntegerField("Instructor Commitment")
    instructor_submit = SubmitField("Create Instructor")

class CreateCohort(FlaskForm):
    # students = StringField("Students") # Student.id separated by commas
    curriculum = IntegerField("Curriculum ID")
    instructor = IntegerField("Instructor ID")
    cohort_submit = SubmitField("Create Cohort")

class CreateCurriculum(FlaskForm):
    name = StringField("Curriculum Name")
    time_to_complete = IntegerField("Time to Complete")
    topics = StringField("Topics") # Topics.id separated by comma
    curriculum_submit = SubmitField("Create Curriculum")

class CreateTopic(FlaskForm):
    name = StringField("Topic Name")
    difficulty = IntegerField("Topic Difficulty")
    prerequisite = IntegerField("Understanding Required")
    time_to_cover = IntegerField("Time to Cover")
    topic_submit = SubmitField("Create Topic")

class CreateEvent(FlaskForm):
    name = StringField("Event Name")
    time_to_pass = IntegerField("Time to Pass")
    likelihood = FloatField("Likelihood")
    event_submit = SubmitField("Create Event")