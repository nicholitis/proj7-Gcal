from busy_times import busy_times
import nose

def test_for_transparency():
    events = [{'transparency': 'transparent'}]
    range_start = ""
    range_end = ""
    result = busy_times(events, range_start, range_end)
    assert result == []

def test_for_empty_list():
    events = []
    range_start = ""
    range_end = ""
    result = busy_times(events, range_start, range_end)
    assert result == []

def test_for_events():
    events = [{'summary': 'event', 'start':{'date': '2017-01-03'}, 'end':{'date': '2017-01-03'}}]
    range_start = "2017-01-01T00:00:00+00:00"
    range_end = "2017-03-01T00:00:00+00:00"
    result = busy_times(events, range_start, range_end)
    assert result != []
