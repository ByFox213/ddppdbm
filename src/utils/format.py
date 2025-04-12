from tabulate import tabulate

__all__ = ("columns", "to_tabbed", "combine_data", "format_user", "format_users")

columns = ("id", "Username", "Password", "RegisterDate", "isLoggedIn")
columns += tuple("LastLogoutIGN" + str(i) for i in range(1, 6))
columns += tuple("IP_" + str(i) for i in range(1, 4))
columns += tuple("Clan" + str(i) for i in range(1, 4))
columns += ("Level", "Money", "Exp", "TaserLevel")
columns += tuple("Block" + x for x in ["Points", "Kills", "Deaths", "Skill"])
columns += ("isModerator", "isAccFrozen")


def to_tabbed(data) -> str:
    return tabulate(data.items(), headers=["Key", "Value"])


def combine_data(_columns, user_info):
    return dict(zip(_columns, user_info))


def format_user(_columns, user_info=None, hide_sensitive=False):
    tabbed = combine_data(_columns, user_info)
    if hide_sensitive:
        tabbed["Password"] = "**hidden**"

    return str(f"<code>{to_tabbed(tabbed)}</code>")


def format_users(user_info: list[tuple]):
    users = [combine_data(columns, x) for x in user_info]
    text = ""

    for user in users:
        text += f"/user{user['id']}\t{user['Username']}\n"
    return text

