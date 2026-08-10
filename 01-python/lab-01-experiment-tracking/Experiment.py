# Defining Class Experiment:
class Experiment:

    # Class level attribute
    exp_host = "ITI AI Lab"

    def __init__(self, name, researcher, score):
        self.name = name
        self.researcher = researcher

        # Internally used (protected) variable
        self._score = score
        print('New Experiment Instance')

    # Print the object nicely as string
    def __repr__(self):
        return self.name

    # Property Decorator
    @property
    def score(self):
        return self._score

    @ score.setter
    def score(self, value):
        if 0 <= value <= 1:
            self._score = value
        else: 
            raise ValueError("score must always remain between 0 and 1")

    # Using a "Class Method" to Create an Instance of the Class given a Dictionary of State Data
    @classmethod
    def config_dict(cls, dict):
        return cls(dict["name"], dict["researcher"], dict["score"])

    # Generic report method
    def report(self):
        return f"""Experiment Report (provided by {self.exp_host}): 
        Experiment Name -> {self.name}
        Experiment Researcher -> {self.researcher}
        Experiment Score -> {self.score}"""




    


    
