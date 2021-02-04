from flask_wtf import FlaskForm
from wtforms import StringField, DateField, SelectField, SubmitField, TextAreaField
from wtforms.ext.sqlalchemy.fields import QuerySelectField, QuerySelectMultipleField
from wtforms.validators import DataRequired, Length
from books_app.models import Audience, Book, Author, Genre


class BookForm(FlaskForm):
    """Form to create a book."""

    title = StringField(
        "Book Title", validators=[DataRequired(), Length(min=3, max=80)]
    )
    publish_date = DateField("Date Published")
    author = QuerySelectField(
        "Author", query_factory=lambda: Author.query, allow_blank=False
    )
    audience = SelectField("Audience", choices=Audience.choices())
    genres = QuerySelectMultipleField("Genres", query_factory=lambda: Genre.query)
    submit = SubmitField("Submit")


class AuthorForm(FlaskForm):
    """Form to create an author."""

    # STRETCH CHALLENGE: Add more fields here as well as in `models.py` to
    # collect more information about the author, such as their birth date,
    # country, etc.
    name = StringField("Name", validators=[DataRequired(), Length(min=3, max=30)])
    biography = TextAreaField("Biography")
    submit = SubmitField("Submit")


class GenreForm(FlaskForm):
    """Form to create a genre."""

    name = StringField("Name", validators=[DataRequired(), Length(min=3, max=30)])
    submit = SubmitField("Submit")
