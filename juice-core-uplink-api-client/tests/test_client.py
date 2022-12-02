from juice_core import SHTRestInterface

client = SHTRestInterface()


def test_plans():
    plans = client.plans()
    assert len(plans) > 0


def test_segments():
    plans = client.plans()
    name = plans.loc[0]["name"]
    segments = client.plan_segments(name)
    assert len(segments) > 0


def test_segments_by_plan_id():
    plans = client.plans()
    id = plans.loc[0]["id"]
    segments = client.plan_segments(id)
    assert len(segments) > 0


def test_engineering_segments():
    segs = client.engineering_segments()
    assert len(segs) > 0


def test_serie():
    series = client.known_series()
    name = series.loc[0]["mnemonic"]
    serie = client.series(name)
    assert len(serie) > 0


def test_events():
    events = client.event_types()
    name = events.loc[0]["mnemonic"]
    print(f"trying to retrieve events for {name}")
    events = client.events(name)
    assert len(events) > 0
