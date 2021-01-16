# Base16 Shell
BASE16_SHELL="$HOME/.config/base16-shell/"
[ -n "$PS1" ] && \
    [ -s "$BASE16_SHELL/profile_helper.sh" ] && \
        eval "$("$BASE16_SHELL/profile_helper.sh")"
# vi mode
set -o vi

# color with ls
alias ls='ls --color=auto'

# scripts directory
export PATH=$PATH:~/Documents/scripts
