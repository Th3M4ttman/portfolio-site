# -*- coding: utf-8 -*-

from sqlalchemy.orm.mapper import configure_mappers

from flaskstarter import create_app
from flaskstarter.extensions import db
from flaskstarter.user import Users, ADMIN, USER, ACTIVE, Comment
from flaskstarter.projects.models import Project, Implementation
from flaskstarter.projects import update

application = create_app()


@application.cli.command("initdb")
def initdb():
    """Init/reset database."""
    
    db.drop_all()
    configure_mappers()
    db.create_all()

    admin = Users(name='Admin Flask-Starter',
                  email=u'workmatthewjharris94@gmail.com',
                  password=u'adminpwd',
                  role_code=ADMIN,
                  status_code=ACTIVE)

    db.session.add(admin)

    for i in range(1, 2):
        user = Users(name='Demo User',
                     email=u'demo@your-mail.com',
                     password=u'demopassword',
                     role_code=USER,
                     status_code=ACTIVE)
        db.session.add(user)

    
    x = Comment(0, 0, 0, 0, "Nice")
    db.session.add(x)
    db.session.commit()
    print("Database initialized with 2 users (admin, demo)")
    update.populate(application)
    db.session.commit()
    print("Initialised Project DB")
    
    
    
