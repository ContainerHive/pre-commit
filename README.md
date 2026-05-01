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

#### `generate`
Generate templates for ContainerHive projects. Runs `ch generate`.

#### `verify`
Verify ContainerHive project structure. Runs `ch verify`.

#### `run`
Run an arbitrary ContainerHive command. By default runs `ch` with no
subcommand. Pass arguments to ch via `args`.
