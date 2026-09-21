<div align="center">

# Countries War Bot
# 🤖🌍⚔️

### A Persian Rubika Strategy Game Bot

An asynchronous nation-strategy bot for Rubika: players found a country, grow an economy, form alliances, and compete on a shared leaderboard — with persistent JSON storage and a full keypad interface.

<br>

# 👨‍💻 **Sadra Hatami**

### *Developer • Software Engineer • Creator*

<br>

[![Python](https://img.shields.io/badge/Python-3.8%2B-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![Rubka](https://img.shields.io/badge/Rubka-Rubika%20Bot-8E44AD?style=for-the-badge)](https://pypi.org/)
[![AsyncIO](https://img.shields.io/badge/AsyncIO-Asynchronous-2C3E50?style=for-the-badge&logo=python&logoColor=white)](https://docs.python.org/3/library/asyncio.html)
[![JSON](https://img.shields.io/badge/Storage-JSON-003B57?style=for-the-badge)](#-architecture)
[![Persian](https://img.shields.io/badge/Language-Persian-success?style=for-the-badge)](https://en.wikipedia.org/wiki/Persian_language)
[![License](https://img.shields.io/badge/License-MIT-green.svg?style=for-the-badge)](LICENSE)
![GitHub](https://img.shields.io/badge/Open_Source-Project-black?style=for-the-badge&logo=github)

<br>

[🌐 GitHub Profile](https://github.com/sadra-hatami)
•
[📘 نسخه فارسی راهنما](README.fa.md)
•
[📧 Email](mailto:sadra.hatami.1732@gmail.com)

</div>

---

# 📑 Table of Contents

- [About](#-about)
- [Related Repositories](#-related-repositories)
- [Why This Project?](#-why-this-project)
- [Key Features](#-key-features)
- [Architecture](#-architecture)
- [Project Structure](#-project-structure)
- [Technologies](#️-technologies)
- [Installation](#-installation)
- [Configuration](#️-configuration)
- [Usage](#️-usage)
- [Target Audience](#-target-audience)
- [Roadmap](#️-roadmap)
- [FAQ](#-faq)
- [Contributing](#-contributing)
- [Contact](#-contact)
- [License](#-license)
- [Copyright](#-copyright)
- [Support](#-support)

---

# 📖 About

**Countries War Bot** is a large-scale Persian strategy bot for the Rubika platform.

Each player registers a nation, then manages resources, ranks, buildings, research, and diplomacy through inline keypads. Progress is stored locally so countries, alliances, and rankings survive a restart.

The codebase is a single asynchronous application (`bot.py`) built with `rubka`. It is designed as a portfolio piece for game-like bot architecture: state, menus, economy, and multiplayer competition in one process.

> **Tagline:** *A Persian Rubika strategy bot where players run a country, grow an economy, and compete with other nations.*

---

# 🔗 Related Repositories

This bot is part of a broader Rubika / messaging collection.

| Repository | Role |
|------------|------|
| **[Countries War Bot](https://github.com/sadra-hatami/Countries-War-Bot)** | Nation strategy game (this repo) |
| **[Rubika Group Bot](https://github.com/sadra-hatami/Rubika-Group-Bot)** | Lightweight group lock bot |
| **[Rubika Advanced Group Bot](https://github.com/sadra-hatami/Rubika-Advanced-Group-Bot)** | Full group management, automation, and extra tools |
| **[Telegram Rubika Account Panel](https://github.com/sadra-hatami/Telegram-Rubika-Account-Panel)** | Telegram panel for a Rubika user account |

Group bots use `rubka` and a bot token. The account panel uses Telegram + `rubpy`. This repository is a **game bot**, not a group moderator.

---

# 🚀 Why This Project?

Most chat bots answer a command and stop.

This project keeps a living world:

- Every player owns a named country
- Economy and rank change over time
- Players meet through challenges, alliances, and clans
- Daily loops reset missions and rewards
- An operator panel can review the player base

It shows how a messaging bot can carry a full game loop, not only a help menu.

---

# ✨ Key Features

- 🏛️ Country registration and profile
- 💰 Resource and rank progression
- 🛒 Economy, shops, and upgrades
- 🏗️ Buildings and research
- 🐾 Collectible companions
- 🎖️ Achievements
- 🤝 Alliances and clans
- ⚔️ Player challenges
- 📜 Daily and weekly missions
- 🏆 Leaderboards
- 🎛️ Keypad-first Persian interface
- 💾 Persistent JSON storage
- 🛡️ Operator tools for the running instance

---

# 🏗️ Architecture

```text
Player
 └─ Rubika chat + keypads
     └─ bot.py
         └─ JSON save file
```

- Incoming button IDs route into game systems
- User records live in a local JSON document
- Background asyncio tasks handle daily resets
- Secrets belong in environment variables, not in the file

---

# 📁 Project Structure

```text
Countries-War-Bot/
├── bot.py
└── README.md
```

`bot.py` is the application. The JSON database is created at runtime and should stay out of git.

---

# 🛠️ Technologies

- Python 3.8+
- `rubka` (async Robot, Message, ChatKeypadBuilder)
- asyncio
- JSON persistence

---

# 🚀 Installation

```bash
git clone https://github.com/sadra-hatami/Countries-War-Bot.git
cd Countries-War-Bot
pip install rubka
```

```bash
python bot.py
```

---

# ⚙️ Configuration

```python
import os
from rubka.asynco import Robot

bot = Robot(os.environ["RUBIKA_BOT_TOKEN"])
```

Optional:

```text
RUBIKA_BOT_TOKEN
ADMIN_PASSWORD
```

Add to `.gitignore`:

```text
.env
*.json
__pycache__/
```

---

# ▶️ Usage

1. Put the token in the environment.
2. Run `bot.py`.
3. Open the bot in Rubika.
4. Found a country and use the keypad menu.

---

# 🎓 Target Audience

- Rubika communities that want a long-session strategy game
- Developers studying large keypad-driven bots
- Students building a games or backend portfolio

---

# 🗺️ Roadmap

- Split systems into packages
- Optional database backend
- Richer season events
- Safer default configuration
- Command documentation per menu

---

# ❓ FAQ

### Is this a group lock bot?

No. Group tools live in [Rubika Group Bot](https://github.com/sadra-hatami/Rubika-Group-Bot) and [Rubika Advanced Group Bot](https://github.com/sadra-hatami/Rubika-Advanced-Group-Bot).

### Does progress survive a restart?

Yes, when the JSON file is kept on disk.

### Can I publish my token?

No. Use environment variables only.

---

# 🤝 Contributing

Bug reports, menu polish, and safer configuration are welcome.

---

# 📬 Contact

**Developer:**

### Sadra Hatami

📧 [Email](mailto:sadra.hatami.1732@gmail.com)

🌐 [GitHub](https://github.com/sadra-hatami)

---

# 📄 License

This project is licensed under the **MIT License**.

---

# © Copyright

© 2026 **Sadra Hatami**

All rights reserved.

---

# ⭐ Support

If this bot belongs in a portfolio or a community, please consider giving it a ⭐ on GitHub.

---

<div align="center">

## Designed & Developed with ❤️ for the developer community of Iran and the world by **Sadra Hatami**

</div>
