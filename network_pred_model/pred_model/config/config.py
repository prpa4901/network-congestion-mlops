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

# final set of features to be preserved
FEATURES = ['packet_size', 'latency', 'throughput', 'scenario', 'protocol',
       'errors', 'retransmissions', 'device_type', 'bandwidth',
       'signal_strength', 'network_load', 'error_rate', 'sdwan_link_status',
       'bgp_link_status', 'mpls_link_status', 'time_category']

NUM_COLS = ['packet_size', 'latency', 'throughput', 'errors', 'retransmissions', 'bandwidth',
            'signal_strength', 'network_load','error_rate']
CAT_COLS = ['scenario', 'protocol', 'sdwan_link_status', 'bgp_link_status', 'mpls_link_status',
            'time_category','device_type']

FEATURES_TO_ENCODE = ['scenario', 'protocol', 'sdwan_link_status', 'bgp_link_status', 
                      'mpls_link_status', 'time_category', 'device_type']

# NEW_FEATURES = ['combined_load', 'efficiency', 'reliability_issues', 'signal_to_bandwidth']

EXISTING_COLS_FOR_NEW_FEATURES = {
    'combined_load': ['throughput', 'latency'],
    'efficiency': ['bandwidth', 'errors'],
    'reliability_issues': ['errors', 'retransmissions'],
    'signal_to_bandwidth': ['signal_strength', 'bandwidth']
}

FEATURES_TO_DROP = ['network_load', 'error_rate', 'throughput', 'latency', 'errors', 'retransmissions', 
                    'signal_strength','bandwidth']

LOG_TRANSFORM_COLS = ['packet_size', 'combined_load', 'efficiency', 'reliability_issues']


def validate_config():
    # Check if paths exist
    if not PACKAGE_ROOT.exists():
        raise FileNotFoundError(f"Package root not found: {PACKAGE_ROOT}")
    if not DATAPATH.exists():
        raise FileNotFoundError(f"Data path not found: {DATAPATH}")
    if not MODEL_TO_SAVE_PATH.exists():
        raise FileNotFoundError(f"Model save path not found: {MODEL_TO_SAVE_PATH}")

    # Check if target and features are correctly specified
    if TARGET not in FEATURES:
        raise ValueError(f"Target {TARGET} is not in the list of features.")
    
    # Add more checks as necessary
    print("Configuration validation passed.")

# Call the validation function at the end of the config file
validate_config()

