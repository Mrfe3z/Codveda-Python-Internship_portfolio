# from os import path
from fast_file_encryption import IntegrityError
import fast_file_encryption as ffe
from pathlib import Path

pub_key = Path('public.pem')
priv_key = Path('private.pem')
if not priv_key.exists() or not pub_key.exists():
    print("System: Keys missing. Generating new master keys...")
    ffe.save_key_pair(public_key=pub_key, private_key=priv_key)
else:
    print("System: Existing master keys found and locked in.")


def file_encryption(file, output_path):
    '''
    opens and encrypts a file and adds a meta data,
    creates a copy of original file
    returns None
    '''
    encryptor = ffe.Encryptor(ffe.read_public_key(Path('public.pem')))
    # encrypted_file = Path('encrypted_file.ffe')
    encryptor.copy_encrypted(
        file,
        output_path,
        add_source_metadata=True
    )


def file_decryption(file, output_path):
    '''
    opens and decrypts a file and viewing of meta data,
    returns decrypted file,
    '''
    decryptor = ffe.Decryptor(ffe.read_private_key(Path('private.pem')))
    # decrypted_file = Path('decrypted_file.txt')
    decryptor.copy_decrypted(
        file,
        output_path
    )
    content = output_path.read_text()

    return content\



def get_save_path(original_file, default_suffix):
    '''
    Prompts the user for a save location. 
    Auto-generates a path if the user leaves it blank.
    '''
    save_as = input(
        'Save as (Press Enter to auto-generate):\n> ').strip('\"\'')

    if save_as == '':
        # Combine the original name with the new suffix
        return original_file.parent / f"{original_file.stem}{default_suffix}"

    return Path(save_as)


while True:
    print("---START---")
    print('what do you need?')
    choice = input('''1.Encrypt
2.Decrypt
3.Exit
    ''')

    try:
        choice = int(choice)
    except ValueError as e:
        print('please select a valid option')
        continue

    if choice == 1:
        print('--ENCRYPTION--')
        file_name = Path(input('''Enter file name:
    HINT = use file paths for now:\n>''').strip('\"\''))
        output_path = get_save_path(file_name, '_encrypted.ffe')

        print('ENCRyPTing.......')
        file_encryption(file_name, output_path)
        print('ENCRYPTION COMPLETE')
        print(' ')

    elif choice == 2:
        print('--DECRYPTION--')
        file_name = Path(input('''Enter File name:
    HINT = use file paths for now:\n>''').strip('\"\''))
        output_path = get_save_path(file_name, '_encrypted.ffe')

        print('DeCRyPting......')
        try:
            content = file_decryption(file_name, output_path)
        except IntegrityError as e:
            print('sorry no can do, crashed ')
            break
        print(' ')
        print(content)
        print(' ')
        print('DECRYPTION COMPLETE')
        print(' ')

    elif choice == 3:
        print('thanks for using our service, Goodbye!!')
        break
