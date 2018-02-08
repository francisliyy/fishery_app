from flask.ext.appbuilder import Model
from flask.ext.appbuilder.models.mixins import AuditMixin, FileColumn, ImageColumn
from sqlalchemy import Column, Integer, String, ForeignKey, DateTime, Date, TIMESTAMP
from sqlalchemy.orm import relationship
from datetime import datetime
from flask import Markup, url_for
from flask_appbuilder import Model
from flask_appbuilder.filemanager import get_file_original_name
from flask_appbuilder.models.mixins import AuditMixin, FileColumn


"""

You can use the extra Flask-AppBuilder fields and Mixin's

AuditMixin will add automatic timestamp of created and modified by who


"""

class StockSynFile(AuditMixin,Model):
	__tablename__ = "stock_syn_file"
	id = Column(Integer,primary_key=True)
	file = Column(FileColumn, nullable=False)
	description = Column(String(150))

	def download(self):
		return Markup(
			'<a href="' + url_for('StockSynFileView.download', filename=str(self.file)) + '">Download</a>')

	def file_name(self):
		return get_file_original_name(str(self.file))