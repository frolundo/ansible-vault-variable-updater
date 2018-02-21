# ansible-vault-variable-updater

This is a simple script that helps updating embedded vault strings in ansible config:
http://docs.ansible.com/ansible/2.4/vault.html#use-encrypt-string-to-create-encrypted-variables-to-embed-in-yaml

The problem it solves: ansible has no utils to easily work with yaml document in a convenient way.
This script is very basic, but it shows principle of decrypt-encrypt process which can be used in a complex script.
For example, I did a Jenkins job with input parameters that updates values (Including encrypted variables) in yml on-demand, than pushes changes to git repository.

Here is the corresponding feature-request on ansible side:
https://github.com/ansible/ansible/issues/26190
I do not believe it will be implemented anywhere soon.
