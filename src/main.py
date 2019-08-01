from edmot import EdMot
from parser import parameter_parser
from utils import tab_printer, graph_reader, membership_saver

def main():
    """
    Parsing command line parameters, reading data, fitting an NGCN and scoring the model.
    """
    args = parameter_parser()
    tab_printer(args)
    graph = graph_reader(args.edge_path)
    model = EdMot(graph, args.components, args.cutoff)
    memberships = model.fit()
    membership_saver(args.membership_path, memberships)
    
if __name__ == "__main__":
    main()
