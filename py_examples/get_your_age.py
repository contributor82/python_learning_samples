"""Module for knowing your age """
__all__ = ['KnowYourAge']
from datetime import datetime
class KnowYourAge:
    """Know your age class """
    current_date: datetime

    def __init__(self) -> None:
        """Initializing current date from datetime """
        self.current_date: datetime = datetime.today()

    def get_your_age(self, birth_year: int)-> int:
        """Get your age """
        age: int = self.current_date.year - birth_year
        return age

    def get_day_of_your_birth_date(self, birth_date: datetime) -> str:
        """Get day of your birth date """
        birth_week_day: str = ''
        week_day: int = birth_date.weekday()
        match str(week_day):
            case '0': birth_week_day = 'Monday'
            case '1': birth_week_day = 'Tuesday'
            case '2': birth_week_day = 'Wednesday'
            case '3': birth_week_day = 'Thursday'
            case '4': birth_week_day = 'Friday'
            case '5': birth_week_day = 'Saturday'
            case '6': birth_week_day = 'Sunday'
            case _: pass
        return birth_week_day


if __name__ == '__main__':
    know_ur_age_instance = KnowYourAge()
    print(' Birth year: ', know_ur_age_instance.current_date,
          '\n Age: ', know_ur_age_instance.get_your_age(know_ur_age_instance.current_date.year-10))

    birth_date_as_input: datetime = know_ur_age_instance.current_date  # datetime(2023,8,20)

    print(' Birth date: ', str(birth_date_as_input.date()),
          '\n Week day: ',
          know_ur_age_instance.get_day_of_your_birth_date(birth_date_as_input))
