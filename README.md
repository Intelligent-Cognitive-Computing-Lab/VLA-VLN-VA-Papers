# VLA-VLN-VA-Papers

HENU-EAI Team VLA-VLN-VA-Papers Collection

This repository contains a collection of papers and resources related to VLA, VLN, and VA research by the HENU-EAI team.

---

### 🔄 Sync Status

[![Sync Commit](https://img.shields.io/badge/sync%20commit-bb1fa52-blue)](https://github.com/jonyzhang2023/awesome-embodied-vla-va-vln/commit/bb1fa52)
[![Last Synced](https://img.shields.io/badge/last%20synced-July%2010%2C%202025-brightgreen)](https://github.com/jonyzhang2023/awesome-embodied-vla-va-vln)

This repository is based on [awesome-embodied-vla-va-vln](https://github.com/jonyzhang2023/awesome-embodied-vla-va-vln), with added PDF files for all listed papers to enable offline reading.

---

## 📦 Large Files Notice (Git LFS)

This repository uses [Git Large File Storage (LFS)](https://git-lfs.com/) to manage large files such as datasets, pretrained models, and other heavy assets.

To work with this repository properly, especially if you need access to large files, follow the instructions below.

---

### 🛠️ Clone with Git LFS (Recommended)

First, make sure Git LFS is installed:

```bash
# macOS (Homebrew)
brew install git-lfs

# Ubuntu / Debian
sudo apt-get install git-lfs

# Windows
choco install git-lfs
````

Then initialize it (only needed once):

```bash
git lfs install
```

Clone the repository as usual:

```bash
git clone https://github.com/Intelligent-Cognitive-Computing-Lab/VLA-VLN-VA-Papers.git
cd VLA-VLN-VA-Papers
```

Git LFS will automatically download the necessary large files.

---

### 🚫 Clone Without Downloading Large Files (Optional)

If you only want to browse the code or documents and do **not** need the large files right away, you can skip downloading them at clone time:

```bash
GIT_LFS_SKIP_SMUDGE=1 git clone git@github.com:Intelligent-Cognitive-Computing-Lab/VLA-VLN-VA-Papers.git
cd VLA-VLN-VA-Papers
```

This will leave LFS-managed files as small text pointer files.

To download them later when needed:

```bash
git lfs pull                 # Download all LFS files
git lfs pull --include="path/to/file_or_dir"   # Download specific files
```

---

### 📋 Check LFS Tracked Files

To see which files are managed by Git LFS:

```bash
git lfs ls-files
```

---

If you encounter any issues with Git LFS, please refer to the [official Git LFS documentation](https://git-lfs.com/) or contact the repository maintainer.

