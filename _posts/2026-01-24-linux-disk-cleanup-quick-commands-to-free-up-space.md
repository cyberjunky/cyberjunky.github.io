---
layout: post
title: 'Linux Disk Cleanup: Quick Commands to Free Up Space'
slug: linux-disk-cleanup-quick-commands-to-free-up-space
status: published
date: 2026-01-24 20:39:08 +0000
tags:
- linux
- fixes
- docker
category: linux
author: Ron
excerpt: "Running low on disk space? It happens to the best of us. Whether it's accumulated\
  \ cache files, forgotten Docker images, or orphaned Python virtual environments,\
  \ disk space has a way of disappearing. This quick reference guide covers the most\
  \ effective commands to reclaim your precious storage.\n\n\n\nOverview\n\n\nThis\
  \ guide covers:\n\n\n * Checking disk usage and finding space hogs\n * Cleaning\
  \ cache and log files\n * Pruning Docker resources\n * Removing Python virtual environments\n\
  \ * Package manager cache"
feature_image: /assets/images/2026/01/linux-disk-cleanup-feature.png
ghost_id: 69752dec79baac0001dcd1c3
ghost_url: https://cyberjunky.nl/linux-disk-cleanup-quick-commands-to-free-up-space/
---

{% raw %}
Running low on disk space? It happens to the best of us. Whether it's accumulated cache files, forgotten Docker images, or orphaned Python virtual environments, disk space has a way of disappearing. This quick reference guide covers the most effective commands to reclaim your precious storage.

## Overview

This guide covers:

- Checking disk usage and finding space hogs
- Cleaning cache and log files
- Pruning Docker resources
- Removing Python virtual environments
- Package manager cache cleanup
- Finding and managing large files

## Check Disk Usage First

Before cleaning, let's see where your space went.

### Overall Disk Usage

```
df -h
```

This shows all mounted filesystems and their usage. Look for partitions at 90%+ capacity.

### Find Largest Directories

```
du -h --max-depth=2 /home/$USER 2>/dev/null | sort -rh | head -30
```

This reveals the top 30 space consumers in your home directory.

### Find Python Virtual Environments

```
find /home/ron -maxdepth 3 -type d -name ".venv" -exec du -sh {} \; 2>/dev/null | sort -rh
```

Virtual environments can easily consume 500MB+ each!

## Quick Cleanup Commands

### 1. Clear User Cache (~2-3GB typical savings)

The `~/.cache` directory accumulates data from browsers, package managers, and applications. It's safe to clear:

```
rm -rf ~/.cache/*
```

Don't worry—applications will rebuild their caches as needed.

### 2. Clean Journal Logs

Systemd journal logs can grow surprisingly large over time:

```
sudo journalctl --vacuum-size=100M
```

This keeps only the most recent 100MB of logs.

### 3. Clean Docker (can free 10GB+)

Docker is notorious for consuming space with unused images, containers, and volumes:

```
docker system prune -a
```

⚠️ **Warning**: This removes all unused images, not just dangling ones. Make sure you don't need to quickly restore any containers.

### 4. Remove Python Virtual Environments

Virtual environments are easy to recreate, so they're safe to delete:

```
# Remove all venvs in home subdirectories
rm -rf ~/*/.venv

# Or remove a specific one
rm -rf ~/path/to/project/.venv
```

To recreate a venv later:

```
uv sync
# or
pip install -r requirements.txt
```

### 5. Clean Package Manager Caches

#### APT (Debian/Ubuntu)

```
sudo apt-get clean
sudo apt-get autoremove
```

#### Python pip

```
pip cache purge
```

#### UV (fast Python package manager)

```
uv cache clean
```

### 6. Find Large Files

Hunt down those forgotten ISO files and log dumps:

```
find /home/ron -type f -size +100M -exec ls -lh {} \; 2>/dev/null | sort -k5 -rh
```

This finds all files larger than 100MB, sorted by size.

## Pro Tips

- **Always check before deleting**: Use `du` and `find` to verify what you're about to remove
- **Virtual environments are disposable**: They can always be recreated from `requirements.txt` or `pyproject.toml`
- **Archive old projects**: Move unused projects to external storage rather than deleting
- **Set up log rotation**: Configure systemd journal to limit log size automatically:

  ```
  sudo journalctl --vacuum-time=7d
  ```
- **Monitor regularly**: Add `df -h` to your routine to catch issues early

## Conclusion

With these commands in your toolkit, you can quickly reclaim gigabytes of disk space. The biggest wins usually come from Docker cleanup, cache clearing, and removing unused virtual environments. Make it a habit to run these cleanups monthly, and you'll never be caught off guard by a full disk again.

---

*Written for CyberJunky's Blog*
{% endraw %}
