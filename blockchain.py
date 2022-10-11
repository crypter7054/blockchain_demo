import json
import os
import hashlib

BLOCK_DIR = 'block/'

def get_hash(prev_block):
    with open(BLOCK_DIR + prev_block, 'rb') as f:
        content = f.read()
    return hashlib.sha256(content).hexdigest()

def validate():
    files = sorted(os.listdir(BLOCK_DIR), key=lambda x: int(x))

    results = []

    # print(files)
    for file in files[1:]:
        with open(BLOCK_DIR + file) as f:
            block = json.load(f)

        prev_hash = block.get('prev_block').get('hash')
        prev_filename = block.get('prev_block').get('filename')

        # print(prev_hash)

        actual_hash = get_hash(prev_filename)

        if prev_hash == actual_hash:
            res = 'data valid'
        else:
            res = 'INVALID'
        
        print(f'Block {prev_filename}: {res}')
        results.append({'block': prev_filename, 'result': res})

    return results

def write_block(pemilik, penyewa, lokasi, harga):
    
    block_count = len(os.listdir(BLOCK_DIR))
    prev_block = str(block_count)

    data = {
        "pemilik": pemilik, 
        "penyewa": penyewa, 
        "location": lokasi, 
        "harga": harga,
        "prev_block": {
            "hash": get_hash(prev_block),
            "filename": prev_block 
        }
    }

    current_block = BLOCK_DIR + str(block_count + 1)

    with open(current_block, 'w') as f:
        json.dump(data, f, indent=4, ensure_ascii=False)
        f.write('\n')


def main():
    # write_block(pemilik="Yos", penyewa="Soy", lokasi="107 S Oak St #458, Sheridan, Arkansas 72150, USA", harga=100)
    validate()

if __name__ == '__main__':
    main()

