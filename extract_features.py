import pefile
import os
import pandas as pd

def extract_features(path):
    try:
        pe = pefile.PE(path)
        return {
            'NumberOfSections': len(pe.sections),
            'EntryPoint': pe.OPTIONAL_HEADER.AddressOfEntryPoint,
            'ImageBase': pe.OPTIONAL_HEADER.ImageBase,
            'SectionAlignment': pe.OPTIONAL_HEADER.SectionAlignment,
            'FileAlignment': pe.OPTIONAL_HEADER.FileAlignment,
            'SizeOfImage': pe.OPTIONAL_HEADER.SizeOfImage,
            'SizeOfHeaders': pe.OPTIONAL_HEADER.SizeOfHeaders,
            'EntropyMean': sum(s.get_entropy() for s in pe.sections)/len(pe.sections)
        }
    except:
        return None

def create_dataset(malware_dir, benign_dir):
    rows = []
    for label, folder in [(1, malware_dir), (0, benign_dir)]:
        for f in os.listdir(folder):
            feats = extract_features(os.path.join(folder, f))
            if feats:
                feats['label'] = label
                rows.append(feats)
    return pd.DataFrame(rows)

df = create_dataset("dataset/malware", "dataset/benign")
df.to_csv("malware_dataset.csv", index=False)
