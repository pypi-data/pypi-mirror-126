import argparse
import os
import torch
import sys
import torch.multiprocessing
torch.multiprocessing.set_sharing_strategy('file_system')
sys.path.insert(0, os.path.join(
    os.path.dirname(os.path.realpath(__file__)), "../../"))
from torch.utils.data import DataLoader
from deep_audio_features.dataloading.dataloading import FeatureExtractorDataset
from deep_audio_features.utils import load_dataset
from deep_audio_features.lib.training import test
from deep_audio_features.models.cnn import load_cnn
from sklearn.metrics import classification_report
from deep_audio_features.bin import config


def test_report(model_path, folders, layers_dropped):
    """Warning: This function is using the file_system as a shared memory
    in order to run on a big amount of data, since due to batch_size = 1,
    the share strategy used in torch.multiprocessing results in memory errors
    """

    model, hop_length, window_length = load_cnn(model_path)

    max_seq_length = model.max_sequence_length
    files_test, y_test = load_dataset.load(
        folders=folders, test=False, validation=False)

    spec_size = model.spec_size
    zero_pad = model.zero_pad
    fuse = model.fuse

    # Load sets
    test_set = FeatureExtractorDataset(X=files_test, y=y_test,
                                        fe_method=
                                        config.FEATURE_EXTRACTION_METHOD,
                                        oversampling=config.OVERSAMPLING,
                                        max_sequence_length=max_seq_length,
                                        zero_pad=zero_pad,
                                        forced_size=spec_size,
                                        fuse=model.fuse,
                                        hop_length=hop_length, window_length=window_length)

    test_loader = DataLoader(test_set, batch_size=1,
                              num_workers=4, drop_last=True, shuffle=True)

    device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
    print(f"DEVICE: {device}")

    _, y_pred, y_true = test(model=model, dataloader=test_loader,
                       cnn=True,
                       classifier=True if layers_dropped == 0 else False)

    report = classification_report(y_true, y_pred)
    print("Classification report: ")
    print(report)


if __name__ == '__main__':

    # Read arguments -- a list of folders
    parser = argparse.ArgumentParser()
    parser.add_argument('-m', '--model', required=True,
                        type=str, help='Model')

    parser.add_argument('-i', '--input', required=True,
                        type=str, nargs='+', help='Input folders')

    parser.add_argument('-L', '--layers', required=False, default=0,
                        help='Number of final layers to cut. Default is 0.')
    args = parser.parse_args()

    # Get arguments
    model_path = args.model
    folders = args.input

    layers_dropped = int(args.layers)

    # Fix any type errors
    folders = [f.replace(',', '').strip() for f in folders]

    # Check that every folder exists
    for f in folders:
        if os.path.exists(f) is False:
            raise FileNotFoundError()

    # Test the model
    test_report(model_path, folders, layers_dropped)
