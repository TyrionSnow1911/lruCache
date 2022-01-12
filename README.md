# Environment

- Angular CLI: 12.2.1
- OS: linux x64
- https://codebots.com/docs/ubuntu-18-04-virtual-machine-setup

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

# 2. Run LRU

```
cd ~/lruCache/src/server
python3 lru.py -s <size of lru>
```

# Run LRU via Client-Server CLI interface.

# 1. Clone repository

```
cd ~
git clone https://github.com/TyrionSnow1911/lruCache.git
```

# 2. Start Server

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

# Unit Testing Server

```
cd ~/lruCache/src/server/test
python3 test.py
```
