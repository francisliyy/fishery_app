from flask import render_template
from flask_appbuilder.models.sqla.interface import SQLAInterface
from flask_appbuilder.views import ModelView, CompactCRUDMixin
from app import appbuilder, db
from flask_appbuilder import BaseView, expose, has_access
from app.models import *
from app.rutils import *
from os.path import basename

class ProcessView(BaseView):


    @expose('/showProcess/')
    @has_access
    def showProcess(self):

"""
        rUtil = RUtil();
        rUtil.runScript("/Users/yli120/rfish/rplots.r");
"""

        return self.render_template('/process.html')


class StockSynFileView(ModelView):

    datamodel = SQLAInterface(StockSynFile)

    label_columns = {'file_name': 'File Name','description':'Description','download': 'Download'}
    add_columns = ['file', 'description']
    edit_columns = ['file', 'description']
    list_columns = ['file_name', 'description', 'created_by', 'created_on', 'changed_by', 'changed_on', 'download']
    show_fieldsets = [
        ('Info', {'fields': ['file_name', 'description', 'download']}),
        ('Audit', {'fields': ['created_by', 'created_on', 'changed_by', 'changed_on'], 'expanded': False})
    ]

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

appbuilder.add_view(StockSynFileView,"Stock Synthesis File", icon='fa-folder-open-o', category='Management',category_icon="fa-envelope")
appbuilder.add_view(ProcessView,"prcess", href='/processview/showProcess', category='Process View')
