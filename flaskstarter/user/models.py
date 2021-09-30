# -*- coding: utf-8 -*-

from sqlalchemy import Column, types
from sqlalchemy.ext.mutable import Mutable
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin

from ..extensions import db
from ..utils import get_current_time, STRING_LEN
from .constants import USER, USER_ROLE, ADMIN, INACTIVE, USER_STATUS

from flask_login import current_user
from flask_admin.contrib import sqla
from sqlalchemy import inspect
from ..projects.models import Project, Implementation


class DenormalizedText(Mutable, types.TypeDecorator):
    """
    Stores denormalized primary keys that can be
    accessed as a set.

    :param coerce: coercion function that ensures correct
                   type is returned

    :param separator: separator character
    """

    impl = types.Text

    def __init__(self, coerce=int, separator=" ", **kwargs):

        self.coerce = coerce
        self.separator = separator

        super(DenormalizedText, self).__init__(**kwargs)

    def process_bind_param(self, value, dialect):
        if value is not None:
            items = [str(item).strip() for item in value]
            value = self.separator.join(item for item in items if item)
        return value

    def process_result_value(self, value, dialect):
        if not value:
            return set()
        return set(self.coerce(item) for item in value.split(self.separator))

    def copy_value(self, value):
        return set(value)


class Users(db.Model, UserMixin):

    __tablename__ = 'users'

    id = Column(db.Integer, primary_key=True)

    name = Column(db.String(STRING_LEN))

    email = Column(db.String(STRING_LEN), unique=True)
    email_activation_key = Column(db.String(STRING_LEN))

    created_time = Column(db.DateTime, default=get_current_time)

    _password = Column('password', db.String(100), nullable=False)

    def _get_password(self):
        return self._password

    def _set_password(self, password):
        self._password = generate_password_hash(password)

    # Hide password encryption by exposing password field only.
    password = db.synonym('_password',
                          descriptor=property(_get_password,
                                              _set_password))

    def check_password(self, password):
        if self.password is None:
            return False
        return check_password_hash(self.password, password)

    role_code = Column(db.SmallInteger, default=USER, nullable=False)

    @property
    def role(self):
        return USER_ROLE[self.role_code]

    def is_admin(self):
        return self.role_code == ADMIN

    def is_authenticated(self):
        return True

    # One-to-many relationship between users and user_statuses.
    status_code = Column(db.SmallInteger, default=INACTIVE)

    @property
    def status(self):
        return USER_STATUS[self.status_code]

    # Class methods

    @classmethod
    def authenticate(cls, login, password):
        user = cls.query(Users).filter_by(Users.email.ilike(login)).first()

        if user:
            authenticated = user.check_password(password)
        else:
            authenticated = False

        return user, authenticated

    @classmethod
    def get_by_id(cls, user_id):
        return cls.query.filter_by(id=user_id).first_or_404()

    def check_email(self, email):
        return Users.query.filter(Users.email == email).count() == 0

    def __unicode__(self):
        _str = '%s. %s' % (self.id, self.name)
        return str(_str)


# Customized User model admin
class UsersAdmin(sqla.ModelView):
    column_list = ('id', 'name', 'email', 'role_code', 'status_code',
                   'created_time', 'activation_key')
    column_sortable_list = ('id', 'name', 'email', 'created_time',
                            'role_code', 'status_code')
    column_searchable_list = ('email', Users.email)
    column_filters = ('id', 'name', 'email', 'created_time', 'role_code')

    form_excluded_columns = ('password')

    form_choices = {
        'role_code': [
            ('2', 'User'),
            ('0', 'Admin')
        ],
        'status_code': [
            ('0', 'Inactive Account'),
            ('1', 'New Account'),
            ('2', 'Active Account')
        ]
    }

    column_choices = {
        'role_code': [
            (2, 'User'),
            (1, 'Staff'),
            (0, 'Admin')
        ],
        'status_code': [
            (0, 'Inactive Account'),
            (1, 'New Account'),
            (2, 'Active Account')
        ]
    }

    def __init__(self, session):
        super(UsersAdmin, self).__init__(Users, session)

    def is_accessible(self):
        if current_user.role == 'admin':
            return current_user.is_authenticated()

class Comment(db.Model):
	__tablename__ = "comments"
	id = Column(db.Integer, primary_key=True)
	user_id = Column(db.Integer, db.ForeignKey("users.id"))
	project_id = Column(db.Integer, db.ForeignKey("projects.id"))
	imp_id = Column(db.Integer, db.ForeignKey("implementations.imp_id"))
	content = Column(db.String(500))
	parent_id = db.Column(db.Integer, db.ForeignKey("comments.id"))
	replies = db.relationship("Comment", backref=db.backref('parent', remote_side=[id]), lazy='dynamic')
	user = db.relationship("Users")
	project = db.relationship("Project")
	implementation = db.relationship("Implementation")
	
	def __init__(self, id, uid, pid, iid, content):
		self.id = id
		self.user_id = uid
		self.project_id = pid
		self.imp_id = iid
		self.content = content
		#self.parent_id = parent
		#self.replies = replies
		
# Customized comment model admin
class CommentAdmin(sqla.ModelView):
    can_delete = True
    column_hide_backrefs = False
    column_display_pk = True
    column_list = [c_attr.key for c_attr in inspect(Comment).mapper.column_attrs]
    column_sortable_list = ('id', 'user_id', 'project_id', 'imp_id', "content", "parent_id", "replies")
    column_filters = ('id', 'user_id', 'project_id', 'imp_id', "content", "parent_id", "replies")
    column_searchable_list = ('user_id', Users.id)

    def __init__(self, session):
        super(CommentAdmin, self).__init__(Comment, session)

    def is_accessible(self):
        if current_user.role == 'admin':
            return current_user.is_authenticated()
            
