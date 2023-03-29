## Twitter application

The application enables users to view, like and comment tweets from people that they follow, and to write their own tweets.

Technologies: python, TKInter and SQLite

# Documentation

- [Instructions](./documentation/instructions.md)
- [Requirement specification](./documentation/requirementspecification.md)
- [Architecture of application](./documentation/architecture.md)
- [Testing of application](./documentation/testing.md)
- [Time accounting](./documentation/timeaccounting.md)
- [Changelog](./documentation/changelog.md)


## Installation

1. Install dependencies

```bash
poetry install
```

2. Build the source and wheels archives

```bash
poetry run invoke build
```

3. Start application 

```bash
poetry run invoke start
```

## Shell commands

### Run application

```bash
poetry run invoke start
```

### Run tests

```bash
poetry run invoke test
```

### Test coverage report (to _htmlcov_ file)

```bash
poetry run invoke coverage-report
```

