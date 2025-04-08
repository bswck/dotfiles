alias c=clear
alias pn=pnpm
alias sv='pnpx sv'
alias poetry='uvx poetry'
alias e='exa -F'
alias autin='atuin'

f() {
    code -r "$1"
}

if which wine 1> /dev/null 2>&1; then
    export C=~/.wine/drive_c
    jazz() {
        wine $C/Games/Jazz2/Jazz2.exe $@
    }
fi

function where() {
    which -a $1 | uniq
}

function rm-containers() {
    docker rm -vf $(docker ps -aq)
}

function rm-images() {
    docker rmi -f $(docker images -aq)
}

[ -f ~/.private_aliases ] && . ~/.private_aliases
[ "$PWD" != "$HOME" ] && [ -f .private_aliases ] && . .private_aliases
