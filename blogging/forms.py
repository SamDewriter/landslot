from wtforms import Form, StringField, TextAreaField, validators, SubmitField

class PostForm(Form):
    title = StringField('Title', [validators.DataRequired()])
    content = TextAreaField('Content', [validators.DataRequired()])
    image_url = StringField('Image URL', [validators.DataRequired()])
    submit = SubmitField('Submit')