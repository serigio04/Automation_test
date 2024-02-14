from src.models.languageModel import LanguageModel

def test_get_language_not_none():
    languages = LanguageModel.get_language()
    assert languages != None
    
def test_get_language_has_elements():
    languages = LanguageModel.get_language()
    assert len(languages) > 0

def test_get_language_check_elements_length():
    languages = LanguageModel.get_language()
    for language in languages:
        assert len(language) > 0
