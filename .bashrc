# ~*- ~/.bashrc ~*~

# -*- Shell -*-
[[ $- != *i* ]] && return  # If not running interactively, don't do anything

PS1="\[\033[38;5;69m\][\[$(tput sgr0)\]\[\033[38;5;219m\]\u\[$(tput sgr0)\]\[\033[38;5;75m\]@\[$(tput sgr0)\]\[\033[38;5;205m\]\h\[$(tput sgr0)\]\[\033[38;5;69m\]](\[$(tput sgr0)\]\[\033[38;5;227m\]\W\[$(tput sgr0)\]\[\033[38;5;69m\])\\$\[$(tput sgr0)\] \[$(tput sgr0)\]"
shopt -s autocd
shopt -s cdspell
bind "set completion-ignore-case on"

# -*- Export -*-
export TERM="xterm-256color"
export EDITOR="emacsclient -t -a ''"
export VISUAL="emacsclient -c -a emacs"
export MANPAGER="sh -c 'col -bx | bat -l man -p'"
export HISTCONTROL=ignoredups:erasedups
export GIT_SSH_COMMAND="ssh -i ~/.ssh/github_key -F /dev/null"

# -*- Alias -*-
alias ls='exa -l -s type --color=always --group-directories-first'
alias lsa='exa -al -s type --color=always --group-directories-first'
alias grep='grep --color=auto'
alias ..='cd ..'
alias ...='cd ../..'
alias mv='mv -i'
alias rm='rm -i'
alias cp='cp -i'
alias cat='bat'
alias doom='~/.emacs.d/bin/doom'
# - Django
alias djmm='python3 manage.py makemigrations'
alias djm8='python3 manage.py migrate'
alias djsu='python3 manage.py createsuperuser'
alias djsh='python3 manage.py shell'
alias djrun='python3 manage.py runserver'
# - Git
alias gs='git status'
alias ga='git add'
alias gc='git commit -m'
alias gp='git push'
alias gpu='git pull'
