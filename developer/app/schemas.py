import marshmallow as ma

# Schemas
class ProbeResponseSchema(ma.Schema):
    """Kubernetes probe response schema"""
    status = ma.fields.String(required=True)
    error = ma.fields.String(dump_only=True)

class ResultResponseSchema(ma.Schema):
    """Generic result response schema"""
    result = ma.fields.String(required=True)

class AddRequestSchema(ma.Schema):
    """Add request schema"""
    num1 = ma.fields.Number(required=True)
    num2 = ma.fields.Number(required=True)

class TimeRequestSchema(ma.Schema):
    """Time request schema"""
    days = ma.fields.Number(required=True)

class WeatherRequestSchema(ma.Schema):
    """Weather proxy request schema"""
    uszip = ma.fields.String(required=True)
