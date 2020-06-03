from app.website.routes.courses import courses_bp
from app.website.routes.user import user_bp
from app.website.routes.register import register_bp
from app.website.routes.enrollment import enrollment_bp
from app.website.routes.index import index_bp
from app.website.routes.login import login_bp

blueprints = [
    courses_bp,
    user_bp,
    register_bp,
    enrollment_bp,
    index_bp,
    login_bp,
]
