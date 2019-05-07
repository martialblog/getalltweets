[![Build Status](https://travis-ci.org/martialblog/getalltweets.svg?branch=master)](https://travis-ci.org/martialblog/getalltweets)
[![Coverage Status](https://coveralls.io/repos/github/martialblog/getalltweets/badge.svg?branch=master)](https://coveralls.io/github/martialblog/getalltweets?branch=master)

# getalltweets

Python Module to scrap all Tweets of a specific user or topic, without using the Twitter API.

# Examples

CLI with stdout:

```bash
# Returns one Tweet per line
getalltweets-cli --username sometwitterino > sometwitterino.ldjson
```

CLI for multiple users:

```bash
for user in $(cat "users.txt")
do
    echo "Getting Tweets for $user"
    python3 getalltweets-cli -n 123 --username $user > tweets/$user.ldjson
done
```

# Setup

```bash
pip3 install -r requirements.txt
```

# Development

## Fixtures

To install all fixtures for development:

```bash
pip3 install -r requirements-dev.txt
```

## Unit Test

To run the Unit Tests:

```bash
pytest -v
```

## Pylint

To run pylint:

```bash
pylint getalltweets/
```
