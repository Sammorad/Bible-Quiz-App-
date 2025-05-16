import pytest 
import Bible_quiz_app_02 as bible_quiz
from unittest.mock import patch 

# Fixtures
@pytest.fixture
def mock_quiz():
    """Fixture providing a standard quiz for testing"""
    return [
        {"question": "Who was the first king of Israel",
         "options": [
             "A. Saul",
             "B. David",
             "C. Solomon",
             "D. Samuel"
         ],
         "answer": "A"},
        {"question": "Who led the Israelites out of Egypt?",
         "options": [
             "A. Joshua ",
             "B. Moses",
             "C. Aaron",
             "D. David"
         ],
         "answer": "B"}
    ]

@pytest.fixture
def empty_quiz():
    """Fixture providing an empty quiz for testing"""
    return []

@pytest.fixture
def mock_save():
    """Fixture for mocking the save_quiz function"""
    with patch("Bible_quiz_app_02.save_quiz") as mock:
        yield mock

@pytest.fixture
def mock_load(mock_quiz):
    """Fixture for mocking the load_quiz function"""
    with patch("Bible_quiz_app_02.load_quiz", return_value=mock_quiz) as mock:
        yield mock

# Markers
pytestmark = [
    pytest.mark.unit,
    pytest.mark.quiz_operations
]

# Tests for modify_question
@pytest.mark.modify
def test_modify_question(mock_load, mock_save):
    """Test modifying a question in the quiz"""
    with patch("builtins.input", side_effect=[
        "2",  # Question number to modify
        "yes",  # Confirmation
        "Who was the father of the twelve tribes of Israel",  # New question
        "C",  # New answer
        "A. Isaac",  # Option A
        "B. Abraham",  # Option B
        "C. Jacob",  # Option C
        "D. Joseph"  # Option D
    ]):
        bible_quiz.modify_question()
        
        mock_save.assert_called_with([
            {"question": "Who was the first king of Israel",
             "options": [
                 "A. Saul",
                 "B. David",
                 "C. Solomon",
                 "D. Samuel"
             ],
             "answer": "A"},
            {"question": "Who was the father of the twelve tribes of Israel",
             "options": [
                 "A. Isaac",
                 "B. Abraham",
                 "C. Jacob",
                 "D. Joseph"
             ],
             "answer": "C"}
        ])

@pytest.mark.modify
def test_modify_question_invalid_number(mock_load, mock_save):
    """Test modifying a question with an invalid number"""
    with patch("builtins.input", side_effect=["5", "q"]):
        bible_quiz.modify_question()
        mock_save.assert_not_called()

@pytest.mark.modify
def test_modify_question_cancelled(mock_load, mock_save):
    """Test cancelling the modify operation"""
    with patch("builtins.input", side_effect=["2", "no"]):
        bible_quiz.modify_question()
        mock_save.assert_not_called()

# Tests for add_question_and_answer
@pytest.mark.add
def test_add_question_and_answer(mock_load, mock_save):
    """Test adding a new question to the quiz"""
    with patch("builtins.input", side_effect=[
        "Which city's walls fell down after the Israelites marched around it for seven days?",  # Question
        "A. Jericho",  # Option A
        "B. Ai",  # Option B
        "C. Bethel",  # Option C
        "D. Samaria",  # Option D
        "A"  # Answer
    ]):
        bible_quiz.add_question_and_answer()
        
        mock_save.assert_called_with([
            {"question": "Who was the first king of Israel",
             "options": [
                 "A. Saul",
                 "B. David",
                 "C. Solomon",
                 "D. Samuel"
             ],
             "answer": "A"},
            {"question": "Who led the Israelites out of Egypt?",
             "options": [
                 "A. Joshua ",
                 "B. Moses",
                 "C. Aaron",
                 "D. David"
             ],
             "answer": "B"},
            {"question": "Which city's walls fell down after the Israelites marched around it for seven days?",
             "options": [
                 "A. Jericho",
                 "B. Ai",
                 "C. Bethel",
                 "D. Samaria"
             ],
             "answer": "A"}
        ])

@pytest.mark.add
def test_add_question_and_answer_empty_quiz(empty_quiz, mock_save):
    """Test adding a question when the quiz is empty"""
    with patch("Bible_quiz_app_02.load_quiz", return_value=empty_quiz), \
         patch("builtins.input", side_effect=[
             "Which city's walls fell down after the Israelites marched around it for seven days?",
             "A. Jericho",
             "B. Ai",
             "C. Bethel",
             "D. Samaria",
             "A"
         ]):
        bible_quiz.add_question_and_answer()
        
        mock_save.assert_called_with([
            {"question": "Which city's walls fell down after the Israelites marched around it for seven days?",
             "options": [
                 "A. Jericho",
                 "B. Ai",
                 "C. Bethel",
                 "D. Samaria"
             ],
             "answer": "A"}
        ])

# Tests for delete_question
@pytest.mark.delete
def test_delete_question(mock_load, mock_save):
    """Test deleting a question from the quiz"""
    with patch("builtins.input", side_effect=["2", "yes"]):
        bible_quiz.delete_question()
        
        mock_save.assert_called_with([
            {"question": "Who was the first king of Israel",
             "options": [
                 "A. Saul",
                 "B. David",
                 "C. Solomon",
                 "D. Samuel"
             ],
             "answer": "A"}
        ])

@pytest.mark.delete
def test_delete_question_invalid_number(mock_load, mock_save):
    """Test deleting a question with an invalid question number"""
    with patch("builtins.input", side_effect=["5", "q"]):
        bible_quiz.delete_question()
        mock_save.assert_not_called()

@pytest.mark.delete
def test_delete_question_cancelled(mock_load, mock_save):
    """Test cancelling the delete operation"""
    with patch("builtins.input", side_effect=["2", "no"]):
        bible_quiz.delete_question()
        mock_save.assert_not_called()


                                                
                                                                                          


