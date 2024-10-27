# MinecraftAutoVoting - Concept - Archive

This project was built in a short timeframe of a few days and consists of two main roles:

1. **Voting Automation**: 
   - Opens the voting sites of the targeted server to cast votes and receive rewards using web scraping via a custom Tampermonkey script (not included in the repo, as I couldn't find a backup).
   
2. **Minecraft Interaction**: 
   - Launches Minecraft(UltimMC Client for easier configurations) and autoclicks its way into the specific game mode to collect rewards from each vote.

### Tools I Experimented With:
- **Flask**: 
  - Utilized Flask to communicate with my Tampermonkey script, checking the site's status and timer to know when to scrape and vote again.
  
- **Python Libraries**:
  - **Pygetwindow**: For window management.
  - **Pyautogui**: To automate mouse movements and clicks.
  - **Pywinauto**: For interacting with the Minecraft application.

### Why Flask?
A major reason for using Flask with a portable Chromium browser instead of a Selenium script was to bypass Cloudflare's detection that would block access to the voting sites.
