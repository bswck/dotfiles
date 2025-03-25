alias c=clear
alias pn=pnpm
alias sv='pnpx sv'
alias poetry='uvx poetry'
alias e='exa -F'

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

# https://github.com/astral-sh/ruff/issues/9019
linked-worktrees() {
    git worktree list --porcelain | \
    rg "worktree (.+)" -r '$1' | \
    # Exclude the main worktree
    tail -n +2
}

ruff() {
    # shellcheck disable=SC2046,SC2048,SC2086
    case "$1" in
        check) command ruff check $(linked-worktrees | xargs -l echo --extend-exclude) ${*:3};;
        *) command ruff ${*:1};;
    esac
}

[ -f ~/.private_aliases ] && . ~/.private_aliases
[ "$PWD" != "$HOME" ] && [ -f .private_aliases ] && . .private_aliases
