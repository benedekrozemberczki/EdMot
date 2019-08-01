import argparse

def parameter_parser():
    """
    A method to parse up command line parameters. By default it trains on the Cora dataset.
    The default hyperparameters give a good quality representation without grid search.
    """

    parser = argparse.ArgumentParser(description = "Run EdMot.")

    parser.add_argument("--edge-path",
                        nargs = "?",
                        default = "./input/cora_edges.csv",
	                help = "Edge list csv.")

    parser.add_argument("--membership-path",
                        nargs = "?",
                        default = "./output/cora_membership.json",
	                help = "Cluster memberhip json.")

    parser.add_argument("--components",
                        type = int,
                        default = 1,
	                help = "Number of training epochs. Default is 200.")

    parser.add_argument("--cutoff",
                        type = int,
                        default = 2,
	                help = "Number of training epochs. Default is 200.")

    return parser.parse_args()

