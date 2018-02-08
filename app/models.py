from flask.ext.appbuilder import Model
from flask.ext.appbuilder.models.mixins import AuditMixin, FileColumn, ImageColumn
from sqlalchemy import Column, Integer, String, ForeignKey, DateTime, Date, TIMESTAMP
from sqlalchemy.orm import relationship
from datetime import datetime
"""

You can use the extra Flask-AppBuilder fields and Mixin's

AuditMixin will add automatic timestamp of created and modified by who


"""

class UploadFile(Model):
	id = Column(Integer,primary_key=True)
	name =  Column(String(50),nullable=False)
	upload_user = Column(String(50))
	upload_date = Column(TIMESTAMP(),nullable=False,default=datetime.utcnow)

	def __repr__(self):
		return self.name

        
