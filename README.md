# Environment

- Angular CLI: 12.2.1
- Node: 12.22.7
- Package Manager: npm 7.20.5
- OS: linux x64
- https://codebots.com/docs/ubuntu-18-04-virtual-machine-setup
- https://mvthanoshan.medium.com/how-to-setup-angular-on-ubuntu-14633ee93a57

# Project Dependencies

- Python 3.8.10

# Usage Instructions

- The lru can be run locally or through client/server CLI interface.

# Running LRU locally

# 1. Clone repository

```
cd ~
git clone https://github.com/TyrionSnow1911/lruCache.git
```

# 2. Run lru

```
cd ~/lruCache/src/server
python3 lru.py
```

# Run LRU via Client-Server CLI interface.

# 1. Clone repository

```
cd ~
git clone https://github.com/TyrionSnow1911/lruCache.git
```

# 2. Start Backend Server

```
cd ~/lruCache/src/server
pip3 install -r requirements.txt
python3 server.py -s <size of lru>
```

# 3. Start Client

```
cd ~/lruCache/src/client
python3 client.py
```

# Unit Testing

```
cd ~/lruCache/src/server/test
python3 test.py
```
