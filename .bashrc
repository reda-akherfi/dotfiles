#
# ~/.bashrc
#

# activate vim mode 
# set -o vi

# If not running interactively, don't do anything
[[ $- != *i* ]] && return

alias ls='ls --color=auto'
alias grep='grep --color=auto'

#setting up the EDITOR
export EDITOR="vim"
# icons for lf
export LF_ICONS=$(cat ~/.config/lf/icons)

# path
export PATH=$PATH:~/.local/bin/
export PATH=$PATH:~/.local/scripts/
## my programs' aliases
## epub reader zathura
alias zah="zathura --fork ~/Documents/mental_haven.epub"
alias zathura="zathura --fork"
## neovim and config files
alias v="vim"
alias vq="nvim ~/redalo_setup/qtile_shit/qtile/config.py"
alias vb="nvim ~/.bashrc"
# starting the X server
alias x="startx"
# ncmpcpp 
alias n="ncmpcpp"
# youtube-dl 
alias youtube-dl="yt-dlp"
## # clipmenud setup
## export CM_DEBUG=1
## export CM_DIR=$XDG_CACHE_HOME/clipmenu_cache
## export CM_LAUNCHER=dmenu
## export CM_SELECTIONS="primary clipboard secondary"

# tmux
alias tx="tmux -key-table vi"



################################################################################
###    prompt customization
################################################################################
# starts with \[\033[ or \e[ and ends with \] :::: \[\033[0;32m\]
# PS1="\e[0;32m\]\u\[\033[0m\] \e[0;32m\]󰣇\[\033[0m\] \e[0;32m\]\h in \[\033[0m\] \e[0;31m\] \w \[\033[0m\]\e[0;31m\] \n-->  \]\033[0m\]"
# Define color codes
RED='\033[0;31m'
GREEN='\033[0;32m'
BROWN='\033[0;33m'
LIGHT_BLUE='\033[1;34m'
YELLOW='\033[1;33m'
NC='\033[0m' # No Color

# Set prompt string
PS1="\n${BROWN}\u ${GREEN}󰣇 ${BROWN}\h ${RED}in ${LIGHT_BLUE}\w ${GREEN}${NC}\n$  "

# Explanation:
# - RED, GREEN, BROWN, LIGHT_BLUE, YELLOW, NC: define color codes using escape sequences.
# - PS1: defines the prompt string.
# - ${RED}reda: sets "reda" in red color.
# - ${GREEN}λ: sets the lambda symbol (λ) in green color (replace with another symbol if desired).
# - ${BROWN}archlinux: sets "archlinux" in brown color.
# - ${LIGHT_BLUE}in: sets "in" in light blue color.
# - ${YELLOW}~/.config/qtile: sets the path in yellow color.
# - ${NC}: resets color to default.
# - $: displays the current working directory and command prompt symbol.

################################################################################
###    aliases
################################################################################
# vim related aliases
alias v="vim"
alias vb="vim /home/reda/.bashrc"
alias dmenu_themed="dmenu -fn 'JetBrainsMono Nerd Font Mono,JetBrainsMono NFM Light:style=Bold,Regular:size=18' -l 10 -nb '#333333' -nf '#f5f5f5' -sf '#ffd700' -sb '#333333'"
# aliases for ls
alias la="ls -a"
alias ll="ls -la"
# git aliases
alias gst="git status"
alias gll="git log --oneline"
alias gc="git commit -m"
alias gad="git add ."
alias gpm="git push -u origin main"
# systemd aliases
alias sscl="sudo systemctl"



################################################################################
###    bash functions
################################################################################
# openning man pages using vim
#  viman () { text=$(man "$@") && echo "$text" | vim -R +":set ft=man" - ; }
vm () { text=$(man "$@") && echo "$text" | vim -R +":set ft=man" - ; }


################################################################################
###  XDG stuff
################################################################################
### !!!! the No No's | never touch them
# ~/.profile
### the good guys
export XDG_DATA_HOME="/home/reda/.local/share"
export XDG_CONFIG_HOME="/home/reda/.config"
export XDG_STATE_HOME="/home/reda/.local/state"
export XDG_CACHE_HOME="/home/reda/.cache"
# XDG ninja recommendations
export ANDROID_USER_HOME="$XDG_DATA_HOME"/.android
alias adb='HOME="$XDG_DATA_HOME"/.android adb'
export HISTFILE="${XDG_STATE_HOME}"/bash/history
export GTK2_RC_FILES="$XDG_CONFIG_HOME"/gtk-2.0/gtkrc
export MYPY_CACHE_DIR="$XDG_CACHE_HOME"/mypy
export NPM_CONFIG_USERCONFIG=$XDG_CONFIG_HOME/npm/npmrc
export _JAVA_OPTIONS=-Djava.util.prefs.userRoot="$XDG_CONFIG_HOME"/java
export PASSWORD_STORE_DIR="$XDG_DATA_HOME"/pass
export PSQL_HISTORY="$XDG_DATA_HOME/psql_history"
export PYTHONSTARTUP="$XDG_CONFIG_HOME"/python/pythonrc


