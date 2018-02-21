#!/usr/bin/env python
import codecs
import yaml
from ansible.parsing import vault
from ansible.parsing.dataloader import DataLoader
from ansible.parsing.yaml import objects
from ansible.parsing.yaml.dumper import AnsibleDumper
from ansible.parsing.yaml.loader import AnsibleLoader


def main():
    vault_file = '~/.vaultpass'
    in_file = "variables.yml"

    target_env = 'test'
    external_system_name = 'blabla'
    external_system_password = 'This is a password!'

    # Load vault password and prepare secrets for decryption
    loader = DataLoader()
    secret = vault.get_file_vault_secret(filename=vault_file, loader=loader)
    secret.load()
    vault_secrets = [('default', secret)]
    _vault = vault.VaultLib(vault_secrets)

    # Load encrypted yml for processing
    with codecs.open(in_file, 'r', encoding='utf-8') as f:
        loaded_yaml = AnsibleLoader(f, vault_secrets=_vault.secrets).get_single_data()

    # Modify yml with new encrypted values
    new_encrypted_variable = objects.AnsibleVaultEncryptedUnicode.from_plaintext(external_system_password, _vault, vault_secrets[0][1])

    loaded_yaml[target_env]['credentials'][external_system_name]['password'] = new_encrypted_variable

    # Write a new encrypted yml
    with open('new_variables.yml','w') as fd:
        yaml.dump(loaded_yaml, fd, Dumper=AnsibleDumper, encoding=None, default_flow_style=False)

    print(loaded_yaml)


if __name__ == '__main__':
    main()
