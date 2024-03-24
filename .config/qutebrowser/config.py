# Autogenerated config.py
#
# NOTE: config.py is intended for advanced users who are comfortable
# with manually migrating the config file on qutebrowser upgrades. If
# you prefer, you can also configure qutebrowser using the
# :set/:bind/:config-* commands without having to write a config.py
# file.
#
# Documentation:
#   qute://help/configuring.html
#   qute://help/settings.html

# Uncomment this to still load settings configured via autoconfig.yml
# config.load_autoconfig()
# Or uncomment this line to load settings from config.py
config.load_autoconfig(False)

# Aliases for commands. The keys of the given dictionary are the
# aliases, while the values are the commands they map to.
# Type: Dict
c.aliases = {'q': 'quit', 'w': 'session-save', 'wq': 'quit --save'}

# Setting dark mode
#config.set("colors.webpage.darkmode.enabled", True)


# Which cookies to accept. With QtWebEngine, this setting also controls
# other features with tracking capabilities similar to those of cookies;
# including IndexedDB, DOM storage, filesystem API, service workers, and
# AppCache. Note that with QtWebKit, only `all` and `never` are
# supported as per-domain values. Setting `no-3rdparty` or `no-
# unknown-3rdparty` per-domain on QtWebKit will have the same effect as
# `all`.
# Type: String
# Valid values:
#   - all: Accept all cookies.
#   - no-3rdparty: Accept cookies from the same origin only. This is known to break some sites, such as GMail.
#   - no-unknown-3rdparty: Accept cookies from the same origin only, unless a cookie is already set for the domain. On QtWebEngine, this is the same as no-3rdparty.
#   - never: Don't accept cookies at all.
config.set('content.cookies.accept', 'all', 'chrome-devtools://*')

# Which cookies to accept. With QtWebEngine, this setting also controls
# other features with tracking capabilities similar to those of cookies;
# including IndexedDB, DOM storage, filesystem API, service workers, and
# AppCache. Note that with QtWebKit, only `all` and `never` are
# supported as per-domain values. Setting `no-3rdparty` or `no-
# unknown-3rdparty` per-domain on QtWebKit will have the same effect as
# `all`.
# Type: String
# Valid values:
#   - all: Accept all cookies.
#   - no-3rdparty: Accept cookies from the same origin only. This is known to break some sites, such as GMail.
#   - no-unknown-3rdparty: Accept cookies from the same origin only, unless a cookie is already set for the domain. On QtWebEngine, this is the same as no-3rdparty.
#   - never: Don't accept cookies at all.
config.set('content.cookies.accept', 'all', 'devtools://*')

# User agent to send.  The following placeholders are defined:  *
# `{os_info}`: Something like "X11; Linux x86_64". * `{webkit_version}`:
# The underlying WebKit version (set to a fixed value   with
# QtWebEngine). * `{qt_key}`: "Qt" for QtWebKit, "QtWebEngine" for
# QtWebEngine. * `{qt_version}`: The underlying Qt version. *
# `{upstream_browser_key}`: "Version" for QtWebKit, "Chrome" for
# QtWebEngine. * `{upstream_browser_version}`: The corresponding
# Safari/Chrome version. * `{qutebrowser_version}`: The currently
# running qutebrowser version.  The default value is equal to the
# unchanged user agent of QtWebKit/QtWebEngine.  Note that the value
# read from JavaScript is always the global value. With QtWebEngine
# between 5.12 and 5.14 (inclusive), changing the value exposed to
# JavaScript requires a restart.
# Type: FormatString
config.set('content.headers.user_agent', 'Mozilla/5.0 ({os_info}) AppleWebKit/{webkit_version} (KHTML, like Gecko) {upstream_browser_key}/{upstream_browser_version} Safari/{webkit_version}', 'https://web.whatsapp.com/')

# User agent to send.  The following placeholders are defined:  *
# `{os_info}`: Something like "X11; Linux x86_64". * `{webkit_version}`:
# The underlying WebKit version (set to a fixed value   with
# QtWebEngine). * `{qt_key}`: "Qt" for QtWebKit, "QtWebEngine" for
# QtWebEngine. * `{qt_version}`: The underlying Qt version. *
# `{upstream_browser_key}`: "Version" for QtWebKit, "Chrome" for
# QtWebEngine. * `{upstream_browser_version}`: The corresponding
# Safari/Chrome version. * `{qutebrowser_version}`: The currently
# running qutebrowser version.  The default value is equal to the
# unchanged user agent of QtWebKit/QtWebEngine.  Note that the value
# read from JavaScript is always the global value. With QtWebEngine
# between 5.12 and 5.14 (inclusive), changing the value exposed to
# JavaScript requires a restart.
# Type: FormatString
config.set('content.headers.user_agent', 'Mozilla/5.0 ({os_info}; rv:71.0) Gecko/20100101 Firefox/71.0', 'https://accounts.google.com/*')

# User agent to send.  The following placeholders are defined:  *
# `{os_info}`: Something like "X11; Linux x86_64". * `{webkit_version}`:
# The underlying WebKit version (set to a fixed value   with
# QtWebEngine). * `{qt_key}`: "Qt" for QtWebKit, "QtWebEngine" for
# QtWebEngine. * `{qt_version}`: The underlying Qt version. *
# `{upstream_browser_key}`: "Version" for QtWebKit, "Chrome" for
# QtWebEngine. * `{upstream_browser_version}`: The corresponding
# Safari/Chrome version. * `{qutebrowser_version}`: The currently
# running qutebrowser version.  The default value is equal to the
# unchanged user agent of QtWebKit/QtWebEngine.  Note that the value
# read from JavaScript is always the global value. With QtWebEngine
# between 5.12 and 5.14 (inclusive), changing the value exposed to
# JavaScript requires a restart.
# Type: FormatString
config.set('content.headers.user_agent', 'Mozilla/5.0 ({os_info}) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99 Safari/537.36', 'https://*.slack.com/*')

# User agent to send.  The following placeholders are defined:  *
# `{os_info}`: Something like "X11; Linux x86_64". * `{webkit_version}`:
# The underlying WebKit version (set to a fixed value   with
# QtWebEngine). * `{qt_key}`: "Qt" for QtWebKit, "QtWebEngine" for
# QtWebEngine. * `{qt_version}`: The underlying Qt version. *
# `{upstream_browser_key}`: "Version" for QtWebKit, "Chrome" for
# QtWebEngine. * `{upstream_browser_version}`: The corresponding
# Safari/Chrome version. * `{qutebrowser_version}`: The currently
# running qutebrowser version.  The default value is equal to the
# unchanged user agent of QtWebKit/QtWebEngine.  Note that the value
# read from JavaScript is always the global value. With QtWebEngine
# between 5.12 and 5.14 (inclusive), changing the value exposed to
# JavaScript requires a restart.
# Type: FormatString
config.set('content.headers.user_agent', 'Mozilla/5.0 ({os_info}; rv:71.0) Gecko/20100101 Firefox/71.0', 'https://docs.google.com/*')

# User agent to send.  The following placeholders are defined:  *
# `{os_info}`: Something like "X11; Linux x86_64". * `{webkit_version}`:
# The underlying WebKit version (set to a fixed value   with
# QtWebEngine). * `{qt_key}`: "Qt" for QtWebKit, "QtWebEngine" for
# QtWebEngine. * `{qt_version}`: The underlying Qt version. *
# `{upstream_browser_key}`: "Version" for QtWebKit, "Chrome" for
# QtWebEngine. * `{upstream_browser_version}`: The corresponding
# Safari/Chrome version. * `{qutebrowser_version}`: The currently
# running qutebrowser version.  The default value is equal to the
# unchanged user agent of QtWebKit/QtWebEngine.  Note that the value
# read from JavaScript is always the global value. With QtWebEngine
# between 5.12 and 5.14 (inclusive), changing the value exposed to
# JavaScript requires a restart.
# Type: FormatString
config.set('content.headers.user_agent', 'Mozilla/5.0 ({os_info}; rv:71.0) Gecko/20100101 Firefox/71.0', 'https://drive.google.com/*')

# Load images automatically in web pages.
# Type: Bool
config.set('content.images', True, 'chrome-devtools://*')

# Load images automatically in web pages.
# Type: Bool
config.set('content.images', True, 'devtools://*')

# Enable JavaScript.
# Type: Bool
config.set('content.javascript.enabled', True, 'chrome-devtools://*')

# Enable JavaScript.
# Type: Bool
config.set('content.javascript.enabled', True, 'devtools://*')

# Enable JavaScript.
# Type: Bool
config.set('content.javascript.enabled', True, 'chrome://*/*')

# Enable JavaScript.
# Type: Bool
config.set('content.javascript.enabled', True, 'qute://*/*')

# Allow websites to show notifications.
# Type: BoolAsk
# Valid values:
#   - true
#   - false
#   - ask
config.set('content.notifications.enabled', True, 'https://www.reddit.com')

# Allow websites to show notifications.
# Type: BoolAsk
# Valid values:
#   - true
#   - false
#   - ask
config.set('content.notifications.enabled', True, 'https://www.youtube.com')


# When to show the tab bar.
# Type: String
# Valid values:
#   - always: Always show the tab bar.
#   - never: Always hide the tab bar.
#   - multiple: Hide the tab bar if only one tab is open.
#   - switching: Show the tab bar when switching tabs.
c.tabs.show = 'always'


# Search engines which can be used via the address bar.  Maps a search
# engine name (such as `DEFAULT`, or `ddg`) to a URL with a `{}`
# placeholder. The placeholder will be replaced by the search term, use
# `{{` and `}}` for literal `{`/`}` braces.  The following further
# placeholds are defined to configure how special characters in the
# search terms are replaced by safe characters (called 'quoting'):  *
# `{}` and `{semiquoted}` quote everything except slashes; this is the
# most   sensible choice for almost all search engines (for the search
# term   `slash/and&amp` this placeholder expands to `slash/and%26amp`).
# * `{quoted}` quotes all characters (for `slash/and&amp` this
# placeholder   expands to `slash%2Fand%26amp`). * `{unquoted}` quotes
# nothing (for `slash/and&amp` this placeholder   expands to
# `slash/and&amp`).  The search engine named `DEFAULT` is used when
# `url.auto_search` is turned on and something else than a URL was
# entered to be opened. Other search engines can be used by prepending
# the search engine name to the search term, e.g. `:open google
# qutebrowser`.
# Type: Dict
c.url.searchengines = {'DEFAULT':'https://search.brave.com/search?q={}','dcdc': 'https://duckduckgo.com/?q={}', 'am': 'https://www.amazon.com/s?k={}', 'aw': 'https://wiki.archlinux.org/?search={}', 'goog': 'https://www.google.com/search?q={}', 'hoog': 'https://hoogle.haskell.org/?hoogle={}', 're': 'https://www.reddit.com/r/{}', 'ub': 'https://www.urbandictionary.com/define.php?term={}', 'wiki': 'https://en.wikipedia.org/wiki/{}', 'yt': 'https://www.youtube.com/results?search_query={}'}

# Text color of the completion widget. May be a single color to use for
# all columns or a list of three colors, one for each column.
# Type: List of QtColor, or QtColor
c.colors.completion.fg = ['#9cc4ff', 'white', 'white']

# Background color of the completion widget for odd rows.
# Type: QssColor
c.colors.completion.odd.bg = '#1c1f24'

# Background color of the completion widget for even rows.
# Type: QssColor
c.colors.completion.even.bg = '#232429'

# Foreground color of completion widget category headers.
# Type: QtColor
c.colors.completion.category.fg = '#e1acff'

# Background color of the completion widget category headers.
# Type: QssColor
c.colors.completion.category.bg = 'qlineargradient(x1:0, y1:0, x2:0, y2:1, stop:0 #000000, stop:1 #232429)'

# Top border color of the completion widget category headers.
# Type: QssColor
c.colors.completion.category.border.top = '#3f4147'

# Bottom border color of the completion widget category headers.
# Type: QssColor
c.colors.completion.category.border.bottom = '#3f4147'

# Foreground color of the selected completion item.
# Type: QtColor
c.colors.completion.item.selected.fg = '#282c34'

# Background color of the selected completion item.
# Type: QssColor
c.colors.completion.item.selected.bg = '#ecbe7b'

# Foreground color of the matched text in the selected completion item.
# Type: QtColor
c.colors.completion.item.selected.match.fg = '#c678dd'

# Foreground color of the matched text in the completion.
# Type: QtColor
c.colors.completion.match.fg = '#c678dd'

# Color of the scrollbar handle in the completion view.
# Type: QssColor
c.colors.completion.scrollbar.fg = 'white'

# Background color for the download bar.
# Type: QssColor
c.colors.downloads.bar.bg = '#282c34'

# Background color for downloads with errors.
# Type: QtColor
c.colors.downloads.error.bg = '#ff6c6b'

# Font color for hints.
# Type: QssColor
c.colors.hints.fg = '#282c34'

# Font color for the matched part of hints.
# Type: QtColor
c.colors.hints.match.fg = '#98be65'

# Background color of an info message.
# Type: QssColor
c.colors.messages.info.bg = '#282c34'

# Background color of the statusbar.
# Type: QssColor
c.colors.statusbar.normal.bg = '#282c34'

# Foreground color of the statusbar in insert mode.
# Type: QssColor
c.colors.statusbar.insert.fg = 'white'

# Background color of the statusbar in insert mode.
# Type: QssColor
c.colors.statusbar.insert.bg = '#497920'

# Background color of the statusbar in passthrough mode.
# Type: QssColor
c.colors.statusbar.passthrough.bg = '#34426f'

# Background color of the statusbar in command mode.
# Type: QssColor
c.colors.statusbar.command.bg = '#282c34'

# Foreground color of the URL in the statusbar when there's a warning.
# Type: QssColor
c.colors.statusbar.url.warn.fg = 'yellow'

# Background color of the tab bar.
# Type: QssColor
c.colors.tabs.bar.bg = '#000000'

# Background color of unselected odd tabs.
# Type: QtColor
c.colors.tabs.odd.bg = '#000000'
c.colors.tabs.odd.fg = '#ffffff'

# Background color of unselected even tabs.
# Type: QtColor
c.colors.tabs.even.bg = '#000000'
c.colors.tabs.even.fg = '#ffffff'

# Background color of selected odd tabs.
# Type: QtColor
c.colors.tabs.selected.odd.bg = '#ffffff'
c.colors.tabs.selected.odd.fg = '#000000'

# Background color of selected even tabs.
# Type: QtColor
c.colors.tabs.selected.even.bg = '#ffffff'
c.colors.tabs.selected.even.fg = '#000000'

# Background color of pinned unselected odd tabs.
# Type: QtColor
c.colors.tabs.pinned.odd.bg = 'seagreen'

# Background color of pinned unselected even tabs.
# Type: QtColor
c.colors.tabs.pinned.even.bg = 'darkseagreen'

# Background color of pinned selected odd tabs.
# Type: QtColor
c.colors.tabs.pinned.selected.odd.bg = '#282c34'

# Background color of pinned selected even tabs.
# Type: QtColor
c.colors.tabs.pinned.selected.even.bg = '#282c34'

# Default font families to use. Whenever "default_family" is used in a
# font setting, it's replaced with the fonts listed here. If set to an
# empty value, a system-specific monospace default is used.
# Type: List of Font, or Font
c.fonts.default_family = 'Roboto Mono'

# Default font size to use. Whenever "default_size" is used in a font
# setting, it's replaced with the size listed here. Valid values are
# either a float value with a "pt" suffix, or an integer value with a
# "px" suffix.
# Type: String
c.fonts.default_size = '19pt'

# Font used in the completion widget.
# Type: Font
c.fonts.completion.entry = '19pt "Roboto Mono"'

# Font used for the debugging console.
# Type: Font
c.fonts.debug_console = '39pt "Roboto Mono"'

# Font used for prompts.
# Type: Font
c.fonts.prompts = 'default_size Roboto Mono'

# Font used in the statusbar.
# Type: Font
c.fonts.statusbar = '19pt "Roboto Mono"'

# Bindings to use dmenu rather than qutebrowser's builtin search.
#config.bind('o', 'spawn --userscript dmenu-open')
#config.bind('O', 'spawn --userscript dmenu-open --tab')

# Bindings for normal mode
config.bind('M', 'hint links spawn mpv {hint-url}')
config.bind('Z', 'hint links spawn st -e youtube-dl {hint-url}')
config.bind('t', 'cmd-set-text -s :open -t')
config.bind('xb', 'config-cycle statusbar.show always never')
config.bind('xt', 'config-cycle tabs.show always never')
config.bind('xx', 'config-cycle statusbar.show always never;; config-cycle tabs.show always never')

# Bindings for cycling through CSS stylesheets from Solarized Everything CSS:
# https://github.com/alphapapa/solarized-everything-css
config.bind('ap', 'config-cycle content.user_stylesheets ~/.config/qutebrowser/solarized-everything-css/css/apprentice/apprentice-all-sites.css ""')
config.bind('ar', 'config-cycle content.user_stylesheets ~/.config/qutebrowser/solarized-everything-css/css/darculized/darculized-all-sites.css ""')
config.bind('av', 'config-cycle content.user_stylesheets ~/.config/qutebrowser/solarized-everything-css/css/gruvbox/gruvbox-all-sites.css ""')
config.bind('sd', 'config-cycle content.user_stylesheets ~/.config/qutebrowser/solarized-everything-css/css/solarized-dark/solarized-dark-all-sites.css ""')
config.bind(',sl', 'config-cycle content.user_stylesheets ~/.config/qutebrowser/solarized-everything-css/css/solarized-light/solarized-light-all-sites.css ""')

# dark mode
config.set("colors.webpage.darkmode.enabled", True)

# keys
bindings = {
    "aa": 'cmd-set-text -s :quickmark-add {url} "',
}

for key, bind in bindings.items():
    config.bind(key, bind)

################################################################################
###   these are helper functions
################################################################################
# * Helper Functions
def bind(key, command, mode):  # noqa: E302
    """Bind key to command in mode."""
    # TODO set force; doesn't exist yet
    config.bind(key, command, mode=mode)


def nmap(key, command):
    """Bind key to command in normal mode."""
    bind(key, command, 'normal')


def imap(key, command):
    """Bind key to command in insert mode."""
    bind(key, command, 'insert')


def cmap(key, command):
    """Bind key to command in command mode."""
    bind(key, command, 'command')


# def cimap(key, command):
#     """Bind key to command in command mode and insert mode."""
#     cmap(key, command)
#     imap(key, command)


def tmap(key, command):
    """Bind key to command in caret mode."""
    bind(key, command, 'caret')


def pmap(key, command):
    """Bind key to command in passthrough mode."""
    bind(key, command, 'passthrough')


def unmap(key, mode):
    """Unbind key in mode."""
    config.unbind(key, mode=mode)


def nunmap(key):
    """Unbind key in normal mode."""
    unmap(key, mode='normal')

################################################################################
###   here goes the full convinience config
################################################################################
config.set('downloads.position', 'bottom')      # they look ugly af up there
config.set('zoom.default', '170%')              # for obvious reasons
config.set('confirm_quit', ['always'])              # don't quit on me private! that't an order!!
c.editor.command = ["gvim", '{}'] # vim is for life!!
c.tabs.last_close = "startpage"      # I would like to finish when I say so!!
c.tabs.select_on_remove = "prev"     # this thing drove me crazy with add popups in aniwave
c.auto_save.session = True           # you can't be too careful with super important work plus need to save them pornstars
c.session.lazy_restore = True        # load restored pages as soon as they are focused, just a bit of love for my CPU
c.tabs.background = True             # # open new tabs (middleclick/ctrl+click) in the background
c.tabs.new_position.unrelated = 'next'  # open -t to the right, imagine having a fuckload of tabs, just keep it local
c.hints.auto_follow = 'always' # don't require enter after hint keys
c.downloads.location.directory = '~/torrents/watch-dir/' # might as well  put everything in there | I'll w a script for categ later
c.downloads.location.prompt = False  # since I would w a script for handling the cleanup then what's the use!
c.content.autoplay = False           # you know what! I hate surprises!
c.statusbar.position = "top"        # keep you head held high soldier
# aliases
c.aliases['c'] = 'config-source'
# setting up ranger as the file handler | make it floating in qtile
config.set("fileselect.handler", "external")
config.set("fileselect.single_file.command", ['alacritty', '--class', 'ranger_qtbr_file_picker_alacritty', '-e', 'ranger', '--choosefile', '{}'])
config.set("fileselect.multiple_files.command", ['alacritty', '--class', 'ranger_qtbr_file_picker_alacritty', '-e', 'ranger', '--choosefiles', '{}'])
# key bindings relying on the helper functions
# ** Zooming
nmap('zi', 'zoom-in')                   # this is much harder than + and - but it would help me improve my typing
nmap('zo', 'zoom-out')                  # since  it would teach me to press z before i 
# C-y for pasting
imap('<Ctrl-y>', 'fake-key <Ctrl-v>')           
cmap('<Ctrl-y>', 'fake-key --global <Ctrl-v>')
# ** Passthrough
nmap(',', 'enter-mode passthrough')      
pmap('<Escape>', 'mode-leave')
# prevent c-w from closing tab
#del c.bindings.default['normal']['<Ctrl-w>']
# swap ; and :
import re
nmap(';', 'cmd-set-text :')
nunmap(':')
hints_dict = dict()  # pylint: disable = C0103
for k, v in c.bindings.default['normal'].items():
    if k.startswith(';'):
        hints_dict[re.sub(r'^;(.*)', r':\1', k)] = v
c.bindings.commands['normal'].update(hints_dict)
# caret mode 
tmap('j', 'move-to-next-line')
tmap('k', 'move-to-prev-line')
tmap('l', 'move-to-next-char')
tmap('h', 'move-to-prev-char')
# add back e functionality
tmap('e', 'move-to-end-of-word')
# vimlike navigation between suggestions in the search bar
config.bind('<Ctrl+k>', 'completion-item-focus prev', mode='command')
config.bind('<Ctrl+j>', 'completion-item-focus next', mode='command')
#nmap('<Ctrl+k>', 'completion-item-focus prev')
#nmap('<Ctrl+j>', 'completion-item-focus next')
##########################################################################################
### these are caret mode default key bindings
##########################################################################################
"""
Default:
        
        caret:
        
        $: move-to-end-of-line
        
        0: move-to-start-of-line
        
        <Ctrl-Space>: selection-drop
        
        <Escape>: mode-leave
        
        <Return>: yank selection
        
        <Space>: selection-toggle
        
        G: move-to-end-of-document
        
        H: scroll left
        
        J: scroll down
        
        K: scroll up
        
        L: scroll right
        
        V: selection-toggle --line
        
        Y: yank selection -s
        
        [: move-to-start-of-prev-block
        
        ]: move-to-start-of-next-block
        
        b: move-to-prev-word
        
        c: mode-enter normal
        
        e: move-to-end-of-word
        
        gg: move-to-start-of-document
        
        h: move-to-prev-char
        
        j: move-to-next-line
        
        k: move-to-prev-line
        
        l: move-to-next-char
        
        o: selection-reverse
        
        v: selection-toggle
        
        w: move-to-next-word
        
        y: yank selection
        
        {: move-to-end-of-prev-block
        
        }: move-to-end-of-next-block
"""
# insert mode
unmap('i', "normal")
nmap('i', 'hint inputs')
# ** Editor
imap('<Ctrl-i>', 'open-editor')


##########################################################################################
###   setting up quickmarks  
##########################################################################################
# might want to put in its own .py file and write a script that allows you to add .... to it
# ** Quickmarks and Marks
nunmap("'")
# real quickmarks
nmap("'t", ':open --tab localhost:9091')                 
nmap("'y", ':open --tab https://www.youtube.com/')                 
nmap("'p1", ':open --tab https://1337x.to/home/')         
nmap("'pp", ':open --tab https://pirate-bays.net/torrent-search')        
nmap("'b", ':open --tab https://search.brave.com/')               
nmap("'r", ':open --tab https://www.reddit.com/')               


################################################################################
###   to do 
################################################################################
#------------------------------------------------------------------------------------------
#[[[[ this is [maybe] what gets displayed in the window name in qtile
# The format to use for the window title. The following placeholders are
# defined:
#   * `{perc}`: The percentage as a string like `[10%]`.
#   * `{perc_raw}`: The raw percentage, e.g. `10`
#   * `{title}`: The title of the current web page
#   * `{title_sep}`: The string ` - ` if a title is set, empty otherwise.
#   * `{id}`: The internal window ID of this window.
#   * `{scroll_pos}`: The page scroll position.
#   * `{host}`: The host of the current web page.
#   * `{backend}`: Either ''webkit'' or ''webengine''
#   * `{private}` : Indicates when private mode is enabled.
#     c.window.title_format = "{private}{perc}{title}{title_sep}qutebrowser"
c.tabs.title.format = '{index}{private}{title_sep}{current_title}'
#------------------------------------------------------------------------------------------
#------------------------------------------------------------------------------------------
# ** Home/Start Page
# TODO generic user home directory reference instead
c.url.default_page = 'https://wiki.archlinux.org/title/Special:Random'
c.url.start_pages = ['https://wiki.archlinux.org/title/Special:Random']
#------------------------------------------------------------------------------------------

