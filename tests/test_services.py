# tests/test_services.py
from app.services.ai_ml.nlp_engine import NLPEngine

def test_nlp_engine():
    engine = NLPEngine()
    result = engine.generate_copy("Test prompt")
    assert isinstance(result, str)
