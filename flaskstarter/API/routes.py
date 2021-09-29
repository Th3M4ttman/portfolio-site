from flask import Blueprint
from ..extensions import db
from ..projects import Project
from ..extensions import db
from flask import jsonify
import json
from flask_cors import cross_origin, CORS
import random as r



bp = Blueprint('API', __name__)
CORS(bp)

@bp.route('/get_project/<id>', methods=['GET','POST','OPTIONS'])
#@cross_origin(origin='*')
#@login_required
def get_project(id):
    try:
    	id = int(id)
    	title = False
    except:
    	title = True
    	
    projects = db.session.query(Project).all()
    
    if not title:
    	if id > len(projects):
    		return json.dumps({"Success": False}, indent=4)
    	content = projects[id]
    else:
    	for project in projects:
    		if project.title.lower().replace(" ", "")== id.lower().replace(" ", ""):
    			response = jsonify(project)
    			response.headers.add('Access-Control-Allow-Origin', '*')
    			return response
    	response = jsonify({"success": False})
    	response.headers.add('Access-Control-Allow-Origin', '*')
    	return response
    response = jsonify(content)
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response
    
@bp.route('/get_projects/', methods=['GET','POST','OPTIONS'])
@cross_origin()
def get_projects():
    projects = db.session.query(Project).all()
    response = jsonify(projects)
    #response.headers.set('Access-Control-Allow-Origin', 'localhost')
    return response
    
@bp.route('/random/<int:low>/<int:high>', methods=['GET','POST','OPTIONS'])
#@cross_origin(origin='*')
def random(low = 0, high = 0):
    
    response = jsonify({"Number": r.randint(low, high)})
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response