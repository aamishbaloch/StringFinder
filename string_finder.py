
class Finder:
    """
    Finder is a Python class that accepts a list of strings in the constructor and will expose a find
    function that accepts a string. The function will return all strings from the list that contain the
    exact same characters as the string passed into it.
    """

    def __init__(self, data):
        self.data = data

    def find(self, key):
        """
        The function will return all strings from the list that contain the
        exact same characters as the string passed into it. The order of the
        characters in the strings is not relevant. Character case and count
        matters. Return empty array if no condition satisfy.
        :param key: A key will be searched in the list
        :return: A list of items matched with the string
        """
        return [item for item in self.data if sorted(item) == sorted(key)] if key else []
