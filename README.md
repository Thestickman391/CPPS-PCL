I simply added CPSC to the list of servers. The rest of this is from the original README.MD

# CPPS-PCL
A Penguin Client Library for Club Penguin Private Servers written in Python.

**Warning:** High ban risk - Do not use with your own main penguin.

This PCL contains an API, alongside two CLI interactive modes:

### 1. Single-Login

A simple login with one penguin.

### 2. Multi-Login

A complex login with multiple penguins managed by a certain shape.

## Requirements
- Python 2.x
- Internet connection
- _For Club Penguin Rewritten_: [cefpython](https://github.com/cztomczak/cefpython) (can be installed with: `pip install cefpython3`)

## Usage

### API
TODO

### Single-Login
1. Run login.py:
```
python login.py [-r yes|no|ask] [<cpps>] [<server>] [<username>]

Options:
	-r  Remember password in the future
```
2. Choose a server (if you didn't do that in the command line)
3. Enter your username and password (if you didn't do that in the command line)
4. Choose a server (if you didn't do that in the command line)
5. Waddle on!

### Multi-Login
1. Run multi.py:
```
python multi.py [-r yes|no|ask] [<cpps>] [<server>] [<shape>]

Options:
	-r  Remember password in the future
```
2. Choose a server (if you didn't do that in the command line)
3. Choose a shape (defined in json/shapes.json, if you didn't do that in the command line)
4. Enter your usernames and passwords (as many as needed for the shape)
5. Waddle on!

## Interactive Commands
| Mode | Command | Parameters | Description |
| ---- | ------- | ---------- | ----------- |
| Both | `help` | _None_ | Prints "HELP" (will be implemented in the future). |
| Single-Login only | `log` | _None_ | Toggles logging on/off. |
| Single-Login only | `log` | `level` | Sets logging level to `level`.<br>`level` must be one of the following:<ul><li>`all` - Logs all messages below.</li><li>`debug` - Logs debug messages such as sent and received packets, and below.</li><li>`info` - Logs higher-level messages such as walking, talking etc., and below.</li><li>`warning` - Logs warning messages such as unhandled packets, and below.</li><li>`error` - Logs failure messages such as "Could not add item", and below (default).</li><li>`critical` - Logs fatal error messages such as "Connection lost".</li></ul> |
| Both | `internal` | _None_ | Prints current internal room ID. |
| Single-Login only | `id` | _None_ | Prints current penguin ID. |
| Both | `id` | `penguin_name...` | Prints ID of penguin(s) named `penguin_name`. |
| Both | `name` | _None_ | Prints current penguin name. |
| Both | `name` | `penguin_id...` | Prints name of penguin(s) with ID `penguin_id`. |
| Both | `room` | _None_ | Prints current room name. |
| Both | `room` | `room_id` | Goes to room with ID `room_id`. |
| Both | `room` | `room_name` | Goes to room named `room_name`. |
| Single-Login only | `igloo` | _None_ | Goes to your igloo. |
| Both | `igloo` | `penguin_id` | Goes to igloo of penguin with ID `penguin_id`. |
| Both | `igloo` | `penguin_name` | Goes to igloo of penguin named `penguin_name`. |
| Single-Login only | `penguins` | _None_ | Lists all penguins in current room. |
| Both | `color` | _None_ | Prints current color item ID. |
| Both | `color` | `item_id` | Equips color item with ID `item_id`. |
| Both | `head` | _None_ | Prints current head item ID. |
| Both | `head` | `item_id` | Equips head item with ID `item_id`. |
| Both | `face` | _None_ | Prints current face item ID. |
| Both | `face` | `item_id` | Equips face item with ID `item_id`. |
| Both | `neck` | _None_ | Prints current neck item ID. |
| Both | `neck` | `item_id` | Equips neck item with ID `item_id`. |
| Both | `body` | _None_ | Prints current body item ID. |
| Both | `body` | `item_id` | Equips body item with ID `item_id`. |
| Both | `hand` | _None_ | Prints current hand item ID. |
| Both | `hand` | `item_id` | Equips hand item with ID `item_id`. |
| Both | `feet` | _None_ | Prints current feet item ID. |
| Both | `feet` | `item_id` | Equips feet item with ID `item_id`. |
| Both | `pin` | _None_ | Prints current pin item ID. |
| Both | `pin` | `item_id` | Equips pin item with ID `item_id`. |
| Both | `background` | _None_ | Prints current background item ID. |
| Both | `background` | `item_id` | Equips background item with ID `item_id`. |
| Single-Login only | `clothes` | _None_ | Prints all current item IDs. |
| Both | `clothes` | `penguin_id...` | Prints all current item IDs of penguin(s) with ID `penguin_id`. |
| Both | `clothes` | `penguin_name...` | Prints all current item IDs of penguin(s) named `penguin_name`. |
| Both | `inventory` | _None_ | Prints current inventory. |
| Single-Login only | `buddies` | _None_ | Prints current buddies. |
| Single-Login only | `stamps` | _None_ | Prints all earned stamps. |
| Single-Login only | `stamps` | `penguin_id...` | Prints all earned stamps by penguin(s) with ID `penguin_id`. |
| Single-Login only | `stamps` | `penguin_name...` | Prints all earned stamps by penguin(s) named `penguin_name`. |
| Both | `walk` | `x` `y` | Walks to (`x`, `y`). |
| Both | `dance` | _None_ | Dances. |
| Both | `wave` | _None_ | Waves. |
| Both | `sit` | _None_ | Sits in direction South. |
| Both | `sit` | `direction` | Sits in direction `direction`.<br>`direction` must be one of the following:<ul><li>`se` - South East.</li><li>`e` - East.</li><li>`ne` - North East.</li><li>`n` - North.</li><li>`nw` - North West.</li><li>`w` - West.</li><li>`sw` - South West.</li><li>`s` - South.</li></ul> |
| Both | `snowball` | `x` `y` | Throws a snowball to (`x`, `y`). |
| Both | `say` | `message...` | Says `message`. |
| Both | `joke` | `joke_id` | Tells joke with ID `joke_id`. |
| Both | `emote` | `emote_id` | Reacts emote with ID `emote_id`. |
| Both | `mail` | `penguin_id` `postcard_id` | Sends to a penguin with ID `penguin_id` a postcard with ID `postcard_id`. |
| Both | `mail` | `penguin_name` `postcard_id` | Sends to a penguin named `penguin_name` a postcard with ID `postcard_id`. |
| Both | `buy` | `item_id...` | Buys item(s) with ID `item_id`. |
| Both | `ai` | `item_id...` | Buys item(s) with ID `item_id`. |
| Both | `coins` | _None_ | Prints current coins. |
| Both | `coins` | `amount` | Earns `amount` coins. |
| Both | `ac` | `amount` | Earns `amount` coins. |
| Both | `stamp` | `stamp_id...` | Earns stamp(s) with ID `stamp_id`. |
| Both | `add_igloo` | `igloo_id...` | Buys igloo(s) with ID `igloo_id`. |
| Both | `add_furniture...` | `furniture_id` | Buys furniture(s) with ID `furniture_id`. |
| Both | `music` | `music_id` | Sets igloo music to `music_id`. |
| Both | `buddy` | `penguin_id...` | Sends a buddy request to penguin(s) with ID `penguin_id`. |
| Both | `buddy` | `penguin_name...` | Sends a buddy request to penguin(s) named `penguin_name`. |
| Single-Login only | `find` | `penguin_id...` | Finds room of buddy/buddies with ID `penguin_id`. |
| Single-Login only | `find` | `penguin_name...` | Finds room of buddy/buddies named `penguin_name`. |
| Single-Login only | `follow` | _None_ | Prints currently followed penguin. |
| Both | `follow` | `penguin_id` | Follows a penguin with ID `penguin_id`. |
| Both | `follow` | `penguin_name` | Follows a penguin named `penguin_name`. |
| Both | `follow` | `penguin_id` `dx` `dy` | Follows a penguin with ID `penguin_id` with offset (`dx`, `dy`). |
| Both | `follow` | `penguin_name` `dx` `dy` | Follows a penguin named `penguin_name` with offset (`dx`, `dy`). |
| Both | `unfollow` | _None_ | Stops following. |
| Both | `logout` | _None_ | Logouts from the game. |
| Both | `exit` | _None_ | Logouts from the game. |
| Both | `quit` | _None_ | Logouts from the game. |

## Tips and Tricks
- Define more CPPSs and servers in json/servers.json
- Define more shapes in json/shapes.json
