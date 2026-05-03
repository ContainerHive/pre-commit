# containerhive-pre-commit

pre-commit hooks for [ContainerHive](https://github.com/containerhive/containerhive).

See also: https://pre-commit.com

### Using containerhive-pre-commit with pre-commit

Add this to your `.pre-commit-config.yaml`:

```yaml
-   repo: https://github.com/containerhive/pre-commit.git
    rev: main  # Use the ref you want to point at
    hooks:
    -   id: run
```

### Hooks available

#### `run`
Run an arbitrary ContainerHive command. Use the `args` key to pass any
subcommand and arguments to `ch`. This hook has no default subcommand.

Examples:

```yaml
-   repo: https://github.com/containerhive/pre-commit.git
    rev: main  # Use the ref you want to point at
    hooks:
    # Run ch verify
    -   id: run
        args: [verify]
```
