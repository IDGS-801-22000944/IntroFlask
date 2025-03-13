from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, RadioField
from wtforms.validators import DataRequired, Length, NumberRange

class ZodiacoForm(FlaskForm):
    nombre = StringField("Nombre", validators=[DataRequired(message="El campo es requerido")])
    apellidoPa = StringField("Apellido Paterno", validators=[DataRequired()])
    apellidoMa = StringField("Apellido Materno", validators=[DataRequired()])
    
    dia = IntegerField("Día", validators=[DataRequired(), NumberRange(min=1, max=31)])
    mes = IntegerField("Mes", validators=[DataRequired(), NumberRange(min=1, max=12)])
    anio = IntegerField("Año", validators=[DataRequired()])
    
    sexo = RadioField("Sexo", choices=[("masculino", "Masculino"), ("femenino", "Femenino")], default="masculino")
