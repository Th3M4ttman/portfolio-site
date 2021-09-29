
from ..projects import Project, Implementation
import json
from ..extensions import db
import os

PROJECT_FILE = os.path.abspath("/storage/emulated/0/Dev/Portfolio/Test/NewTest/Projects/Projects.json")

def populate(app):
	with app.app_context():
		projects = db.session.query(Project).all()
		implementations = db.session.query(Implementation).all()
	i = 0
	ii = 0
	with open(PROJECT_FILE, "r") as proj_file:
		string = ""
		for line in proj_file:
			string += line + "\n"
	found_projects = json.loads(string)["Projects"]
	
	for _project, path in found_projects.items():
		string = ""
		with open(path + "/" + _project + ".proj", "r") as in_file:
			for line in in_file:
				string += line + "\n"
		project_dict = json.loads(string)
				
		title = project_dict["title"]
		desc = project_dict["description"]
		cat = project_dict["category"]
		sub = project_dict["subcategory"]
		
		add_project(i, title, cat, sub, desc)
		for imp in project_dict["implementations"].keys():
			imp = project_dict["implementations"][imp]
			language = imp["languages"]
			major = imp["major"]
			minor = imp["minor"]
			rev = imp["rev"]
			add_imp(i, ii, language, major, minor, rev)
			ii += 1
		i += 1
	return
	for k, project in found_projects.items():
		string = ""
		with open(project + "/" + k + ".proj", "r") as in_file:
			for line in in_file:
				string += line + "\n"
		project_dict = json.loads(string)
		
		title = project_dict["title"]
		desc = project_dict["description"]
		cat = project_dict["category"]
		sub = project_dict["subcategory"]
		
		add_project(i, title, cat, sub, desc)
		for imp in project_dict["implementations"].keys():
			imp = project_dict["implementations"][imp]
			language = imp["languages"]
			major = imp["major"]
			minor = imp["minor"]
			rev = imp["rev"]
			add_imp(i, ii, language, major, minor, rev)
			ii += 1
		i += 1
	
def add_project(id, title, cat, sub, desc):
	#print("Project("+str(id), title, cat, sub, desc+")", sep=", ")
	proj = Project(id, title, cat, sub, desc)
	db.session.add(proj)
	
def add_imp(project_id, imp_id, language, major=0, minor=0, rev=0):
	#print("Implementation("+str(project_id), imp_id, language, major, minor, str(rev)+")", sep=", ")
	imp = Implementation(project_id, imp_id, language, major, minor, rev)
	db.session.add(imp)
	
def del_proj(id):
	projects = db.session.query(Project).all()
	if len(projects) > 0:
		db.session.delete(projects[id])
		
def del_imp(id):
	implementations = db.session.query(Implementation).all()
	if len(implementations) > 0:
		db.session.delete(implementations[id])
		
def get_project(id):
	return db.session.query(Project).all()[id]
	
def get_project_id(title):
	for project in db.session.query(Project).all():
		if project.title.lower() == title.lower():
			return project.id
	return None