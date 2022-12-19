''' *** Required libraries *** '''
# Basic libraries
import os
import re
import sys

# Installed libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import librosa
import librosa.display

# Custom libraries
import accent_recognition.conifg as cfg

# =============================================

''' *** Functions *** '''

# -- Data preparation
def get_recording_path(file : list) -> str:
    '''
        `file` - list with elements:
                0   -   accent
                1   -   num
                2   -   extension
    '''
    path = cfg.RECORDINGS_DIR / ('.'.join((''.join((file[0], file[1])), file[2])))
    return str(path)


def get_data() -> pd.DataFrame:
    '''
        Load data from `RECORDINGS_DIR`
        Standardize data to list of lists:
            0   -   accent
            1   -   num
            2   -   extension
    '''
    filenames = []
    
    for path in os.listdir(cfg.RECORDINGS_DIR):
        if os.path.isfile(os.path.join(cfg.RECORDINGS_DIR, path)):
            filenames.append(path)
    
    
    files = []
    regex = r"^(?P<accent>.*?)(?P<num>\d*)\.(?P<ext>.*)$"
    
    for filename in filenames:
        res = re.match(regex, filename)
        if res:
            accent, num, ext = res.group('accent'), res.group('num'), res.group('ext')
            path = get_recording_path([accent, num, ext])
            record = [accent, num, ext, path]
            files.append(record)
    
    columns = ['accent', 'num', 'ext', 'path']
    files_df = pd.DataFrame(files, columns=columns)

    return files_df


# -- Audio file features extraction
def extract_features_from_audiofile(filepath : str) -> list:
    '''
        Features:
            y       -   audio data / signal
            sr      -   framerate / sample rate
            mfcc    -   Mel frequency cepstrum
    '''
    SAMPLE_RATE = 6000  
    DURATION = 30       
    MFFC_SEGMENTS = 10  
    
    y, sr = librosa.load(filepath, sr=SAMPLE_RATE, duration=DURATION)
    mfcc = librosa.feature.mfcc(y=y, sr=SAMPLE_RATE, n_mfcc=MFFC_SEGMENTS)
    mfcc = np.asarray(mfcc)
    
    return [y, sr, mfcc]


def extract_features(files : pd.DataFrame) -> pd.DataFrame:
    features = []
    
    files_colums = files.columns
    
    for index, row in files.iterrows():
        path = row[files_colums[-1]]
        feats = extract_features_from_audiofile(path)
        
        features.append(feats)
    
    features_df = pd.DataFrame(features, columns=['y', 'sr', 'mfcc'])

    return features_df


# -- Save features to CSV
def save_to_csv(files : pd.DataFrame, features : pd.DataFrame):
    pass
    

# ---------------------------------------------

def main():
    # Load data from `cfg.RECORDINGS_DIR`
    print('Data loading... ', end='')
    files : pd.DataFrame = get_data()
    print('Done.')
    
    print(files)
    
    # Extract features from audio
    print('Features extracting... ', end='')
    features : pd.DataFrame = extract_features(files)
    print('Done.')
    
    print(features)
    
    # Save features of each recording to csv
    print('Saving features to csv... ', end='')
    
    print('Done.')
    
    # Sample plots for the first recording
    #   -- MFCC
    plt.figure(figsize=(12, 5))
    librosa.display.specshow(data=features["mfcc"].iloc[0])
    plt.title(f'{files["accent"].iloc[0]}{files["num"].iloc[0]}.{files["ext"].iloc[0]}  :  Audio sampled at {features["sr"].iloc[0]} Hz')
    plt.ylabel('MFCC')
    plt.xlabel('Time [s]')
    plt.colorbar()
    
    #   -- Audio signal / wave plot
    plt.figure(figsize=(12, 5))
    librosa.display.waveshow(y=features["y"].iloc[0], sr=features["sr"].iloc[0])
    plt.title(f'{files["accent"].iloc[0]}{files["num"].iloc[0]}.{files["ext"].iloc[0]}  :  Audio sampled at {features["sr"].iloc[0]} Hz')
    plt.ylabel('Signal')
    plt.xlabel('Time [s]')
    
    plt.show()
    

if __name__ == '__main__':
    main()
    sys.exit(0)
    