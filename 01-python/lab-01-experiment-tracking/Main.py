from Experiment import Experiment
from ClassificationExperiment import ClassificationExperiment
from RetrievalExperiment import RetrievalExperiment
from ExperimentDashboard import ExperimentDashboard

# Testing
class Main:

    # Class-level data
    print(Experiment.__dict__)
    print(Experiment.exp_host)

    print()

    # Creating an Instance of Class Experiment
    experimentA = Experiment("Sentiment Analysis", "Ahmed", 0.85)

    # Instance-level data
    print(experimentA.__dict__)
    print(experimentA.name)
    print(experimentA.researcher)
    print(experimentA.exp_host)

    print()

    # Accessing & Modifying Protected Variable using Convention
    # experimentA._score = 1.2
    print(experimentA._score)    # no actual restrictions forced


    # Accessing & Modifying protected variable using @Property setter & getter
    experimentA.score = 0.87
    print(experimentA.score)
    # experimentA.score = 2.5  # -> ERROR! "Restrictions Enforced"

    print()

    # Altenative Constructor
    experiment_data = {
        "name" : "Cell Morphology",
        "researcher" : "Biology",
        "score" : 0.76
    }
    experimentB = Experiment.config_dict(experiment_data)

    # 2nd Instance data
    print(experimentB.name)
    print(experimentB.researcher)
    print(experimentB.score)
    print(experimentB.exp_host)

    # Editing Class-level variable
    experimentB.exp_host = "Creativa Hub Lab"
    print(experimentB.__dict__)

    print()

    # Inheritance 
    experimentC_class = ClassificationExperiment("Arabic RAG Search", "Mariam", 0.91, 2)
    # experimentC_class.score = 2.3  # -> ERROR! "Parent behaviour Inherited"

    experimentD_ret = RetrievalExperiment("Image Classification", "Youseff", 0.83, 5)
    experimentD_ret.exp_host = "NTI AI Lab "

    print()

    # Polymorphism
    print(experimentA.report())    # Generic class (parent) behaviour
    print()
    print(experimentC_class.report())    # Specific child behaviour
    print()
    print(experimentD_ret.report())    # Specific child behaviour

    print()

    # Experiment Dashboard
    exp_dash = ExperimentDashboard()

    print()

    # Adding experiment objects into the Dashboard
    exp_dash.add_experiment(experimentA)
    print(exp_dash.experiments)
    exp_dash.add_experiment(experimentB)
    print(exp_dash.experiments)
    exp_dash.add_experiment(experimentC_class)
    print(exp_dash.experiments)
    exp_dash.add_experiment(experimentD_ret)
    print(exp_dash.experiments)

    print()

    # Printing reports
    exp_dash.show_reports()

    # Return the best experiment
    print(f"Best Experiment -> {exp_dash.best_experiment()}")
    print(f"Best Experiment score -> {exp_dash.best_experiment().score}")

    print()

    # BONUS: Prevent Repitition 

    # Attempting to add the exact experiment twice
    # exp_dash.add_experiment(experimentA) # -> ERROR! Can not store two Experiments with the same name

    # Attempting to add a new experiment that happen to have the same name 
    experimentE = Experiment("Arabic RAG Search", "Nada", 0.88)
    # exp_dash.add_experiment(experimentE) # -> ERROR! Can not store two Experiments with the same name

    



    
