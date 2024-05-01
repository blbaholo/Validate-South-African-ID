from validate_id_number.validate_id import (
    length_and_characters,
    last_number_checksum,
    citizenship,
    day_month_year,
)


def test_id_number_is_given():
    assert length_and_characters("2001014800086") == True


def test_id_number_is_too_short():
    assert length_and_characters("200101480008") == False


def test_id_number_is_too_long():
    assert length_and_characters("20010148000860") == False


def test_id_number_contains_non_numbers():
    assert length_and_characters("200101a800086") == False


def test_id_number_day():
    assert day_month_year("2001324800086") == False


def test_id_number_month():
    assert day_month_year("2013014800086") == False


def test_id_number_days_in_february():
    assert day_month_year("2002304800086") == False


def test_number_of_days_in_month():
    assert day_month_year("2011314800086") == False


def test_id_number_year():
    assert day_month_year("-201014800086") == False


def test_citizen_status():
    assert citizenship("2001014800286") == False


def test_luhn_algorithm():
    assert last_number_checksum("2001014800081") == False
