from Experiment import Experiment

class ClassificationExperiment(Experiment):

    def __init__(self, name, researcher, score, number_of_classes):
        # inherited attributes
        super().__init__(name, researcher, score)
        self.number_of_classes = number_of_classes

        print("New Classification Experiment Instance -> Inherits Experiment")

    # Overriding parent mehtod
    def report(self):
        return f"""Classification-specific Report (provided by {self.exp_host}): 
        Classification Experiment Name -> {self.name}
        Classification Experiment Researcher -> {self.researcher}
        Classification Experiment Score -> {self.score}
        Number of Classes -> {self.number_of_classes}"""



