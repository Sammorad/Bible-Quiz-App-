import pytest 
import Bible_quiz_app_02 as bible_quiz
import json
from unittest.mock import patch, mock_open

mock_quiz_data = [
    {
        "question": "Who was the first created man",
        "options" : ["A. Adam", "B. Noah", "C. Moses", "D. Abraham"], 
        "answer": "A"
    }, 
    {
        "question": "Where was Jesus born?",
        "options": ["A. Nazareth", "B. Bethlehem", "C. Galilee", "D. Jerusalem"],
        "answer": "B"
    }
    
]

def test_load_quiz():
    with patch ("builtins.open", mock_open(read_data = json.dumps(mock_quiz_data))):
        assert bible_quiz.load_quiz() == mock_quiz_data

def test_save_quiz():
    expected_data = json.dumps(mock_quiz_data, indent= 4)
    with patch ("builtins.open", mock_open()) as mocked_file:
        bible_quiz.save_quiz(mock_quiz_data)
        write_calls = mocked_file().write.call_args_list
        actual_data = "". join(call[0][0] for call in write_calls)
        assert actual_data == expected_data
        