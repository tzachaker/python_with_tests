import pytest
from app import fetch_website

def test_fetch_website():
    assert fetch_website("https://www.example.com") == 200
