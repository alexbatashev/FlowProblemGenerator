import argparse


def main():
    parser = argparse.ArgumentParser(description='Flow Problem Data Generator')
    parser.add_argument('--num-isp', type=int,
                        help='Number of ISP nodes in graph')
    parser.add_argument('--num-backbone', type=int,
                        help='Number of backbone nodes in graph')
    parser.add_argument('--min-clients', type=int,
                        help='Min number of client nodes in graph')
    parser.add_argument('--max-clients', type=int,
                        help='Max number of client nodes in graph')
    parser.add_argument('--min-isp-edges', type=int,
                        help='Min number of edges in ISP in graph')
    parser.add_argument('--max-isp-edges', type=int,
                        help='Max number of edges in ISP in graph')
    parser.add_argument('--min-isp-bandwidth', type=int,
                        help='Max number of edges in ISP in graph')
    parser.add_argument('--max-isp-bandwidth', type=int,
                        help='Max number of edges in ISP in graph')
    parser.add_argument('--min-client-bandwidth', type=int,
                        help='Max number of edges in ISP in graph')
    parser.add_argument('--max-client-bandwidth', type=int,
                        help='Max number of edges in ISP in graph')

    args = parser.parse_args()
    generate(args.num_isp,
             args.num_backbone,
             args.min_clients,
             args.max_clients,
             args.min_isp_edges,
             args.max_isp_edges,
             args.min_isp_bandwidth,
             args.max_isp_bandwidth,
             args.min_client_bandwidth,
             args.max_client_bandwidth,
             )


if __name__ == '__main__':
    main()
