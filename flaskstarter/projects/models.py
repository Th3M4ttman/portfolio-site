from sqlalchemy import Column, Integer, String, Boolean, Numeric, orm, ForeignKey, MetaData, Table
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from ..extensions import db
from flask_admin.contrib import sqla
from sqlalchemy import inspect
import json
from flask_login import current_user

from json import JSONEncoder

def _default(self, obj):
    return getattr(obj.__class__, "to_json", _default.default)(obj)

_default.default = JSONEncoder().default
JSONEncoder.default = _default

class Project(db.Model):
	__tablename__ = 'projects'
	
	id=Column(Integer, primary_key=True)
	title=Column('title', String(32))
	cat=Column('category', String(32))
	sub=Column('subcategory', String(32))
	desc=Column('description', String(32))
	imps = orm.relationship("Implementation", uselist=True, cascade="delete, delete-orphan")
	
	def __init__(self, id, title, cat, sub, desc, imps):
		self.id = id
		self.title = title
		self.cat = cat
		self.sub = sub
		self.desc = desc
		self.imps = imps
	
	def to_json(self):
		return {"id": self.id, "title": self.title, "cat": self.cat, "sub": self.sub, "desc": self.desc}
		

class Implementation(db.Model):
	__tablename__ = 'implementations'
	
	imp_id=Column(Integer, primary_key=True)
	language=Column('language', String(32))
	major=Column('major', Integer)
	minor=Column("minor", Integer)
	rev=Column("rev", Integer)
	project_id = Column(Integer, ForeignKey("projects.id"))
	
	def __init__(self, project_id, imp_id, language, major=0, minor=0, rev=0):
		
		self.project_id = project_id
		self.imp_id = imp_id
		self.language = language
		self.major = major
		self.minor = minor
		self.rev = rev
		self.project_id = imp_id
	
	def to_json(self):
		return json.dumps(self.__dict__)

# Customized comment model admin
class ProjectAdmin(sqla.ModelView):
    can_delete = True
    column_hide_backrefs = False
    column_display_pk = True
    column_list = [c_attr.key for c_attr in inspect(Project).mapper.column_attrs]
    column_sortable_list = ('id', 'title', 'cat', "sub", "desc")
    column_filters = ('id', 'title', 'cat', "sub", "desc")
    column_searchable_list = ('id', 'title', 'cat', "sub", "desc")

    def __init__(self, session):
        super(ProjectAdmin, self).__init__(Project, session)

    def is_accessible(self):
        if current_user.role == 'admin':
            return current_user.is_authenticated()
            
# Customized comment model admin
class ImpAdmin(sqla.ModelView):
    can_delete = True
    column_hide_backrefs = False
    column_display_pk = True
    column_list = [c_attr.key for c_attr in inspect(Implementation).mapper.column_attrs]
    column_sortable_list = ("project_id", "imp_id", "language", "major", "minor", "rev")
    column_filters = ("project_id", "imp_id", "language", "major", "minor", "rev")
    column_searchable_list = ("project_id", "imp_id", "language", "major", "minor", "rev")

    def __init__(self, session):
        super(ImpAdmin, self).__init__(Implementation, session)

    def is_accessible(self):
        if current_user.role == 'admin':
            return current_user.is_authenticated()	