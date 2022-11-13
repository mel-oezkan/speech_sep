import pathlib
from typing import List
from speechbrain.dataio.dataio import read_audio

import os 


def check_files() -> bool:
    """ checks if all assets exist and returns a boolean"""

    valid = True
    for idx in range(4):
        for value in ['mixture', 'source1', 'source2']:
            path = pathlib.Path('.').joinpath('assets', f'{value}_{idx}.wav')
            
            if not path.exists():
                valid = False
                break

    return valid

def download_speakers() -> List[dict]:
    """ Downloads the speaker and the cominded mixture wav files
    from the provided speechbrian link
    
    :returns (List[dict]): dict containing the resulting mixtures and speakers
    """

    # checks if the files already exist
    if not check_files():

        # download files using the script
        os.system('sh download_assets.sh')

    asssets = []
    for idx in range(4):
        
        _item = {}
        for value in ['mixture', 'source1', 'source2']:
            path = pathlib.Path('.').joinpath('assets', f'{value}_{idx}.wav')

            # read the audio and append files
            audio_out = read_audio(str(path))  
            _item[value] = audio_out

        asssets.append(_item)

    return asssets
