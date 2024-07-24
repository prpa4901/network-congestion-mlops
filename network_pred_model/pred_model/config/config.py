import pathlib
import os
import pred_model

PACKAGE_ROOT = pathlib.Path(pred_model.__file__).resolve().parent

DATAPATH = os.path.join(PACKAGE_ROOT, "datasets")

TRAIN_FILE = 'train_network.csv'

TEST_FILE = 'test_network.csv'

MODEL_NAME = 'network-cong-classifier.pkl'

MODEL_TO_SAVE_PATH = os.path.join(PACKAGE_ROOT, 'trained_models')

TARGET = 'congestion'

FEATURES = ['packet_size', 'latency', 'throughput', 'scenario', 'protocol',
       'errors', 'retransmissions', 'device_type', 'bandwidth',
       'signal_strength', 'network_load', 'error_rate', 'sdwan_link_status',
       'bgp_link_status', 'mpls_link_status', 'time_category']

NUM_COLS = ['packet_size', 'latency', 'throughput', 'errors', 'retransmissions', 'bandwidth',
            'signal_strength', 'network_load','error_rate']
CAT_COLS = ['scenario', 'protocol', 'sdwan_link_status', 'bgp_link_status', 'mpls_link_status',
            'time_category']

FEATURES_TO_ENCODE = ['scenario', 'protocol', 'sdwan_link_status', 'bgp_link_status', 
                      'mpls_link_status', 'time_category']

NEW_FEATURES = ['combined_load', 'efficiency', 'reliability_issues', 'signal_to_bandwidth']

FEATURES_TO_DROP = ['network_load', 'error_rate', 'throughput', 'latency', 'errors', 'retransmissions', 
                    'signal_strength','bandwidth']

LOG_TRANSFORM = ['packet_size', 'combined_load', 'efficiency', 'reliability_issues']

