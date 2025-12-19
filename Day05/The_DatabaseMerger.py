# Goal: You have two dictionaries: defaults={"theme":"light","audio":"on"} and user_pref={"theme":"dark"}. Merge them so user_pref overrides defaults.

defaults={"theme":"light","audio":"on"}
user_pref={"theme":"dark"}
defaults.update(user_pref)
print(defaults)
