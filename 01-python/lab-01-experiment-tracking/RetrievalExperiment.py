from Experiment import Experiment

class RetrievalExperiment(Experiment):

    def __init__(self, name, researcher, score, top_k):
        # inherited attributes
        super().__init__(name, researcher, score)
        self.top_k = top_k

        print("New Retrieval Experiment Instance -> Inherits Experiment")

        
    # Overriding parent mehtod
    def report(self):
        return f"""Retrieval-specific Report (provided by {self.exp_host}): 
        Retrieval Experiment Name -> {self.name}
        Retrieval Experiment Researcher -> {self.researcher}
        Retrieval Experiment Score -> {self.score}
        Top Chosen -> {self.top_k}"""