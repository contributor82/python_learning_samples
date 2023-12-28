"""Module for obtaining moon list and planets """


class ObtainMoonListAndPlanets:
    """Obtain moon list and planets class """
    planet_moons: dict[str, int]

    def __init__(self) -> None:
        """Initializing planet moons dictionary """
        self.planet_moons = {'Mercury': 0, 'Venus': 0, 'Earth': 1, 'Mars': 2, 'Jupiter': 79,
                             'Saturn': 82, 'Uranus': 27, 'Neptune': 14, 'pluto': 5, 'Ceres': 0,
                             'Eris': 1, 'Haumea': 2, 'Makemake': 1, 'Sedna': 1, 'Orcus': 1}

    def get_moon_list(self) -> list[int]:
        """Get moon list """
        moons: list[int] = list(self.planet_moons.values())
        return moons

    def get_planets(self) -> list[str]:
        """Get planets """
        planets: list[str] = list(self.planet_moons.keys())
        return planets

    def get_total_moons(self) -> None:
        """Get total moons """
        total_moons: int = sum(self.planet_moons.values())
        print('Total moons: ', total_moons)

    def get_total_planets(self) -> None:
        """Get total planets """
        total_planets: int = len(self.planet_moons)
        print('Total planets: ', total_planets)

    def get_average_moons(self) -> None:
        """Get average moons """
        average_moons: float = sum(
            self.planet_moons.values()) / len(self.planet_moons)
        print('Average moons: ', average_moons)


if __name__ == '__main__':
    obtain_moon_list_and_planets_instance = ObtainMoonListAndPlanets()
    print(' Moon list: ', obtain_moon_list_and_planets_instance.get_moon_list(),
          '\n Planets: ', obtain_moon_list_and_planets_instance.get_planets())

    obtain_moon_list_and_planets_instance.get_total_moons()
    obtain_moon_list_and_planets_instance.get_total_planets()
    obtain_moon_list_and_planets_instance.get_average_moons()
