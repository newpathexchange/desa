from types import SimpleNamespace
from flask.views import MethodView
from . import blp
from ..schemas import ProbeResponseSchema

@blp.route('/k8s/alive')
class LivenessView(MethodView):
    """Kubernetes liveness API methods"""
    @blp.response(200, ProbeResponseSchema)
    def get(self):
        return SimpleNamespace(status='OK')

@blp.route('/k8s/ready')
class ReadinessView(MethodView):
    """Kubernetes readiness API methods"""
    @blp.response(200, ProbeResponseSchema)
    def get(self):
        return SimpleNamespace(status='OK')
