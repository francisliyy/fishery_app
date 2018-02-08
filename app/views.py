from flask import render_template
from flask.ext.appbuilder.models.sqla.interface import SQLAInterface
from flask.ext.appbuilder import ModelView
from app import appbuilder, db
from flask_appbuilder import BaseView, expose, has_access
from app.models import UploadFile



class ProcessView(BaseView):


    @expose('/showProcess/')
    @has_access
    def showProcess(self):

        return self.render_template('/process.html')


class UploadFileView(ModelView):

    datamodel = SQLAInterface(UploadFile)

    label_columns = {'name':'Upload File Name'}

    add_columns = ['name','upload_user']

    list_columns = ['id','name','upload_user','upload_date']


"""
    Create your Views::


    class MyModelView(ModelView):
        datamodel = SQLAInterface(MyModel)


    Next, register your Views::


    appbuilder.add_view(MyModelView, "My View", icon="fa-folder-open-o", category="My Category", category_icon='fa-envelope')
"""


"""
    Application wide 404 error handler
"""
@appbuilder.app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html', base_template=appbuilder.base_template, appbuilder=appbuilder), 404

db.create_all()

appbuilder.add_view(UploadFileView,"File Management", icon='fa-folder-open-o', category='Management',category_icon="fa-envelope")
appbuilder.add_view(ProcessView,"prcess", href='/processview/showProcess', category='Process View')


