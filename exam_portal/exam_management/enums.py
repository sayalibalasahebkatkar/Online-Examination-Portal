from enum import Enum

class QuestionType(Enum):
    MULTIPLE_CHOICE_SINGLE = 'multiple_choice_single'
    MULTIPLE_CHOICE_MULTIPLE = 'multiple_choice_multiple'
    FILL_IN_THE_BLANK = 'fill_in_the_blank'

    def __str__(self):
        return self.value