from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms import TextAreaField, DecimalField
from wtforms.validators import ValidationError, DataRequired, Email, EqualTo
import wtforms.validators as validators

from app.models import Asset

class AssetForm(FlaskForm):

    name = StringField('Name', validators=[DataRequired(), validators.required(), validators.length(max=100)])
    owner = StringField('Owner', validators=[validators.required(), validators.length(max=100)])
    properties = StringField('Properties (comma or space separated)', validators=[validators.required(), validators.length(max=1200)])
    services = StringField('Services (comma or space separated)', validators=[validators.required(), validators.length(max=1200)])
    events = StringField('Events (comma or space separated)', validators=[validators.required(), validators.length(max=1200)])
    submit = SubmitField('Add device')

#description = TextAreaField('Description', validators=[validators.required(), validators.length(max=1000)], render_kw={'rows': "8", 'cols': "30"})
#latitude = DecimalField('Latitude', places=4, validators=[], render_kw={'readonly':'readonly'},)

# document.getElementById("myText").disabled = true;
# document.getElementById('foo').readOnly = true;
# <input type="text" disabled="disabled" />
# <input type="text" readonly="readonly" />
# https://wiki.selfhtml.org/wiki/HTML/Formulare/ausgrauen_mit_readonly,_disabled#readonly_vs._disabled
# disabled is not submitted

