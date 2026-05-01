# containerhive-pre-commit

pre-commit hooks for [ContainerHive](https://github.com/containerhive/containerhive).

See also: https://pre-commit.com

### Using containerhive-pre-commit with pre-commit

Add this to your `.pre-commit-config.yaml`:

```yaml
-   repo: https://github.com/containerhive/pre-commit.git
    rev: v0.1.0  # Use the ref you want to point at
    hooks:
    -   id: verify
    # -   id: generate
```

### Hooks available

#### `run`
Run an arbitrary ContainerHive command. Use the `args` key to pass any
subcommand and arguments to `ch`. This hook has no default subcommand.

Examples:

```yaml
-   repo: https://github.com/containerhive/pre-commit.git
    rev: v0.1.0
    hooks:
    # Run ch generate
    -   id: run
        args: [generate]

    # Run ch verify
    -   id: run
        args: [verify]

    # Run ch generate --output ./custom-dir
    -   id: run
        args: [generate, --output, ./custom-dir]

    # Run ch verify --strict
    -   id: run
        args: [verify, --strict]
```
