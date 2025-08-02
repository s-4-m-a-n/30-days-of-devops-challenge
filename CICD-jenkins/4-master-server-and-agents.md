# Jenkins Master server and Agents

Master server
- java and jenkins

Agents server : (workers node)
- java


## Communication
- communcation in done using ssh
so master needs to communicate with agents so
- `master` should have a `private key`
- and `agent` should have the `public key`

# Setup keys in master and agents
- go to .ssh folder
```
cd ~/.ssh
```
- generate key pair
```
ssh-keygen
```
- print and copy the public key (.pub)
```
cat <public_key_name>.pub
```
expected output example:
```
ssh-ed25519 AAAAC3NzaC1lZDI1NTE5AAAAIMMn/t75J0+Y4qq+ay5C4F9TVu2m5T/J9H4s/PQrfCP3 ubuntu@ip-172-31-8-142

```




