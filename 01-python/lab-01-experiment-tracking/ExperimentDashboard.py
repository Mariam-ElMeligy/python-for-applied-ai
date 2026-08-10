class ExperimentDashboard:

    # defining dashbaord storage
    def __init__(self):
        self.experiments = []
        self.experiment_scores = {}

        print("Experiment Dasboard Instance Created Successfully")

    @staticmethod
    def check_repitition(experiments, experiment):
        for exp in experiments:
            if exp.name == experiment:
                raise ValueError("Can not store two Experiments with the same name")

    # add new experiment to dashboard
    def add_experiment(self, experiment):
        self.check_repitition(self.experiments, experiment.name)
        self.experiments.append(experiment)

    # show reports of all existing experiments 
    def show_reports(self):
        for experiment in self.experiments:
            print(experiment.report())
            print()

    # find the best experiment
    def best_experiment(self):
        for experiment in self.experiments:
            self.experiment_scores[experiment] = experiment.score
        return max(self.experiment_scores, key=self.experiment_scores.get)