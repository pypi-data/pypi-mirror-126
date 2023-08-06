# qtile-profiles
Im using my laptop for work and private stuff and wanted to use some kind of profiles.

## Installation
You can install the package using pip
```bash
pip install qtile-profiles
```
## Usage
```python
from qtile_profiles import Profile, ProfileManager

def set_browser(browser: str):
    subprocess.run(
            f"xdg-mime default {browser} x-scheme-handler/http",
            shell=True,
        )
    subprocess.run(
            f"xdg-mime default {browser} x-scheme-handler/https",
            shell=True,
        )


work = Profile(
        programs={ # define some aliases for shorter commands later
            "firefox": "firefox",
            "thunderbird": "flatpak run org.mozilla.Thunderbird", # see 6 lines down
            "teams": "chromium --app=https://teams.office.com",
            },
        init=[ # spawn these program when calling initialize
            ("web", ["firefox"]),
            ("chat", ["mattermost-desktop", "teams"]),
            ("mail", ["tunderbird"]), # here we can use thunderbird insead of calling flatpak
            ("kp", ["keepassxc"]),
            ],
        on_load=lambda qtile: set_browser("firefox.desktop") # callback, call when profile is selected
        )
privat = Profile(
        programs={
            "firefox": "firefox -P privat",
            "thunderbird": "thunderbird",
            "discord": "discord",
            },
        init=[
            ("web", ["firefox"]),
            ("chat", ["signal-desktop", "discord"]),
            ("mail", ["thunderbird"]),
            ("kp", ["keepassxc"]),
            ],
        on_load=lambda qtile: set_browser("firefox-privat.desktop")
        )

profiles = ProfileManager([work, privat])

keys.extend([
    Key([super], "p", lazy.function(profiles.next_profile)),
    Key([super], "f", lazy.function(profiles.spawn, "firefox")),
    Key([super], "i", lazy.function(profiles.current_profile.spawn_init)),
    ])
```
