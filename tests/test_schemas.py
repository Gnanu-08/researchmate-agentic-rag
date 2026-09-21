from app.models.schemas import Plan

def test_plan_schema():
    p = Plan(action="retrieve", search_query="attendance", reason="policy question")
    assert p.action == "retrieve"
