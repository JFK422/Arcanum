[![Build Status](https://travis-ci.com/JFK422/Arcanum.svg?branch=master)](https://travis-ci.com/JFK422/Arcanum)
[![Snap Status](https://build.snapcraft.io/badge/JFK422/Arcanum.svg)](https://build.snapcraft.io/user/JFK422/Arcanum)
[![Status](https://kennethmathis.ch/shields/beta)](https://github.com/JFK422/Arcanum/releases)
# Arcanum
A small tool for generating, encrypting and saving passwords.

On startup it will show a dialog to connect to a database where the passwords and keys will be stored.
At the moment one can only connect to database servers. (SQLite/offline storage is planned)
Feel free to have a look around and modfiy the code to your needs.

## Status:
Arcanum's password storing is finishing its alpha phase. There are still improvements needed to speed up En-&Decryption.
The settings tab is there but a buggy mess atm. Will be fixed wit the next few additions.
There is a key management system planned but not implemented at the moment.

## Notes:
- I can't guarante that your passwords will be secure. Use this programm at your own risk.
- Logging is enabled by default with no personal information being logged.
- For encryption the python-gnupg module is used.
- The connection data will not be saved. Needs to be hardcoded in like my testserver.
- The connected database needs to have a schema called passwords present otherwise connecting will fail.
- The required tables are automaticly created upon startup. No setup work needed here.
- The snap is building but not launchable due to misaligned file paths.
- Arcanum uses the python implementation of the [QProgressIndicator from mojocorp](https://github.com/mojocorp/QProgressIndicator)