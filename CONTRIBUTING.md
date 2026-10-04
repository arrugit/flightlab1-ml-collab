# Contributing

## Branches
- `main`: production, released and tagged models only
- `staging`: release candidate, reproduced before release
- `dev`: integration of finished work
- `feat/<name>`: features and pipeline changes (from `dev`)
- `data/<name>`: dataset updates tracked with DVC (from `dev`)
- `exp/<member>-<idea>`: experiments, never merged directly (from `dev`)
- `fix/<name>`: urgent production fixes (from `main`, then merged back into `dev`)

Nobody pushes directly to `dev`, `staging` or `main`. Every change arrives through a pull request.

## Commit messages
We use Conventional Commits: `feat:`, `fix:`, `data:`, `exp:`, `docs:`, `chore:`, `build:`, `ci:`, `test:`.
Examples: `feat: add scaling step`, `data: remove duplicate rows`.

## Pull requests
- Every PR into `dev` is **squash-merged**, so each PR becomes one commit on `dev`.
- Every PR needs one approving review from a teammate who has checked out the branch.
- Delete the branch after merging.
- Run `dvc push` before `git push` whenever data or models changed.

## Setup
    uv sync
    uv run pre-commit install
    uv run dvc pull